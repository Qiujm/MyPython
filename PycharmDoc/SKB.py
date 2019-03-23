import random

chosen1 = (1, 2, 3)
chosen2 = ("0", "石头", "剪刀", "布")


# print(chosen2[4])

def compare(player, computer):
    if player == computer:
        print("玩家出了" + chosen2[player] + ",电脑出了" + chosen2[computer])
        print("平局")
    elif player - computer in (-1, 2):
        # elif (player==1 and computer==2) or (player==2 and computer==3) or (player==3 and computer==1):
        print("玩家出了" + chosen2[player] + ",电脑出了" + chosen2[computer])
        print("恭喜你获得胜利")
    else:
        print("玩家出了" + chosen2[player] + ",电脑出了" + chosen2[computer])
        print("很遗憾你输了")


while True:
    player = ''
    while len(player) != 1 or ord(player) not in range(ord('1'), ord('4')):
        player = input("请输入要出的拳(石头1 剪刀2 布3,退出请输入quit):")
        if player.lower() == "quit":
            exit()
            # player = input("输入错误，请重新输入要出的拳(石头1 剪刀2 布3,退出请输入quit):")
    player = int(player)
    computer = random.randint(1, 3)
    print(computer)
    compare(player, computer)


