import re


def main():
    # names = ["name1", "_name2", "1name3", "name_4", "__name__"]
    names = ["age", "-age", "_age", "1age", "age1", "a_age", "age_a", "age-a", "a#123", "________"]
    for name in names:
        # match 中自带判断开头，但是没有判断结尾，$符号判断结尾 ^符号判断开头
        # ret = re.match(r"[a-zA-Z_][a-zA-Z_]*", name)
        ret = re.match(r"[a-zA-Z_][a-zA-Z_]*$", name)
        if ret:
            print("变量名%s符合命名规范...通过正则表达式匹配到的结果%s" % (name, ret.group()))
        else:
            print("变量名%s不符合规范" % name)


if __name__  == "__main__":
    main()
