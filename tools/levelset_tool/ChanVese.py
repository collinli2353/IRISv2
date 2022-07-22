# coding:utf-8
import sys
import numpy as np
import cv2
import math

import nibabel as nib


def iterateChanVese2D(lsf, img, mu, nu, epison, step):
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

def iterateChanVese3D(lsf, img, mu, nu, epison, step):
    Drc = (epison / math.pi) / (epison*epison + lsf*lsf)
    Hea = 0.5*(1 + (2 / math.pi) * np.arctan(lsf/epison))
    Iz, Iy, Ix = np.gradient(lsf)
    s = np.sqrt(Ix*Ix+Iy*Iy)
    Nx = Ix / (s+1e-6)
    Ny = Iy / (s+1e-6)
    Nz = Iz / (s+1e-6)
    Mxx, Nxx, Oxx = np.gradient(Nx)
    Myy, Nyy, Ozz = np.gradient(Ny)
    Mzz, Nzz, Ozz = np.gradient(Nz)
    cur = Nxx + Myy + Ozz
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

def runChanVese2D(img, lsf, mu=1, nu=0.2, max_iter=30, epison=0.1, step=0.1):
    for _ in range(1, max_iter): lsf = iterateChanVese2D(lsf, img, mu, nu, epison, step)
    return lsf
    
def runChanVese3D(img, lsf, mu=1, nu=0.2, max_iter=30, epison=0.1, step=0.1):
    for _ in range(1, max_iter): lsf = iterateChanVese3D(lsf, img, mu, nu, epison, step)

    return lsf