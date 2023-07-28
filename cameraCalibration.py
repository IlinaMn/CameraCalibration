import argparse
from helpers.cameraInfo import CameraInfo

if __name__ == '__main__':

    import pickle

    import numpy as np
    import cv2 as cv
    import glob

    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Camera Calibration')
    parser.add_argument('camera', help='Name of the camera')

    args = parser.parse_args()

    camera = args.camera

    # termination criteria
    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
    # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
    objp = np.zeros((6 * 8, 3), np.float32)
    objp[:, :2] = np.mgrid[0:8, 0:6].T.reshape(-1, 2)
    # Arrays to store object points and image points from all the images.
    objpoints = []  # 3d point in real world space
    imgpoints = []  # 2d points in image plane.

    images = glob.glob('./gridPhotos/*.jpg')

    print(images)

    for fname in images:
        img = cv.imread(fname)
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        # Find the chess board corners
        ret, corners = cv.findChessboardCorners(gray, (8, 6), None)
        # If found, add object points, image points (after refining them)
        if ret:
            objpoints.append(objp)

        corners2 = cv.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
        imgpoints.append(corners2)
        # Draw and display the corners
        cv.drawChessboardCorners(img, (8, 6), corners2, ret)
        cv.imshow('img', img)
        cv.waitKey(100)

        ret1, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

    cameraInfo = CameraInfo(mtx, dist)

    pickle_file = "./" + camera + ".pkl"

    # Pickle the object and save it to the file
    with open(pickle_file, "wb") as file:
        pickle.dump(cameraInfo, file)

    cv.destroyAllWindows()
