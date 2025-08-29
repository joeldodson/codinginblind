# Getting Started with Python on Windows

This is the configuration I use to develop in Python on Windows.
It's of course not the only way to go, and maybe not even the best way to go.
It works for me though and, I think, is fairly easy to setup.

I'm not going to add a lot of links in this article.
It's not (entirely) out of laziness.
Its more about not wanting links to become stale,
and I think I'm giving enough detail for others to find resources they trust.

One of the most valuable skills you'll need as a developer these days is finding sites you trust when you have questions.
Be discerning though as some sites have a very poor content to advertisement ratio.
They seem to be better at optimizing for search engines than generating anything everyone else hasn't already said.

Think of this article as an introduction with very high level notes.
If this setup sounds reasonable, 
it would be good to dig deeper into VS Code, PowerShell, and Virtual Environments on your own.

## Operating System - Windows 11

I moved to Windows 11 (from Windows 10)in, I think, early 2023.
It works well and I tend to install all the updates when they're available.
I know some people like to get something working and stick with it.
I can appreciate that point and will not try to convince anyone to do otherwise.
I personally though find staying current helps when I want to try new features with different technologies.

### Linux?

Yes, you'll almost certainly need to get some experience with Linux if you want to work as a software developer.
Before losing my sight, I used a Mac mainly because of its UNIX core.
I switched to Windows on the advice of other blind developers when I was focused on having an accessible development environment.
Fortunately, this was around the time Windows Subsystem for Linux (WSL) was taking off.
I now use WSL2 to run Ubuntu and other Linux distributions.

There are other options for accessing a Linux environment.

- You can create a Virtual Machine (VM) in a cloud provider (    I find 
[Linode](https://linode.com) to be the most accessible).
You would then use a Windows SSH client to access your VM.

- You can run a version of Linux in a Docker container on Windows.
For this you'll need Docker Desktop and should use it with WSL2. 
I might write another article on how I use Docker locally.
I've started to prefer this over running Ubuntu directly in WSL.
For now, this is probably all I'll say regarding Docker.
There is plenty of information out there already and I encourage anyone interested to learn about Docker (containers in general)

## Screen Reader - NVDA

I use the NVDA screen reader from 
[NVAccess](https://www.nvaccess.org) on Windows 11.
I have Line Indenting Reporting set to tone and speak 
under the Document Formatting settings.
I consider this essential for Python and still nice to have for other languages.

## Code Editor - Visual Studio Code (VS Code) 

I use 
[Visual Studio Code](https://code.visualstudio.com)
with the Microsoft Python extension.  
The documentation is very good and Microsoft seems to have a commitment to accessibility beyond lip service.
You might want to start by reading the 
[docs regarding accessibility](https://code.visualstudio.com/docs/editor/accessibility)

### Is VSCode Visual Studio?

No. [Visual Studio](https://visualstudio.com) 
is an Integrated Development Environment (IDE).
VS Code is technically a code editor.
The details are not that important.
Think of an IDE as batteries included (e.g., compilers and debuggers), 
where as in a code editor you'll need to install extensions (or plugins, or whatever your editor calls them).

You can certainly use the Visual Studio IDE if you prefer,
I hear its accessibility is good as well.
It might be easier though to start with VS Code as it has fewer options and very broad adoption  across the industry.

### Extensions, Keyboard Shortcuts, and the Command Pallet

Once you've familiarized yourself with the layout of VS Code and the accessibility features,
spend time learning some of the most useful keyboard shortcuts (ctrl+k, ctrl+s) and the command pallet (ctrl+shift+p).
Also, since much of the functionality you'll use will come from extensions, learn how to search and install them (ctrl+shift+x).
You can practice this by installing the Python extension from Microsoft.

### Which Extensions Should I use?

I'd start with fewer extensions as you're getting familiar with the editor.
VS Code is good at suggesting extensions if you're trying to do something and don't have that functionality available.
For example, if you're trying to format your code (alt-shift-f) and don't have a Python formatting extension installed,
VS Code will suggest one for you.
I suggest starting with only the Python extension (from Microsoft) and go with whatever else VS Code suggests.

If VS Code does suggest an extension and you can't remember what it said,
go to the status bar (f6) then arrow until you get to "notifications".  
Hit enter on notifications and you'll find the message regarding the extension.
From there you can select 'yes' to have the extension installed.

## Python Interpreter

Continuing the theme of simplicity and broad adoption, I like the defacto-standard cPython interpreter.
I opt for installing it from 
[python.org/download](https://python.org/download)
it's easy to download and run the installer, 
and it installs a little program called ``` py.exe``` as well (more on that below).
Make sure to check the box to have the installation update your PATH.

### Why Not Install from the Windows Store?

You certainly can do that, and I have done that before.
My information is old so maybe I'm wrong.
My experience though was the Windows store did not have the latest versions of the various Python versions,
(e.g., 3.10.11, 3.11.5)
and I don't like the Store UX/UI.  It's painful even if it is technically accessible.

Regardless of how you choose to install Python, and which interpreter and/or environment you use,
I suggest being consistent (always use the store, or python.org, don't mix them). 

### Multiple Versions of Python (py.exe)

You can install multiple versions of Python either through the store or from python.org (and other ways).
I currently have versions 3.10, 3.11, and 3.12 installed from python.org.

To use a specific version, I can specifically type the version:
``` bash
%> python3.11 --version 
```
That only works if I have my PATH setup with all versions of Python, which I don't.

I do however have ``` py.exe ``` on my PATH.
And because I've installed all my Python versions from python.org, ``` py.exe ``` knows about them all.
And I think ``` py.exe ``` is only installed from python.org, but not sure.
That is, if you've installed Python from the Windows Store and don't have ``` py.exe```, that might be why.

I can list all the versions ``` py.exe ``` knows of:
``` bash 
PS C:\Users\joeld> py --list
 -V:3.12 *        Python 3.12 (64-bit)
 -V:3.11          Python 3.11 (64-bit)
 -V:3.10          Python 3.10 (64-bit)
```
And I can run a specific version
(NOTE: the argument ```--version ``` on the command line is to tell the Python interpreter to print its version string.
It's an easy way to check if your PATH is correct and your interpreter actually runs.):
``` bash 
PS C:\Users\joeld> py -3.11 --version
Python 3.11.5
```

## PowerShell and Always Use a Virtual Environment

### The Command Line

I've always been more comfortable in a command line environment.
And now, as a blind developer, I like the accessibility of the command line.
On Windows, I use PowerShell, currently on version 7.3.9.
I recall there was already some kind of PowerShell available when I installed Windows 10 the first time, that's not the right one.
Windows 11 might already come with PowerShell 7.  If not, install it from Microsoft.

The following commands for creating an development environment are all run from a PowerShell prompt (though I edited the prefix) 

### Creating the Virtual Environment
Here is a 
[great article on virtual environments](https://realpython.com/python-virtual-environments-a-primer/).
I highly suggest you read it to understand how Python knows which files to install from where.
(RealPython is one of the Python sites I trust for very good explanations.)

If I want to develop or test something using Python 3.10,
I'll start by creating a virtual environment (plus some other steps):
``` bash 
tmp> mkdir py3.10-project
[edited output]
tmp> cd py3.10-project
tmp\py3.10-project> py -3.10 -m venv --prompt 3.10project .venv
tmp\py3.10-project> ./.venv/scripts/activate
(3.10project) tmp\py3.10-project> python --version
Python 3.10.11
(3.10project) tmp\py3.10-project> where.exe python
C:\Users\joeld\tmp\py3.10-project\.venv\Scripts\python.exe
C:\Program Files\Python311\python.exe
C:\Users\joeld\AppData\Local\Programs\Python\Python312\python.exe
C:\Users\joeld\AppData\Local\Programs\Python\Python310\python.exe
C:\Users\joeld\AppData\Local\Microsoft\WindowsApps\python.exe
```

Let's go over what just happened:

1. created a new directory for the project and cd into it 
1. created a virtual environment using ``` py ``` to specify I want to run python version 3.10
    * ``` -m venv ``` is to run the venv module which is now included in the standard cPython distribution 
    * ``` --prompt 3.10project ``` is to specify a prompt for this virtual environment 
    * ``` .venv ``` is to have the virtual environment created in a directory named .venv
1. I activate the environment by running the activate script in the new virtual environment
    * Notice after this the command line prompt has changed to include '(3.10project)'
1. Now that I'm in the activated virtual environment, ``` python ``` refers to the version of Python used to create the virtual environment
    * ran ``` python --version ``` to show this
1. where.exe shows everywhere on your PATH the specified program exists
    * notice python in our new virtual environment is the first one, that's good

### Launching VS Code

Now that we have an activated virtual environment, let's start VS Code.
From the command prompt, simply type:
``` bash 
(3.10project) tmp\py3.10-project> code .
```
That is, ``` code ``` is the program name and ``` . ``` (dot) is the directory to open.
(The dot (period character) always represents the current directory.)
The VS Code UI will open ready to edit files in that directory.

## Tell VS Code which Python to use

We'll use the command pallet for this, and the shortcut keys to get there.

Assuming you've installed the Microsoft Python extension already, 
type ``` ctrl+shift+p``` to bring up the command pallet.
You'll be automatically in the search field.
Type 'select python interpreter' and you should be on the command.
The number of matches is filtered as you type, you probably will not need to type all three words.
Hit enter and you should get a list of available python environments.

If you launched VS Code from within an activated virtual environment, 
the python interpreter from the .venv environment should already be selected.
And you can simply hit enter to keep that choice.
Otherwise, you can arrow up and down to select the appropriate interpreter. 

## Edit and Run Your Python Files

Now you can create your hellow_world.py file in VS Code.
You can run the file directly in VS Code, and there is a terminal that is accessible.
I'm not a big fan of that workflow though.
I like to edit the code then pop back out to my PowerShell to run the code.
That is, ``` alt+tab ``` to get back to your PowerShell window, then:
``` bash 
(3.10project) tmp\py3.10-project > python hello_world.py 
``` 
And you should see any output in that window (like we did when creating the virtual environment).

Ken noted you can also use ``` ctrl+shift+c ``` to have VS Code open a command shell using it's current working directory. 
If you had opened VS Code as described above, that should be the directory with your source code.
Ken also noted you can change the default shell from ``` sh ``` to something else, e.g.e, PowerShell. 
That's done in the settings which can take some getting used to.
Instead of trying to explain it here, I suggest you bing it. 

## I Think That's It 

Hopefully this gets you started with a basic environment and understanding to build from.
If you have questions, or want more details, please open an issue at the
[the codinginblind repo](https://github.com/joeldodson/codinginblind/issues).

Cheers!

Joel 

## Credits

I'll add notes here to give credit to people who help make this better and correct my mistakes.

*  Thanks Ken for pointing out the alt-f4 which should be alt-tab 
  (already fixed if you don't see any alt-f4 in the text.)
    And thanks for the ctrl+shift+c shortcut reminder.
