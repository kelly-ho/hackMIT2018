import cv2

img = cv2.imread("12.jpg")

calibration = {}

#Get specific pixels from image
height = img.shape[0]
width = img.shape[1]

print(height, width)

imgSeg = img[height//2-int(0.05*height):height//2+int(0.05*height), width//2-int(0.05*width):width//2+int(0.05*width)]
cv2.imwrite("croppedImage.jpg", imgSeg)

#order is blue, green, red
average_color = [imgSeg[:, :, i].mean() for i in range(img.shape[-1])]

print(average_color)

color = average_color.index(max(average_color))
gbr = {0:"blue", 1:"green", 2:"red"}

print("Avg", gbr[color],"color:", max(average_color))
