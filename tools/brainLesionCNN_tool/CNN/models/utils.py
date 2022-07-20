import os
import json
import torch
import numpy as np
import nibabel as nib
from collections import OrderedDict

from tools.brainLesionCNN_tool.CNN.models.unetVggGNObject import unetVggGNObject
from tools.brainLesionCNN_tool.CNN.models.unetResV1Offset import unetResV1Offset

def getDevice(gpu_id):

    if gpu_id == -1:
        device = torch.device('cpu')
        print("---->>>> CPU is used for inference")
    else:
        os.environ["CUDA_VISIBLE_DEVICES"] = str(gpu_id)
        device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
        
        print("---->>>> GPU is used for inference")

    return device

def convert_state_dict(state_dict):
    
    if not next(iter(state_dict)).startswith("module."):
        return state_dict  # abort if dict is not a DataParallel model_state

    new_state_dict = OrderedDict()
    for k, v in state_dict.items():
        name = k[7:]  # remove `module.`
        new_state_dict[name] = v
    return new_state_dict

def loadSegModel(device, model_fp):
    
    print("---->>>> Loading CNN lesion segmentation model")
    model = unetVggGNObject(in_channels=3).to(device)
    states = torch.load(model_fp, map_location=device)
    states = convert_state_dict(states)
    model.load_state_dict(states)
    
    return model

def loadSepModel(device, model_fp):
    
    print("---->>>> Loading CNN lesion separation model")
    model = unetResV1Offset(in_channels=3).to(device)
    states = torch.load(model_fp, map_location=device)
    states = convert_state_dict(states)
    model.load_state_dict(states)
    
    return model

def normalizeData(img):
    res = (img - np.min(img)) / np.max(img)
    res = (res * 1.0 - np.mean(res)) / np.std(res)

    return res

def loadPredMask(idx, mask, crop_pos):
    sx, sy, sz, ex, ey, ez = crop_pos[3:]
    mask = mask[sx:ex+1, sy:ey+1, sz:ez+1]

    return mask

def loadAndPrepData(file_fp):
    t1_path = file_fp['T1']
    t2_path = file_fp['T2']
    fl_path = file_fp['FLAIR']
    
    t1 = nib.load(t1_path)
    t2 = nib.load(t2_path)
    fl = nib.load(fl_path)
    header = fl.header
    affine = fl.affine

    t1 = t1.get_data()
    t2 = t2.get_data()
    fl = fl.get_data()
    
    img_x, img_y, imgz = fl.shape
    sx, sy, sz, ex, ey, ez = getBrainBoundary(fl)
    
    sx, ex = handleGap(sx, ex, 128)
    sy, ey = handleGap(sy, ey, 160)
    sz, ez = handleGap(sz, ez, 128)
    
    t1 = normalizeData(t1[sx:ex+1, sy:ey+1, sz:ez+1])
    t2 = normalizeData(t2[sx:ex+1, sy:ey+1, sz:ez+1])
    fl = normalizeData(fl[sx:ex+1, sy:ey+1, sz:ez+1])
    
    img = np.stack([t1,t2,fl])
    crop_pos = np.asarray([img_x, img_y, imgz, sx, sy, sz, ex, ey, ez])
    
    return img, header, affine, crop_pos

def reshapeToOriSizeWithCrop(pred, param):
    w,h,d = param[:3]
    img = np.zeros([w,h,d])
    sx, sy, sz, ex, ey, ez = param[3:]
    img[sx:ex+1, sy:ey+1, sz:ez+1] = pred

    return img

def handleGap(s, e, val):
    ss = s
    ee = e
    if e-s+1 < val:
        diff = val-e+s-1 
        ee += diff // 2
        ss -= diff // 2 + diff % 2

    return ss, ee

def getBrainBoundary(brain_mask):
    minx = miny = minz = 0
    maxx = maxy = maxz = 0

    n,m,p = brain_mask.shape

    for i in range(n):
        uniques = np.unique(brain_mask[i,:,:])
        if len(uniques) > 1:
            minx = i
            break
    
    for i in range(n-1,-1,-1):
        uniques = np.unique(brain_mask[i,:,:])
        if len(uniques) > 1:
            maxx = i
            break

    for i in range(m):
        uniques = np.unique(brain_mask[:,i,:])
        if len(uniques) > 1:
            miny = i
            break
    
    for i in range(m-1,-1,-1):
        uniques = np.unique(brain_mask[:,i,:])
        if len(uniques) > 1:
            maxy = i
            break
    
    for i in range(p):
        uniques = np.unique(brain_mask[:,:,i])
        if len(uniques) > 1:
            minz = i
            break
    
    for i in range(p-1,-1,-1):
        uniques = np.unique(brain_mask[:,:,i])
        if len(uniques) > 1:
            maxz = i
            break

    return minx, miny, minz, maxx, maxy, maxz