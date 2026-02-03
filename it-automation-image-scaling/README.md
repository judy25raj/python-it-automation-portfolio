<h1 align="center">Scaling and Converting Images using PIL</h1>

<p align="center">
  Python • Pillow (PIL) • Batch Image Processing
</p>

<hr/>

This project is based on the Google IT Automation with Python lab
"Scaling and converting images using PIL".

## 🧩 Scenario
Your company is updating its website and hired a contractor to design new icon graphics. Unfortunately, the contractor delivered the final files in the wrong format:

- .tiff images  
- 192x192 resolution (too large)  
- Rotated 90° anti-clockwise  

You need to use Python and the Pillow (PIL) library to batch-fix these images so they’re ready for the website launch:

- Convert to .jpeg  
- Resize to 128x128  
- Rotate 90° clockwise (so they appear straight)  
- Save all corrected images into a separate directory  

## ✅ What This Project Demonstrates
Using Pillow (PIL) to:
- Open images  
- Rotate images  
- Resize images  
- Convert color modes (e.g. RGBA → RGB for JPEG)  
- Save images in a new format and location  
- Iterating through a directory of files with pathlib / os  
- Building a small, reusable batch-processing script  

## 📂 Project Structure
```
google-it-automation-image-scaling-pil/
├─ transform_images.py   # Main script: rotate, resize, convert, save as JPEG
├─ images/               # (Optional) Put your source images here (.tiff, .png, etc.)
└─ README.md             # This file
```

## ▶️ How It Works
**transform_images.py**
- Iterates through all files in the input directory
- For each image file:
  - Opens the image with PIL.Image.open
  - Rotates it 90° clockwise
  - Resizes it to 128x128
  - Converts it to RGB
  - Saves it into the output directory as .jpeg

## Configuration
By default:
- INPUT_DIR = "images"
- OUTPUT_DIR = "icons"

You can change these via environment variables.

## ▶️ How to Run
Install Pillow:
```
pip install pillow
```

Place your input images in the images/ directory.

Run:
```
python3 transform_images.py
```

Check output:
```
ls icons
```

## 🧠 Project Story (Portfolio Narrative)
This project shows how I can use Python to solve a very practical problem in web development and operations by automating image transformations for production-ready assets.
