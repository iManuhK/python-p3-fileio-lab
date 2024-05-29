def write_file(file_name, file_content):
    with open(f'{file_name}.txt', mode = "w", encoding = "utf-8") as file_name:
        file_name.write(file_content)

def append_file(file_name, append_content):
    with open(f'{file_name}.txt', mode = "a", encoding = "utf-8") as file_name:
        file_name.write(append_content)

def read_file(file_name):
    with open(f'{file_name}.txt', mode = "r", encoding = "utf-8") as file_name:
        file_content = file_name.read()
    return file_content
