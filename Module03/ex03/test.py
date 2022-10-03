from ImageProcessor import ImageProcessor
from ColorFilter import ColorFilter


IP = ImageProcessor()
CF = ColorFilter()
arr = IP.load("../resources/elon_canaGAN.png")


inv = CF.invert(arr)
IP.display(inv)
blu = CF.to_blue(arr)
IP.display(blu)
green = CF.to_green(arr)
IP.display(green)
red = CF.to_red(arr)
IP.display(red)
cell = CF.to_celluloid(arr)
IP.display(cell)
grym = CF.to_grayscale(arr, "mean")
IP.display(grym)
gryw = CF.to_grayscale(arr, "weight", weights = [0.2, 0.3, 0.5])
IP.display(gryw)