import file_path_read
file_pathin_students = "F:\\Python\\TestCheck\\01abc.txt"
file_pathout_students = "F:\\Python\\TestCheck\\02abc.txt"
file_path_answers = "F:\\Python\\TestCheck\\03abc.txt"

file_read_students= file_path_read.file_path_read(file_pathin_students)
file_read_answers= file_path_read.file_path_read(file_path_answers) #整个文件的内容
# file_write_students= file_path_read.file_path_read(file_pathin_students) #整个文件的内容
# print(type(file_read_students))
index=0
# print(file_read_students.__len__())
while index<file_read_students.__len__():
    line_read_student=file_read_students[index].strip()
    line_read_answers=file_read_answers[index].strip()
    # print(line_read_student)
    # print(line_read_answers)

    index+=1




