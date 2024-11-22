from PIL import Image

# XSS payload
xss_payload = "<script>alert('XSS');</script>"

# Open an image file
image = Image.open("original.jpg")

# Convert the image to RGB mode
image = image.convert("RGB")

# Get the image dimensions
width, height = image.size

# Create a new image with the same dimensions
new_image = Image.new("RGB", (width, height))

# Paste the original image onto the new image
new_image.paste(image)

# Draw the XSS payload onto the new image
draw = ImageDraw.Draw(new_image)
draw.text((10, 10), xss_payload, fill=(255, 255, 255))

# Save the modified image
new_image.save("injected.jpg")
