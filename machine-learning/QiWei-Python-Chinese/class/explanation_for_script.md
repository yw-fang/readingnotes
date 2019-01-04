List of the scripts:

Note that theses python scripts use python 3.

- class_01.py: create a simple class and understand the structure in a class

- class_02.py: arguments in CLASS

- class_03.py: namespaces in Python

- class_04.py: single inheritance in CLASS

- class_05.py: multiple inheritance in CLASS

- class_06.py: show the sequence of inheritance in CLASS

- class_07.py: introduce a problem without using super function

- class_08.py: solve problem in class_07.py by using super function

- class_09.py: simple introductory example of staticmethod and classmethod

- class_10.py: better understand the differences between staticmethod and classmethod

Additional note in Chinese:

许多编程语言中都有类的概念。类这一概念的出现，为面向对象编程中的三个特性（封装性、
继承性、多态性）提供了实现手段。

类使对某一群具有同样属性和方法的对象的抽象。

在 Python 中，习惯性地，我们命名类的时候，采用"驼峰式"命名规则，即单词的首字母为大写，例如
class PhonopyElement. 

在 Python 的类中，函数（方法）(注意这里排除了 staticmethod 和 classmethod) 的参数跟
一般 Python 函数的参数样式有区别，即每个函数包含一个 self
参数，并且使默认的第一个参数。它对应着具体的实例。

在 Python 类中，都会有一个 \__init\__ 初始化函数，有的书称之为构造函数，但其实 Python 中只有
唯一一个构造函数 \__new\__。因此，我们最好都称呼 \__init\__ 初始化函数，

Python 中，类与实例都是对象，因此就有了"类属性"和"实例属性"。

Python 3 中，多重继承的顺序采用 "广度优先" 的原则。

类中的静态方法，依然使用def来定义，但是括号内没有self。由于没有了self，那么也就无法访问
实例变量、类和实例属性了。（？ don't understand very well）

类中的动态方法，类方法的参数中也没有self，但是有cls这个参数。在动态类方法中，能够
访问类属性，但是不能访问实例属性。