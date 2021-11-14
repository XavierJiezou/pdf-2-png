import os
import sys
import fitz
from tqdm import tqdm
from PIL import Image


def pdf2png(pdf_path: str, save_dir_name: str = 'imgs', zoom_x: int = 3, zoom_y: int = 3):
    """convert pdf to png

    Args:
        pdf_path (str): Path of pdf document
        save_dir_name (str): Save path of pictures in png format. Default to `imgs`
        zoom_x (int): Set the resolution of pictures in png format. Default to 3
        zoom_y (int): Set the resolution of pictures in png format. Default to 3
    """
    os.makedirs(save_dir_name, exist_ok=True)
    doc = fitz.open(pdf_path)
    for page in tqdm(doc, desc='Pdf2png: '): 
        pix = page.get_pixmap(matrix=fitz.Matrix(zoom_x, zoom_y))
        pix.writePNG(f'{save_dir_name}/{page.number+1}.png')
    doc.close()


def composite_long_graph(save_dir_name: str = 'imgs'):
    """Composite long graph

    Args:
        save_dir_name (str): Save path of pictures in png format
    """
    imgs_list = [Image.open(os.path.join(save_dir_name, i)) for i in os.listdir(save_dir_name)]
    width, height = imgs_list[0].size
    result = Image.new(imgs_list[0].mode, (width, height * len(imgs_list)))
    for i, img in tqdm(enumerate(imgs_list), total=len(imgs_list), desc='Combine: '):
        result.paste(img, box=(0, i * height))
    result.save('long.png')


def main(save_dir_name: str = 'imgs', zoom_x: int = 3, zoom_y: int = 3):
    """Main function
    """
    try:
        pdf_path = input('Please input the path of pdf document: ').replace('\\', '/')
        pdf_path = eval(pdf_path) if '"' in pdf_path else pdf_path
        pdf2png(pdf_path, save_dir_name, zoom_x, zoom_y)
        composite_long_graph(save_dir_name)
    except Exception as e:
        print(e)
    os.system('pause')


if __name__ == "__main__":
    main()
