
def calculator(str1, str2):
    flag = False
    # result = ""
    result=[]
    len1 = len(str1)
    len2 = len(str2)
    index = max(len1, len2) - 1
    if len1 < len2:
        str1 = "%s%s" % ("0" * (len2 - len1), str1)
    elif len2 < len1:
        str2 = "%s%s" % ("0" * (len1 - len2), str2)

    while index >= 0:
        if flag:
            temp = int(str1[index]) + int(str2[index]) + 1
            add = temp % 2
        else:
            temp = int(str1[index]) + int(str2[index])
            add = temp % 2
        # result = "%d%s" % (add, result)
        result.append(str(add))
        index -= 1
        flag = temp // 2 == 1

    if flag:
        result.append('1')
        # result = "%d%s" % (1, result)
    result.reverse()
    return result


# num1 = 111111
# num2 = 1011111
nums = ["", ""]
index = 0
while index < nums.__len__():
    temp = input("输入二进制数,退出请输入q: ")
    if (temp.lower() == "q"):
        exit()
    for ch in temp:
        if not (ch in ["0", "1"]):
            temp = input("输入二进制数,退出请输入q")
            # print("格式错误请重新输入")

    nums[index] = temp
    index += 1

print(nums)
result = calculator(nums[0], nums[1])
print("%s + %s = %s" % (nums[0], nums[1], ''.join(result)))
