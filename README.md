
# Learn Python - A simplified documentation on Python.

Hello folks, you can call me PEACE. As you can see the heading, this is an unofficial, simplified documentation for Python, for beginners. In this repository, I have tried to explain Python as simple as possible. So without wasting any more time, let's begin!

## **Python**
**What is Python ?** 

Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. In sort, it's an easy programming language that one can learn. It's readability is way better as compared to any other programming language out there. Also the Python community is so helpful, healthy and active.  I believe this is all you need to know about Python(summary ofcourse).

## **Python VS**
**Now let's begin to compare python with other programming language(s).**\
I will be comparing Python only with Java, Javascript, C++, C and Pearl here.

****VS JAVA****\
Runs slower as compared to Java but at the same time Python also takes less time to 
to develop.Usually a python program is 3 to 5 times smaller when compared to Java.

****VS JAVASCRIPT****\
Python's "object-based" subset is roughly equivalent to JavaScript. Like Javascript, Python uses simple language unlike putting everything under class.

****VS PERL****\
Both kinda comes from same background, [unix scripting](https://www.tutorialspoint.com/unix/shell_scripting.htm) and do share many similarities despite having a different philosophy. Like both do have different purpose but yet they share some similiarities.

****VS C++****\
This comparision will be somewhat similar to Python VS Java. Almost everything discussed with Java is same with C++ but usually Python program is 10 to 15 times smaller when compared with C++ Program.

****VS C****\
In simplified language, there is ease of development in Python when compared with C. Also this comparsion is similar to Python VS Java and C++.


# Installing Python
- [Windows](https://www.python.org/ftp/python/3.11.1/python-3.11.1-amd64.exe) ⚠️Note that Python 3.9+ cannot be used on Windows 7 or earlier.
- [macOS](https://www.python.org/ftp/python/3.11.1/python-3.11.1-macos11.pkg)
- [Other OS](https://www.python.org/download/other/)

# IDE(s) for Python
Virtual Studio Code aka VSCode
- [Windows](https://code.visualstudio.com/sha/download?build=stable&os=win32-x64-user) ⚠️ windows 8 and above only.
- [macOS](https://code.visualstudio.com/sha/download?build=stable&os=darwin-universal)
- [Linux .deb](https://code.visualstudio.com/sha/download?build=stable&os=linux-deb-x64)
- [Linux .rpm](https://code.visualstudio.com/sha/download?build=stable&os=linux-rpm-x64)

PyCharm by JETBRAINS
- [Windows](https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=windows)
- [macOS .dmg intel](https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=mac)
- [macOS .dmg silicon](https://download.jetbrains.com/python/pycharm-professional-2022.3.1-aarch64.dmg)
- [Linux](https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=linux)

Above are some of good ide(s) in which you can code python on. I personally use PyCharm more because it's UI is so simple, I mean VSCode UI is good too but for some reason I prefer PyCharm.

# Writing first code in Python.

Let's begin with Writing our first code in Python. Literally in every single documentation and books, first code I have ever seen is printing hello world. Have you ever wondered why? I got to know recently, it is because in a book named [The C Programming Language by Brian Kernighan and Dennis Ritchie](https://en.wikipedia.org/wiki/The_C_Programming_Language) had first code as printing hello world, since then it is kind of made universal to have print hello world as a first code for any beginner in any programming language. Guess what? our first code won't be to print "Hello world".

[First code](https://github.com/peacekeeper09/Learn-Python/blob/main/first%20program.py)\
```print("Spread PEACE")```
# Python Syntax
**Python Indentation**\
Indentation refers to the spaces at the beginning of a code line.\
Important in Python.\
Python uses indentation to indicate a block of code.

**Python Variables**\
Declaring variables in Python? It is easy. Python Variable does not needs to define the data type or such like in some programming language.

We have to always keep the variable name in string, it should not be any special character or any integer.
You can check how to use variables from [here](https://github.com/peacekeeper09/Learn-Python/blob/main/variables.py).

You should keep a note that variable is case sensitive. Example [here](https://github.com/peacekeeper09/Learn-Python/blob/main/case%20sensitive-variable.py).

# Comments in Python

You can simply add up a comment in Python by using #, example [here](https://github.com/peacekeeper09/Learn-Python/blob/main/comment.py).\
Adding up a comment in a program makes it user friendly and actually allows you or your fellow worker to understand the code easily when you are accessing it later for rewriting the code or updating some feature.

# Data Type(s) in Python

|Text Type| str     | 
| :-------- | :------- |
| Numeric Types     | 	int, float, complex|
|Sequence Types|	list, tuple, range|
|Mapping Type|	dict|
|Set Types|	set, frozenset|
|Boolean Type|	bool|
|Binary Types|	bytes, bytearray, memoryview|
|None Type|	NoneType|

You can get to see the example/usage of each data types in [here](https://github.com/peacekeeper09/Learn-Python/blob/main/data%20type.py).

# Types of operators in Python.

Operators are used to perform operations in Python.\
One of simplest example of operators is addition and substraction.

**Let's dive more deeper into "operators in Python."**\
Operators in Python can be divided into following major groups:-

- Arithmetic operators
- Assignment operators
- Comparison operators
- Logical operators
- Identity operators
- Membership operators
- Bitwise operators

Now let's see each operators closely.

- ****Arithmetic operators in Python****\
Used only with numeric values to perform simple/complex mathematics opeartions/calculations.

|Arithmetic operators|  sign | usage|
| :---- | :----|:------- |
|  Addition   | 	+| [x+y](https://github.com/peacekeeper09/Learn-Python/blob/main/operators.py)|
|substraction|	-|[x-y](https://github.com/peacekeeper09/Learn-Python/blob/main/operators.py)|
| Multiplication|	*|[x*y](https://github.com/peacekeeper09/Learn-Python/blob/main/operators.py)|
|Division|	/|[x/y](https://github.com/peacekeeper09/Learn-Python/blob/main/operators.py)|
|Modulus|	%|[x%y](https://github.com/peacekeeper09/Learn-Python/blob/main/operators.py)|
|Exponentation|**|[x**y](https://github.com/peacekeeper09/Learn-Python/blob/main/operators.py)|
|Floor Division|	//|[x//y](https://github.com/peacekeeper09/Learn-Python/blob/main/operators.py)|

- ****Assignment Operators in Python****
> Used to assign values to a specified variable.

|Assignment Operators | usage| same as|
| :---- |:------- |:---|
|  =   | [x= 7](https://github.com/peacekeeper09/Learn-Python/blob/main/operators.py)| x= 7|
|+=	| [x += 7](https://github.com/peacekeeper09/Learn-Python/blob/main/operators.py)| x= x+7|
| -=|[x-=7](https://github.com/peacekeeper09/Learn-Python/blob/main/operators.py)| x = x-7|
|*=|[x *= 7](https://github.com/peacekeeper09/Learn-Python/blob/main/operators.py)|x = x*7|
|/=|	[x/=7](https://github.com/peacekeeper09/Learn-Python/blob/main/operators.py)| x = x/7|
|%=|[x%=7](https://github.com/peacekeeper09/Learn-Python/blob/main/operators.py)| 	x = x % 7|
|//= |[x//=7](https://github.com/peacekeeper09/Learn-Python/blob/main/operators.py)|x = x // 7|
|  **=  | [x**=7](https://github.com/peacekeeper09/Learn-Python/blob/main/operators.py)| x = x ** 7|
|&=	| [x &=	7](https://github.com/peacekeeper09/Learn-Python/blob/main/operators.py)| 	x = x & 7|
| ^= 	|[x ^= 7](https://github.com/peacekeeper09/Learn-Python/blob/main/operators.py)| x = x ^ 7|
|>>=	|[x>>=	7](https://github.com/peacekeeper09/Learn-Python/blob/main/operators.py)|	x = x >> 7|
|<<=|	[x<<=7](https://github.com/peacekeeper09/Learn-Python/blob/main/operators.py)| x = x << 7|


- ****Comparison Operators in Python****
> Use to compare two values.


|Comparison operators|  sign | usage|what does it do?
| :---- | :----|:------- |:--|
|  Equal   |==	| [x==y](https://github.com/peacekeeper09/Learn-Python/blob/main/operators.py)| compares if the value of two given element is same or not.|
|Not equal|!=|[x!=y](https://github.com/peacekeeper09/Learn-Python/blob/main/operators.py)|checks if the value of two given element is not equal or not.|
| Greater than|	>|[x>y](https://github.com/peacekeeper09/Learn-Python/blob/main/operators.py)|checks if the value of a given element is greater than that of another element.|
|Less than	|	<	|[x<y](https://github.com/peacekeeper09/Learn-Python/blob/main/operators.py)| checks if the value of a given element is smaller than that of another element.|
|Greater than or equal to	|	>=	|[x>=	y](https://github.com/peacekeeper09/Learn-Python/blob/main/operators.py)| checks if the value of a given element is greater than or equal to the another element.
|Less than or equal to	|<=|[x<=y](https://github.com/peacekeeper09/Learn-Python/blob/main/operators.py)| checks if the value of a given element is smaller than or equal to the another element.

- **Logical Operators in Python**
> Basically used to combine up operators.

|Logical Operators | usage| what does it do?|
| :---- |:------- |:---|
|  and | [x < 7 and  x < 9](https://github.com/peacekeeper09/Learn-Python/blob/main/operators.py)| This will return True if the given condition is true. |
|or	| [x < 7 or  x < 9](https://github.com/peacekeeper09/Learn-Python/blob/main/operators.py)| This will return True if any of the given condition is true.|
| not|[not(x < 7 and x < 9)](https://github.com/peacekeeper09/Learn-Python/blob/main/operators.py)| This will return False if the condition is true and True if the condition is false.|

- **Identity Operators in Python**
> Used to check if two element are equal or not.

|Identity Operators | usage| what does it do?|
| :---- |:------- |:---|
|  is  | [x is y](https://github.com/peacekeeper09/Learn-Python/blob/main/operators.py)| This will return True if both the elements are same. |
|is not| [x is not y](https://github.com/peacekeeper09/Learn-Python/blob/main/operators.py)| This will return True if both the elements are not same.|

- **Membership Operators in Python**
> Membership operators are used to test if a sequence is presented in an element.

|Membershit Operators | usage| what does it do?|
| :---- |:------- |:---|
|  in   | [x in  y](https://github.com/peacekeeper09/Learn-Python/blob/main/operators.py)| This will return True sequence with the specified value is present in the element. |
|is not| [x is not y](https://github.com/peacekeeper09/Learn-Python/blob/main/operators.py)| This will return True if True if a sequence with the specified value is not present in the object.|

- **Bitwise Operators**
> Used to compare binary numbers.

|Bitwise Operators|NAME| what does it do?|
| :---- |:------- |:---|
|  &    |AND| 	Sets each bit to 1 if both bits are 1.|
|^|	XOR|	Sets each bit to 1 if only one of two bits is 1.|
|~|	NOT|	Inverts all the bits.|
|<<	|Zero| fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off.|
|>>	|Signed right shift	|Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off.|

`|`	`OR` `Sets each bit to 1 if one of two bits is 1.`\
That's it. We covered all the operators in Python! 🤗 

# Python If Else
Let's begin with understand `If` and `Else` in Python.


