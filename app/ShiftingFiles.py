import sys, os
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class ShiftingFiles(FileSystemEventHandler):
    """
    This class is going to allow us to override the FileSystemEventHandler
    methods.
    """
    def on_modified(self, event):
        # path = "/Users/milindvishnoi/Desktop/test"
        for file_name in os.listdir(path):
            print(file_name)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    # path = sys.argv[1] if len(sys.argv) > 1 else '.'
    path = "/Users/milindvishnoi/Desktop/test"
    event_handler = ShiftingFiles()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
