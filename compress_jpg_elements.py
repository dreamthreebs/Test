# this is code for compressing image but will decrease the quality of files.
from PIL import Image

# 打开 JPG 图像文件
with Image.open("image.jpg") as im:
    # 调整图像质量
    im = im.save("compressed_image.jpg", quality=10)
