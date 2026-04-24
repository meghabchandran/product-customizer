import cv2
import os
from django.conf import settings
from PIL import Image
import numpy as np

def apply_design(product_path, design_path, x, y, w, h):
    print("Product path:", product_path)
    print("Design path:", design_path)

    # Load product (BGR)
    product = cv2.imread(product_path)

    # Load design with transparency (IMPORTANT)
    design = cv2.imread(design_path, cv2.IMREAD_UNCHANGED)

    if product is None or design is None:
        print("ERROR: Image not loaded")
        return "output/error.png"

    # Resize design to fit area
    design = cv2.resize(design, (w, h))

    # Extract ROI
    roi = product[y:y+h, x:x+w]

    if roi.shape[0] == 0 or roi.shape[1] == 0:
        print("ERROR: ROI invalid")
        return "output/error.png"

    # =========================
    # HANDLE TRANSPARENCY
    # =========================
    if design.shape[2] == 4:
        # Split RGBA
        b, g, r, a = cv2.split(design)

        alpha = a / 255.0
        alpha = cv2.merge([alpha, alpha, alpha])

        design_rgb = cv2.merge([b, g, r])

        # Smooth blending (real print feel)
        blended = (roi * (1 - alpha) + design_rgb * alpha).astype("uint8")

    else:
        # If no transparency → create mask
        gray = cv2.cvtColor(design, cv2.COLOR_BGR2GRAY)
        _, mask = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)

        mask = cv2.GaussianBlur(mask, (21, 21), 0)
        mask = mask / 255.0
        mask = cv2.merge([mask, mask, mask])

        # Normalize
        roi_float = roi.astype(float) / 255
        design_float = design.astype(float) / 255

        # Blend (realistic print)
        blended_float = (roi_float * (1 - mask)) + (design_float * mask)
        blended = (blended_float * 255).astype("uint8")

    # Place back
    product[y:y+h, x:x+w] = blended

    # Convert to RGB for saving
    product_rgb = cv2.cvtColor(product, cv2.COLOR_BGR2RGB)

    # Save path
    output_path = "output/result.png"
    full_path = os.path.join(settings.MEDIA_ROOT, output_path)

    # Fix folder issue
    output_dir = os.path.dirname(full_path)

    if os.path.exists(output_dir) and not os.path.isdir(output_dir):
        os.remove(output_dir)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Save using Pillow
    Image.fromarray(product_rgb).save(full_path)

    print("Saved at:", full_path)

    return output_path