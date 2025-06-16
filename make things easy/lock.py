import os
import time
import shutil
from zipfile import ZipFile

def lock_folder_zip(folder_name, lock_seconds):
    user_home = os.path.expanduser("~")
    desktop_path = os.path.join(user_home, "Desktop")
    documents_path = os.path.join(user_home, "Documents")

    original_folder = os.path.join(desktop_path, folder_name)
    zip_base_name = os.path.join(documents_path, folder_name)
    zip_file = zip_base_name + ".zip"

    # Check if the folder exists
    if not os.path.exists(original_folder):
        print(f" Folder '{folder_name}' not found on Desktop.")
        return

    print(f" Locking folder '{folder_name}' for {lock_seconds} seconds...")

    # Create ZIP 
    shutil.make_archive(zip_base_name, 'zip', original_folder)

    # Delete original folder
    shutil.rmtree(original_folder)
    print(f"Folder zipped to: {zip_file}")
    print("Waiting...")

    # Wait for unlock
    time.sleep(lock_seconds)

    # Extract ZIP back to Desktop
    with ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(desktop_path)

    # Delete the ZIP 
    os.remove(zip_file)
    print(f"Folder 'chair' restored to Desktop and zip deleted.")

if __name__ == "__main__":
    lock_folder_zip("hide_this_folder", 600)  # 600 seconds