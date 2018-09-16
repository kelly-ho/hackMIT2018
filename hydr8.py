import cv2, os, math, scipy.stats, pyqtgraph as plt

def getImageAbsorbence(imgName, i0):
    img = cv2.imread(imgName)
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

absorbs = []
concens = []

i0 = getI0(waterFile)

for img in range(0, len(imgNames)):
    concen = float(input("Concentration of sample "+imgNames[img] + ": "))
    concens.append(concen)
    absorbs.append(getImageAbsorbence("Pictures/"+imgNames[img], i0))

slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(concens, absorbs)
print("\nslope:", slope)
print("intercept", intercept)
unknownImgName = "Unknown/"+os.listdir("Unknown/.")[0]
unknownAbsorb = getImageAbsorbence(unknownImgName, i0)
print("Unknown sample's absorbance:", unknownAbsorb)
unknownConc = (unknownAbsorb - intercept) / slope
print("\nUNKNOWN SAMPLE'S CONCENTRATION:", unknownConc)

#API: Mapbox map https://api.mapbox.com/styles/v1/shobhita/cjm4yenu15g5a2rp0g1z3vifm.html?fresh=true&title=true&access_token=pk.eyJ1Ijoic2hvYmhpdGEiLCJhIjoiY2ptNHlkdjNxMHJ5ejNxa2M5djdxY2hydCJ9.EIpZ95tz6_5jj7XTs6-1tg#12.8/42.354520/-71.044705/0
