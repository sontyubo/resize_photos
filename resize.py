import re
from PIL import Image

import glob
from natsort import natsorted


FOLDER_PATH = './photos'


def main():

    pattern = r'IMG_\d*\.JPG'

    file_paths = natsorted(glob.glob(f'{FOLDER_PATH}/*'))
    #file_paths = ['./photos/IMG_7443.JPG']

    for file_path in file_paths:

        # リサイズ前の画像を読み込み
        img = Image.open(file_path)

        match = re.search(pattern, file_path)

        if match:
            img_name = match.group()
        else:
            raise AssertionError('NoMatchPattern')

        # 読み込んだ画像の幅、高さを取得し半分に
        (width, height) = (img.width // 2, img.height // 2)

        # 画像をリサイズする
        img_resized = img.resize((width, height))

        # ファイルを保存
        img_resized.save(f'resized_photos/{img_name}', quality=90)

if __name__ == '__main__':
    main()
