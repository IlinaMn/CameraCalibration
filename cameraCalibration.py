import argparse
from helpers.cameraInfo import CameraInfo
import pickle

import numpy as np
import cv2 as cv
import glob
import os

if __name__ == '__main__':

    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Camera Calibration')
    parser.add_argument('camera', help='Name of the camera')

    args = parser.parse_args()

    camera = args.camera

    # termination criteria
    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
    # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
    objp = np.zeros((7 * 4, 3), np.float32)
    objp[:, :2] = np.mgrid[0:7, 0:4].T.reshape(-1, 2)
    # Arrays to store object points and image points from all the images.
    objpoints = []  # 3d point in real world space
    imgpoints = []  # 2d points in image plane.

    images = glob.glob('./gridPhotos/*.jpg')

    if not os.path.exists(f'{camera}.pkl'):

        if glob.glob(f'gridPhotos/{camera}_*'):
            for fname in images:
                img = cv.imread(fname)
                gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
                # Find the chess board corners
                ret, corners = cv.findChessboardCorners(gray, (7, 4), None)
                # If found, add object points, image points (after refining them)
                if ret:
                    objpoints.append(objp)
                corners2 = cv.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
                imgpoints.append(corners2)
                # Draw and display the corners
                cv.drawChessboardCorners(img, (7, 4), corners2, ret)
                cv.imwrite(f'out/{fname}', img)
                cv.imshow('img', img)
                cv.waitKey(0)

                ret1, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

            cameraInfo = CameraInfo(mtx, dist)

            pickle_file = 'matrix/' + camera + ".pkl"

            # Pickle the object and save it to the file
            with open(pickle_file, "wb") as file:
                pickle.dump(cameraInfo, file)
            print(f'Camera matrix saved in file matrix/{camera}.pkl')

            cv.destroyAllWindows()
        else:
            print("First you need to capture grid photos with this camera. Move them into the gridPhotos folder.")
    else:
        print('This Camera was already calibrated')
