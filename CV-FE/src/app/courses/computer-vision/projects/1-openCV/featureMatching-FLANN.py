"""
#SIFT Detector: Identifies distinctive keypoints in both images that are invariant to scale and rotation.

FLANN Matcher: Efficiently matches descriptors between images using approximate nearest neighbors, which is faster than brute-force matching for large datasets.

Lowe's Ratio Test: Filters out ambiguous matches by comparing the distance of the closest match to the second-closest match, retaining only those where the closest is significantly better
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the images in grayscale
img1 = cv2.imread('image1.jpg', cv2.IMREAD_GRAYSCALE)  # Query image
img2 = cv2.imread('image2.jpg', cv2.IMREAD_GRAYSCALE)  # Train image

# Initialize SIFT detector
sift = cv2.SIFT_create()

# Detect keypoints and compute descriptors
keypoints1, des1 = sift.detectAndCompute(img1, None)
keypoints2, des2 = sift.detectAndCompute(img2, None)

# Set FLANN parameters
FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
search_params = dict(checks=50)

# Initialize FLANN matcher
flann = cv2.FlannBasedMatcher(index_params, search_params)

# Perform KNN matching with k=2
matches = flann.knnMatch(des1, des2, k=2)

# Apply Lowe's ratio test to filter good matches
good_matches = []
for m, n in matches:
    if m.distance < 0.7 * n.distance:
        good_matches.append(m)

# Draw matches
result_img = cv2.drawMatches(img1, keypoints1, img2, keypoints2, good_matches, None, flags=2)

# Display the result
plt.figure(figsize=(12, 6))
plt.imshow(result_img)
plt.title('Feature Matching with SIFT and FLANN')
plt.axis('off')
plt.show()
