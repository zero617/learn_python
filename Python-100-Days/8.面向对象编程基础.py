# PS:
from time import sleep


class Student(object):

    # __init__是一个特殊方法用于在创建对象时进行初始化操作
    # 通过这个方法我们可以为学生对象绑定name和age两个属性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s正在学习%s.' % (self.name, course_name))

    # PEP 8要求标识符的名字用全小写多个单词用下划线连接
    # 但是部分程序员和公司更倾向于使用驼峰命名法(驼峰标识)
    def watch_movie(self):
        if self.age < 18:
            print('%s只能观看《熊出没》.' % self.name)
        else:
            print('%s正在观看岛国爱情大电影.' % self.name)


def main():
    # 创建学生对象并指定姓名和年龄
    stu1 = Student('骆昊', 38)
    # 给对象发study消息
    stu1.study('Python程序设计')
    # 给对象发watch_av消息
    stu1.watch_movie()
    stu2 = Student('王大锤', 15)
    stu2.study('思想品德')
    stu2.watch_movie()


if __name__ == '__main__':
    main()

# 访问可见性：


class Test:

    def __init__(self, foo, foo2):
        self.__foo = foo
        self.foo2 = foo2

    def __bar(self):
        print(self.__foo)
        print('__bar')

    def bar(self):
        print(self.__foo)
        print('bar')


def main():
    test = Test('hello', 'hello')

    test.bar()
    test.__bar()  # AttributeError: 'Test' object has no attribute '__bar'

    print(test.foo2)
    print(test.__foo)  # AttributeError: 'Test' object has no attribute '__foo'


if __name__ == "__main__":
    main()

# 并不建议设置为私有


class Test:

    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')


def main():
    test = Test('hello')
    """
    常常让属性名以单下划线开头来表示属性是受保护的，本类之外的代码在访问这样的属性时应该要保持慎重。
    这种做法并不是语法上的规则，单下划线开头的属性和方法外界仍然是可以访问的，所以更多的时候它是一种暗示或隐喻
    """
    test._Test__bar()
    print(test._Test__foo)


if __name__ == "__main__":
    main()


"""练习1：定义一个类描述数字时钟。"""


class clock:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def run(self):
        self.seconds += 1
        if self.seconds == 60:
            self.seconds = 0
            self.minutes = self.minutes + 1
            if self.minutes == 60:
                self.minutes = 0
                self.hours = self.hours + 1
                if self.hours == 24:
                    self.hours = 0

    def show(self):
        return '%02d:%02d:%02d' % (self.hours, self.minutes, self.seconds)


def main():
    clock1 = clock(23, 59, 59)
    while True:
        clock1.run()
        sleep(1)
        print(clock1.show())


if __name__ == "__main__":
    main()
