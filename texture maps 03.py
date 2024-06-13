from PIL import Image, ImageDraw

# Create a new image with a specified size (e.g., 512x512 pixels)
width, height = 512, 512
base_color = (255, 255, 255)  # White base color
base_image = Image.new("RGB", (width, height), base_color)

# 1. Base Color Map
base_image.save("base_color.png")

# 2. Roughness Map (Grayscale)
roughness_image = Image.new("L", (width, height))
roughness_draw = ImageDraw.Draw(roughness_image)
roughness_value = 128  # Adjust this value as needed
roughness_draw.rectangle((0, 0, width, height), fill=roughness_value)
roughness_image.save("roughness.png")

# 3. Normal Map (RGB)
normal_image = Image.new("RGB", (width, height))
normal_draw = ImageDraw.Draw(normal_image)
normal_color = (128, 128, 255)  # Adjust this color as needed
normal_draw.rectangle((0, 0, width, height), fill=normal_color)
normal_image.save("normal.png")

# 4. Bump Map (Grayscale)
bump_image = Image.new("L", (width, height))
bump_draw = ImageDraw.Draw(bump_image)
bump_value = 128  # Adjust this value as needed
bump_draw.rectangle((0, 0, width, height), fill=bump_value)
bump_image.save("bump.png")

# Repeat the process for other maps (e.g., metallic, displacement, etc.)

print("Texture maps generated successfully!")
