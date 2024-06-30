import os
import pandas as pd
from openpyxl import load_workbook


def write_data(key_list, all_data):
    columns = key_list + ['地址']
    df = pd.DataFrame(all_data, columns=columns)
    output_path = os.path.abspath('./documents index.xlsx')  # 输出文件路径
    df.to_excel(output_path, index=False)
    adjust_column_widths(output_path)
    # print(f"Data has been written to {output_path}")


def adjust_column_widths(filepath):
    wb = load_workbook(filepath)
    ws = wb.active
    for column in ws.columns:
        max_length = 0
        column = list(column)
        for cell in column:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(cell.value)
            except:
                pass
        adjusted_width = (max_length + 2) * 1.2
        ws.column_dimensions[column[0].column_letter].width = adjusted_width
    wb.save(filepath)
