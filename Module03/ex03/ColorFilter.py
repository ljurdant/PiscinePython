from re import M
import numpy as np


class ColorFilter:
    def invert(self, array):
        """
        Inverts the color of the image received as a numpy array.
        Args:
        -----
            array: numpy.ndarray corresponding to the image.
        Return:
        -------
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
        -------
            This function should not raise any Exception.
        """
        try:
            return (1 - array)
        except:
            return None

    def to_blue(self, array):
        """
        Applies a blue filter to the image received as a numpy array.
        Args:
        -----
            array: numpy.ndarray corresponding to the image.
        Return:
        -------
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
        -------
            This function should not raise any Exception.
        """
        try:
            return (np.dstack((np.zeros(array.shape)[:,:,:2],array[:,:,2:])))
        except:
            return None

    def to_green(self, array):
        """
        Applies a green filter to the image received as a numpy array.
        Args:
        -----
            array: numpy.ndarray corresponding to the image.
        Return:
        -------
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
        -------
            This function should not raise any Exception.
        """
        try:
            return array*[0,1,0]
        except:
            None
    
    def to_red(self, array):
        """
        Applies a red filter to the image received as a numpy array.
        Args:
        -----
            array: numpy.ndarray corresponding to the image.
        Return:
        -------
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
        -------
            This function should not raise any Exception.
        """
        # print(array[:,:,2:])
        # print(array - self.to_blue(array))
        try:
            return array - self.to_blue(array) - self.to_green(array)
        except:
            return None
    
    def to_celluloid(self, array):
        """
        Applies a celluloid filter to the image received as a numpy array.
        Celluloid filter must display at least four thresholds of shades.
        Be careful! You are not asked to apply black contour on the object,
        you only have to work on the shades of your images.
        Remarks:
            celluloid filter is also known as cel-shading or toon-shading.
        Args:
        -----
            array: numpy.ndarray corresponding to the image.
        Return:
        -------
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
        -------
            This function should not raise any Exception.
        """
        shades = 4
        try:
            values = np.linspace(array.min(),array.max(),num=shades)
            new_arr = np.copy(array)
            for i in range(1, shades):
                new_arr[(new_arr > values[i - 1])&(new_arr <= values[i])] = values[i]
            return (new_arr)
        except:
            return None
    
    def to_grayscale(self, array, filter, **kwargs):
        """
        Applies a grayscale filter to the image received as a numpy array.
        For filter = 'mean'/'m': performs the mean of RBG channels.
        For filter = 'weight'/'w': performs a weighted mean of RBG channels.
        Args:
        -----
            array: numpy.ndarray corresponding to the image.
            filter: string with accepted values in ['m','mean','w','weight']
            weights: [kwargs] list of 3 floats where the sum equals to 1,
            corresponding to the weights of each RBG channels.
        Return:
        -------
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
        -------
            This function should not raise any Exception.
        """

        try:
            new_arr = np.copy(array)
            if filter in ["m", "mean"]:
                if len(kwargs):
                    raise
                for i in new_arr:
                    for j in i:
                        m = np.sum(j) / 3
                        for k in range(3):
                            j[k] = m
            elif filter in ["w","weight"]:
                w = kwargs["weights"]
                if len(w) != 3 or sum(w) !=  1 or len(kwargs) != 1:
                    raise
                for i in new_arr:
                    for j in i:
                        m = sum(j*w)
                        for k in range(3):
                            j[k]=m
        except:
            return None
        return new_arr