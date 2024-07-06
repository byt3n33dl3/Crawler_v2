import os

file_path = 'Desktop'

if not os.path.exists(Desktop):
    print(f"File {Desktop} does not exist.")
else:
    try:
        os.remove(Desktop)
        print(f"File {Desktop} has been deleted.")
    except Exception as e:
        print(f"Error deleting file: {e}")
