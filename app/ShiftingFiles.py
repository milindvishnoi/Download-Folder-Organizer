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
            os.rename(download_folder + "/" + file_name,
                      transfer_folder + "/" + file_name)


if __name__ == "__main__":
    # To set location
    download_folder = download_location
    transfer_folder = transfer_location

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
