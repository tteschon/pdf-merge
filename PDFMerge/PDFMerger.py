#!/usr/bin/env python3

#import libraries
from operator import concat
import os
from PyPDF2 import PdfMerger
from tkinter import Tk
from tkinter.filedialog import askdirectory

#function that prompts user to select folder path for input
def GetFolderPath():
	path = askdirectory(title='Select Folder') # shows dialog box and return the path
	return path

#function that loops through all pdf's in the folder and merges them
def MergePDFsInFolder(path):
	#create merger obejct
	merger = PdfMerger()
	for pdf in os.listdir(path):
		print(path + pdf)
		if pdf.endswith(".pdf"):
			merger.append(path + "/" + pdf)
		else:
			continue
	# Write to an output PDF document
	merger.write(path + "/" + "merged-pdf.pdf")
	# Close File Descriptor
	merger.close()
	print("merge complete")