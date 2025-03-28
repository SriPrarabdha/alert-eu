import json
import os

def concatenate_json_files(file_list, output_file):
    """
    Concatenates multiple JSON files with potentially different keys into a single JSON file.

    Args:
        file_list (list): A list of file paths to the JSON files.
        output_file (str): The path to the output JSON file.
    """
    combined_data = {}

    for file_path in file_list:
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                for key, value in data.items():
                    if key in combined_data:
                        combined_data[key].extend(value) #extend the list if the key already exists
                    else:
                        combined_data[key] = value

        except FileNotFoundError:
            print(f"Error: File not found - {file_path}")
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON format in - {file_path}")
        except Exception as e:
            print(f"An unexpected error occurred processing {file_path}: {e}")

    with open(output_file, 'w') as outfile:
        json.dump(combined_data, outfile, indent=4)

# Example usage:
file_paths = ["new_alert_eu_prompts.json", "new_alert_eu_prompts1.json", "new_alert_eu_prompts2.json"] # Replace with your file paths
output_file_path = "combined.json"

concatenate_json_files(file_paths, output_file_path)
