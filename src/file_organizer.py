import os
import shutil
from datetime import datetime
from .utils.logger import Logger

class FileOrganizer:
    def __init__(self, directory):
        self.directory = directory
        self.logger = Logger()
        self.extensions = {
            'images': ['.jpg', '.jpeg', '.png', '.gif', '.svg', '.webp'],
            'documents': ['.pdf', '.doc', '.docx', '.txt', '.xlsx', '.csv'],
            'videos': ['.mp4', '.mov', '.avi', '.mkv', '.wmv'],
            'audio': ['.mp3', '.wav', '.flac', '.m4a', '.aac'],
            'archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
            'installers': ['.dmg', '.pkg', '.app', '.exe', '.msi'],
            'code': ['.py', '.java', '.cpp', '.html', '.css', '.js']
        }

    def _create_directories(self):
        for folder in self.extensions:
            folder_path = os.path.join(self.directory, folder)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
                self.logger.log_info(f"Created directory: {folder}")

    def _move_files(self):
        for filename in os.listdir(self.directory):
            file_path = os.path.join(self.directory, filename)
            
            # Skip if it's a directory or hidden file
            if os.path.isdir(file_path) or filename.startswith('.'):
                continue

            # Get file extension
            file_ext = os.path.splitext(filename)[1].lower()
            
            # Find appropriate folder for the file
            moved = False
            for folder, extensions in self.extensions.items():
                if file_ext in extensions:
                    destination = os.path.join(self.directory, folder, filename)
                    # Move file if it's not already in the correct folder
                    if file_path != destination:
                        try:
                            shutil.move(file_path, destination)
                            self.logger.log_info(f"Moved {filename} to {folder}")
                            moved = True
                        except PermissionError:
                            self.logger.log_error(f"Permission denied: Cannot move {filename}")
                        except FileExistsError:
                            new_filename = f"{os.path.splitext(filename)[0]}_{datetime.now().strftime('%Y%m%d_%H%M%S')}{file_ext}"
                            new_destination = os.path.join(self.directory, folder, new_filename)
                            shutil.move(file_path, new_destination)
                            self.logger.log_info(f"Moved {filename} to {folder} as {new_filename}")
                            moved = True
                    break
            
            # If no matching folder found, move to 'others'
            if not moved:
                others_dir = os.path.join(self.directory, 'others')
                if not os.path.exists(others_dir):
                    os.makedirs(others_dir)
                destination = os.path.join(others_dir, filename)
                if file_path != destination:
                    try:
                        shutil.move(file_path, destination)
                        self.logger.log_info(f"Moved {filename} to others")
                    except PermissionError:
                        self.logger.log_error(f"Permission denied: Cannot move {filename}")

    def organize(self):
        try:
            self._create_directories()
            self._move_files()
            self.logger.log_info("File organization completed successfully")
        except Exception as e:
            self.logger.log_error(f"Error during organization: {str(e)}")
