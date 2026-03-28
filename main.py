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

