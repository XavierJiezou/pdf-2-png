# PDF-2-PNG

Convert a `pdf` document to pictures in `png` format and combine them into a long picture.

## Intall

```bash
pip install -r requirements.txt
```

## Usage

```bash
git clone https://github.com/XavierJiezou/pdf-2-png.git
cd pdf-2-png
python main.py
```

## Build

```bash
pipenv install
pipenv shell
pip install requests tqdm
pip install pyinstaller
pyinstaller -F -i favicon.ico main.py
pipenv --rm
```

## Releases

### V1.0.1

- Fix the bug: Errors will be raised if there are spaces in the PDF file name.

**Download**

- [Pdf2png-1.0.1-win64.exe](https://github.com/XavierJiezou/pdf-2-png/releases/download/v1.0.1/Pdf2png-1.0.1-win64.exe)

### V1.0.0

- Pdf2png: a tool that can convert a pdf document to pictures in png format and combine them into a long picture.

**Download**

- [Pdf2png-1.0.0-win64.exe](https://github.com/XavierJiezou/pdf-2-png/releases/download/v1.0.0/Pdf2png-1.0.0-win64.exe)

## References

> - [how-to-make-images-from-document-pages](https://pymupdf.readthedocs.io/en/latest/faq.html#how-to-make-images-from-document-pages)
> - [PIL.Image.new](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.new)
