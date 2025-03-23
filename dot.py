from PIL import Image
import numpy as np

# 正しい16色のパレットを定義
palette = [
    (0, 0, 0), (29, 43, 83), (126, 37, 83), (95, 87, 79), (171, 82, 54),
    (0, 135, 81), (131, 118, 156), (255, 0, 77), (255, 119, 168), (41, 173, 255),
    (255, 163, 0), (194, 195, 199), (0, 228, 54), (255, 204, 170), (255, 236, 39),
    (255, 241, 232)
]

# 画像を読み込む
img = Image.open('image.png')

# 画像を128x128にリサイズ
img = img.resize((128, 128))

# 画像をRGBに変換
img = img.convert('RGB')

# 画像をnumpy配列に変換
img_np = np.array(img)

# 各ピクセルを最も近いパレットの色に変換
def closest_color(pixel, palette):
    colors = np.array(palette)
    distances = np.sqrt(np.sum((colors - pixel) ** 2, axis=1))
    return tuple(colors[np.argmin(distances)])

# 画像全体を変換
new_img_np = np.array([[closest_color(pixel, palette) for pixel in row] for row in img_np])

# 変換した画像をPILイメージに戻す
new_img = Image.fromarray(np.uint8(new_img_np))

# 変換した画像を保存
new_img.save('converted_image.png')
