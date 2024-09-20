#!/usr/bin/env python3

#import libraries
import os
from datetime import datetime
import logging
from tkinter.filedialog import askdirectory
from PyPDF2 import PdfMerger

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

    # Initialize merger object
    merger = PdfMerger()

    # set PDF counter to 0
    pdf_count = 0

    # loop through all files in the input folder
    for filename in os.listdir(path):
        # check if file is a PDF
        if filename.endswith(".pdf"):
            logger.info("Merging file: %s", filename)
            # create full file path to the PDF
            filepath = os.path.join(path, filename)
            # append PDF to the merger object
            merger.append(filepath)
            # increment PDF counter
            pdf_count += 1
        else:
            # skip non-PDF files
            continue

    # check if at least one PDF was found
    if pdf_count == 0:
        logger.warning("No PDFs found in input folder")
        return

    # create output file name
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file_name = f"merged_{os.path.basename(os.path.normpath(path))}_{timestamp}.pdf"
    logger.info("Output file name: %s", output_file_name)
    
    # Define the output file path
    output_path = os.path.normpath(os.path.join(path, output_file_name))
    logger.info("Output file path: %s", output_path)

    # write to an output PDF document
    try:
        with open(output_path, 'wb') as output_file:
            merger.write(output_file)
    except Exception as e:
        logger.error("Error while writing to output file: %s", e)
        return

    # close merger object
    merger.close()

    print("complete")
