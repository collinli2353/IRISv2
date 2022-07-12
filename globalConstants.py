import numpy as np
import nibabel as nib

class IMG_OBJ:
    FP = None
    NIBABEL_IMG = None
    ORIG_NP_IMG = np.zeros([100, 100, 100])
    NP_IMG = np.zeros([100, 100, 100])
    AFFINE = None
    HEADER = None
    SHAPE = (100, 100, 100)
    MIN_MAX_INTENSITIES = (0, 0)
    WINDOW_LEVEL = 0
    LEVEL_VALUE = 0
    FOC_POS = [50, 50, 50]
    ZOOM_FACTOR = 1
    TRANS = [0, 0, 0]
    RAI_CODE = None
    AXISMAPPING = [[1, 2], [0, 2], [0, 1]]
    VIEWER_MAPPING = {
        'topLeft': 2,
        'topRight': 0,
        'botRight': 1,
    }
    VIEWER_TYPE = 4
    IS_DICOM = False

    def __init__(self):
        self.FP = None
        self.NIBABEL_IMG = None
        self.ORIG_NP_IMG = np.zeros([100, 100, 100])
        self.NP_IMG = np.zeros([100, 100, 100])
        self.AFFINE = None
        self.HEADER = None
        self.SHAPE = (100, 100, 100)
        self.MIN_MAX_INTENSITIES = (0, 0)
        self.WINDOW_LEVEL = 0
        self.LEVEL_VALUE = 0
        self.FOC_POS = [50, 50, 50]
        self.ZOOM_FACTOR = 1
        self.TRANS = [0, 0, 0]
        self.RAI_CODE = None
        self.VIEWER_MAPPING = {
            'topLeft': 2,
            'topRight': 0,
            'botRight': 1,
        }
        self.AXISMAPPING = [[2, 1], [0, 2], [0, 1]]
        self.VIEWER_TYPE = 4
        self.IS_DICOM = False

    def __loadImage__(self, fp):
        self.FP = fp

        # TODO: make work for dcm files
        if fp.split('.')[-1] == 'dcm':
            self.IS_DICOM = True
        else:
            self.NIBABEL_IMG = nib.load(fp)
            self.ORIG_NP_IMG = self.NIBABEL_IMG.get_fdata()
            self.NP_IMG = (self.ORIG_NP_IMG - self.ORIG_NP_IMG.min()) / (self.ORIG_NP_IMG.max() - self.ORIG_NP_IMG.min())
            self.AFFINE = self.NIBABEL_IMG.affine
            self.HEADER = self.NIBABEL_IMG.header
            self.SHAPE = self.ORIG_NP_IMG.shape
            self.MIN_MAX_INTENSITIES = (self.ORIG_NP_IMG.min(), self.ORIG_NP_IMG.max())
            self.WINDOW_LEVEL = (self.ORIG_NP_IMG.max() - self.ORIG_NP_IMG.min()) / 2
            self.LEVEL_VALUE = self.ORIG_NP_IMG.mean()
            self.FOC_POS = [self.SHAPE[0] // 2, self.SHAPE[1] // 2, self.SHAPE[2] // 2]
            self.ZOOM_FACTOR = 1
            self.TRANS = [0, 0, 0]
            self.RAI_CODE = None

    def FOC_POS_PERCENT(self):
        return [self.FOC_POS[i] / self.SHAPE[i] for i in range(len(self.FOC_POS))]

class TOOL_OBJ:
    ACTIVE_TOOL = 0
    ACTIVE_TOOL_NAME = 'curser'