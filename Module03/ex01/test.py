from ImageProcessor import ImageProcessor

IP = ImageProcessor()

arr = IP.load("./42AI.png")
IP.load("non_existent.png")
IP.load("./ImageProcessor.py")
print(arr)
IP.display(arr)
IP.display([3.4])