import os

def count_files_characters_and_lines(folder_path):
    total_files = 0
    total_characters = 0
    total_lines = 0

    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            total_files += 1

            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    total_characters += len(content)
                    lines = content.split('\n')
                    total_lines += len(lines)
            except Exception as e:
                print(f"Error reading file {file_path}: {e}")

    return total_files, total_characters, total_lines

# Replace 'your_folder_path' with the path to the folder you want to analyze
folder_path = './ifcelec/'
files_count, characters_count, lines_count = count_files_characters_and_lines(folder_path)
print(f"Total files: {files_count}")
print(f"Total characters: {characters_count}")
print(f"Total lines: {lines_count}")

