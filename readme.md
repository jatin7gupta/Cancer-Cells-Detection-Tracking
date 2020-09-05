# Cancer-Cells-Detection-Tracking
Detecting and Tracking cancer (HeLa) cells using Computer Vision techniques. The project also detects cell division and analyses cell motion such as speed, distance travelled etc. The project uses OpenCV3 for image processing.
![](phc.gif)

# Requirements
The application is intended to be run using Python 3.7+.

# Execution Instructions
Run main.py to launch the application.
The parameters of the application are sequence_directory and mode.
sequence_directory is the relative path to directory containing the sequence of images.
The mode parameter chooses the preprocessing and segmentation methods to be used, which depends on the imageset.

Modes: 
* 0: DIC-C2DH-HeLa
* 1: Fluo-N2DL-HeLa
* 2: PhC-C2DL-PSC

```
python3 main.py path/to/sequence mode 
```
Examples:
```
python3 main.py path/to/DIC/sequence 0 
```
```
python3 main.py path/to/Fluo/sequence 1 
```
```
python3 main.py path/to/PhC/sequence 2
```

During the run of the application, you can pause the animation at any time by pressing the 'Pause' button, and continue the animation by pressing the 'Continue' button.
After all images in the sequence have been processed and displayed, you can reset and start again from the beginning by pressing the 'Rerun' button.

### You can left-click on any segmented cell in the image at any time to show the metrics of that particular cell at the time it is clicked.

# Features
The image data to be used in the group project is taken from the international Cell Tracking Challenge (CTC) and is provided as sequences of images (one sequence for each timelapse microscopy recording). The data set contains multiple sequences from different biological experiments. The developed methods should work on all these data.
* Feature 1: Detect and Track Cells

    The program performs the following steps:
    1. Detect all the cells and draw a bounding box around each of them. For each image in a sequence the program should show the bounding boxes for that image only.
    2. Draw the trajectory (also called track or path) of each cell. For each image in a sequence the program should show for each cell the past trajectory up to that time point.
    3. Print (directly in the image window) the real-time count of the cells detected in each image of the sequence.
* Feature 2: Detect Cell Divisions
    1. Changes the colour of the cell’s bounding box for those time points during which the cell is in the process of dividing. After the division is complete, the program tracks the two daughter cells as new cells.
    2. Prints (directly in the image window) the real-time count of the cells that are dividing at each time point.
* Feature 3: Analyse Cell Motion
    1. Speed of the cell at that time point. This can be estimated by taking the Euclidean distance (in pixels) between the coordinates of the cell’s bounding box center in the current time point and the previous time point, divided by the time difference (the latter is simply 1 frame, so the unit of speed is pixels/frame).
    2. Total distance travelled up to that time point. This is the sum of the Euclidean distances (in pixels) computed from the first time point of a cell’s trajectory to the second, from the second to the third, and so on, until the current time point.
    3. Net distance travelled up to that time point. This is the Euclidean distance (in pixels) directly between the cell’s coordinates in the current time point and its coordinates in the first time point of its trajectory.
    4. Confinement ratio of the cell motion. This is the ratio between the total distance travelled by the cell up to the current time point (computed in 3-2) and the net distance travelled up to the current time point (computed in iii).
