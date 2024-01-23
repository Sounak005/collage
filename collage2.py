import cv2
import numpy as np
# Load the two images
image1 = cv2.imread('image1.jpg')
image2 = cv2.imread('image2.jpg')
# Resize the images to a common size
image1 = cv2.resize(image1, (350, 300))
image2 = cv2.resize(image2, (350, 300))
# Create frames (black backgrounds) for each image
frame1 = np.zeros((300, 400, 3), dtype=np.uint8)
frame2 = np.zeros((300, 400, 3), dtype=np.uint8)
# Place the images within the frames
frame1[0:300, 0:350] = image1
frame2[0:300, 50:400] = image2
# Concatenate the two frames horizontally to create the combined image
combined_image = cv2.hconcat([frame1, frame2])
# Save the combined image
cv2.imwrite('combined_image.jpg', combined_image)
# Display the combined image
cv2.imshow('Combined Image', combined_image)
cv2.waitKey(0)
cv2.destroyAllWindows()