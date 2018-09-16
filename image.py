import cv2, os, math, scipy.stats

def getImageAbsorbence(imgName, i0):
    img = cv2.imread("Pictures/"+imgName)
    height = img.shape[0]
    width = img.shape[1]

    imgSeg = img[height//2-int(0.05*height):height//2+int(0.05*height), width//2-int(0.05*width):width//2+int(0.05*width)]
    cv2.imwrite("croppedImage.jpg", imgSeg)

    #order is blue, green, red
    average_color = [imgSeg[:, :, i].mean() for i in range(img.shape[-1])]

    finalColorRead = max(average_color)
    color = average_color.index(finalColorRead)
    gbr = {0:"blue", 1:"green", 2:"red"}
    print("Avg", gbr[color],"color:", finalColorRead)

    i = finalColorRead
    absorbence = math.log10(i/i0)
    return absorbence

def getI0(imgName):
    img = cv2.imread("Pictures/"+imgName)
    height = img.shape[0]
    width = img.shape[1]

    imgSeg = img[height//2-int(0.05*height):height//2+int(0.05*height), width//2-int(0.05*width):width//2+int(0.05*width)]
    cv2.imwrite("croppedImage.jpg", imgSeg)

    average_color = [imgSeg[:, :, i].mean() for i in range(img.shape[-1])]

    finalColorRead = max(average_color)
    return (finalColorRead)

imgNames = os.listdir('Pictures/.')
print(imgNames)

for i,a in enumerate(imgNames):
    print ('%d - %s' % (i, a))

waterIndex = int(input("Water image: "))
waterFile = imgNames[waterIndex]
imgNames.remove(imgNames[waterIndex])
print(imgNames)

absorbs = []
concens = []

i0 = getI0(waterFile)

for img in range(0, len(imgNames)):
    concen = float(input("Concentration of sample "+imgNames[img] + ": "))
    concens.append(concen)
    absorbs.append(getImageAbsorbence(imgNames[img], i0))

slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(absorbs, concens)
print("slope:", slope)
print("intercept", intercept)

unknown = float(input("Unknown sample's absorbance: "))
unknownConc = (unknown - intercept) / slope
print(unknownConc)
