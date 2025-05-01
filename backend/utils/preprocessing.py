# backend/utils/preprocessing.py
import numpy as np
import cv2
from PIL import Image, ImageOps

def preprocess_image(pil_img):
    img = pil_img.convert('L')  # Grayscale
    img = ImageOps.invert(img)  # Invert
    img_array = np.array(img)

    # Binarize using threshold
    _, img_array = cv2.threshold(img_array, 127, 255, cv2.THRESH_BINARY)

    # Find bounding box
    coords = cv2.findNonZero(255 - img_array)
    if coords is not None:
        x, y, w, h = cv2.boundingRect(coords)
        digit = img_array[y:y+h, x:x+w]
    else:
        digit = img_array  # fallback

    # Force pure binarization
    _, digit = cv2.threshold(digit, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Smooth strokes a little bit
    digit = cv2.GaussianBlur(digit, (3, 3), 0)

    # Resize to 20x20
    resized_digit = cv2.resize(digit, (20, 20), interpolation=cv2.INTER_AREA)

    # Center in 28x28
    canvas28 = np.zeros((28, 28), dtype=np.uint8)
    x_offset = (28 - 20) // 2
    y_offset = (28 - 20) // 2
    canvas28[y_offset:y_offset+20, x_offset:x_offset+20] = resized_digit

    # Perfect centering using center of mass
    M = cv2.moments(canvas28)
    if M["m00"] != 0:
        cx = int(M["m10"] / M["m00"])
        cy = int(M["m01"] / M["m00"])
    else:
        cx, cy = 14, 14
    shiftx = 14 - cx
    shifty = 14 - cy
    transform_matrix = np.float32([[1, 0, shiftx], [0, 1, shifty]])
    canvas28 = cv2.warpAffine(canvas28, transform_matrix, (28, 28))

    # Normalize
    canvas28 = canvas28.astype(np.float32) / 255.0

    # Flatten
    img_flatten = canvas28.flatten().reshape(1, -1)

    return img_flatten
