import os

def read_key():
    key_list = []
    key_document = []

    try:
        with open("key.txt", "r", encoding="utf-8") as f:
            line = f.readline()
            while line:
                key = line.strip()  # 使用 strip() 去除每行末尾的换行符
                key_list.append(key)
                key_document.append(key + ".txt")
                line = f.readline()
    except FileNotFoundError:
        print("文件 key.txt 不存在")
    return key_list, key_document



def read_key_from_folder(folder_path, key_document):
    data = []
    for filename in key_document:
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                line = f.readline().strip()
                data.append(line)
        else:
            data.append("No Information")
    data.append(folder_path.replace("\\", "/"))
    return data

def read_all_folders(base_path, key_document):
    all_data = []
    for folder_name in os.listdir(base_path):
        folder_path = os.path.join(base_path, folder_name)
        if os.path.isdir(folder_path):
            folder_data = read_key_from_folder(folder_path, key_document)
            all_data.append(folder_data)
    return all_data

