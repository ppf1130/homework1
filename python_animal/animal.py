# 创建Animal类
class Animal:
    # 构造方法
    def __init__(self):
        self.name = "动物"
        self.color = "黑色"
        self.age = 3
        self.gender = "female"

    # 会叫方法
    def animal_sound(self):
        print("我会叫！")

    # 会跑方法
    def animal_run(self):
        print("我会跑！")

if __name__ == "__main__":
    animal = Animal()
    print(f"我是一只{animal.name}")
    print(f"我的颜色是{animal.color}")
    print(f"我{animal.age}岁了")
    print(f"我是{animal.gender}")
    animal.animal_sound()
    animal.animal_run()