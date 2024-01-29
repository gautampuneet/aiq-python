import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def apply_custom_color_map(image_array):
    """
    Apply a custom color map to the given image represented by a NumPy array.

    Parameters:
    - image_array: 2D NumPy array representing the grayscale image.

    Returns:
    - color_mapped_image: PIL Image object representing the color-mapped image.
    """

    # Define your custom color map logic here
    def custom_color_map(value):
        # This is a simple example; customize based on your needs
        return (value, 0, 255 - value)

    # Apply the custom color map to each pixel in the image_array
    height, width = image_array.shape
    color_mapped_pixels = np.zeros((height, width, 3), dtype=np.uint8)

    for i in range(height):
        for j in range(width):
            color_mapped_pixels[i, j] = custom_color_map(image_array[i, j])

    # Create a PIL Image from the color-mapped pixel values
    color_mapped_image = Image.fromarray(color_mapped_pixels, 'RGB')

    return color_mapped_image


# Example usage:
# Assuming 'image_array' is your 2D NumPy array representing the image
# Replace this with the actual image data from your context

# Generate a sample grayscale image for testing
image_array = [[
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    224,
    225,
    226,
    225,
    223,
    221,
    219,
    217]]
# image_array =   np.random.randint(0, 256, size=(200, 150), dtype=np.uint8)


image_array = np.array(image_array)

# Apply the custom color map
# color_mapped_image = apply_custom_color_map(image_array)
#
# # Display the original and color-mapped images
# fig, ax = plt.subplots(1, 2, figsize=(10, 5))
#
# ax[0].imshow(image_array, cmap='gray')
# ax[0].set_title("Original Image")
#
# ax[1].imshow(color_mapped_image)
# ax[1].set_title("Color-Mapped Image")
#
# plt.show()
