import read
import writenif

@click.command()
@click.argument('dicom_path',type=click.Path(exists=True, file_okay=True),required=True,help='DICOM file or directory of DICOM files to be converted to nifti.')
@click.argument('nifti_path',type=click.Path(exists=True, file_okay=True),required=True,help='Path to save nifti file to.')

def dicom_to_nifti(dicom_path, nifti_path):
    d_data, d_spacing = read.read_dicom(dicom_path)
    writenif.write_nifti(d_data, d_spacing, nifti_path)

