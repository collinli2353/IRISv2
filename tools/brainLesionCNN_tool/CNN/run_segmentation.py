import os
import time
import torch
import argparse
import nibabel as nib

from tools.brainLesionCNN_tool.CNN.models.utils import getDevice, loadSegModel, loadAndPrepData, reshapeToOriSizeWithCrop


def run_segmentation(t1_fp, t2_fp, fl_fp, model_fp, threshold=0.01, gpu_id=-1): 

    device = getDevice(gpu_id)
    model = loadSegModel(device, model_fp)
    model.eval()
    
    print("--------------------runing segmentation--------------------")
    file_fp = {
        'T1': t1_fp,
        'T2': t2_fp,
        'FLAIR': fl_fp,
    }
    st = time.time()
    img, header, affine, crop_pos = loadAndPrepData(file_fp)
    img = torch.from_numpy(img).unsqueeze(0).to(device)
    
    with torch.no_grad():
        msk = model(img)
    msk = (msk.squeeze(0).squeeze(0).sigmoid() >= threshold)
    msk = msk.detach().cpu().numpy().astype(float)
    msk = reshapeToOriSizeWithCrop(msk,crop_pos)
    

    print("---->>>> Segmentation is processed, using %.2fs" % (time.time()-st))
    return msk
    

if __name__ == "__main__":
    pass