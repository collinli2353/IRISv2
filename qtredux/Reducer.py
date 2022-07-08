import copy
import numpy as np


def Reducer(state, action=None):

    if state is None:
        return {
            'triggers': {
                'init_msk': None,
                'changed_msk': None,
                'changed_tool': 'Q',
                'changed_size': None,
                'key_pressed': None,
                'key_released': None,
                'key_ctrl': False,
                'img_fp': None,
                'msk_fp': None,
                'org_fp': None,
                'flair_fp': None,
                'msg': None,
                'lbl_ids': [0],
            },
            'img_obj': {
                'img': np.zeros([320, 320, 320]),
                'affine': None,
                'header': None,
                'img_size': (320, 320, 320),
                'min_max': [0, 0],
                'val_win': 0,
                'val_lev': 0,
                'foc_pos': [160, 160, 100],
                'point_pos': [[160, 160, 100], [160, 160, 100]],
                'zoom': 1.0,
                'shift': [0, 0, 0],
                'RAIcode': 'LAI',
                'axismapping': None,
                'transX': [0, 0, 0],
                'transY': [0, 0, 0],
                'ismain': [False, False, False],
                'isdisplay': [True, True, True],
                'isimgloaded': False,
                'isdicom': False,
            },
            'msk_obj': {
                'msk': None,
                'opa': 50,
                'lbl_ids': [0],
                'isnew': True,
            },
            'organ_obj': {
                'msk': None,
                'msk_edges': None,
            },
            'tool_type': 'cursor',
            'brush_obj': {
                'enable': False,
                'style': 's',  # s or c which denotes square or circle
                'size': 4,
                'lbl': 1,
            },
            'lv_obj': {
                'enable': False,
                'step': 0.5,  # step size
                'stop': 4,    # when to stop
            },
            'sp_obj': {
                'enable': False,
                'lbls': [],
                'n_comps': 0,
            },
            'smartclick_obj': {
                'enable': False,
                'style': '3D',
                'sensitivity': 10,
                'fillholes': True,
            },
            'smartlevelset_obj': {
                'enable': False,
                'style': '2D',
                'invert': True,
                'mode': 0,  # 0 is global segment, and 1 is local segment
                'mu': 0.1,
                'nu': 0.2,
                'max_iter': 30,
                'epison': 0.1,
                'step': 0.1,
                'sensitivity': 10,
                'range': [0, 1],
            },
            'smartboundary_obj': {
                'enable': False,
                'style': '2D',
                'sensitivity': 10,
                'fillholes': True,
                'tumor_points': [],
                'tumor_intensity': [],
                'background_points': [],
                'background_intensity': [],
                'include_points': [],
                'exclude_points': [],
            },
            'levelset_obj': {
                'enable': False,
                'mode': 0,  # 0 is global segment, and 1 is local segment
                'width': 20,
                'height': 20,
            },
        }

    def updateState(s, a):

        # =============== Trigger Obj ================== #
        # ============================================== #
        if a['type'] == 'UPDATE_TRIGGER_INIT_MSK':
            return {
                **s,
                'triggers': {
                    **s['triggers'],
                    'init_msk': a['init_msk']
                }
            }

        return s

    if type(action) == dict:
        state = updateState(state, action)
    elif type(action) == list:
        for act in action:
            state = updateState(state, act)

    return state
