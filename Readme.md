# Image RGB 3d Bar Visualization

This script performs image downsampling and visualizes the pixel by pixel RGB composition of an image in a 3D bar plot.

## Features

- Down samples an image to enhance readability
- Converts an image to a NumPy array for processing
- Support for RGB and RGB + Alpha Channels: whether your image has RGB channels only or includes an Alpha channel, the
  script can handle both cases for accurate plotting
- Visualizes the RGB composition using a 3D bar plot
- Normalizes the RGB composition of each pixel, with each bar's height representing the total intensity
- All bars are plotted to the same height, with each segment (R, G, B) proportional to its composition
- Adjustable downsampling factor to fine-tune the level of detail
- Simple usage with minimal dependencies

## Requirements

- Python 3.7+
- NumPy
- Pillow (PIL)
- Matplotlib

## Installation

1. Clone the repository or download the script:

    ```bash
    git clone https://github.com/osstd/plot_rgb_3dbar_.git
    cd pixelizer-3dbar
    ```

2. Install the required packages:

    ```bash
    pip install numpy pillow matplotlib
    ```

## Usage

1. Edit the `local.py` file to specify the path to your image:

    ```bash
    image_path = "path/to/your/image"
    ```

2. Run the script:

    ```bash
    python local.py
    ```

3. The script will open the specified image, downs sample it, and display a 3D bar plot of the RGB composition.

### Additional Notes

1. Adjust the `downsampling_factor` variable for better readability of pixel values:

    ```bash
    downsampling_factor = 20
    ```

    variable for better readability of pixel values.

2. Could also experiment with the `bar_height` variable for different bar normalization heights

    ````bash
   bar_height = 1
    ````

## Demonstration

[For demonstration](https://what-is-a-pixel-vercel.vercel.app/visualize3)

## Examples

![Demonstration](https://i.imgur.com/OgOWNX6.png)

![Demonstration](https://i.imgur.com/cbyt7CY.png)

![Demonstration](https://i.imgur.com/tUACK9n.png)

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.