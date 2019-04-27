from pymysql import *


class JD(object):
    def __init__(self):
        # 创建connection连接
        self.sql = None
        self.conn = connect(host='localhost', port=3306, user='root', password='123456', database='jing_dong',
                            charset='utf8')
        # 获得cursor对象
        self.cs1 = self.conn.cursor()

    def __del__(self):
        # 关闭cursor对象和connect连接
        self.cs1.close()
        self.conn.close()

    @staticmethod
    def tip_massage():
        # 显示提示信息
        print("[0]退出程序")
        print("[1]显示所有的数据表")
        print("[2]显示数据表中所有数据")
        print("[3]显示所有的商品分类")
        print("[4]显示所有的商品品牌的分类")
        print("[5]添加一个商品分类")
        print("[6]根据名字查询一个商品")

    def execute_sql(self, sql):
        # 执行sql语句并显示
        self.sql = sql
        self.cs1.execute(self.sql)
        result = self.cs1.fetchall()
        for temp in result:
            print(temp)

    def show_all_tables(self):
        # 显示所有的数据表
        sql = 'show tables;'
        self.execute_sql(sql)

    def show_all_date(self):
        # 显示数据表中所有的商品信息
        sql = "select * from goods;"
        self.execute_sql(sql)

    def show_all_cates(self):
        # 显示所有品牌的分类
        sql = "select name from goods_cates group by name;"
        self.execute_sql(sql)

    def show_all_brands(self):
        # 显示所有的商品品牌分类
        sql = "select name from goods_brands group by name;"
        self.execute_sql(sql)

    def add_brand(self):
        # 添加一个商品分类
        item_name = input("请输入需要添加品牌名字：")
        sql = """insert into goods_brands (name) values("%s");""" % item_name
        self.cs1.execute(sql)
        self.conn.commit()

    def get_info_by_name(self):
        # 根据名字查询一个商品
        find_name= input("请输入需要查找的商品名称：")
        sql = """select * from goods where name="%s";""" % find_name
        self.execute_sql(sql)

    def run(self):
        while True:
            self.tip_massage()
            # 输入想要实现的操作
            num = input("请输入需要执行的操作：")
            # 调用相关操作
            if num == '0':
                break
            elif num == "1":
                self.show_all_tables()
            elif num == "2":
                self.show_all_date()
            elif num == "3":
                self.show_all_cates()
            elif num == "4":
                self.show_all_brands()
            elif num == "5":
                self.add_brand()
            elif num == "6":
                self.get_info_by_name()
            else:
                print("请输入正确的操作！！！")


def main():
    """"实现总体的控制"""
    jd = JD()
    jd.run()


if __name__ == "__main__":
    main()
