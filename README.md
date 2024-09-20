# PDF Merger

## About
Python script that merges pdf files.

The script will prompt you for the folder location of the PDF files, merge them in their current order (it is advised to pre-order them prior to merging), and then create a merged PDF file in the same folder named 'merged-pdf'. The target folder will open when finished.

## Installation

1. **Clone the repository:**
   <br>*clone using [Github CLI](https://cli.github.com/)*
   ```bash
   gh repo clone tteschon/pdf-merge
    ```
2. **Create a virtual environment *(optional but recommended)*:**
   ```bash
   python -m venv venv
   ```
   activate the virtual environment:
    ```bash
    source venv/bin/activate
    ```
3. **Install the package:**<br>
    *(the '.' assumes you are installing from within the project folder that contains the pyproject.toml file)* 
    ```bash
    python -m pip install .
    ```
4. **Run the script:**
    ```bash
    pdf-merge
    ```

## Dependencies
- PyPDF2
