
import nibabel as nib
import numpy as np


def write_nifti(data, spacing, file_path):
    """
    Write pixel data to a NIfTI file using the given voxel spacing.

    :param data: Pixel data to be saved as a NIfTI image.
    :param spacing: Voxel spacing for each image dimension.
    :param file_path: Path where the NIfTI file will be saved.
    :raises ValueError: If the voxel spacing does not match the data dimensions.
    """
    affine = np.eye(4)
    for i in range(len(spacing)):
        affine[i, i] = spacing[i]
    nift = nib.nifti1.Nifti1Image(data, affine)
    nib.nifti1.save(nift, file_path)

    if len(spacing) != data.ndim:
        raise ValueError("Voxel spacing does not match pixel data")



