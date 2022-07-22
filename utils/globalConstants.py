import numpy as np
import nibabel as nib

from utils.maskManager import maskManager

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class IMG_OBJ(metaclass=Singleton):
    FP = None
    NIBABEL_IMG = None
    ORIG_NP_IMG = None
    NP_IMG = None
    MARGIN = None
    AFFINE = None
    HEADER = None
    SHAPE = None
    MIN_MAX_INTENSITIES = None
    WINDOW_VALUE = None
    LEVEL_VALUE = None
    FOC_POS = None
    POINT_POS = None
    ZOOM_FACTOR = None
    SHIFT = None
    IMG_FLIP = None
    ORIG_RAI_CODE = None
    CURRENT_RAI_CODE = None
    RAI_DISPLAY_LETTERS = None
    AXISMAPPING = None
    VIEWER_MAPPING = None
    VIEWER_TYPE = None
    IS_DICOM = None

    UPDATE_VIEWERS = None

    def __init__(self):
        self.FP = None
        self.NIBABEL_IMG = None
        self.ORIG_NP_IMG = np.zeros([100, 100, 100])
        self.NP_IMG = np.zeros([100, 100, 100])
        self.MARGIN = {
            'axi': [0, 0],
            'sag': [0, 0],
            'cor': [0, 0],
        }
        self.AFFINE = None
        self.HEADER = None
        self.SHAPE = (100, 100, 100)
        self.MIN_MAX_INTENSITIES = (0, 0)
        self.WINDOW_VALUE = 0
        self.LEVEL_VALUE = 0
        self.FOC_POS = [50, 50, 50]
        self.POINT_POS = [50, 50, 50]
        self.ZOOM_FACTOR = 1
        self.SHIFT = [0, 0, 0]
        self.IMG_FLIP = {
            'axi': [False, False],
            'sag': [False, False],
            'cor': [False, False],
        }
        self.ORIG_RAI_CODE = None
        self.RAI_CODE = None
        self.RAI_DISPLAY_LETTERS = [
            ['S', 'P', 'I', 'A'],
            ['S', 'L', 'I', 'R'],
            ['A', 'L', 'P', 'R'],
        ]
        self.VIEWER_MAPPING = {
            'axi': 2,
            'sag': 0,
            'cor': 1,
            'topLeft': 'axi',
            'topRight': 'sag',
            'botRight': 'cor',
            2: 'axi',
            0: 'sag',
            1: 'cor',
        }
        self.VIEWER_INDEX_MAPPING = {
            'topLeft': 2,
            'topRight': 0,
            'botRight': 1,
        }
        self.AXISMAPPING = {
            'axi': [0, 1],
            'sag': [1, 2],
            'cor': [0, 2],
            2: [0, 1],
            0: [1, 2],
            1: [0, 2],
        }
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
            self.MARGIN = {
                'axi': [0, 0],
                'sag': [0, 0],
                'cor': [0, 0],
            }
            self.AFFINE = self.NIBABEL_IMG.affine
            self.HEADER = self.NIBABEL_IMG.header
            self.SHAPE = self.ORIG_NP_IMG.shape
            self.MIN_MAX_INTENSITIES = (self.NP_IMG.min(), self.NP_IMG.max())
            self.WINDOW_VALUE = self.ORIG_NP_IMG.max() - self.ORIG_NP_IMG.min()
            self.LEVEL_VALUE = (self.ORIG_NP_IMG.max() + self.ORIG_NP_IMG.min()) / 2
            self.FOC_POS = [self.SHAPE[0] // 2, self.SHAPE[1] // 2, self.SHAPE[2] // 2]
            self.ZOOM_FACTOR = 1
            self.SHIFT = [0, 0, 0]
            self.IMG_FLIP = {
                'axi': [False, False],
                'sag': [False, False],
                'cor': [False, False],
            }
            self.ORIG_RAI_CODE = nib.aff2axcodes(self.AFFINE, (('R', 'L'), ('P', 'A'), ('I', 'S')))
            self.CURRENT_RAI_CODE = ('R', 'P', 'I') 

            # Desired RAI code is RPI
            if self.ORIG_RAI_CODE[0] != 'R':
                self.swapVoxelXAxis()

            if self.ORIG_RAI_CODE[1] != 'P':
                self.swapVoxelYAxis()

            if self.ORIG_RAI_CODE[2] != 'I':
                self.swapVoxelZAxis()

    def swapVoxelXAxis(self):
        self.IMG_FLIP['axi'][0] = not self.IMG_FLIP['axi'][0] # Flip axial horizontally
        self.IMG_FLIP['cor'][0] = not self.IMG_FLIP['cor'][0] # Flip cornal horizontally

    def swapVoxelYAxis(self):
        self.IMG_FLIP['axi'][1] = not self.IMG_FLIP['axi'][1] # Flip axial vertically
        self.IMG_FLIP['sag'][0] = not self.IMG_FLIP['sag'][0] # Flip saggital horizontally

    def swapVoxelZAxis(self):
        self.IMG_FLIP['cor'][1] = not self.IMG_FLIP['cor'][1] # Flip cornal vertically
        self.IMG_FLIP['sag'][1] = not self.IMG_FLIP['sag'][1] # Flip saggital vertically


    def __str__(self):
        return f'''
file_path: {self.FP}
margin: {self.MARGIN}
affine: {self.AFFINE}
header: {self.HEADER}
shape: {self.SHAPE}
min_max_intensities: {self.MIN_MAX_INTENSITIES}
window_value: {self.WINDOW_VALUE}
level_value: {self.LEVEL_VALUE}
foc_pos: {self.FOC_POS}
zoom_factor: {self.ZOOM_FACTOR}
shift: {self.SHIFT}
img flip: {self.IMG_FLIP}
orig rai code: {self.ORIG_RAI_CODE}
current rai code: {self.CURRENT_RAI_CODE}
viewer type: {self.VIEWER_TYPE}
is dicom: {self.IS_DICOM}
        '''

    def FOC_POS_PERCENT(self):
        return [self.FOC_POS[i] / self.SHAPE[i] for i in range(len(self.FOC_POS))]

class MSK_OBJ(metaclass=Singleton):
    MSK = None
    TEMP_MSK = None
    OPA = None
    LBL_IDS = [0, 1]
    CURRENT_LBL = 1
    maskChangeManager = maskManager()

    def __init__(self):
        self.MSK = np.zeros([100, 100, 100])
        self.TEMP_MSK = np.zeros([100, 100, 100])
        self.OPA = 50
        self.LBL_IDS = [0, 1]
        self.CURRENT_LBL = 1
        self.maskChangeManager = maskManager()

    def newMsk(self, msk):
        self.MSK = msk
        self.TEMP_MSK = np.zeros_like(self.MSK)
        self.OPA = 50
        self.LBL_IDS = [int(i) for i in np.unique(self.MSK)]
        self.CURRENT_LBL = self.LBL_IDS[-1]
        self.addLabel()
        self.maskChangeManager = maskManager()

    def updateMaskManager(self, msk):
        self.MSK = msk
        self.maskChangeManager.updateNewChange(msk)

    def undo(self):
        self.MSK = self.maskChangeManager.undoMaskChange(self.MSK)

    def redo(self):
        self.MSK = self.maskChangeManager.redoMaskChange(self.MSK)

    def addLabel(self):
        self.LBL_IDS.append(self.LBL_IDS[-1]+1)
        self.CURRENT_LBL = self.LBL_IDS[-1]
    
    def removeLabel(self):
        if self.CURRENT_LBL == 0: return
        self.LBL_IDS.pop(self.LBL_IDS.index(self.CURRENT_LBL)+1)

    def __str__(self):
        return f'''
opa: {self.OPA}
lbl ids: {self.LBL_IDS}
current lbl: {self.CURRENT_LBL}
        '''

class TOOL_OBJ(metaclass=Singleton):
    ACTIVE_TOOL_INDEX = None
    ACTIVE_TOOL_NAME = None
    INIT_MOUSE_POS = None

    def __init__(self):
        self.ACTIVE_TOOL_INDEX = 0
        self.ACTIVE_TOOL_NAME = 'curser'
        self.INIT_MOUSE_POS = {
            'axi': [0, 0],
            'sag': [0, 0],
            'cor': [0, 0],
        }

    def __str__(self):
        return f'''
active tool index: {self.ACTIVE_TOOL_INDEX}
active tool name: {self.ACTIVE_TOOL_NAME}
        '''