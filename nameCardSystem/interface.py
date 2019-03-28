class Interface():
    def __init__(self):
        self.intface = "欢迎使用【名片管理系统】V1.0 \n\n1.新建名片 \n2.显示全部 \n3.查询名片 \n\n0.退出系统"
        self.actions = ["1", "2", "3", "0"]
        self.show_interface()

    def get_action(self):
        action = input("请输入执行的操作：")
        while action not in self.actions:
            action = input("输入错误，请重新输入：")
        print("您选择的操作是：%s" % action)
        return action

    def show_interface(self):
        print("*" * 40)
        print(self.intface)
        print("*" * 40)
