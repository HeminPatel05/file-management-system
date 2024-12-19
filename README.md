# Automated File Management System

The Automated File Management System is a Python-based application that helps organize files, monitor folders for changes, and handle duplicate files within a specified directory. It streamlines file organization by categorizing files based on their extensions and provides options to handle duplicate files effectively.

## Features

- **File Organization**: Automatically organizes files into categorized subfolders (e.g., images, documents, videos).
- **Folder Monitoring**: Continuously monitors a specified folder for changes and organizes new or modified files.
- **Duplicate Handling**: Detects duplicate files and provides options to log, delete, or move them to a designated folder.

## Requirements

- **Python**: Version 3.7 or higher
- **Required Python libraries**:
  - `argparse`
  - `os`
  - `shutil`
  - `time`
  - `watchdog`

## Installation

1. Clone the repository:

```bash
git clone https://github.com/HeminPatel05/file-management-system.git
```

2. Navigate to the project directory:

```bash
cd file-management-system
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the script using the following command:

```bash
python main.py --path <directory_path> [--monitor] [--handle-duplicates <log|delete|move>]
```

### Arguments

- `--path`: The path of the directory to organize (required).
- `--monitor`: Enable folder monitoring for real-time organization (optional).
- `--handle-duplicates`: Action to take on duplicate files:
  - `log` (default): Log duplicates without taking action.
  - `delete`: Remove duplicate files.
  - `move`: Move duplicates to a duplicates folder.

### Examples

1. Organize files in a directory:
   python main.py --path /path/to/directory

2. Organize files and monitor the folder for changes:
   python main.py --path /path/to/directory --monitor

3. Organize files and delete duplicates:
   python main.py --path /path/to/directory --handle-duplicates delete

4. Organize files and move duplicates to a duplicates folder:
   python main.py --path /path/to/directory --handle-duplicates move

## Project Structure

```perl
file-management-system/
├── src/
│ ├── file_organizer.py # Handles file categorization and organization
│ ├── file_monitor.py # Monitors folder for real-time changes
│ ├── duplicate_handler.py # Detects and handles duplicate files
│ └── utils/
│ └── logger.py # Logging utility
├── requirements.txt # Python dependencies
├── main.py # Entry point of the application
└── README.md # Project documentation
```

## Logging

All logs are saved in the `logs/` directory. Logs include information about file movements, duplicate handling, and any errors encountered during execution.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributions

Contributions are welcome! Please open an issue or submit a pull request on GitHub for any enhancements or bug fixes.

## Acknowledgments

- Inspired by real-world file management challenges.
- Built using Python's `watchdog` library for folder monitoring.

## Authors

- Hemin Patel
- GitHub: [https://github.com/HeminPatel18](https://github.com/HeminPatel18)
