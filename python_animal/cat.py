
from python_animal.animal import Animal

# 创建Cat类
class Cat(Animal):

    # 重写构造方法
    def __init__(self):
        self.hair = "短毛"

        # 继承父类的构造方法
        super().__init__()

        self.name = "猫"

    # 重新父类会叫的方法
    def animal_sound(self):
        print("我会喵喵叫！")

    # 新建方法,会捉老鼠
    def catch_mouse(self):
        print("我会捉老鼠哦！")

if __name__ == "__main__":
    cat = Cat()
    print(f"我是一只{cat.name}")
    print(f"我的颜色是{cat.color}")
    print(f"我{cat.age}岁了")
    print(f"我是{cat.gender}")
    print(f"我的毛发是{cat.hair}")
    cat.animal_sound()
    cat.animal_run()
    cat.catch_mouse()