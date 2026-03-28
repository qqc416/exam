import os
import random
import time

# 学生数据类
class Student:
    def __init__(self, name, gender, class_name, college, student_id):
        self.name = name
        self.gender = gender
        self.class_name = class_name
        self.college = college
        self.student_id = student_id#定义学生数据

    def __str__(self):#输出学生信息
        return f"学号：{self.student_id}，姓名：{self.name}，性别：{self.gender}，班级：{self.class_name}，学院：{self.college}"
# 考试系统类，管理学生成绩
class ExamSystem:
    def __init__(self, filename):
        self.students = []#存储学生数据的列表
        self.load_students(filename)

    # 从文件中加载学生名单
    def load_students(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                for line in lines:
                    parts = line.strip().split()#通过空格分隔数据
                    if len(parts) == 5:
                        name, gender, class_name, college, student_id = parts
                        self.students.append(Student(name, gender, class_name, college, student_id))
        except FileNotFoundError:
            print("文件不存在！")

    # 1. 查找学生
    def find_student(self, student_id):
        for s in self.students:
            if s.student_id == student_id:
                return s
        return None

    # 2. 随机点名
    def random_call(self, n):
        if n < 1 or n > len(self.students):#判断人数是否在范围内
            return None
        return random.sample(self.students, n)#使用该函数随机抽取学生

    # 3. 生成考场安排表
    def generate_exam_list(self):
        shuffled = random.sample(self.students, len(self.students))#随机打乱学生列表
        now = time.strftime("%Y-%m-%d %H:%M:%S")#读取时间
        with open("考场安排表.txt", 'w', encoding='utf-8') as f:#创建数据写入考试安排文件
            f.write(f"生成时间：{now}\n")
            for i, s in enumerate(shuffled, 1):#打乱后写入数据
                f.write(f"{i} {s.name} {s.student_id}\n")
        return shuffled#返回文件

    # 4. 生成准考证
    def generate_tickets(self, shuffled):#判断准考证文件是否存在，不存在则创建
        if not os.path.exists("准考证"):
            os.mkdir("准考证")
        for i, s in enumerate(shuffled, 1):#打乱顺序，利用函数生成准考证
            filename = f"准考证/{i:02d}.txt"
            with open(filename, 'w', encoding='utf-8') as f:#写入准考证信息
                f.write(f"座位号：{i}\n姓名：{s.name}\n学号：{s.student_id}")

    # 静态方法
    @staticmethod
    def check_id(student_id):#检验学号是否正确，为数字
        return student_id.isdigit()

