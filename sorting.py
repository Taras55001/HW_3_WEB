import os
import shutil
import threading
import time

def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Час виконання функції {func.__name__}: {execution_time} сек.")
        return result
    return wrapper

@measure_execution_time
def sort_files_by_extension(source_folder, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    files = []
    for root, _, filenames in os.walk(source_folder):
        for filename in filenames:
            files.append(os.path.join(root, filename))

    def process_file(file):
        extension = os.path.splitext(file)[1][1:].lower()
        destination_path = os.path.join(destination_folder, extension, os.path.basename(file))

        
        if os.path.exists(destination_path):
            base_name = os.path.splitext(os.path.basename(file))[0]
            counter = 1
            while os.path.exists(destination_path):
                new_base_name = f"{base_name}_{counter}"
                destination_path = os.path.join(destination_folder, extension, f"{new_base_name}.{extension}")
                counter += 1

        os.makedirs(os.path.dirname(destination_path), exist_ok=True)
        shutil.move(file, destination_path)

    threads = []
    for file in files:
        thread = threading.Thread(target=process_file, args=(file,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()


if __name__ == '__main__':
    source_folder = 'sd1'
    destination_folder = 'Сортовані файли'
    try:
        sort_files_by_extension(source_folder, destination_folder)
    except FileExistsError as error:
        print(error)
