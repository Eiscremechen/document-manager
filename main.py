# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import os
from read_key.read_key import read_key, read_all_folders
from write_data.write_data import write_data



# def print_hi(name):
#     # 在下面的代码行中使用断点来调试脚本。
#     print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    key_list, key_document = read_key()

    # base_path = './documents'
    base_path = os.path.abspath('./documents')

    # 判断 ./documents 是否存在，如果不存在则创建
    if not os.path.exists(base_path):
        os.makedirs(base_path)
        print(f"Created directory: {base_path}")

    all_data = read_all_folders(base_path, key_document)

    write_data(key_list,all_data)



