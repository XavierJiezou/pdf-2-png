import os
import fitz
from tqdm import tqdm
from PIL import Image


def pdf2png(pdf_path: str, save_dir_name: str, zoom_x: int, zoom_y: int):
    """convert pdf to png

    Args:
        pdf_path (str): Path of pdf document
        save_dir_name (str): Save path of pictures in png format
        zoom_x (int): Set the resolution of pictures in png format
        zoom_y (int): Set the resolution of pictures in png format
    """
    os.makedirs(save_dir_name, exist_ok=True)
    doc = fitz.open(pdf_path)
    for page in tqdm(doc, desc='pdf2png: '): 
        pix = page.get_pixmap(matrix=fitz.Matrix(zoom_x, zoom_y))
        pix.writePNG(f'{save_dir_name}/{page.number+1}.png')
    doc.close()


def composite_long_graph(save_dir_name: str):
    """Composite long graph

    Args:
        save_dir_name (str): Save path of pictures in png format
    """
    imgs_list = [Image.open(os.path.join(save_dir_name, i))
                 for i in os.listdir(save_dir_name)]
    width, height = imgs_list[0].size
    result = Image.new(imgs_list[0].mode, (width, height * len(imgs_list)))
    for i, img in tqdm(enumerate(imgs_list), total=len(imgs_list), desc='composite_long_graph: '):
        result.paste(img, box=(0, i * height))
    result.save('long.png')


def main():
    """Main function
    """
    pdf2png("test.pdf", 'imgs', zoom_x=3, zoom_y=3)
    composite_long_graph('imgs')
    os.system('pause')


if __name__ == "__main__":
    main()