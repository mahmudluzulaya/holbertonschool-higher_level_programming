#!/usr/bin/python3
"""XML serialization and deserialization"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary into XML and saves it to a file.
    """
    try:
        # Create root element
        root = ET.Element("data")

        # Add each dictionary key/value as child elements
        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)  # Ensure text format

        # Build the tree and write to file
        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)

    except Exception:
        pass


def deserialize_from_xml(filename):
    """
    Deserializes XML from a file and returns a Python dictionary.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        result = {}

        # Each child becomes a key-value pair
        for child in root:
            result[child.tag] = child.text

        return result

    except Exception:
        return None
