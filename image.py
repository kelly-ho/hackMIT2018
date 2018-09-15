import cv2
import math


def getImageAbsorbence(imgName):
    img = cv2.imread("12.jpg")
    height = img.shape[0]
    width = img.shape[1]

    print(height, width)

    imgSeg = img[height//2-int(0.05*height):height//2+int(0.05*height), width//2-int(0.05*width):width//2+int(0.05*width)]
    cv2.imwrite("croppedImage.jpg", imgSeg)

    #order is blue, green, red
    average_color = [imgSeg[:, :, i].mean() for i in range(img.shape[-1])]

    print(average_color)

    finalColorRead = max(average_color)
    color = average_color.index(finalColorRead)
    gbr = {0:"blue", 1:"green", 2:"red"}
    print("Avg", gbr[color],"color:", finalColorRead)

    i0 = 255
    i = finalColorRead
    absorbence = math.log10(i/i0)
    return absorbence

imgNames = []
calibration = {}

for img in range(1, len(imgNames)+1):
    conc = input("Concentration of sample", img)
    abs = getImageAbsorbence(img)
    calibration[abs] = conc
