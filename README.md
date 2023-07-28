# CameraCalibration
Automate camera calibration for distortion-free imaging. Supports various camera models, visualization tools, and easy customization. Open-source, Python-based. Get precise measurements for computer vision, 3D reconstruction, and robotics.

# Camera Calibration Script

This script performs camera calibration to obtain accurate and distortion-free imaging. It calibrates the camera using a set of images of a chessboard pattern.

## Prerequisites
- Python 3.x
- OpenCV (cv2) library
- NumPy library

## Usage
1. Make sure you have the required dependencies installed.
2. Organize your chessboard images in the `gridPhotos` folder, where each image captures the chessboard pattern from different angles.
3. Run the script by executing the following command in the terminal:

```
python cameraCalibration.py <camera_name>
```

Replace `<camera_name>` with a descriptive name for your camera setup.

The script will process the images, find the chessboard corners, and calibrate the camera using the collected data. The resulting camera matrix and distortion coefficients will be saved in a pickle file with the `<camera_name>.pkl` format.

**Note:** Ensure that your chessboard images are properly captured and cover various angles to achieve accurate calibration.

For any questions or issues, feel free to open an [issue](link-to-issues) on this repository.

**Disclaimer:** This project is provided as-is without any warranty. Use it at your own risk.

## License
This project is licensed under the [MIT License](link-to-license-file).
