# coding:utf-8

import os

count = 0
def all_files(path, file_type):    # 生成path路径下全部file_type类型文件绝对路径列表
    f_list = []
    def files_list(father_path):
        sub_path = os.listdir(father_path)    # 读取父路径下全部文件或文件夹名称
        for sp in sub_path:
            full_sub_path = os.path.join(father_path, sp)    # 生成完整子路径
            if os.path.isfile(full_sub_path):    # 判断是否为文件
                file_name, post_name = os.path.splitext(full_sub_path)    # 获取文件后缀名
                if post_name == file_type:
                    f_list.append(file_name + post_name)
            else:    # 如果是文件夹，递归调用
                files_list(full_sub_path)

    files_list(path)
    return f_list 
a = all_files('/Users/yangyu/Documents/yach_71_ios/Yach/Yach/','.swift')
print(len(a))