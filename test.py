
import read
import writenif
import dicomnifti
import maskgaus
from pmi_viewer import view

def test(file_path):
    d_data, d_spacing = read.read_dicom(file_path)
    writenif.write_nifti(d_data, d_spacing, 'images/test.nii.gz')
    n_data, n_spacing = read.read_nifti('images/test.nii.gz')
    dicomnifti.dicom_to_nifti(file_path, 'images/test2.nii.gz')

    mask = d_data > 600
    if len(d_spacing) == 2:
        sigma = (1.0, 1.0)
    elif len(d_spacing) == 3:
        sigma = (1.0, 1.0, 1.0)
    masked_image = maskgaus.masked_gaussian_filter(d_data, mask, sigma)
    return d_data, d_spacing, n_data, n_spacing, masked_image

d_data, d_spacing, n_data, n_spacing, masked_image = test('images/ct_jaw')
view(d_data, spacing=d_spacing, orientation='sag')
view(n_data, spacing= n_spacing, orientation='sag')
