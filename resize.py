import re

from PIL import Image
import glob
from natsort import natsorted


FOLDER_PATH = "./photos"
# PATTERN = r"[a-zA-Z0-9_\-]+\.png$"    # 正規表現
SHRINK = 2  # 縮小率


def main():
    file_paths = natsorted(glob.glob(f"{FOLDER_PATH}/*"))

    for file_path in file_paths:
        img = Image.open(file_path)  # 画像を読み込む

        PATTERN = file_path[9:]  # ファイル名の取得
        match = re.search(PATTERN, file_path)

        if match:
            img_name = match.group()
        else:
            raise AssertionError("NoMatchPattern")

        width, height = (
            img.width // SHRINK,
            img.height // SHRINK,
        )  # 画像のサイズを変更

        # 画像をリサイズする
        img_resized = img.resize((width, height))

        # ファイルを保存
        img_resized.save(f"resized_photos/{img_name}", quality=90)


if __name__ == "__main__":
    main()
