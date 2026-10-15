import read
import writenif

def dicom_to_nifti(filepath_in, filepath_out):
    d_data, d_spacing = read.read_dicom(filepath_in)
    writenif.write_nifti(d_data, d_spacing, filepath_out)

