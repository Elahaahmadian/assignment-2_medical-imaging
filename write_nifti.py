import os

import nibabel as nib
import numpy as np


def write_nifti(pixel_data, voxel_spacing, file_path):
    pixel_data = np.asarray(pixel_data)
    voxel_spacing = tuple(voxel_spacing)

    if len(voxel_spacing) != pixel_data.ndim:
        raise ValueError("Voxel spacing does not match pixel data")



