import cv2 as cv
import sys

from application import Application
from directory_reader import DirectoryReader
import global_vars

if __name__ == '__main__':
    # Check argv
    if len(sys.argv) < 3:
        sys.exit(
            'Missing required arguments!\n'
            'Parameters: sequence_directory mode\n'
            'Modes: 0 -> DIC, 1 -> Fluo, 2 -> PhC\n'
        )

    # Get files
    sequence_files = DirectoryReader(sys.argv[1]).get_sequence_files()
    if len(sequence_files) == 0:
        sys.exit(f"There are no files in '{sys.argv[1]}'.")

    # Init global vars
    global_vars.init()

    # Run App
    Application(sequence_files, int(sys.argv[2])).run()
