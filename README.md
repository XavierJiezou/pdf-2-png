# PDF-2-PNG

Convert a pdf document to pictures in png format and combine them into a long picture.

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
## Reference

> - [https://pymupdf.readthedocs.io/en/latest/faq.html#how-to-make-images-from-document-pages](https://pymupdf.readthedocs.io/en/latest/faq.html#how-to-make-images-from-document-pages)
> - [https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.new](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.new)
