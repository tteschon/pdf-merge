import os
from PDFMerge import PDFMerger

def main():
    # get the folder path
    path = PDFMerger.GetFolderPath()
    # merge the files
    PDFMerger.MergePDFsInFolder(path)
    # open the folder path
    os.startfile(path)

if __name__ == "__main__":
    main()
