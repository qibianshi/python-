import os
import multiprocessing


def copy_file(file_name, new_folder_name, old_folder_name):
    """拷贝文件函数"""

    old_f = open(old_folder_name + "/" + file_name, "rb")
    content = old_f.read()
    old_f.close()

    new_f = open(new_folder_name + "/" + file_name, "wb")
    new_f.write(content)
    new_f.close()

    # 创建一个新的文件，打开文件，并将内容写入到新的文件夹中
    # 关闭文件


def main():
    """主函数"""
    # 获取需要copy的文件夹名字

    # global new_folder_name

    old_folder_name = input("请输入需要copy的文件夹名字：")
    # 创建一个新的空文件夹
    try:
        new_folder_name = old_folder_name + "附件"
        os.mkdir(new_folder_name)
    except Exception as res:
        print(res)
        print("异常")
    # 获取该文件夹下所有的文件名
    file_names = os.listdir(old_folder_name)
    # 创建一个新的进程池，最大进程数为5
    p0 = multiprocessing.Pool(5)
    # 调用copy文件函数将旧文件夹的所有内容copy到新的文件夹中
    # copy_file(file_names, p0, new_folder_name)

    # 向进程池中添加拷贝文件任务
    # 获取文件夹中的文件名
    for file_name in file_names:
        p0.apply_async(copy_file, args=(file_name, new_folder_name, old_folder_name))
    # 关闭进程池
    p0.close()
    # 等待所有的子进程执行完毕
    p0.join()


if __name__ == "__main__":
    main()
