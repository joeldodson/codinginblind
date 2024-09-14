# Python and Python3

Here is a very brief description why you type ``` python ``` or ``` python3 ``` at the command line.

## Backward Compatibility

You need to understand this term to appreciate the issue between the commands ``` python ``` and ``` python3 ```.

To say python version X is fully backward compatible means all python programs written for python versions less than X will work with python version X.

This is not the case between python versions 2 and 3. 

## Why is Python 3 not Backward Compatible?

There is no lack of information regarding the decision to break backward compatibility with python3.  Here are two articles from highly regarded voices in the Python community:

* [Python 3 Q & A - Nick Coghlan's Python Notes](https://python-notes.curiousefficiency.org/en/latest/python3/questions_and_answers.html),
* [Why Python 3 exists - Brett Cannon](https://snarky.ca/why-python-3-exists/)

If you're at the very beginning of learning to program and/or brand new to Python, you might want to simply accept that python 3 is not backward compatible and move on.
There's some great details, and history in those articles though, they're interesting for many reasons.

### The Good News

Python 3 was initially released in December, 2008, and python 2 support officially ended in January 2020.
Unless you're maintaining old Python code, you really don't need to know any details other than you might need to run ``` python3 ``` instead of ``` python ```.

If you're considering using a module that still doesn't support Python version 3,
you're almost certainly asking for extra work. 

## Why Not Settle on the Command ``` python ``` Now?

Python was around for many hears before version 3 stirred the pot.
Thus there are probably millions of lines of Python version 2 code still running in the wild.
If a system still has Python version 2 code, scripts running that code will be using the command ``` python ```.
If the ``` python ``` command runs Python version 3, the scripts will most likely fail.

Now, consider needing to update a system that has Python version 2 scripts.
It's highly unlikely you can update all those scripts at one time.
This puts you in a position to need both ``` python ``` and ``` python3 ``` on the same system.
Which also puts you in the position of having the comannd ``` python3 ``` embedded in some of your system scripts.

Now you've completed the migration of your version 2 code to version 3,
you can get rid of the ``` python ``` command.
However, you still have the ``` python3 ``` command in your system scripts.
Thus you need to continue to support ``` python3 ``` as the command to run Python version 3.

## Can I Configure ``` python ``` to also run ``` python3 ```?

If you're absolutely sure there is nothing on your system expecting the command ``` python ``` to be Python version 2,
you can create an alias, or whatever the configuration is on your system,
for ``` python ``` to be Python version 3.

If you system came with Python version 2 already installed as ``` python ```, you'll almost certainly break something if you globally change ``` python ``` to run version 3.