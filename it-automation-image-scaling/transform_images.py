#!/usr/bin/env python3
"""transform_images.py

Google Project 5 – Scaling and Converting Images using PIL (Pillow)

Scenario:
- A design contractor delivered icon images in the wrong format:
    * .tiff files
    * 192x192 resolution
    * Rotated 90° anti-clockwise
- You need to prepare them for the website:
    * Convert to .jpeg
    * Resize to 128x128
    * Rotate 90° clockwise (to straighten)

This script:
- Iterates through all image files in an input directory
- Opens each image with Pillow
- Rotates, resizes, converts to RGB (for JPEG)
- Saves the result into an output directory as .jpeg
"""

import os
from pathlib import Path

from PIL import Image


def process_images(input_dir: str, output_dir: str, size=(128, 128)):
    """Process all images in input_dir and save transformed versions in output_dir.

    Steps:
    - Rotate 90° clockwise
    - Resize to `size`
    - Convert to RGB
    - Save as .jpeg in output_dir

    Args:
        input_dir: Directory containing source images (.tiff, .png, etc.).
        output_dir: Directory to write transformed .jpeg icons.
        size: Target (width, height) tuple.
    """
    src = Path(input_dir)
    dst = Path(output_dir)
    dst.mkdir(parents=True, exist_ok=True)

    if not src.is_dir():
        print(f"[ERROR] Input directory not found: {src}")
        return

    for entry in src.iterdir():
        if not entry.is_file():
            continue

        # Only process typical image extensions; adjust as needed
        if entry.suffix.lower() not in {".tiff", ".tif", ".png", ".jpg", ".jpeg"}:
            continue

        try:
            with Image.open(entry) as img:
                # Rotate 90° clockwise (which is -90 degrees)
                rotated = img.rotate(-90, expand=True)
                # Resize
                resized = rotated.resize(size)
                # Ensure RGB for JPEG
                rgb_img = resized.convert("RGB")

                # Build output filename with .jpeg extension
                output_name = entry.stem + ".jpeg"
                output_path = dst / output_name

                rgb_img.save(output_path, "JPEG")
                print(f"[OK] Processed {entry.name} -> {output_path.name}")
        except Exception as e:
            print(f"[ERROR] Failed to process {entry.name}: {e}")


def main():
    # In the original lab:
    #   input dir: ~/images (unzipped from images.zip)
    #   output dir: /opt/icons/
    #
    # For portability, we default to:
    #   input: images/
    #   output: icons/
    #
    # You can override via environment variables:
    #   INPUT_DIR, OUTPUT_DIR
    input_dir = os.environ.get("INPUT_DIR", "images")
    output_dir = os.environ.get("OUTPUT_DIR", "icons")

    process_images(input_dir, output_dir)


if __name__ == "__main__":
    main()
