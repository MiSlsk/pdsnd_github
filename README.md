>**Note**: Please **fork** the current Udacity repository so that you will have a **remote** repository in **your** Github account. Clone the remote repository to your local machine. Later, as a part of the project "Post your Work on Github", you will push your proposed changes to the remote repository in your Github account.

### Date created
2024-06-04

### Project Title
Memoize helper function

### Description
**Wrapper function** _to cache_ temporary results and _speed up_ calculations.

### Files used
memoize.py

### Example
```
from memoize import memoize

@memoize
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

if __name__ == '__main__':
    print(fib(5))
    print(fib(25))
    print(fib(50))
    print(fib(100))
```

### Credits
Thank you Udacity for the contecn.
The most interesting project so far is this one
[Advanced Python Techniques](https://github.com/udacity/cd0010-advanced-python-techniques-project-starter.git)

