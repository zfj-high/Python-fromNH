from random import randint

# 输入要抽查的人数
s = int(input('请输入要抽查的人数(不超过49)'))
if s > 49:
    s = 49

# 定义各个组的学生学号
group1 = [16, 37, 26, 27, 28, 34, 20, 38, 29, 32, 16, 31]
group2 = [8, 24, 2, 18, 46, 44, 10, 7, 5, 39, 22, 40]
group3 = [11, 0]
group4 = [1, 42, 6, 30, 14, 49, 12, 21, 33, 35, 41, 48]
group5 = [19, 45, 17, 3, 9, 13, 23, 47, 36, 4, 43, 25]

# 输入各个区域的学号
group_all = [group1, group2, group3, group4, group5]

def finder(number):  # 找到该学生在表中的位置
    for i, group in enumerate(group_all):
        for j, student in enumerate(group):
            if student == number:
                return [i, j, number]
    return None  # 如果找不到学生，返回 None

def printer(a):  # 位置打印
    print('------------------------')
    for region in a:
        for i in range(0, len(region), 2):
            if i + 1 < len(region):
                print(region[i], region[i + 1])
        print('------------------------')  # 防止混淆区域

def dw(a):  # 全空列表学生定位
    list = [[] for _ in range(len(group_all))]
    for student_info in a:
        list[student_info[0]].append(student_info[2])  # 使用 student_info[0] 作为索引
    return list

si = 0  # 类似于索引
flag = [False] * 49

while si < s:  # 幸运抽奖（哪个学生要被检查）
    temp_int = randint(0, 48)
    if not flag[temp_int]:  # 如果该学生没有被选中
        flag[temp_int] = True
        si += 1

student_cc = []  # 学生学号调整（索引改成学号）
for i in range(len(flag)):
    if flag[i]:
        student_cc.append(i + 1)  # 将随机数转变为学号（下标 + 1）

student_information = []  # 要检查学生的学号、表中的位置
for c in student_cc:
    info = finder(c - 1)  # 找学号为 c-1 的学生
    if info:  # 确保找到学生信息
        student_information.append(info)

list_end = dw(student_information)
printer(list_end)
print("抽取出的学生学号:", student_cc)