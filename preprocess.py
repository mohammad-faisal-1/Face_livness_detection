# import os

# # Define the paths to your folders
# labels_folder = r'C:\Users\Shahid\Desktop\Faisal_Data\DL_project\Datasets\valid\labels'
# images_folder = r'C:\Users\Shahid\Desktop\Faisal_Data\DL_project\Datasets\valid\images'

# # Get the list of files in the labels folder
# label_files = os.listdir(labels_folder)

# for label_file in label_files:
#     # Construct the full path to the label file
#     label_file_path = os.path.join(labels_folder, label_file)

#     # Open and read the label file
#     with open(label_file_path, 'r') as file:
#         lines = file.readlines()

#     # Check if any line starts with '1'
#     delete_file = False
#     for line in lines:
#         if line.startswith('2'):
#             delete_file = True
#             break

#     # If a line starting with '1' is found, delete the label file and the corresponding image file
#     if delete_file:
#         # Delete the label file
#         os.remove(label_file_path)
#         print(f"Deleted label file: {label_file_path}")

#         # Construct the corresponding image file name
#         image_file_name = os.path.splitext(label_file)[0] + '.jpg'  # assuming images are in .jpg format
#         image_file_path = os.path.join(images_folder, image_file_name)

#         # Check if the image file exists and delete it
#         if os.path.exists(image_file_path):
#             os.remove(image_file_path)
#             print(f"Deleted image file: {image_file_path}")

# print("Task completed.")



import os

# Define the paths to your folders
labels_folder = r''
images_folder = r''

# Get the list of files in the labels folder
label_files = os.listdir(labels_folder)

for label_file in label_files:
    # Construct the full path to the label file
    label_file_path = os.path.join(labels_folder, label_file)

    # Open and read the label file
    with open(label_file_path, 'r') as file:
        lines = file.readlines()

    # Replace '1' with '3' in any line that starts with '1'
    new_lines = []
    for line in lines:
        if line.startswith('3'):
            new_line = '0' + line[1:]  # Replace '1' with '3' but keep the rest of the line
            new_lines.append(new_line)
        else:
            new_lines.append(line)

    # Write the modified lines back to the file
    with open(label_file_path, 'w') as file:
        file.writelines(new_lines)
        print(f"Updated label file: {label_file_path}")

print("Task completed.")
