import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

image_path = "path/for/your/image"
image = Image.open(image_path)

image_array = np.array(image)

height, width, channels = image_array.shape

downsampling_factor = 20

rgb_values = np.zeros(((height // downsampling_factor) + 1, (width // downsampling_factor) + 1, 3))

for i in range(0, height, downsampling_factor):
    for j in range(0, width, downsampling_factor):
        if channels == 4:  # RGB + Alpha
            r, g, b, _ = image_array[i, j] / 255.0
        else:  # RGB without Alpha
            r, g, b = image_array[i, j, :3] / 255.0
        rgb_values[i // downsampling_factor, j // downsampling_factor] = np.array([r, g, b])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Constant height for the bars
bar_height = 1

for i in range(rgb_values.shape[0]):
    for j in range(rgb_values.shape[1]):
        r, g, b = rgb_values[i, j]
        # Normalize RGB values
        total_intensity = r + g + b
        if total_intensity != 0:
            normalized_r = r / total_intensity
            normalized_g = g / total_intensity
            normalized_b = b / total_intensity
        else:
            # Handle the case when total_intensity is zero
            normalized_r, normalized_g, normalized_b = 0, 0, 0

        # Calculate heights for each segment based on normalized values
        height_r = normalized_r * bar_height
        height_g = normalized_g * bar_height
        height_b = normalized_b * bar_height

        dz = [height_r, height_g, height_b]
        if height_r == 0 and height_g == 0 and height_b == 0:
            colors = [(1, 1, 1), (1, 1, 1), (1, 1, 1)]
        else:
            colors = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]

        z_pos = 0
        for x in range(3):
            ax.bar3d(j, i, z_pos, .25, .25, dz[x], color=colors[x])
            z_pos += dz[x]

ax.set_xlabel('Width')
ax.set_ylabel('Height')
ax.set_zlabel('RGB Composition')

plt.show()
