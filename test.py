
import numpy as np
from pmi_lib.write_nifti import write_nifti

def test_files(file_path):
    image = np.zeros((10, 10, 10))
    spacing = (1.0, 1.0, 1.0)

    write_nifti(image, spacing, file_path)

test_files("src/pmi_lib/images/test.nii.gz")
