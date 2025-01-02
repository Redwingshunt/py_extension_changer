import os

def append_txt_to_files(folder_path):
    try:
        # List all files in the folder
        for filename in os.listdir(folder_path):
            if filename =="Loop_files_rename_txt.py":
                continue
            file_path = os.path.join(folder_path, filename)
            # Check if it's a file
            if os.path.isfile(file_path):
                # Append ".txt" to the file's extension
                new_filename = f"{filename}.txt"
                new_file_path = os.path.join(folder_path, new_filename)
                os.rename(file_path, new_file_path)
                print(f"Renamed: {filename} -> {new_filename}")
    except Exception as e:
        print(f"An error occurred glanza: {e}")

# Example usage:
folder_path = "C://Users//vaiibbhav//Downloads//Compressed//New folder (2)//Debloat-Windows-10-master//scripts//"  # Replace with your folder path
append_txt_to_files(folder_path)
