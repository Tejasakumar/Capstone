import os
import random
import shutil


def move_random_files(source_folder, destination_folder, num_files=75):
    # Ensure both folders exist
    if not os.path.isdir(source_folder):
        print(f"Source folder '{source_folder}' does not exist.")
        return
    if not os.path.isdir(destination_folder):
        os.makedirs(destination_folder)
        print(f"Destination folder '{destination_folder}' created.")

    # List all files in the source folder
    files = [f for f in os.listdir(source_folder) if os.path.isfile(
        os.path.join(source_folder, f))]

    # Check if there are enough files to move
    if len(files) < num_files:
        print(f"Not enough files to move. Only found {len(files)} files.")
        num_files = len(files)  # Adjust to available file count

    # Randomly select files
    files_to_move = random.sample(files, num_files)

    # Move each file to the destination folderfiles/test/mal/
    for file_name in files_to_move:
        source_path = os.path.join(source_folder, file_name)
        destination_path = os.path.join(destination_folder, file_name)
        shutil.move(source_path, destination_path)
        print(f"copied: {file_name}")

    print(
        f"Successfully moved {num_files} files from '{source_folder}' to '{destination_folder}'.")


# Example usage
source_folder = r"malconv/train/mal"
destination_folder = r"malconv/test/mal"
move_random_files(source_folder, destination_folder,3000)