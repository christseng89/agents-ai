# OCR Scanned PDFs

## Installation Instructions
```cmd
choco install tesseract
choco install ghostscript
choco install pngquant
pip install ocrmypdf

set PATH=%PATH%;C:\Users\%USERNAME%\AppData\Roaming\Python\Python310\Scripts
ocrmypdf --version
    16.10.2
ocrmypdf input_scanned.pdf output_searchable.pdf

```