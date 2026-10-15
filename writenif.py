
import nibabel as nib
import numpy as np


def write_nifti(data, spacing, file_path):
    data = np.asarray(data)
    spacing = tuple(spacing)
    affine = np.eye(4)
    for i in range(len(spacing)):
        affine[i, i] = spacing[i]
    nift = nib.nifti1.Nifti1Image(data, affine)
    nib.nifti1.save(nift, file_path)

    if len(spacing) != data.ndim:
        raise ValueError("Voxel spacing does not match pixel data")



