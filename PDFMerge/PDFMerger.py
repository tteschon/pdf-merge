#!/usr/bin/env python3

#import libraries
import os
import logging
from PyPDF2 import PdfMerger
from tkinter import Tk
from tkinter.filedialog import askdirectory

#function that prompts user to select folder path for input
def GetFolderPath():
    path = askdirectory(title='Select Folder') # shows dialog box and return the path
    return path

#function that loops through all pdf's in the folder and merges them
def MergePDFsInFolder(path):
    """
    Merges all PDF files in the given input folder and writes the result to a new PDF file with the same name as the input folder.

    Args:
        path (str): The path to the input folder.

    Returns:
        None

    Example:
        # assume that input folder contains the following files:
        # - file1.txt
        # - file2.pdf
        # - file3.pdf
        # - file4.txt
        # - file5.pdf
        MergePDFsInFolder("input_folder")
        # this will create a new file named "input_folder.pdf" containing the merged PDFs
    """
    # create logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    # create console handler
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # add formatter to ch
    ch.setFormatter(formatter)
    # add ch to logger
    logger.addHandler(ch)

    # check if input folder exists
    if not os.path.isdir(path):
        logger.error("Input folder does not exist")
        return

    # create merger object
    merger = PdfMerger()
    pdf_count = 0
    for pdf in os.listdir(path):
        if pdf.endswith(".pdf"):
            merger.append(path + "/" + pdf)
            pdf_count += 1
        else:
            continue

    # check if at least one PDF was found
    if pdf_count == 0:
        logger.warning("No PDFs found in input folder")
        return

    # create output file name
    output_file = os.path.basename(os.path.normpath(path)) + ".pdf"

    # write to an output PDF document
    try:
        merger.write(path + "/" + output_file)
    except Exception as e:
        logger.error("Error while writing to output file: {}".format(e))
        return

    # close file descriptor
    merger.close
