import cv2
import argparse

arg = argparse.ArgumentParser()
arg.add_argument("-i","--image",required = True, help="Path to image")
args = vars(arg.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original Image",image)

(b, g, r) = image[120,10]
print(f"Original Contents of pixel [120,10] : Red {r}\n Green {g}\n Blue {b}")

image[120,10] = (0,0,200)
(b, g, r) = image[120,10]
print(f"Updated Contents of pixel [120,10] : Red {r}\n Green {g}\n Blue {b}")

corner = image[0:110,0:110]
cv2.imshow("Corner",corner)

image[0:110,0:110] = (0,100,0)
cv2.imshow("Colored Corner",image)
cv2.waitKey(0)
