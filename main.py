from src.file_organizer import FileOrganizer
from src.file_monitor import FolderMonitor
from src.duplicate_handler import DuplicateHandler
import argparse
import os


def main():
    parser = argparse.ArgumentParser(description='Automated File Management System')
    parser.add_argument('--path', type=str, required=True, help='Path to organize')
    parser.add_argument('--monitor', action='store_true', help='Enable folder monitoring')
    parser.add_argument('--handle-duplicates', choices=['log', 'delete', 'move'], 
                        default='log', help='Action to take on duplicate files')
    args = parser.parse_args()

    # Organize files
    organizer = FileOrganizer(args.path)
    organizer.organize()

    # Handle duplicates in sorted folders
    handle_duplicates(args.path, args.handle_duplicates)

    # Monitor folder if enabled
    if args.monitor:
        monitor = FolderMonitor(args.path)
        monitor.start_monitoring()


def handle_duplicates(path, action):
    """
    Handle duplicate files in sorted folders based on the specified action: log, delete, or move.
    """
    sorted_folders = [
        os.path.join(path, folder)
        for folder in os.listdir(path)
        if os.path.isdir(os.path.join(path, folder)) and not folder.startswith('.')
    ]

    for folder in sorted_folders:
        duplicate_handler = DuplicateHandler(folder)
        duplicates = duplicate_handler.find_duplicates()

        if duplicates:
            print(f"Found {len(duplicates)} duplicate files in folder '{folder}':")
            for dup, original in duplicates:
                print(f"Duplicate: {dup} | Original: {original}")
            
            if action == 'log':
                # Default: Only log duplicates
                duplicate_handler.logger.log_info(f"Found {len(duplicates)} duplicates in {folder}.")
            
            elif action == 'delete':
                # Delete duplicate files
                for dup, _ in duplicates:
                    try:
                        os.remove(dup)
                        duplicate_handler.logger.log_info(f"Deleted duplicate: {dup}")
                    except Exception as e:
                        duplicate_handler.logger.log_error(f"Error deleting {dup}: {str(e)}")
            
            elif action == 'move':
                # Move duplicates to a "duplicates" folder within the main directory
                duplicates_folder = os.path.join(path, "duplicates")
                os.makedirs(duplicates_folder, exist_ok=True)
                for dup, _ in duplicates:
                    try:
                        new_path = os.path.join(duplicates_folder, os.path.basename(dup))
                        os.rename(dup, new_path)
                        duplicate_handler.logger.log_info(f"Moved duplicate: {dup} to {new_path}")
                    except Exception as e:
                        duplicate_handler.logger.log_error(f"Error moving {dup}: {str(e)}")


if __name__ == "__main__":
    main()
