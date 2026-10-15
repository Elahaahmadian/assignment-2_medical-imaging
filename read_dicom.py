from pydicom import dcmread
import os
import numpy as np

def get_z_position(dicom_image):
    """
    Returns the z-coordinate of the Image Position Patient DICOM attribute.
    """
    return dicom_image.ImagePositionPatient[2]

def read_dicom(path):
    """
    Takes in DICOM file or directory path.

    If path is file (single 2D image): returns image array in HU and pixel spacing.

    If path is directory (3D array of images): returns image array in HU and voxel spacing.
    """

    file_list = []
    dicom_image = []

    # For single 2D Dicom Image
    if os.path.isfile(path) == True:

        dicom_image = dcmread(path)

        # Convert pixel values to physical units
        pixel_values = dicom_image.pixel_array
        intercept = dicom_image.RescaleIntercept
        slope = dicom_image.RescaleSlope

        ct_values = (slope * pixel_values) + intercept

        # Get pixel spacing
        row_spacing, column_spacing = dicom_image.PixelSpacing

        pixel_spacing = (row_spacing, column_spacing)

        return ct_values, pixel_spacing

    # For 3D array of Dicom Images
    elif os.path.isdir(path) == True:

        # Create an array of each file path in directory
        for file_name in os.listdir(path):
            full_name = os.path.join(path, file_name)
            file_list.append(full_name)

        file_array = np.array(file_list)
        unsorted_dicom_image = []

        # Sort images in order of z position
        try:
            for i in range(len(file_array)):
                unsorted_dicom_image.append(dcmread(file_array[i]))
        except InvalidDicomError:                                    #Ignore non-DICOM files in directory and keep iterating
            print(f'{file_array[i]} is not a DICOM file')

        sorted_dicom_image = sorted(unsorted_dicom_image, key=get_z_position)

        # Convert to HU
        for i in range(len(sorted_dicom_image)):
            dicom_image.append((sorted_dicom_image[i].RescaleSlope * sorted_dicom_image[i].pixel_array) + sorted_dicom_image[i].RescaleIntercept)

        # Get pixel spacing
        row_spacing, column_spacing = dcmread(file_list[0]).PixelSpacing

        # Get slice thickness
        slice_thickness = sorted_dicom_image[1].ImagePositionPatient[2] - sorted_dicom_image[0].ImagePositionPatient[2]

        voxel_spacing = (row_spacing, column_spacing, slice_thickness)

        # Make sure all DICOM Images have the same Series Instance UID
        for i in range(len(file_list)):
            if dcmread(file_list[0]).SeriesInstanceUID != dcmread(file_list[i]).SeriesInstanceUID:
                raise ValueError("All DICOM Images do not share the same Series Instance UID")

        return dicom_image, voxel_spacing
