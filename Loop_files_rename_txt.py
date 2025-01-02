import os

def append_txt_to_files(folder_path, new_file_extension):
    try:
        # List all files in the folder
        for filename in os.listdir(folder_path):
            if filename =="Loop_files_rename_txt.py":
                continue
            file_path = os.path.join(folder_path, filename)
            # Check if it's a file
            if os.path.isfile(file_path):
                if filename[-4]==".": #.$$$ extension
                    n = len(filename)
                    new_filename = filename[:n-4]
                    new_filename+=new_file_extension
                    new_file_path = os.path.join(folder_path, new_filename)
                    os.rename(file_path, new_file_path)
                    print(f"Renamed: {filename} -> {new_filename}")
                elif filename[-5]==".": #.$$$$ extension
                    n = len(filename)
                    new_filename = filename[:n-5]
                    new_filename+=new_file_extension
                    new_file_path = os.path.join(folder_path, new_filename)
                    os.rename(file_path, new_file_path)
                    print(f"Renamed: {filename} -> {new_filename}")
                else :  #.$$ extension
                    n = len(filename)
                    new_filename = filename[:n-2]
                    new_filename+=new_file_extension
                    new_file_path = os.path.join(folder_path, new_filename)
                    os.rename(file_path, new_file_path)
                    print(f"Renamed: {filename} -> {new_filename}")
    except Exception as e:
        print(f"An error occurred glanza: {e}")
"""adding the extension here
getting the pwd for the file and working on basis of the user input...

after taking the input the program will change the extension accordingly at O(n)


"""
printing_msg = "whats the extension it has to be renamed to"
print(printing_msg.center(36, '*'))




new_file_extension = input("exe / pdf / txt / zip / rar / xlcs / dll // etc....")
print()
if new_file_extension[0]!=".":
    new_file_extension = "." + new_file_extension

folder_path = "C://Users//vaiibbhav//Downloads//Compressed//New folder (2)//Debloat-Windows-10-master//scripts//"  # Replace with your folder path
append_txt_to_files(folder_path,new_file_extension)
