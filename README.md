# File Sorting Utility with Multithreading

This Python script, `sorting.py`, is a file sorting utility that sorts files based on their extensions into separate folders. It utilizes multithreading to improve performance.

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/Taras55001/HW_3_WEB.git
    cd HW_3_WEB
    ```

2. Run the script:

    ```bash
    python sorting.py
    ```

3. Follow the on-screen instructions to specify the source folder containing the files to be sorted and the destination folder where the sorted files will be moved to.

## Features

- **Multithreading:** The script uses threading to sort files concurrently, improving performance.
- **File Sorting:** Files are sorted based on their extensions into separate folders within the destination folder.

## Functionality

- `sort_files_by_extension(source_folder, destination_folder)`: Sorts files from the `source_folder` into separate folders based on their extensions within the `destination_folder`.
- `measure_execution_time(func)`: Decorator function to measure the execution time of the `sort_files_by_extension` function.

## Example

Here is an example of using the script:

```bash
--------------------------------------------------
Input source folder: sd1
Input destination folder: Sorted_Files
Час виконання функції sort_files_by_extension: 3.212 сек.
```

Feel free to modify and integrate this script into your projects.

## Author

Taras55001

