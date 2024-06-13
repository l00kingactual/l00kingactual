from PIL import Image, ImageDraw

# Function to create and save texture maps
def create_and_save_texture_map(file_name, color):
    texture_image = Image.new("RGB", (width, height))
    texture_draw = ImageDraw.Draw(texture_image)
    texture_draw.rectangle((0, 0, width, height), fill=color)
    texture_image.save(file_name)

# Input parameters (you can customize these)
width, height = 512, 512
base_color = (255, 255, 255)  # White base color
roughness_value = 128  # Grayscale (0-255)
normal_color = (128, 128, 255)  # RGB
bump_value = 128  # Grayscale (0-255)
metallic_value = 128  # Grayscale (0-255)
reflectivity_value = 128  # Grayscale (0-255)
transparency_value = 128  # Grayscale (0-255)
emission_color = (255, 128, 128)  # RGB
coating_roughness_value = 128  # Grayscale (0-255)
coating_bump_value = 128  # Grayscale (0-255)
displacement_value = 128  # Grayscale (0-255)
cutout_value = 128  # Grayscale (0-255)

# Create and save texture maps using input parameters
create_and_save_texture_map("base_color.png", base_color)
create_and_save_texture_map("roughness.png", (roughness_value, roughness_value, roughness_value))
create_and_save_texture_map("normal.png", normal_color)
create_and_save_texture_map("bump.png", (bump_value, bump_value, bump_value))
create_and_save_texture_map("metallic.png", (metallic_value, metallic_value, metallic_value))
create_and_save_texture_map("reflectivity.png", (reflectivity_value, reflectivity_value, reflectivity_value))
create_and_save_texture_map("transparency.png", (transparency_value, transparency_value, transparency_value))
create_and_save_texture_map("emission.png", emission_color)
create_and_save_texture_map("coating_roughness.png", (coating_roughness_value, coating_roughness_value, coating_roughness_value))
create_and_save_texture_map("coating_bump.png", (coating_bump_value, coating_bump_value, coating_bump_value))
create_and_save_texture_map("displacement.png", (displacement_value, displacement_value, displacement_value))
create_and_save_texture_map("cutout.png", (cutout_value, cutout_value, cutout_value))

print("Texture maps generated successfully!")
from PIL import Image

# Open the TIFF image
tiff_image = Image.open("input_image.tiff")

# Convert and save to different formats
tiff_image.save("output_image.jpg")  # Save as JPEG
tiff_image.save("output_image.png")  # Save as PNG
tiff_image.save("output_image.gif")  # Save as GIF
tiff_image.save("output_image.bmp")  # Save as BMP
tiff_image.save("output_image.tiff")  # Save as TIFF (optional)

print("Image conversion completed.")

