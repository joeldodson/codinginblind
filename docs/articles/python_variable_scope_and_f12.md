# Variable Scope in Python and using f12 in VS Code

This is intended as a brief explanation of the scope of variables in Python and how we can use f12 in VS Code to navigate code and hopefully better understand scope.
I'm assuming the reader already understands variables and how to create them in Python.

## What is Scope?

A very high level definition of scope is where in a program a specific variable can be accessed.
Hopefully when you learned about variables the idea of scope was at least mentioned.
You might not have fully internalized it yet though, or appreciated some of the nuance.
To go deeper than I intend to go here, check out this 
[article on scope from RealPython](https://realpython.com/python-scope-legb-rule/).

## Very Basic Global Scope Example

Consider a Python file with only the following lines of code:
``` python title="basic_scope.py"
--8<-- "src/python/basic_scope.py"
```

The first line creates a variable named "subject" in the global (or file, see below) scope.
The variable is then referenced in the print function within the f-string.

You can copy this code into a file and open it in vscode.
Move your cursor to the use of subject in the print function and hit the 'f12' key.  
VSCode should take you to the immediately previous line.

### Global vs File Scope

I searched around to see if there is a technical difference in Python between global and file scope.
I didn't find anything clear and some places suggesting they're the same.
Though some places implying they're the same doesn't 