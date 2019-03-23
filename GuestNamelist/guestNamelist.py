

name = input("请输入您的名字（退出请输入quit）")
while name.rstrip().lower() !="quit":
    print("Hello " + name)
    with open("guest_book.txt",'a') as file:
        file.write(name.rstrip()+'\n')
    name = input("请输入您的名字（退出请输入quit）")
