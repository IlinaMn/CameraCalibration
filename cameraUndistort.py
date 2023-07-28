import pickle
import argparse
import os

import cv2 as cv
from helpers.cameraInfo import CameraInfo

# Parse command line arguments
parser = argparse.ArgumentParser(description='Camera Calibration')
parser.add_argument('camera', help='Name of the camera')
parser.add_argument('image_folder', help='Path to the folder containing the images to be calibrated')
parser.add_argument('output_folder', help='Relative path to save the calibrated images')
parser.add_argument('--alpha',
                    help='Optional argument.Set the percentage of valid information in the undistorted image. Default 1'
                    ,
                    default='1')

args = parser.parse_args()

alpha = int(args.alpha)

# Load camera calibration data
camera = args.camera
file = f"{camera}.pkl"
with open(file, "rb") as file:
    cameraInfo = pickle.load(file)

# Iterate over images in the specified folder
image_folder = args.image_folder
output_folder = args.output_folder

first_image_path = os.path.join(image_folder, os.listdir(image_folder)[0])
first_image = cv.imread(first_image_path)
h, w = first_image.shape[:2]

# Compute optimal new camera matrix and ROI
newcameramtx, roiCoords = cv.getOptimalNewCameraMatrix(cameraInfo.cameraMatrix, cameraInfo.dist, (w, h), alpha, (w, h))

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(image_folder):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        # Read image
        image_path = os.path.join(image_folder, filename)
        img = cv.imread(image_path)

        # Undistort image
        dst = cv.undistort(img, cameraInfo.cameraMatrix, cameraInfo.dist, None, newcameramtx)

        # Save the calibrated image
        output_path = os.path.join(output_folder, filename)
        cv.imwrite(output_path, dst)
