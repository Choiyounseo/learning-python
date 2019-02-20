>>> a = 5
>>> b = 5
>>> id(a) == id(b)
>>> True

Python caches short strings and small numbers, to avoid having many copies of them clogging up the system memory. Everything is handled properly under the hood so you don't need to worry a bit, but make sure that you remember this behavior should your code ever need to fiddle with IDs

---

[special else clause]

One of the features I've seen only in the Python language is the ability to have else clauses after while and for loops. It's very rarely used, but it's definitely nice to have. In short, you can have an else suite after a for or while loop. If the loop ends normally, because of exhaustion of the iterator (for loop) or because the condition is finally not met (while loop), then the else suite (if present) is executed. In case execution is interrupted by a break statement, the else clause is not executed.

---

[global and nonlocal statements]

We can alter what happens to the shadowing of the variable name by using one of these two special statements: global and nonlocal.

> > nonlocal <variable-name>

> > global <variable-name>

---

[variable positional arguments]

when we specify a parameter prepending a * to its name, we are telling Python that that parameter will be collecting a variable number of positional arguments, according to how the function is called

```python
arguments.variable.positional.unpacking.py
def func(*args):
 print(args)
values = (1, 3, -7, 9)
func(values) # equivalent to: func((1, 3, -7, 9))
func(*values) # equivalent to: func(1, 3, -7, 9)
```

---

[variable keyword arguments]

```python
arguments.variable.keyword.py
def func(**kwargs):
 print(kwargs)
# All calls equivalent. They print: {'a': 1, 'b': 42}
func(a=1, b=42)
func(**{'a': 1, 'b': 42})
func(**dict(a=1, b=42))
```

(**) : that they are collected in a dictionary

All the calls are equivalent in the preceding example. You can see that adding a ** in front of the parameter name in the function definition tells Python to use that name to collect a variable number of keyword parameters. On the other hand, when we call the function, we can either pass name=value arguments explicitly, or unpack a dictionary using the same ** syntax

---

[combining input parameters]

You can combine input parameters, as long as you follow these ordering rules:
• When defining a function, normal positional arguments come first (name), then any default arguments (name=value), then the variable positional arguments (*name, or simply *), then any keyword-only arguments (either name or name=value form is good), then any variable keyword arguments (**name).
• On the other hand, when calling a function, arguments must be given in the
following order: positional arguments first (value), then any combination of
keyword arguments (name=value), variable positional arguments (*name),
then variable keyword arguments (**name).

```python
arguments.all.py
def func(a, b, c=7, *args, **kwargs):
 print('a, b, c:', a, b, c)
 print('args:', args)
 print('kwargs:', kwargs)
func(1, 2, 3, *(5, 7, 9), **{'A': 'a', 'B': 'b'})
func(1, 2, 3, 5, 7, 9, A='a', B='b') # same as previous one
```

---

[function return values]

if within the body of a function we don't return anything, the function will return None

```python
return.none.py
def func():
 pass
func() # the return of this call won't be collected. It's lost.
a = func() # the return of this one instead is collected into `a`
print(a) # prints: None
```

---

[anonymous function]

func_name = lambda [parameter_list]: expression.

A function object is returned, which is equivalent to this: 

*def func_name([parameter_list]): return expression.*

```python
# example 1: adder
def adder(a, b):
 return a + b
# is equivalent to:
adder_lambda = lambda a, b: a + b
```

---

[functtion attributes]

Every function is a fully-fledged object and, as such, they have many attributes. Some of them are special and can be used in an introspective way to inspect the function object at runtime

---

[map,zip,filter]

```python
>>> grades = [18, 23, 30, 27, 15, 9, 22]
>>> avgs = [22, 21, 29, 24, 18, 18, 24]
>>> list(zip(avgs, grades))
[(22, 18), (21, 23), (29, 30), (24, 27), (18, 15), (18, 9), (24, 22)]
>>> list(map(lambda *a: a, avgs, grades)) # equivalent to zip
```

```python
>>> test = [2, 5, 8, 0, 0, 1, 0]
>>> list(filter(None, test))
[2, 5, 8, 1]
>>> list(filter(lambda x: x, test)) # equivalent to previous one
/// 위의 경우, return x, x가 true가 되는 0이외의 숫자들만 return
[2, 5, 8, 1]
>>> list(filter(lambda x: x > 4, test)) # keep only items > 4
```

---

[comprehensions]

```python
>>> squares = map(lambda n: n**2, range(10))
>>> list(squares)
/// 과,
>>> [n ** 2 for n in range(10)]
/// 동일
```

---

[nested comprehensions]

```python
items = 'ABCDE'
pairs = [(items[a], items[b])
 for a in range(len(items)) for b in range(a, len(items))]
```

---

[generators]

• Generator functions: These are very similar to regular functions, but instead of returning results through return statements, they use **yield**, which allows them to suspend and resume their state between each call
• Generator expressions: These are very similar to the list comprehensions
we've seen in this chapter, but instead of returning a list they return an object that produces results one by one

<generator functions>

```python
first.n.squares.manual.py
def get_squares_gen(n):
 for x in range(n):
 yield x ** 2
squares = get_squares_gen(4) # this creates a generator object
print(squares) # <generator object get_squares_gen at 0x7f158...>
print(next(squares)) # prints: 0
print(next(squares)) # prints: 1
print(next(squares)) # prints: 4
print(next(squares)) # prints: 9
#  next(squares), we're directly calling squares.__next__().
# the following raises StopIteration, the generator is exhausted,
# any further call to next will keep raising StopIteration
print(next(squares))
```

```python
gen.send.py
def counter(start=0):
 n = start
 while True:
 result = yield n # A
 print(type(result), result) # B
 if result == 'Q':
 break
 n += 1
 
c = counter()
print(next(c)) # C
print(c.send('Wow!')) # D
print(next(c)) # E
print(c.send('Q')) # F

###Execution of the preceding code produces the following:
$ python gen.send.py
0
<class 'str'> Wow!
1
<class 'NoneType'> None # <- #E때문에 발생!
2
<class 'str'> Q
Traceback (most recent call last):
 File "gen.send.py", line 14, in <module>
 print(c.send('Q')) # F
StopIteration
```

<generator expressions>

```python
"""yield from expression"""
for n in range(start, end):
 yield n ** 2
# same with
yield from (n ** 2 for n in range(start, end))
```

```python
>>> type(cubes_gen)
<class 'generator'>
>>> list(cubes_gen) # this will exhaust the generator
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
>>> list(cubes_gen) # nothing more to give
[]
```

```python
gen.filter.py
cubes = [x**3 for x in range(10)]
odd_cubes1 = filter(lambda cube: cube % 2, cubes)
# 일반 list
odd_cubes2 = (cube for cube in cubes if cube % 2)
# generator!
```

```python
sum.example.py
s1 = sum([n**2 for n in range(10**6)])
# list
s2 = sum((n**2 for n in range(10**6)))
# generator
s3 = sum(n**2 for n in range(10**6))
# generator
```

Strictly speaking, they all produce the same sum. The expressions to get s2 and s3 are exactly the same because the braces in s2 are redundant. They are both generator expressions inside the sum function. The expression to get s1 is different though. Inside sum, we find a list comprehension. This means that in order to calculate s1, the sum function has to call next on a list, a million times.

```python
list(a for a in range(10))
# 이것또한 generator!!
```

---

we can say that map calls can be twice as fast as equivalent for loops, and list comprehensions can be (always generally speaking) even faster than equivalent map calls.

---

[name localization]

```python
scopes.noglobal.py
ex1 = [A for A in range(5)]
print(A) # breaks: NameError: name 'A' is not defined
```

```python
scopes.for.py
s = 0
for A in range(5):
 s += A
print(A) # prints: 4
```

