# coding:utf-8
import sys
import numpy as np
import cv2
import math

import nibabel as nib


def iterateChanVese(lsf, img, mu, nu, epison, step):

    Drc = (epison / math.pi) / (epison*epison + lsf*lsf)
    Hea = 0.5*(1 + (2 / math.pi) * np.arctan(lsf/epison))
    Iy, Ix = np.gradient(lsf)
    s = np.sqrt(Ix*Ix+Iy*Iy)
    Nx = Ix / (s+1e-6)
    Ny = Iy / (s+1e-6)
    Mxx, Nxx = np.gradient(Nx)
    Nyy, Myy = np.gradient(Ny)
    cur = Nxx + Nyy
    Length = nu*Drc*cur

    Lap = cv2.Laplacian(lsf, -1)
    Penalty = mu*(Lap - cur)

    s1 = Hea*img
    s2 = (1-Hea)*img
    s3 = (1-Hea)
    C1 = (s1).sum() / (Hea).sum()
    C2 = (s2).sum() / (s3).sum()
    CVterm = Drc*(-1 * (img - C1)*(img - C1) + 1 * (img - C2)*(img - C2))

    lsf = lsf + step*(Length + Penalty + CVterm)

    return lsf


"""
def showImgContour(lsf, img):

    plt.clf()
    plt.imshow(img), plt.xticks([]), plt.yticks([])
    plt.contour(lsf, [0], colors='r', linewidth=2)
    plt.draw()
    plt.show()
"""

def runChanVese(img, lsf, mu=1, nu=0.2, max_iter=30, epison=0.1, step=0.1):
    for _ in range(1, max_iter):
        lsf = iterateChanVese(lsf, img, mu, nu, epison, step)
        # showImgContour(lsf, img)

    return lsf


if __name__ == "__main__":

    img = nib.load("./dicom_vol.nii").get_fdata()

    img = img[:, :, 37]
    # img = img[190:250,100:170]

    lsf = np.ones((img.shape[0], img.shape[1]), img.dtype)
    # lsf[25:45,30:40]= -1
    lsf[190:250, 100:170] = -1
    lsf = -lsf

    runChanVese(img, lsf)
