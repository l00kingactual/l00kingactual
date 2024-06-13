import xml.etree.ElementTree as ET

# Path to the map.i3d file
map_i3d_path = r'C:\Users\actua\OneDrive\Documents\My Games\FarmingSimulator2022\mods\FS22_4xBlankMap\maps\mapUS\map.i3d'


def update_map_boundaries(file_path, size):
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Find the TerrainTransformGroup element
    terrain_group = root.find(".//TerrainTransformGroup")

    if terrain_group is not None:
        # Remove existing Terrain elements if any
        for terrain in terrain_group.findall('Terrain'):
            terrain_group.remove(terrain)

        # Add new Terrain element with updated size
        ET.SubElement(terrain_group, "Terrain", translation="0 0 0", size=f"{size} {size}", heightMapSize="4097", lodBlendStart="20", lodBlendEnd="100", lodDistance="500")
        
        # Write changes back to the file
        tree.write(file_path, encoding="utf-8", xml_declaration=True)
        print(f"Updated map boundaries to {size} x {size} meters.")
    else:
        print("TerrainTransformGroup element not found in the map.i3d file.")

# Update boundaries for a 4x map (8192 x 8192 meters)
update_map_boundaries(map_i3d_path, 8192)

def set_terrain_layer(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    terrain_group = root.find(".//TerrainTransformGroup")

    if terrain_group is not None:
        for terrain_layer in terrain_group.findall('TerrainLayer'):
            terrain_group.remove(terrain_layer)

        ET.SubElement(terrain_group, "TerrainLayer", id="0", name="default", materialId="default", textureId="default")
        tree.write(file_path, encoding="utf-8", xml_declaration=True)
        print("Set TerrainLayer in the map.i3d file.")
    else:
        print("TerrainTransformGroup element not found in the map.i3d file.")

set_terrain_layer(map_i3d_path)
