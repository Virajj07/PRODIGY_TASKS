from PIL import Image


def swap_pixels(pixels):
    # Function to swap pixel values
    return pixels[1], pixels[0], pixels[2]


def apply_math_operation(pixels, key):
    # Function to apply a basic math operation to each pixel
    r, g, b = pixels
    return (r + key) % 256, (g + key) % 256, (b + key) % 256


def encrypt_image(input_path, output_path, key, encryption_method):
    # Open the image
    img = Image.open(input_path)

    # Ensure the image is in RGB mode
    img = img.convert("RGB")

    # Get the pixel data
    pixels = img.load()

    # Encrypt each pixel based on the selected method
    width, height = img.size
    for i in range(width):
        for j in range(height):
            # Handle different modes (RGB, RGBA, etc.)
            try:
                if encryption_method == "swap":
                    pixels[i, j] = swap_pixels(pixels[i, j])
                elif encryption_method == "math":
                    pixels[i, j] = apply_math_operation(pixels[i, j], key)
            except ValueError:
                # In case of different modes, use the first three channels
                if encryption_method == "swap":
                    pixels[i, j] = swap_pixels(pixels[i, j][:3]) + (255,)
                elif encryption_method == "math":
                    pixels[i, j] = apply_math_operation(
                        pixels[i, j][:3], key) + (255,)

    # Save the encrypted image
    img.save(output_path)


def decrypt_image(input_path, output_path, key, encryption_method):
    # Open the encrypted image
    img = Image.open(input_path)

    # Ensure the image is in RGB mode
    img = img.convert("RGB")

    # Get the pixel data
    pixels = img.load()

    # Decrypt each pixel based on the selected method
    width, height = img.size
    for i in range(width):
        for j in range(height):
            # Handle different modes (RGB, RGBA, etc.)
            try:
                if encryption_method == "swap":
                    pixels[i, j] = swap_pixels(pixels[i, j])
                elif encryption_method == "math":
                    # Invert the math operation for decryption
                    pixels[i, j] = apply_math_operation(pixels[i, j], -key)
            except ValueError:
                # In case of different modes, use the first three channels
                if encryption_method == "swap":
                    pixels[i, j] = swap_pixels(pixels[i, j][:3]) + (255,)
                elif encryption_method == "math":
                    pixels[i, j] = apply_math_operation(
                        pixels[i, j][:3], -key) + (255,)

    # Save the decrypted image
    img.save(output_path)

# Example usage


def main():
    # Put the path to your input image here
    input_image_path = r'C:\Users\Viraj\OneDrive\Desktop\prodigy projects\image.png'

    # Put the path for the encrypted image to be saved
    encrypted_image_path = r'C:\Users\Viraj\OneDrive\Desktop\prodigy projects\encrypted_image.png'

    # Put the path for the decrypted image to be saved
    decrypted_image_path = r'C:\Users\Viraj\OneDrive\Desktop\prodigy projects\decrypted_image.png'

    # Choose an encryption key
    encryption_key = 123  # You can choose any integer key

    # Choose an encryption method ("swap" or "math")
    encryption_method = "swap"  # Change to "math" for mathematical operation

    # Encryption
    encrypt_image(input_image_path, encrypted_image_path,
                  encryption_key, encryption_method)
    print("Image encrypted and saved at:", encrypted_image_path)

    # Decryption
    decrypt_image(encrypted_image_path, decrypted_image_path,
                  encryption_key, encryption_method)
    print("Image decrypted and saved at:", decrypted_image_path)


if __name__ == "__main__":
    main()
