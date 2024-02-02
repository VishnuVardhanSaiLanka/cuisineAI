import os

def rename_folders(directory, common_suffix):
    # Ensure the directory exists
    if not os.path.exists(directory):
        print(f"The directory {directory} does not exist.")
        return

    # Iterate over all items in the directory
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        
        # Check if it's a folder/directory
        if os.path.isdir(item_path):
            # Check and remove the suffix if present
            if item.endswith(common_suffix):
                new_name = item[:-len(common_suffix)]  # Remove the suffix
                new_path = os.path.join(directory, new_name)
                os.rename(item_path, new_path)
                print(f"Renamed '{item}' to '{new_name}'")

# Example usage
directory = '/Users/vishnu_lanka/projects/pixie/cuisineAI/data_indexing/screenshots'  # Replace with your directory path
common_suffix = '.f616'  # Replace with the common suffix you want to remove
rename_folders(directory, common_suffix)
