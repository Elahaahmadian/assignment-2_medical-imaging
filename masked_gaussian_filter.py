
import numpy as np
from scipy.ndimage import gaussian_filter

def masked_gaussian_filter(image, mask, sigma):
    """
    :param image: Numpy array containing image data
    :param mask: Boolean Numpy array with the same shape as image
    :param sigma: standard deviation of the gaussian filter as pixels, tuple of float

    """

    image = np.array(image)
    mask = np.array(mask)

    #raise valueError when arguments are incompatible
    if image.shape!= mask.shape:
        raise ValueError('image and mask must have the same shape')
    if mask.dtype != np.bool:
        raise ValueError('mask must be bool')

    #convert image and mask to 32-bit floating
    image = image.astype(np.float32)
    mask = mask.astype(np.float32)

    #Calculate and return M×(G(M×I, σ) / G(M, σ))
    smoothed_image = gaussian_filter(mask * image, sigma)
    smoothed_mask = gaussian_filter(mask, sigma)

    result = mask * (smoothed_image / smoothed_mask)
    result = np.nan_to_num(result, nan=0.0, posinf=0.0, neginf=0.0)

    return result












