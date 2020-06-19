# coding:utf-8

import os



def WriteFileFromArray(FILENAME, LINES_ARR):
    FILE_NEW = "\r\n".join(LINES_ARR)
    FILE_TMP = open(FILENAME, "a+")
    FILE_TMP.write(FILE_NEW)
    FILE_TMP.close()
    return True

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
                    dirname,filename=os.path.split(full_sub_path)
                    f_list.append(filename)
            else:    # 如果是文件夹，递归调用
                files_list(full_sub_path)

    files_list(path)
    return f_list 
a = all_files('/Users/tal/Documents/yach_71_ios2/YachMiddlewareSession/','.h')
b = all_files('/Users/tal/Documents/yach_71_ios2/YachMiddlewareSession/','.m')
c = all_files('/Users/tal/Documents/yach_71_ios/Yach/Yach/','.swift')
d = all_files('/Users/tal/Documents/yach_71_ios/Yach/Yach/','.bundle')
print(len(a))
print(len(b))
WriteFileFromArray('1.md',a)
WriteFileFromArray('1.md',b)
print(len(c))
print(len(d))
