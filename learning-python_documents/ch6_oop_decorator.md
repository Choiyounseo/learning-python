# OOP, Decorators, Iterators

### Decorators

```python
decorators/time.measure.arguments.py
from time import sleep, time

def f(sleep_time=0.1):
 sleep(sleep_time)

def measure(func, *args, **kwargs):
 t = time()
 func(*args, **kwargs)

measure(f, sleep_time=0.3)
measure(f, 0.2)
```

```python
decorators/syntax.py
def func(arg1, arg2, ...):
 pass
func = decorator(func)

# is equivalent to the following:

@decorator
def func(arg1, arg2, ...):
 pass
```

```python
def func(arg1, arg2, ...):
 pass
func = deco1(deco2(func))
# is equivalent to the following:
@deco1
@deco2
def func(arg1, arg2, ...):
 pass
```

The closer the decorator to the function, the sooner it is applied.



```python
decorators/syntax.py
def func(arg1, arg2, ...):
 pass
func = decoarg(argA, argB)(func)
# is equivalent to the following:
@decoarg(argA, argB)
def func(arg1, arg2, ...):
 pass
```

---

### OOP(Object-oriented programming)

Object-oriented programming (OOP) is a programming paradigm based on the concept of "objects", which are data structures that contain data, in the form of attributes, and code, in the form of functions known as methods. A distinguishing feature of objects is that an object's method can access and often modify the data attributes of the object with which they are associated (objects have a notion of "self").

`object = instance of class`



####[Inheritance and Composition]

**Inheritance** means that two objects are related by means of an Is-A type of relationship.

**composition** means that two objects are related by means of a Has-A type of relationship. 

`issubclass()` : library exists



####[Accessing base class]

```python
oop/super.explicit.py
class Book:
 def __init__(self, title, publisher, pages):
     self.title = title
     self.publisher = publisher
     self.pages = pages

class Ebook(Book):
 def __init__(self, title, publisher, pages, format_):
 	Book.__init__(self, title, publisher, pages)
 	self.format_ = format_

# same with
class Ebook(Book):
 def __init__(self, title, publisher, pages, format_):
 	super().__init__(title, publisher, pages)
 	# Another way to do the same thing is:
 	# super(Ebook, self).__init__(title, publisher, pages)
 	self.format_ = format_
```



####[Method resolution order(MRO)]

By now, we know that when you ask for someobject.attribute, and attribute is not found on that object, Python starts searching in the class someobject was created from. If it's not there either, Python searches up the inheritance chain until either attribute is found or the object class is reached. This is quite simple to understand if the inheritance chain is only comprised of single inheritance steps, which means that classes have only one parent. However, when multiple inheritance is involved, there are cases when it's not straightforward to predict what will be the next class that will be searched for if an attribute is not found.

```python
oop/mro.py
class A:
 label = 'a'
class B(A):
 pass # was: label = 'b'
class C(A):
 label = 'c'
class D(B, C):
 pass
d = D()
print(d.label) # 'c'
print(d.__class__.mro()) # notice another way to get the MRO
# prints:
# [<class '__main__.D'>, <class '__main__.B'>,
# <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
```



####[Static & Class methods]

staticmethod에서는 부모클래스의 클래스속성 값을 가져오지만, classmethod에서는 cls인자를 활용하여 cls의 클래스속성을 가져옴.

```python
oop/class.methods.factory.py
class Point:
 def __init__(self, x, y):
     self.x = x
     self.y = y
 @classmethod
 def from_tuple(cls, coords): # cls is Point
     return cls(*coords)
 @classmethod
 def from_point(cls, point): # cls is Point
     return cls(point.x, point.y)

p = Point.from_tuple((3, 7))
print(p.x, p.y) # 3 7
q = Point.from_point(p)
print(q.x, q.y) # 3 7
```



#### [name mangling]

파이썬에서 선언되는 모든 속성(변수)와 method : public(private이 없음)

-> name mangling 사용

> > no leading underscores : public(can access it and modify it freely)

> > single underscore : private ( 내부적으로 사용하는 변수 / used internally and you should not use it or modify it from the outside)

> > doulble underscore : 클래스 외부에서 접근할 수 없도록 내부 변수로 만듦



```python
oop/private.attrs.fixed.py
class A:
 def __init__(self, factor):
 	self.__factor = factor
 def op1(self):
 	print('Op1 with factor {}...'.format(self.__factor))
    
class B(A):
 def op2(self, factor):
 	self.__factor = factor
 	print('Op2 with factor {}...'.format(self.__factor))

obj = B(100)
obj.op1() # Op1 with factor 100...
obj.op2(42) # Op2 with factor 42...
obj.op1() # Op1 with factor 100... <- Wohoo! Now it's GOOD!
```

This means that when you inherit from a class, the mangling mechanism gives your private attribute two different names in the base and child classes so that name collision is avoided. (__)



#### [Property decorator]

```python
class PersonWithAccessors:
 def __init__(self, age):
 self._age = age
 def get_age(self):
 return self._age
 def set_age(self):
 if 18 <= age <= 99:
 self._age = age
 else:
 raise ValueError('Age must be within [18, 99]')
# person.get_age, person.set_age를 이용해 변경 및 값 가져오기 가능
```

```python
# @setter, getter decorator를 이용하는 방법
class PersonPythonic:
 def __init__(self, age):
     self._age = age
     
 @property
 def age(self):
     return self._age
     
 @age.setter
 def age(self, age):
     if 18 <= age <= 99:
         self._age = age
     else:
         raise ValueError('Age must be within [18, 99]')
         
person = PersonPythonic(39)
print(person.age) # 39 - Notice we access as data attribute
person.age = 42 # Notice we access as data attribute
print(person.age) # 42
person.age = 100 # ValueError: Age must be within [18, 99]
```



#### [Operator overloading]

다른 특수 메쏘드들을 정의함으로써, 사용자 정의 형들에 대한 연산자들의 동작을 지정할 수 있습니다. 예를 들어, Time 클래스에 __add__ 라는 메쏘드를 정의하면, Time 객체들에 + 연산자를 사용할 수 있게 됩니다.

---

### custom iterator

• Iterable: An object is said to be iterable if it's capable of returning its
members one at a time. Lists, tuples, strings, dicts, are all iterables. Custom objects that define either of `__iter__` or`__getitem__` methods are also iterables.

• Iterator: An object is said to be an iterator if it represents a stream of data. A custom iterator is required to provide an implementation for `__iter__` that returns the object itself, and an implementation for `__next__`, which returns the next item of the data stream until the stream is exhausted, at which point all successive calls to `__next__` simply raise the StopIteration exception. Built-in functions such as iter and next are mapped to call `__iter__` and `__next__` on an object, behind the scenes.

