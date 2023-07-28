# CameraCalibration
Automate camera calibration for distortion-free imaging. Supports various camera models, visualization tools, and easy customization. Open-source, Python-based. Get precise measurements for computer vision, 3D reconstruction, and robotics.

# Camera Calibration Script

This script performs camera calibration to obtain accurate and distortion-free imaging. It calibrates the camera using a set of images of a chessboard pattern.

## Prerequisites
- Python 3.10
- OpenCV
- NumPy

## Usage
1. Make sure you have the required dependencies installed.
2. Organize your chessboard images in the `gridPhotos` folder, where each image captures the chessboard pattern from different angles.
3. Run the script by executing the following command in the terminal:

```
python cameraCalibration.py <camera_name>
```

Replace `<camera_name>` with a descriptive name for your camera setup.

The script will process the images, find the chessboard corners, and calibrate the camera using the collected data. The resulting camera matrix and distortion coefficients will be saved in a pickle file with the `<camera_name>.pkl` format.

# Camera Undistortion Script

This script performs camera undistortion using the camera calibration data obtained from a previously calibrated camera. It processes a set of images from a specified folder and saves the undistorted images to another folder.

## Prerequisites
- Python 3.10
- OpenCV
- NumPy library

## Usage
1. Ensure you have the required dependencies installed.
2. Make sure you have previously calibrated your camera and saved the calibration data as a pickle file (e.g., `camera.pkl`).
3. Organize the images you want to undistort in the `image_folder`.
4. Run the script by executing the following command in the terminal:

```
python cameraUndistort.py <camera_name> <image_folder> <output_folder> --alpha <alpha_value>
```

Replace the placeholders with the appropriate values:
- `<camera_name>`: The name of the previously calibrated camera.
- `<image_folder>`: The path to the folder containing the images to be undistorted.
- `<output_folder>`: The relative path to save the undistorted images.
- `--alpha <alpha_value>`: (Optional) Set the percentage of valid information in the undistorted image. The default value is 1.

The script will load the camera calibration data, undistort each image in the specified folder, and save the undistorted images to the output folder. The undistortion process utilizes the optimal new camera matrix and region of interest (ROI) for accurate results.

**Note:** Ensure that the images are properly captured and correspond to the previously calibrated camera to achieve accurate undistortion.

For any questions or issues, feel free to open an issue on this repository.

**Disclaimer:** This project is provided as-is without any warranty. Use it at your own risk.

## License
This project is licensed under the MIT License.
