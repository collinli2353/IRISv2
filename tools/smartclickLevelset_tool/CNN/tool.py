from configparser import Interpolation
import cv2
import numpy as np
import torch
import maxflow
from scipy import ndimage
from scipy.ndimage import zoom
from skimage import measure
from tools.levelset_tool.ChanVese import runChanVese
from tools.smartclickCNN_tool.CNN.network import UNet
from tools.smartclickCNN_tool.CNN.utils import (add_countor, add_overlay, cropped_image, extends_points,
                                                          extreme_points, get_bbox, get_largest_two_component,
                                                          get_start_end_points, interaction_euclidean_distance,
                                                          interaction_gaussian_distance,
                                                          interaction_geodesic_distance,
                                                          interaction_refined_geodesic_distance,
                                                          itensity_normalization, itensity_normalize_one_volume,
                                                          itensity_standardization, softmax, softmax_seg, zoom_image)
from matplotlib import pyplot as plt


class tool():
    model_path = './models/smartclickCNN.pth'
    def __init__(self):
        pass

    def initial_model(self):
        model = UNet(2, 2, 16)
        if torch.cuda.is_available():
            model = model.cuda()
        else:
            model = model.cpu()
        model.load_state_dict(torch.load(self.model_path))
        return model

    def add_segment_seed(self, seed):
        self.segmentation_seeds.append(seed)

    def add_revision_seed(self, seed, is_background):
        if is_background:
            if not self.background_seeds.__contains__(seed):
                self.background_seeds.append(seed)
        else:
            if not self.foreground_seeds.__contains__(seed):
                self.foreground_seeds.append(seed)

    def perform_segmentation(self, np_img, segmentation_seeds):
        fig, axs = plt.subplots(2, 2)
        seed_msk = np.zeros_like(np_img)

        if len(segmentation_seeds) == 0: return seed_msk
        
        for seed in segmentation_seeds:
            seed_msk[seed[0], seed[1]] = 1
        
        seed_msk = extends_points(seed_msk)

        bbox = get_start_end_points(seed_msk)
        cropped_img = cropped_image(np_img, bbox)
        x, y = cropped_img.shape
        normal_img = itensity_normalization(cropped_img)
        
        cropped_seed = cropped_image(seed_msk, bbox)
        cropped_geos = interaction_geodesic_distance(
            normal_img, cropped_seed)

        
        axs[0, 0].imshow(normal_img, cmap='gray')
        axs[0, 1].imshow(cropped_geos, cmap='gray')
        axs[1, 0].imshow(cropped_seed, interpolation='none')

        Prob = runChanVese(normal_img, cropped_seed, max_iter=15)

        # crf_param = (5.0, 0.1)
        # fix_predict = maxflow.maxflow2d(normal_img, Prob, crf_param)
        fix_predict = Prob
        
        pred = np.zeros_like(np_img, dtype=np.float)

        pred[bbox[0]:bbox[2], bbox[1]:bbox[3]] = fix_predict

        pred[pred >= 0.5] = 1
        pred[pred < 0.5] = 0

        strt = ndimage.generate_binary_structure(2, 1)
        seg = np.asarray(
            ndimage.morphology.binary_opening(pred, strt), np.uint8)
        seg = np.asarray(
            ndimage.morphology.binary_closing(pred, strt), np.uint8)
        seg = self.largestConnectComponent(seg)
        seg = ndimage.binary_fill_holes(seg)

        seg = np.array(seg, np.uint8)
        axs[1,1].imshow(fix_predict)
        plt.show()

        return seg

    def largestConnectComponent(self, img):
        binaryimg = img

        label_image, num = measure.label(
            binaryimg, background=0, return_num=True)
        areas = [r.area for r in measure.regionprops(label_image)]
        areas.sort()
        if len(areas) > 1:
            for region in measure.regionprops(label_image):
                if region.area < areas[-1]:
                    for coordinates in region.coords:
                        label_image[coordinates[0], coordinates[1]] = 0
        label_image = label_image.astype(np.int8)
        label_image[np.where(label_image > 0)] = 1
        return label_image