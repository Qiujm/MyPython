

def file_path_read(filename):
    with open(filename) as file_object:
        lines = file_object.readlines()
    return lines

# filename = "F:\\Python\\TestCheck\\01abc.txt"
# with open(filename) as file_object:
#     lines=file_object.readlines()
#     print(lines)
#
# for line in lines:
#     print(line.strip())