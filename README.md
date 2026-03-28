张顺乾-25361048-第二次人工智能编程作业
 
1. 任务拆解与 AI 协作策略
 
本次作业是实现学生考场信息管理系统，包含学生类、考试系统类、文件读写、异常处理等功能。我将任务拆解为以下步骤与 AI 协作：

步骤1：我对第二次作业分析以后得出我要分三步完成，首先是对考试信息管理系统的代码编写与实现，然后创建GitHub仓库用于保存与提交，最后撰写README。md对
我完成任务的过程进行具体介绍与细节补充解释；

步骤2：由于对GitHub的不熟练，我先询问AI如何使用GitHub，并事先进行了尝试；

步骤3：我先对AI询问了Python的标准库都有哪些常用，并筛选了我可能需要使用到的比如os，与random；
步骤4：我又让 AI 生成基础的 Student 数据类，学号，姓名，与成绩，并定义了一个函数，用于最基本的输出；
步骤5：随后，是完成代码的主要功能，我让AI生成了考试信息管理系统的逻辑代码，实现要求的查找、随机点名、随机生成文件考试安排表与准考证功能；
步骤6：在这之后，我将代码与老师所提供的名单存储在一个文件夹中，尝试文件是否可用；
步骤7：最后，我让AI生成了主代码，对上述代码进行调用，实现作业中所提到的要求；
步骤8：调试过程中代码出现了报错，我先让AI对代码进行了解释，通过这些解释，我理解了该代码运行的主要原理，又加上我自己所学的编程基础知识，对我存有疑虑
的地方提出了问题，最后通过AI核查与演示，解决了报错问题；
步骤9：在完成代码调试后，我让 AI 优化代码结构，去除了多余的部分，增加了如果出现意外情况时的解释，比如文件不存在等情况。同时，确保仅使用 Python 标准
库，不使用第三方库；
步骤10：最后让 AI 生成逐行注释版代码，我再进行人工校验和修改。
 
2. 核心 Prompt 迭代记录
 
初代 Prompt：
 
我将作业文件发给AI，让AI写一个 Python 学生考场信息管理系统，包含学生信息、查找、点名、生成文件功能，要求代码完整详细。
 
AI 生成的问题/缺陷：

1.AI提供的是在VScode中的解决方案，而我只安装了idle，并且需要频繁使用cmd终端，较为繁琐；
2. 使用了 pandas 库读取文件，违反模块使用限制；
3. 没有进行异常处理，文件不存在会直接报错；
4 没有静态方法或类方法；
5. 代码没有注释，命名繁琐复杂难以分辨，逻辑不清晰，代码可读性极弱。
6.AI给出三段代码，需要创建三个文件，较为复杂；

优化后的 Prompt（追问）：
 
我的电脑只安装了idle，能否以此为根据编写代码，要求是不需要使用到终端，只是用python标准库，且只需要一个文件就能完成，其中代码要逻辑清晰，重要
部分添加注释，命名要相对简洁明了。其中先完成student 类的代码，然后完成ExamSystem部分代码，实现系统功能，最后生成主函数调用其他函数完成功能。
（然而，可能是我要求过多，AI生成的代码不尽人意，于是，我转换思路，在AI新生成的代码基础上，进行了新的逐步追问，内容大致如下：
1. 定义 Student 类，包含 init 和 str 方法；
2. 定义 ExamSystem 类，封装查找、点名、生成文件等功能；
3. 至少包含一个静态方法，用于路径拼接；
4. 仅使用 os、random等 Python 标准库，禁止使用 pandas；
5. 用 try‑except 处理 FileNotFoundError、ValueError 等异常；
6. 代码逻辑清晰，最后生成逐行中文注释版。）
 
3. Debug 与异常处理记录
 
报错类型/漏洞现象：
 
1. FileNotFoundError：生成文件时路径不存在，程序直接崩溃；
2. ValueError：输入学号为非数字时，转换 int 报错；
3. 路径拼接错误：使用字符串直接拼接路径，在不同系统下出错。
 
解决过程：
 
1. 路径拼接错误：我发现 AI 用  path + filename  拼接路径，改为调用静态方法  os.path.join()  解决；
2. FileNotFoundError：在文件读写处加 try‑except，捕获异常并提示“文件不存在”；
3. ValueError：在输入学号处加 try‑except，捕获非数字输入并提示“请输入有效数字学号”；
4. 我将报错信息和修改要求反馈给 AI，AI 修正后我再逐行验证。
 
4. 人工代码审查（Code Review）
 
python
  
# AI生成的核心逻辑代码 + 人工逐行注释
class Student:
    # 初始化学生属性：学号、姓名、考场、座位号
    def __init__(self, stu_id, name, room, seat):
        self.stu_id = stu_id  # 存储学号
        self.name = name      # 存储姓名
        self.room = room      # 存储考场
        self.seat = seat      # 存储座位号

    # 友好打印学生信息
    def __str__(self):
        return f"学号：{self.stu_id}，姓名：{self.name}，考场：{self.room}，座位：{self.seat}"

class ExamSystem:
    # 静态方法：拼接文件路径（满足静态方法要求）
    @staticmethod
    def join_path(folder, filename):
        # 使用os.path.join保证跨系统路径正确
        return os.path.join(folder, filename)

    # 从文件加载学生信息
    def load_students(self, filepath):
        students = []
        try:
            # 尝试打开文件
            with open(filepath, "r", encoding="utf-8") as f:
                for line in f:
                    data = line.strip().split(",")
                    # 转换学号为整数，可能触发ValueError
                    stu_id = int(data[0])
                    student = Student(stu_id, data[1], data[2], data[3])
                    students.append(student)
        # 捕获文件不存在异常
        except FileNotFoundError:
            print("错误：学生信息文件不存在！")
        # 捕获学号非数字异常
        except ValueError:
            print("错误：文件中学号格式错误，必须为数字！")
        return students
