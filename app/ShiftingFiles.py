#!/usr/bin/env python
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
        """
        This function shifts all the files from one location to another,
        excluding the folders that are created by create folder function.
        :return:
        """
        existing_files = os.listdir(download_location)
        for file_name in existing_files:
            if file_name not in folders:
                transfer_folder = self.which_location(file_name)
                os.rename(os.path.join(download_location, file_name),
                          os.path.join(transfer_folder, file_name))

    def which_location(self, file_name: str):
        """
        This function decides what location is suitable for a kind of file
        :param file_name:
        :return: location in string format
        """
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
            if os.path.isdir(os.path.join(download_location, file_name)):
                return folder_location
            return transfer_location


def create_folders():
    for folder_name in folders:
        existing_folders = os.listdir(download_location)
        if folder_name not in existing_folders:
            os.mkdir(os.path.join(download_location, folder_name))


if __name__ == "__main__":
    # The folders that need to be created
    folders = ["photos", "documents", "folders", "music", "zipFiles", "videos",
               "others"]
    # To create separate folders to organize data in
    create_folders()

    # To shift the files as soon as the program is run
    ShiftingFiles().shift()

    # Consuming watchdog API
    event_handler = ShiftingFiles()
    observer = Observer()
    observer.schedule(event_handler, download_location, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(100)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
