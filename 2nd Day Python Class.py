Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
//test pratice of normal function of python

>>> a="gorishankar"
>>> a[1]='a'
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    a[1]='a'
TypeError: 'str' object does not support item assignment
>>> o=[1,2,3,4,5,'gorishankar']
>>> o[1]
2
>>> o[5]
'gorishankar'
>>> o[3]
4
>>> o[1:3:5]
[2]
>>> o[1::6]
[2]
>>> o[2::2]
[3, 5]
>>> o[1::1]
[2, 3, 4, 5, 'gorishankar']
>>> o{1::2]
SyntaxError: invalid syntax
>>> o[1::2]
[2, 4, 'gorishankar']
>>> a[5]="puniya"
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a[5]="puniya"
TypeError: 'str' object does not support item assignment
>>> o[5]="puniya"
>>> o
[1, 2, 3, 4, 5, 'puniya']
>>> p=[2,4,6,8,"puniy"]
>>> o+p
[1, 2, 3, 4, 5, 'puniya', 2, 4, 6, 8, 'puniy']
>>> b=o+p
>>> b
[1, 2, 3, 4, 5, 'puniya', 2, 4, 6, 8, 'puniy']
>>> o
[1, 2, 3, 4, 5, 'puniya']
>>> c=o+2
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    c=o+2
TypeError: can only concatenate list (not "int") to list
>>> c=o+[2]
>>> c
[1, 2, 3, 4, 5, 'puniya', 2]
>>> d=c+[5,4,45]
>>> d
[1, 2, 3, 4, 5, 'puniya', 2, 5, 4, 45]
>>> d.append(65)
>>> d
[1, 2, 3, 4, 5, 'puniya', 2, 5, 4, 45, 65]
>>> 
