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
![](phc.gif)

During the run of the application, you can pause the animation at any time by pressing the 'Pause' button, and continue the animation by pressing the 'Continue' button.
After all images in the sequence have been processed and displayed, you can reset and start again from the beginning by pressing the 'Rerun' button.

### You can left-click on any segmented cell in the image at any time to show the metrics of that particular cell at the time it is clicked.

