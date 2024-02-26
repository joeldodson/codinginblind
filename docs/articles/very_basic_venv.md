# Very Basics of Virtual Environments

If you've used computers a while (including mobile devices) you've probably run across the advice to remove and reinstall some software.
Or, at the very least, restart your computer.
And often this resolves the problem.
One reason for this is most software is complex and has dependencies across the platform.
Python is no different.

Virtual environments are an attempt to minimize this problem with dependencies.
They can help keep your project safe from others,
and keep other software on your system safe from your project.
There are a crazy number of ways to create and manage virtual environments,
and they can sound intimidating when you start pulling back the curtain.
You don't need to know many details to get started though.
You can, and arguably should, use virtual environments from the beginning of your Python journey.

Python and pip come with a very simple way to create and manage virtual environments,
we'll go through that in this article. 

Note: I'll be using ``` python ``` to refer to ``` python3 ``` throughout this artivcle.  If you're on Linux or Mac, you probably need to type ``` python3``` unless you've modified your defaults.

## Why Should I Use a Virtual Environment

Okay, I just said you don't need to know this.
Regardless, a high level appreciation is often helpful.

If you're totally new to Python, and maybe programming in general,
you might not have learned about modules.
Think of a module simply as some code you want to use, the details are not important for now.

CPython ships with a standard set of modules.
You can, and almost certainly will, download other modules though for some functionality not part of the standard CPython.
There are many very commonly used modules that are not standard to CPython which might already be on your system.
If you download a newer version of that module to your system, it could affect other programs using that module.

A virtual environment creates a place for you to install modules specific to your project.
Only your project uses those modules, and it only uses modules from your virtual environment.
Thus, you can install modules in your virtual environment and not affect other programs.
And other programs can install modules (outside your virtual environment) and not affect you.

## Creating the Virtual Environment

You've installed python3, Visual Studio Code, the python extension for VS Code, and git on your laptop.
You've configured VS Code with your python interpreter and cloned the project you want to work on.
You're on the command line in your terminal and about to open VS Code in that project directory.
Hold on, let's create a virtual environment first.

The ``` venv ``` module is part of the standard python distribution.
We will use that to create the virtual environment by running the following command:
``` cmd
python -m venv --prompt some_project .venv 
``` 

### what is that text after ``` python ```?

Those are command line parameters that affect how your python interpreter runs.

* the ``` -m venv ``` parameter tells python to run the venv module 
* the ``` --prompt some_project ``` tells venv to use that string for the virtual environment prompt.
  This is not required, I find it useful though.
* the ``` .venv ``` tells venv to place the virtual environment in a directory called ``` .venv ```. 

When python is done creating the virtual environment ( you get your command prompt back),
list the contents of your directory.
You should see a new sub-directory in there named ``` .venv ```.

## Activate the Virtual Environment

This step is slightly different on Linux and Mac than Windows.
ON Windows, the activate file is executed.
On Linux and MacOS, the activate file is sourced.
Note the file paths are different as well.

After activating your virtual environment, your command line prompt should be prefixed with what you set ``` --prompt ``` to when creating the virtual environment.

### Activating a Virtual Environment on Windows

``` cmd
.venv/scripts/activate
``` 

### Activating the Virtual Environment on Linux and MacOS

``` bash 
source .venv/bin/activate
```

## Now Let's Start VS Code

You've activated the virtual environment and now your command line prompt looks something like:
``` cmd 
(some_project) C;\Users\joeld\projects\some_project> 
```

Remember the "some_project" in parentheses at the beginning of the prompt is because I used the command line parameter ``` --prompt some_project ```.
I used that because that's the name of the directory the project is in.
That's a convention I use, it's not a requirement for virtual environments.

IN the terminal where you activated your virtual environment, type:
``` cmd 
code .
``` 
That's the command ``` code ``` followed by the dot (period) character.
the dot is for the current directory.

You should now be in your Visual Studio Code editor.

## Configure the Python Interpreter for VS Code 

Since you've run ``` code ``` from within your activated virtual environment, VS Code should have selected the python interpreter from that environment.
Let's make sure.

*  go to the command pallet, ``` ctrl+shift+p ```
* type "select interpreter"
  VS Code will filter as you type, you might not need to type the entire string
* hit enter on the select interpreter 
* a dialog with a list of available interpreters will be presented and your screen reader should tell you which is currently selected.
  That is, focus in the list will be on the interpreter VS Code is currently using.
* you can arrow up and down on this list and hear the versions and paths of the various interpreters.
  VS Code will tell you which of these is recommended.
  It should tell you the interpreter from your virtual environment is recommended.
  Note the path shown is relative to where you started VS Code.
  That is, the recommended interpreter should sound something like".venv\scripts\python.exe"

## More Reading for More Details

If you've read other Python related articles I've written, you'll know I'm a fan of
[RealPython](https://realpython.com).
I highly recommend this 
[great article on virtual environments](https://realpython.com/python-virtual-environments-a-primer/).

