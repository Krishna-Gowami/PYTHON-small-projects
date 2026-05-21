# QR Code Generator

A simple Python program to generate QR codes from URLs and save them as PNG images. The program keeps track of generated QR codes using a counter and allows custom naming.

## Features

- Generate QR codes from user-provided URLs
- Automatic counter for unique file naming
- Custom name input for each QR code
- Saves images in a specified output directory
- Automatically opens the latest generated QR code image
- Error handling for counter file operations

## Requirements

- Python 3.x
- Libraries:
  - `qrcode[pil]` (includes PIL support)
  - `Pillow` (PIL)

## Installation

1. Ensure Python 3.x is installed on your system.
2. Install the required libraries using pip:

   ```
   pip install pillow qrcode[pil]
   ```

   Or if using a virtual environment:

   ```
   python -m pip install pillow qrcode[pil]
   ```

## Usage

1. Run the script:

   ```
   python main.py
   ```

2. Enter the URL when prompted.
3. Enter a name for the QR code file.
4. The QR code will be generated, saved, and automatically opened.

The generated QR codes are saved in the `Output-png` directory with filenames like `QR-{name}-{counter}.png`.

## File Structure

- `main.py`: Main script for QR code generation
- `Output-png/`: Directory for saved QR code images
- `Output-png/QR_Code_counter/QRCounter.txt`: File to track the number of generated QR codes

## Notes

- The program uses a counter file to ensure unique filenames.
- Images are saved in PNG format.
- The latest generated image is automatically opened after creation.

## License

This project is open-source. Feel free to modify and distribute.
