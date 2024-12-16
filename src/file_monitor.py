from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
from .utils.logger import Logger
from .file_organizer import FileOrganizer

class FileHandler(FileSystemEventHandler):
    def __init__(self, directory):
        self.directory = directory
        self.organizer = FileOrganizer(directory)
        self.logger = Logger()

    def on_created(self, event):
        if not event.is_directory:
            self.logger.log_info(f"New file detected: {event.src_path}")
            self.organizer.organize()

    def on_modified(self, event):
        if not event.is_directory:
            self.logger.log_info(f"File modified: {event.src_path}")
            self.organizer.organize()

class FolderMonitor:
    def __init__(self, directory):
        self.directory = directory
        self.observer = Observer()
        self.logger = Logger()

    def start_monitoring(self):
        try:
            event_handler = FileHandler(self.directory)
            self.observer.schedule(event_handler, self.directory, recursive=False)
            self.observer.start()
            self.logger.log_info(f"Started monitoring directory: {self.directory}")
            
            try:
                while True:
                    time.sleep(1)
            except KeyboardInterrupt:
                self.observer.stop()
                self.logger.log_info("Monitoring stopped by user")
            
            self.observer.join()
            
        except Exception as e:
            self.logger.log_error(f"Error in monitoring: {str(e)}")

    def stop_monitoring(self):
        self.observer.stop()
        self.observer.join()
        self.logger.log_info("Monitoring stopped")
