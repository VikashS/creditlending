import os
import shutil


def load_data(src_folder, dest_folder):
    # Ensure the destination folder exists
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    # Iterate over all files in the source folder
    for filename in os.listdir(src_folder):
        src_file = os.path.join(src_folder, filename)
        dest_file = os.path.join(dest_folder, filename)

        # Copy each file to the destination folder
        if os.path.isfile(src_file):
            shutil.copy(src_file, dest_file)
            print(f'Copied: {src_file} to {dest_file}')


if __name__ == "__main__":
    source_folder = '../../ingection_data/'
    destination_folder = '../../datalake/bronze_layer/'
    load_data(source_folder, destination_folder)
