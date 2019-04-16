import re


# result = re.match(正则表达式， 要匹配的字符串)
result1 = re.match(r"itcast", "itcast.cn")
result1.group()
print(result1)


result2 = re.match(r"速度与激情[1-35-8]+", "速度与激情88").group()
print(result2)


result3 = re.match(r"速度与激情\s\d", "速度与激情\t8")
print(result3)


html_content = """jhjksdfhjfjafjhfjhf
hfaslfhkjfhlfhaopsfjoifhsajhlsjfkl"""
result4 = (r".*", html_content)
print(result4)