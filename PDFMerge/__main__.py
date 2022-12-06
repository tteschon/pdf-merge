from PDFMerger import GetFolderPath, PdfMerger

def main():
    # get the folder path
    path = GetFolderPath()
    # merge the files
    PdfMerger(path)

if __name__ == "__main__":
    main()
