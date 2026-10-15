import os
import click


# @click.command()
# @click.argument('dicom_path',type=click.Path(exists=True, file_okay=True),required=True,help='DICOM file or directory of DICOM files to be converted to nifti.')
# @click.argument('nifti_path',type=click.Path(exists=True, file_okay=True),required=True,help='Path to save nifti file to.')


def dicom_to_nifti(dicom_path, nifti_path):
    '''
    Converts DICOM file or directory of DICOM files to Nifti images.

    If directory contains non DICOM file, it will be ignored.
    '''

    dicom_image, voxel_spacing = read_dicom(dicom_path)

    # try:
    if os.path.isfile(dicom_path) == True:

        write_nifti(dicom_image, voxel_spacing, nifti_path)

    elif os.path.isdir(dicom_path) == True:
        file_index = 0
        for i in range(len(dicom_image)):
            write_nifti(dicom_image[i], voxel_spacing, f'{nifti_path}/{file_index}')
            file_index += 1

            # try:
            #     write_nifti(dicom_image[i], voxel_spacing, f'{nifti_path}/{file_index}')
            #     file_index+=1
            # except InvalidDicomError:
            #     continue

    # except FileNotFoundError:
    #     print(f'Could not find {dicom_path}')

    # except InvalidDicomError:
    #     print(f'{dicom_path} is not a DICOM file')

    # except TypeError:
    #     print(f'dicom_path argument must be string')




