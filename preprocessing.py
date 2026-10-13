import cv2
import numpy as np

def preprocess_image(image_bytes: bytes):
    # Convert bytes to a numpy array, then decode into an OpenCV image
    nparr = np.frombuffer(image_bytes, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply denoising to remove background artifacts
    denoised = cv2.fastNlMeansDenoising(gray, h=30)

    # Apply Otsu's binarization to create a crisp black-and-white image
    _, binarized = cv2.threshold(denoised, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    return binarized