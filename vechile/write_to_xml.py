import xml.etree.ElementTree as ET
from xml.dom import minidom
import os

vehicles = []
current_vehicle = {}

# Get the directory of the current Python file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "data.txt")

with open(DATA_FILE, "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()

        if line.startswith("---"):
            if current_vehicle:
                vehicles.append(current_vehicle)
                current_vehicle = {}
        elif "=" in line:
            key, value = line.split("=", 1)
            current_vehicle[key.strip()] = value.strip()

if current_vehicle:
    vehicles.append(current_vehicle)

print("Parsed vehicles:")
print(vehicles)

root = ET.Element("Vehicles")

for vehicle in vehicles:
    vehicle_element = ET.SubElement(root, "Vehicle")
    for key, value in vehicle.items():
        child = ET.SubElement(vehicle_element, key)
        child.text = value

rough = ET.tostring(root, "utf-8")
pretty = minidom.parseString(rough).toprettyxml(indent="  ")

xml_path = os.path.join(BASE_DIR, "vehicles.xml")
with open(xml_path, "w", encoding="utf-8") as f:
    f.write(pretty)

print("vehicles.xml created successfully")
