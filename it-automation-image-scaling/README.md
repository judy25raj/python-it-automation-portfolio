# Google Project 5 – Scaling and Converting Images using PIL

This project is based on the **Google IT Automation with Python** lab  
**"Scaling and converting images using PIL"**.

## 🧩 Scenario

Your company is updating its website and hired a contractor to design new icon graphics.
Unfortunately, the contractor delivered the final files in the wrong format:

- `.tiff` images
- 192x192 resolution (too large)
- Rotated 90° anti-clockwise

You need to use Python and the **Pillow (PIL)** library to batch-fix these images so
they’re ready for the website launch:

- Convert to `.jpeg`
- Resize to **128x128**
- Rotate 90° clockwise (so they appear straight)
- Save all corrected images into a separate directory

---

## ✅ What This Project Demonstrates

- Using **Pillow (PIL)** to:
  - Open images
  - Rotate images
  - Resize images
  - Convert color modes (e.g. RGBA → RGB for JPEG)
  - Save images in a new format and location
- Iterating through a directory of files with **`pathlib` / `os`**
- Building a small, reusable batch-processing script

---

## 📂 Project Structure

```text
google-it-automation-image-scaling-pil/
├─ transform_images.py   # Main script: rotate, resize, convert, save as JPEG
├─ images/               # (Optional) Put your source images here (.tiff, .png, etc.)
└─ README.md             # This file
```

> In the original Google lab:
> - Input directory was `~/images` (unzipped from `images.zip`)
> - Output directory was `/opt/icons/`

In this standalone version:
- Default **input** directory is `images/`
- Default **output** directory is `icons/`
- You can override both via environment variables.

---

## ▶️ How It Works

### `transform_images.py`

- Iterates through all files in the input directory
- For each image file:
  1. Opens the image with `PIL.Image.open`
  2. Rotates it **90° clockwise** using:
     ```python
     rotated = img.rotate(-90, expand=True)
     ```
  3. Resizes it to **128x128**:
     ```python
     resized = rotated.resize((128, 128))
     ```
  4. Converts it to **RGB** to ensure JPEG compatibility:
     ```python
     rgb_img = resized.convert("RGB")
     ```
  5. Saves it into the output directory as `.jpeg` with the same base name:
     ```python
     rgb_img.save(output_path, "JPEG")
     ```

### Configuration

By default:

- `INPUT_DIR = "images"`
- `OUTPUT_DIR = "icons"`

You can change these via environment variables:

```bash
export INPUT_DIR="images"
export OUTPUT_DIR="icons"
```

---

## ▶️ How to Run

1. Install Pillow (PIL):

   ```bash
   pip install pillow
   ```

2. Place your input images in the `images/` directory  
   (for example, `.tiff` icons you got from a designer).

3. Run the script:

   ```bash
   python3 transform_images.py
   ```

4. Check the output directory:

   ```bash
   ls icons
   ```

   You should see `.jpeg` versions of your original icons, resized to 128x128 and rotated correctly.

In the original lab, you would:
- Unzip `images.zip` into `~/images`
- Save processed icons into `/opt/icons/`
- Confirm properties in a Python shell using `PIL.Image.open(...)` and inspecting `img.format, img.size`.

---

## 🧠 Project Story (Portfolio Narrative)

This project shows how I can use Python to solve a very practical problem in web
development and operations:

- I started with a batch of incorrectly formatted images from a contractor
  (wrong orientation, wrong size, and wrong file format).
- Using the Pillow library, I automated the image processing in a single script:
  rotating, resizing, and converting the icons to the required `.jpeg` format.
- The script is flexible:
  - It processes *all* images in a folder
  - It supports different input and output locations
  - It can be re-run whenever new icon sets are delivered

In real projects, this pattern can be reused for:
- Normalizing user-uploaded avatars or product images
- Preparing thumbnails for galleries
- Converting legacy image formats into web-friendly versions

You can describe this project as:

> "Automated a batch image-processing workflow using Python and Pillow to rotate,
> resize, and convert icon graphics into standardized JPEG assets ready for use on
> a production website."
