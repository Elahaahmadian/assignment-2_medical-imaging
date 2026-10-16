import numpy

class Image:
    """
    Represents an N-dimensional image.

    :param data: The image data as a NumPy array.
    :param spacing: The pixel spacing in mm of the image as a tuple of floats.
    """

    def __init__(self, data: numpy.ndarray, spacing:tuple[float,float,float]=None):
        self.data = data
        self.spacing = spacing

        if self.spacing != None:
            if len(self.data.shape) != len(self.spacing):
                raise ValueError("Image dimensions are incompatible with specified spacing.")

        if self.spacing != None:
            if not isinstance(self.spacing,tuple):
                raise TypeError("The spacing must be a tuple of floats.")

        if not isinstance(self.data, numpy.ndarray):
            raise TypeError("The image data must be a NumPy array.")

    def __repr__(self):
        return f'A {type(self.data)} image with shape {self.data.shape} and a spacing of {self.spacing} mm.'

    def get_pixel_area(self):
        if len(self.spacing) < 2:
            raise ValueError("Pixel spacing must consist of at least two floats.")
        else:
            return self.spacing[0] * self.spacing[1]


    def get_voxel_volume(self):
        if len(self.spacing) < 3:
            raise ValueError("Pixel spacing must consist of three floats.")
        else:
            return self.spacing[0] * self.spacing [1] * self.spacing[2]

class DicomImage(Image):
    def __init__(self, data, spacing, metadata):
        super().__init__(data, spacing)

    if not isinstance(self.metadata, dict):
        raise TypeError("The metadata must be a dictionary.")