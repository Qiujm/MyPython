import time


def new_cards():
    filename = "cards.txt"
    name = input("请输入姓名：")
    phone = input("请输入电话号码：")
    qq = input("请输入QQ号码：")
    email = input("请输入email地址：")
    tup = (name, phone, qq, email)
    string = "\n姓名：%s  电话：%s  QQ：%s  email：%s" % tup
    exist,info = query(name)
    if exist:
        print("该用户已存在")
        return
    with open(filename, 'a+') as file:
        file.writelines(string)  # 如何添加换行
        print("添加成功！")


def show_all_cards():
    filename = "cards.txt"
    try:
        with open(filename, "r") as file:

            while True:
                item = file.readline()
                if not item:
                    break
                print(item, end="")
    except Exception:
        print("没有记录！")
        # return


def query_cards():
    checked_name = input("请输入要查询的名字：")
    exist,info=query(checked_name)
    if not exist:
        print("用户不存在!")
    else:
        print(info)



def quit_system():
    print("欢迎再次使用【名片管理系统】！")
    time.sleep(1)
    exit()


def query(name):
    """根据姓名查询，返回是否存在及用户信息"""
    filename = "cards.txt"
    exist=False
    get_name_info = ''
    try:
        with open(filename, "r") as file:
            while True:
                item = file.readline()
                if not item:
                    break
                elif name in item:
                    get_name_info = item
                    exist=True
                    # print(item)
        return exist,get_name_info
    except Exception:
        print("记录不存在！")


def check_input(string):
    if not string:
        return False
