from PIL import Image, ImageDraw

# Create a new image with a specified size (e.g., 512x512 pixels)
width, height = 512, 512
base_color = (255, 255, 255)  # White base color
base_image = Image.new("RGB", (width, height), base_color)

# Function to create and save texture maps
def create_and_save_texture_map(file_name, color):
    texture_image = Image.new("RGB", (width, height))
    texture_draw = ImageDraw.Draw(texture_image)
    texture_draw.rectangle((0, 0, width, height), fill=color)
    texture_image.save(file_name)

# 1. Base Color Map
create_and_save_texture_map("base_color.png", base_color)

# 2. Roughness Map (Grayscale)
roughness_value = 128  # Adjust this value as needed
create_and_save_texture_map("roughness.png", (roughness_value, roughness_value, roughness_value))

# 3. Normal Map (RGB)
normal_color = (128, 128, 255)  # Adjust this color as needed
create_and_save_texture_map("normal.png", normal_color)

# 4. Bump Map (Grayscale)
bump_value = 128  # Adjust this value as needed
create_and_save_texture_map("bump.png", (bump_value, bump_value, bump_value))

# 5. Metallic Map (Grayscale)
metallic_value = 128  # Adjust this value as needed
create_and_save_texture_map("metallic.png", (metallic_value, metallic_value, metallic_value))

# 6. Reflectivity Map (Grayscale)
reflectivity_value = 128  # Adjust this value as needed
create_and_save_texture_map("reflectivity.png", (reflectivity_value, reflectivity_value, reflectivity_value))

# 7. Transparency Map (Grayscale)
transparency_value = 128  # Adjust this value as needed
create_and_save_texture_map("transparency.png", (transparency_value, transparency_value, transparency_value))

# 8. Emission Map (RGB)
emission_color = (255, 128, 128)  # Adjust this color as needed
create_and_save_texture_map("emission.png", emission_color)

# 9. Coating Roughness Map (Grayscale)
coating_roughness_value = 128  # Adjust this value as needed
create_and_save_texture_map("coating_roughness.png", (coating_roughness_value, coating_roughness_value, coating_roughness_value))

# 10. Coating Bump Map (Grayscale)
coating_bump_value = 128  # Adjust this value as needed
create_and_save_texture_map("coating_bump.png", (coating_bump_value, coating_bump_value, coating_bump_value))

# 11. Displacement Map (Grayscale)
displacement_value = 128  # Adjust this value as needed
create_and_save_texture_map("displacement.png", (displacement_value, displacement_value, displacement_value))

# 12. Cutout (Opacity) Map (Grayscale)
cutout_value = 128  # Adjust this value as needed
create_and_save_texture_map("cutout.png", (cutout_value, cutout_value, cutout_value))

print("Texture maps generated successfully!")
