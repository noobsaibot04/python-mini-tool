import os
import shutil

path = input("Enter folder path: ")

image_extensions = [".jpg", ".jpeg", ".png"]
video_extensions = [".mp4", ".mkv", ".avi"]
music_extensions = [".mp3", ".wav"]
document_extensions = [".pdf", ".docx", ".txt"]

images_folder = os.path.join(path, "Images")
videos_folder = os.path.join(path, "Videos")
music_folder = os.path.join(path, "Music")
documents_folder = os.path.join(path, "Documents")

if not os.path.exists(images_folder):
    os.mkdir(images_folder)
if not os.path.exists(videos_folder):
    os.mkdir(videos_folder)
if not os.path.exists(music_folder):
    os.mkdir(music_folder)
if not os.path.exists(documents_folder):
    os.mkdir(documents_folder)
files = os.listdir(path)
for file in files:
    source = os.path.join(path, file)

    if file.endswith(tuple(image_extensions)):
        destination = os.path.join(images_folder, file)

        shutil.move(source, destination)

        print(file, "moved to Images folder")

    elif file.endswith(tuple(video_extensions)):

        destination = os.path.join(videos_folder, file)

        shutil.move(source, destination)

        print(file, "moved to Videos folder")

    elif file.endswith(tuple(music_extensions)):

        destination = os.path.join(music_folder, file)

        shutil.move(source, destination)

        print(file, "moved to Music folder")

    elif file.endswith(tuple(document_extensions)):

        destination = os.path.join(documents_folder, file)

        shutil.move(source, destination)

        print(file, "moved to Documents folder")
