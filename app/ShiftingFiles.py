import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from app.locations import *


class ShiftingFiles(FileSystemEventHandler):
    """
    This class is going to allow us to override the FileSystemEventHandler
    methods.
    """
    # Overriding the on_modified() method of FileSystemEventHandler class
    # in the watchdog API
    def on_modified(self, event):
        self.shift()

    def shift(self):
        for file_name in os.listdir(download_folder):
            transfer_folder = self.which_loaction(file_name)
            os.rename(download_folder + "/" + file_name,
                      transfer_folder + "/" + file_name)

    def which_loaction(self, file_name: str):
        if file_name.find(".") != -1:
            file_ext = file_name.split(".")[1]
            if file_ext == "jpg":
                return photo_location
            if file_ext == "mp3":
                return music_location
            if file_ext == "pdf":
                return document_location
            if file_ext == "zip":
                return zipfile_location
            if file_ext == "mp4":
                return video_location
            return transfer_location
        else:
            return folder_location


if __name__ == "__main__":
    # To set location
    download_folder = download_location

    # To shift the files as soon as the program is run
    ShiftingFiles().shift()

    # Consuming watchdog API
    event_handler = ShiftingFiles()
    observer = Observer()
    observer.schedule(event_handler, download_folder, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(100)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


    # lst = ["photos", "documents", "folders", "music", "zipFiles", "videos"]
    # for folderName in lst:
    #     os.mkdir("/Users/milindvishnoi/Desktop/" + folderName)
