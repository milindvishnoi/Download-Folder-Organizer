#!/usr/bin/env python3
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from locations import *


class ShiftingFiles(FileSystemEventHandler):
    """
    This class is going to allow us to override the FileSystemEventHandler
    methods.
    """
    download_folders = ["photos", "documents", "folders", "music", "zipFiles",
                        "videos", "others", "code", ".DS_Store"]
    files = ["photos", "documents", "folders", "music", "zipFiles",
             "videos", "others", "code", ".DS_Store"]

    # Overriding the on_modified() method of FileSystemEventHandler class
    # in the watchdog API

    def on_modified(self, event):
        new_files = []
        files = os.listdir(download_location)
        for file in files:
            if file not in self.download_folders:
                new_files.append(file)
        if len(new_files) > 0:
            self.check_if_downloading()
            self.shift()

    def shift(self):
        """
        This function shifts all the files from one location to another,
        excluding the folders that are created by create folder function.
        :return:
        """
        try:
            existing_files = os.listdir(download_location)
            for file_name in existing_files:
                if file_name not in folders:
                    if file_name != ".DS_Store":
                        transfer_folder = self.which_location(file_name)
                        os.rename(os.path.join(download_location, file_name),
                                  os.path.join(transfer_folder, file_name))
        except FileNotFoundError:
            print("Error Occurred: Some thing went wrong!")
            print("Please run the script again, if the script stops")
            exit()

    def which_location(self, file_name):
        """
        This function decides what location is suitable for a kind of file
        :param file_name:
        :return: location in string format
        """
        if file_name.find(".") != -1:
            temp = file_name.split(".")
            file_ext = temp[len(temp) - 1]
            file_ext = file_ext.lower()
            if file_ext in ["jpg", "tiff", "gif", "png", "raw", "jpeg", "CR2",
                            "HEIC"]:
                return photo_location
            if file_ext in ["mp3", "wav"]:
                return music_location
            if file_ext in ["pdf", "txt", "docs", "docx", "ppt", "pptx"]:
                return document_location
            if file_ext == "zip":
                return zipfile_location
            if file_ext in ["mp4", "avi", "mov", "wmv", "flv"]:
                return video_location
            if file_ext in ["py", "js", "ipynb", "java", "ts"]:
                return code_location
            return other_location
        else:
            if os.path.isdir(os.path.join(download_location, file_name)):
                return folder_location
            return other_location

    def check_if_downloading(self):
        """
        This function is used to check if there is any downloading at the
        moment and then allows the script to shift the files.
        :return:
        """
        new_files = self.get_folders()
        for file_name in new_files:
            original_size = os.path.getsize(os.path.join(download_location,
                                                         file_name))
            temp = file_name.split(".")
            file_ext = temp[len(temp) - 1]
            # When download starts ".com.google.Chrome" is a temporary file
            # created
            if ".com.google.Chrome" not in file_name:
                final_size = os.path.getsize(os.path.join(download_location,
                                                              file_name))
                # To check if any file is downloading as extensions are
                # download and crdownload while downloading
                if "crdownload" in file_ext or "download" in file_ext:
                    # To check for the files that are already downloaded and
                    # have a file extension of download/crdownload
                    if final_size == original_size:
                        self.check_downloaded(file_name, original_size)
                        self.check_if_downloading()
                    else:
                        time.sleep(60)
                        self.check_if_downloading()
            else:
                time.sleep(5)
                self.check_if_downloading()
        self.files = self.download_folders.copy()
        return None

    def check_downloaded(self, file_name, original_size):
        """
        This function is used to check if the files are already downloaded or
        not by comparing size. This should be used when a file extension is
        download or crdownload. We restrict the use as it is a bad way for
        comparision
        """
        time.sleep(5)
        final_size = os.path.getsize(os.path.join(download_location,
                                                         file_name))
        if original_size == final_size:
            return None
        else:
            self.check_downloaded(file_name, original_size)

    def get_folders(self):
        """Returns the folders/files as a list except the ones we create"""
        new_files = []
        files = os.listdir(download_location)
        for file in files:
            if file not in self.files:
                self.files.append(file)
                new_files.append(file)
        return new_files


def create_folders():
    for folder_name in folders:
        existing_folders = os.listdir(download_location)
        if folder_name not in existing_folders:
            os.mkdir(os.path.join(download_location, folder_name))


if __name__ == "__main__":
    # The folders that need to be created
    folders = ["photos", "documents", "folders", "music", "zipFiles", "videos",
               "others", "code"]
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
            time.sleep(1000)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
