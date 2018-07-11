import cv2
import argparse

arg = argparse.ArgumentParser()
arg.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(arg.parse_args())

image = cv2.imread(args["image"])
print(f"Height of image {image.shape[0]}")
print(f"Width of image {image.shape[1]}")
print(f"Channels in image {image.shape[2]}")

cv2.imshow("Image",image)
cv2.waitKey(0)

cv2.imwrite("new_a.jpg",image)