#!/usr/bin/python3
"""Generate personalized invitations from a template and a list of attendees."""
import os


def generate_invitations(template, attendees):
    """Generate invitation files for each attendee from a template.

    Args:
        template (str): Template string with placeholders.
        attendees (list): List of dictionaries with attendee data.
    """
    # Input type checks
    if not isinstance(template, str):
        print(f"Invalid template type: {type(template)}. Expected a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print(f"Invalid attendees type: {type(attendees)}. Expected a list of dictionaries.")
        return

    # Empty template check
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    # Empty attendees list check
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        content = template

        # Replace placeholders with attendee data or "N/A" if missing/None
        for placeholder in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(placeholder)
            if value is None:
                value = "N/A"
            content = content.replace(f"{{{placeholder}}}", str(value))

        # Generate output file
        output_filename = f"output_{index}.txt"
        try:
            with open(output_filename, "w", encoding="utf-8") as f:
                f.write(content)
        except Exception as e:
            print(f"Error writing file {output_filename}: {e}")
