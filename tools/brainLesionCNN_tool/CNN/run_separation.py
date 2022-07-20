import os
import time
import torch
import argparse
import numpy as np
import torch.nn as nn
from torch.serialization import load
import nibabel as nib

from tools.brainLesionCNN_tool.CNN.models.utils import getDevice, loadSepModel, loadAndPrepData, reshapeToOriSizeWithCrop, loadPredMask
from tools.brainLesionCNN_tool.CNN.models.kmeansSep import kmeansSep

def run_separation(t1_fp, t2_fp, fl_fp, msk_np, model_fp, threshold=0.01, gpu_id=-1): 

    device = getDevice(gpu_id)
    model = loadSepModel(device, model_fp)
    model.eval()
    
    kmeans_sep = kmeansSep()
    
    st = time.time()
    file_fp = {
        'T1': t1_fp,
        'T2': t2_fp,
        'FLAIR': fl_fp,
    }

    img, header, affine, crop_pos = loadAndPrepData(file_fp)
    mask = loadPredMask(0, msk_np, crop_pos)
    mask = (mask>0).astype(float)
    img = torch.from_numpy(img).unsqueeze(0).to(device)
    img_size = mask.shape
    
    with torch.no_grad():
        out = model(img)
        out = out[1]    
    out = [x.squeeze_(0).squeeze_(0).detach().cpu().numpy() for x in out]
    hvote = torch.zeros(img_size)
    
    for ii in range(img_size[0]):
        for jj in range(img_size[1]):
            for kk in range(img_size[2]):
                if mask[ii,jj,kk] > 0:
                    x,y,z,w = out[0][ii,jj,kk],out[1][ii,jj,kk],out[2][ii,jj,kk],out[3][ii,jj,kk]
                    x,y,z = int(np.round(x)),int(np.round(y)),int(np.round(z))
                    x = min(max(0,ii-x),img_size[0]-1)
                    y = min(max(0,jj-y),img_size[1]-1)
                    z = min(max(0,kk-z),img_size[2]-1)
                    hvote[x,y,z] += w
                    
    hvote.unsqueeze_(0).unsqueeze_(0)
    pred = kmeans_sep.predict(hvote,mask)
    pred = reshapeToOriSizeWithCrop(pred, crop_pos)
         
    print("---->>>> Lesion separationis processed, using %.2fs" % (time.time()-st))
    return pred

if __name__ == "__main__":
    pass