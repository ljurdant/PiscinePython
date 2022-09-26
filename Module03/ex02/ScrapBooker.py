import numpy as np

class ScrapBooker:
    def crop(self, array, dim, position=(0,0)):
        """
        Crops the image as a rectangle via dim arguments (being the new height
        and width of the image) from the coordinates given by position arguments.
        Args:
        -----
            array: numpy.ndarray
            dim: tuple of 2 integers.
            position: tuple of 2 integers.
        Return:
        -------
            new_arr: the cropped numpy.ndarray.
            None (if combinaison of parameters not compatible).
        Raise:
        ------
            This function should not raise any Exception.
        """
        try:
            new_arr = array[position[0]:dim[0] + 1, position[1]:dim[1]]
        except:
            return None
        if new_arr.shape == dim:
            return (new_arr)    

    def thin(self, array, n, axis):
        """
        Deletes every n-th line pixels along the specified axis (0: Horizontal, 1: Vertical)
        Args:
        -----
            array: numpy.ndarray.
            n: non null positive integer lower than the number of row/column of the array
            (depending of axis value).
            axis: positive non null integer.
        Return:
        -------
            new_arr: thined numpy.ndarray.
            None (if combinaison of parameters not compatible).
        Raise:
        ------
            This function should not raise any Exception.
        """
        try:
            new_arr = np.delete(array, np.s_[n-1::n], axis = not axis)
        except:
            return None

        if axis in (0,1) and n > 0 and new_arr.shape != array.shape:
            return (new_arr)

    def juxtapose(self, array, n, axis):
        """
        Juxtaposes n copies of the image along the specified axis.
        Args:
        -----
            array: numpy.ndarray.
            n: positive non null integer.
            axis: integer of value 0 or 1.
        Return:
        -------
            new_arr: juxtaposed numpy.ndarray.
            None (combinaison of parameters not compatible).
        Raises:
        -------
            This function should not raise any Exception.
        """
        try:
            new_arr = np.tile(array, ((not axis) * n + axis , axis * n + (not axis)))
        except:
            return None
        if axis in (0,1) and n > 0:
            return new_arr

    def mosaic(self, array, dim):
        """
        Makes a grid with multiple copies of the array. The dim argument specifies
        the number of repetition along each dimensions.
        Args:
        -----
            array: numpy.ndarray.
            dim: tuple of 2 integers.
        Return:
        -------
            new_arr: mosaic numpy.ndarray.
            None (combinaison of parameters not compatible).
        Raises:
        -------
            This function should not raise any Exception.
        """

        try:
            new_arr = np.tile(array, dim)
        except:
            return None
        return new_arr