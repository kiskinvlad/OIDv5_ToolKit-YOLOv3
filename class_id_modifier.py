import os
import sys

def modify_first_symbol_in_lines(folder_path, new_class_id):
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "r") as file:
                lines = file.readlines()

            modified_lines = [new_class_id + line[1:] for line in lines]

            with open(file_path, "w") as file:
                file.writelines(modified_lines)
            print(f"Modified '{filename}': Class id in each image label changed to '{new_class_id}'")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py folder_path new_class_id")
    else:
        folder_path = sys.argv[1]
        new_class_id = sys.argv[2]
        modify_first_symbol_in_lines(folder_path, new_class_id)
