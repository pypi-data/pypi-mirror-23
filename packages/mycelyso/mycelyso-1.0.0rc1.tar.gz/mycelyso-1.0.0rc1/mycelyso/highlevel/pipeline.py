# -*- coding: utf-8 -*-
"""
The pipeline module contains the mycelyso-Pipeline, assembled from various functions.
"""

from tunable import TunableManager
from .. import __version__, __banner__

from ..pilyso.application import App, PipelineExecutionContext, PipelineEnvironment, Every, Collected, Meta, Skip
from ..pilyso.pipeline.pipeline import NeatDict
from ..pilyso.imagestack import ImageStack
from ..pilyso.steps import \
    image_source, pull_metadata_from_image, substract_start_frame, rescale_image_to_uint8, set_result, Delete, \
    box_detection, create_boxcrop_from_subtracted_image, calculate_image_sha256_hash
from os.path import basename, abspath

from .steps import *

from ..pilyso.misc.h5writer import hdf5_output, hdf5_node_name
from .. import __banner__


class CropWidth(Tunable):
    """ Crop value (horizontal) of the image [pixels] """
    default = 0


class CropHeight(Tunable):
    """ Crop value (vertical) of the image [pixels] """
    default = 0


class BoxDetection(Tunable):
    """ Whether to run the rectangular microfluidic growth structure detection as ROI detection """
    default = False


class StoreImage(Tunable):
    """ Whether to store images in the resulting HDF5. This leads to a potentially much larger output file. """
    default = False


class SkipBinarization(Tunable):
    """ Whether to directly use the input image as binary mask. Use in case external binarization is desired. """
    default = False


class Mycelyso(App):
    """
    The Mycelyso App, implementing a pilyso App.
    """
    def options(self):
        return {
            'name': "mycelyso",
            'description': "",
            'banner': __banner__,
            'pipeline': MycelysoPipeline
        }

    def arguments(self, argparser):
        argparser.add_argument('--meta', '--meta', dest='meta', default='')
        argparser.add_argument('--interactive', '--interactive', dest='interactive',
                               default=False, action='store_true')
        argparser.add_argument('--output', '--output', dest='output', default='output.h5')

    def handle_args(self):
        self.args.tunables = TunableManager.get_representation()

        if self.args.interactive:
            # if interactive, don't spawn workers
            self.args.processes = 0
            self.run = self.interactive_run

    def interactive_run(self):
        pipeline, fun, args, kwargs = self.pe.complete_args
        assert fun == '__init__'
        pipeline = pipeline(*args, **kwargs)

        import matplotlib.pyplot as plt
        from matplotlib.widgets import Slider

        fig, ax = plt.subplots()

        plt.subplots_adjust(left=0.25, bottom=0.25)

        fig.canvas.set_window_title("Image Viewer")

        slider_background = '#e7af12'
        slider_foreground = '#005b82'

        ax_mp = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=slider_background)
        ax_tp = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=slider_background)

        mp_max = max(self.positions)
        tp_max = max(self.timepoints)

        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            multipoint = Slider(ax_mp, 'Multipoint', 0, mp_max, valinit=0, valfmt="%d", color=slider_foreground)
            timepoint = Slider(ax_tp, 'Timepoint', 0, tp_max, valinit=0, valfmt="%d", color=slider_foreground)

        env = {'show': True}

        def update(_):
            t = int(timepoint.val)
            pos = int(multipoint.val)

            fig.canvas.set_window_title("Image Viewer - [BUSY]")

            plt.rcParams['image.cmap'] = 'gray'

            plt.sca(ax)
            plt.cla()

            plt.suptitle('[left/right] timepoint [up/down] multipoint [h] hide analysis')

            result = pipeline.dispatch(Meta(pos=Every, t=Every), meta=Meta(pos=pos, t=t))

            result = NeatDict(result)

            if env['show']:
                plt.imshow(result.binary)
            else:
                plt.imshow(result.binary)

            fig.canvas.set_window_title("Image Viewer - %s timepoint #%d %d/%d multipoint #%d %d/%d" %
                                        (self.args.input, t, 1 + t, 1 + tp_max, pos, 1 + pos, 1 + mp_max))

            plt.draw()

        update(None)

        multipoint.on_changed(update)
        timepoint.on_changed(update)

        def key_press(event):
            if event.key == 'left':
                timepoint.set_val(max(1, int(timepoint.val) - 1))
            elif event.key == 'right':
                timepoint.set_val(min(tp_max, int(timepoint.val) + 1))
            elif event.key == 'ctrl+left':
                timepoint.set_val(max(1, int(timepoint.val) - 10))
            elif event.key == 'ctrl+right':
                timepoint.set_val(min(tp_max, int(timepoint.val) + 10))
            elif event.key == 'down':
                multipoint.set_val(max(1, int(multipoint.val) - 1))
            elif event.key == 'up':
                multipoint.set_val(min(mp_max, int(multipoint.val) + 1))
            elif event.key == 'h':
                env['show'] = not env['show']
                update(None)
            elif event.key == 'q':
                raise SystemExit

        fig.canvas.mpl_connect('key_press_event', key_press)

        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            fig.tight_layout()

        plt.show()


class MycelysoPipeline(PipelineExecutionContext):
    """
    The MycelysoPipeline, defining the pipeline (with slight alterations based upon arguments passed via command line).
    """
    def __init__(self, args):
        TunableManager.load(args.tunables)

        absolute_input = abspath(args.input)
        h5nodename = hdf5_node_name(absolute_input)

        self.pipeline_environment = PipelineEnvironment(ims=ImageStack(args.input))

        per_image = self.add_stage(Meta(pos=Every, t=Every))

        per_image |= set_result(tunables_hash=TunableManager.get_hash())

        # read the image
        per_image |= image_source
        per_image |= calculate_image_sha256_hash
        per_image |= pull_metadata_from_image

        per_image |= lambda image, raw_image=None: image
        per_image |= lambda image, raw_unrotated_image=None: image

        per_image |= set_empty_crops

        # define what we want (per image) as results

        result_table = {
            '_plain': [
                'calibration', 'timepoint', 'input_height',
                'input_width', 'area', 'covered_ratio', 'covered_area',
                'graph_edge_length', 'graph_edge_count', 'graph_node_count',
                'graph_junction_count', 'graph_endpoint_count',
                'filename', 'metadata', 'shift_x', 'shift_y',
                'crop_t', 'crop_b', 'crop_l', 'crop_r',
                'image_sha256_hash', 'tunables_hash'
            ],
            'graphml': 'data',
            # 'image': 'image',
            # 'raw_unrotated_image': 'image',
            # 'raw_image': 'image',
            'skeleton': 'image',
            'binary': 'image'
        }

        if StoreImage.value:
            result_table['image'] = 'image'

        per_image |= set_result(
            reference_timepoint=1,
            filename_complete=absolute_input,
            filename=basename(absolute_input),
            metadata=args.meta,
            result_table=result_table
        )

        per_image |= substract_start_frame

        if BoxDetection.value:
            per_image |= box_detection
            per_image |= create_boxcrop_from_subtracted_image

        per_image |= rescale_image_to_uint8

        per_image |= set_result(raw_unrotated_image=Delete, raw_image=Delete, subtracted_image=Delete)

        per_image |= lambda image: image[
                                   CropHeight.value:-(CropHeight.value if CropHeight.value > 0 else 1),
                                   CropWidth.value:-(CropWidth.value if CropWidth.value > 0 else 1)
                                   ]

        per_image |= lambda crop_t, crop_b, crop_l, crop_r: (
            crop_t + CropHeight.value,
            crop_b - CropHeight.value,
            crop_l + CropWidth.value,
            crop_r - CropWidth.value
        )

        per_image |= skip_if_image_is_below_size(4, 4)

        # generate statistics of the image
        per_image |= image_statistics

        if not SkipBinarization.value:
            # binarize
            per_image |= binarize
        else:
            def _image_to_binary(image, binary=None):
                return image.astype(bool)

            per_image |= _image_to_binary

        # ... and cleanup
        per_image |= clean_up

        per_image |= remove_small_structures

        per_image |= remove_border_artifacts

        # generate statistics of the binarized image
        per_image |= quantify_binary

        per_image |= skeletonize

        # 'binary', 'skeleton' are kept!
        per_image |= convert_to_nodes

        if not StoreImage.value:
            per_image |= set_result(image=Delete)

        per_image |= set_result(pixel_frame=Delete)

        per_image |= graph_statistics
        per_image |= generate_graphml

        per_position = self.add_stage(Meta(pos=Every, t=Collected))

        per_position |= track_multipoint

        per_position |= generate_overall_graphml

        per_position |= individual_tracking

        per_position |= prepare_tracked_fragments

        per_position |= prepare_position_regressions

        per_position |= lambda meta, meta_pos=None: meta.pos

        per_position |= set_result(
            filename_complete=absolute_input,
            filename=basename(absolute_input),
            metadata=args.meta,
            tunables=TunableManager.get_serialization(),
            version=__version__,
            banner=__banner__,
            result_table={
                '_plain': [
                    'metadata',
                    'filename_complete',
                    'filename',
                    'meta_pos',
                    '*_regression_*'
                ],
                'tunables': 'data',
                'version': 'data',
                'banner': 'data',
                'overall_graphml': 'data',
                'track_table': 'table',
                'track_table_aux_tables': 'table'
            }
        )

        per_position |= hdf5_output(args.output, h5nodename)

        def black_hole(result):
            for k in list(result.keys()):
                del result[k]
            del result
            return {}

        per_position |= black_hole
