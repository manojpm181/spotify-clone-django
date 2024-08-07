import cv2
import numpy as np

# Load the image
image_path = r("C:Users/manoj/OneDrive/Desktop/CGIP/uipath badge.png")
image = cv2.imread(image_path)

# Get the image dimensions
height, width, _ = image.shape

rotation_matrix=cv2.getRotationMatrix2D((height/2,width/2),45,1)
sacling_matrix=np.float32([[1.5,0,0],[0,1.5,0]])
translation_matrix=np.float32([[1,0,100],[0,1,50]])

rotated_img=cv2.warpAffine(image,rotation_matrix,(height,width))
scaled_img=cv2.warpAffine(image,sacling_matrix,(int(width*1.5),int(height*1.5)))
translated_img=cv2.warpAffine(image,translation_matrix,(height,width))


cv2.imshow("Rotated Image", rotated_img)
cv2.imshow("Scaled Image", scaled_img)
cv2.imshow("Translated Image", translated_img)

# Wait for a key press and then close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()