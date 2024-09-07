from PIL import Image, ImageOps

def compress_image(input_path, output_path, quality=85):
    """Compress JPEG/JPG image while maintaining quality."""
    try:
        with Image.open(input_path) as img:
            img = ImageOps.exif_transpose(img)
            # Convert to RGB (necessary for JPEGs in some cases)
            img = img.convert("RGB")

            # Save the image with the specified quality (default 85)
            img.save(output_path, "JPEG", optimize=True, quality=quality)
            print(f"Image saved at {output_path} with quality={quality}")
    except Exception as e:
        print(f"Error compressing image: {e}")
