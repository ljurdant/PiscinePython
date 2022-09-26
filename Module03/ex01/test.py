from ImageProcessor import ImageProcessor

IP = ImageProcessor()

arr = IP.load("./elon_canaGAN.png")
IP.load("non_existent.png")
IP.load("./ImageProcessor.py")
print(arr)
IP.display(arr)
IP.display([3.4])