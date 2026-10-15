import os

import nibabel as nib
import numpy as np
from pydicom import dcmread
from pydicom.pixels import apply_rescale
from pmi_viewer import view

def read_nifti(file_path):

    nifti_image = nib.load(file_path)  # Read the image.
    spacing = nifti_image.header.get_zooms()

    return nifti_image.get_fdata(), spacing

def get_z_position(dicom_image):
    """
    Returns the z-coordinate of the Image Position Patient DICOM attribute.
    """
    return dicom_image.ImagePositionPatient[2]

def get_spacing(dicom_list):
    n = len(dicom_list)
    dx, dy = dicom_list[0].PixelSpacing

    if n > 1:
        z_first = np.array(dicom_list[0].ImagePositionPatient)
        z_last = np.array(dicom_list[-1].ImagePositionPatient)
        dz = np.linalg.norm(z_last - z_first) / (n - 1)
        return [dx, dy, dz]
    else:
        return [dx, dy]


def read_dicom(file_path):
    if os.path.isdir(file_path):
        dicom_image_list = []
        for file_name in os.listdir(file_path):  # Iterate over all items in path_name.
            full_name = os.path.join(file_path,
                                     file_name)  # Join the directory name and item name using the system path separator (\ or /).
            dicom_image = dcmread(full_name)
            dicom_image_list.append(dicom_image)  # this part gets the data and puts it in a list

        dicom_sort = sorted(dicom_image_list, key=get_z_position)  # this part sorts the data

        spacing = get_spacing(dicom_sort)  # here you get the spacing

        dicom_sort_image = []
        for dicom_image in dicom_sort:
            dicom_sort_image.append((dicom_image.pixel_array))  # this part extracts the pixel data from the sorted data
        return np.asarray(dicom_sort_image), spacing

    else:
        dicom_image = dcmread(file_path)
        spacing = get_spacing([dicom_image])
        return np.asarray(dicom_image.pixel_array), spacing
