import re


def main():
    """主函数"""
    email = input("请输入一个邮箱地址：")
    ret = re.match(r"([0-9a-zA-Z]{4,20})@(163|126)\.com$", email).group()
    if ret:
        print("匹配正确,匹配到的邮箱地址为%s" % ret)
    else:
        print("%s不符合要求" % ret)


if __name__ == "__main__":
    main()
