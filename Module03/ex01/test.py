from ImageProcessor import ImageProcessor

IP = ImageProcessor()

arr = IP.load("./42AI.png")
IP.load("non_existent.png")
IP.load("./ImageProcessor.py")
IP.load(None)
print(arr)
IP.display(arr)
IP.display([3.4])
IP.display(None)