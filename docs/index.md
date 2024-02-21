# Coding In Blind

## It's a play on words

Most people reading this page have probably heard the term "going in blind."
It generally means going into something without any, or very little, prior knowledge.
It's figurative, for most people.

This is a site initially created for the blind software developer community.
My intent is to write posts, with examples, and maybe even make videos 
showing coding with a screen reader.

I am by far standing on the shoulders of giants in this space.
There are many highly talented blind developers 
who have been developing software very successfully for decades.
I lost my sight in 2017 thus have been coding with a screen reader since then.
I guess another benefit I'm hoping to get from this site
is encouraging me to be better with the existing tools, so I can, maybe, someday, be one of those giants.

## Why the .vip domain?

Yes, to be sure, everyone these days is a very important person.
In blindness communities however, VIP is often used as Visually Impaired Person.

As I was scrolling through NameCheap to determine if anyone else was using codinginblind, I found all the usual domains were available.
I thought, how about .io, it's cooler than .com.
Or maybe go retro with .net.
Then I scrolled to .vip and thought, "HA! It's got to be that one."

If you're paying close attention though, you'll see 
the address bar in your browser is no longer "codinginblind.vip".
I'm using a 3xx redirect from NameCheap to route requests to my github pages.
If this project really takes off, maybe I'll pay for github enterprise and use my own domain on pages.

## Intent: What Am I Trying to do Here 

There is certainly no lack of online information available to learn most anything (for better or worse).
And much of that information is accessible (as in a11y) to some useful degree.
I don't intend to write, for example, a Python tutorial.
Or something like an in depth article on, say, what is scope and how does it work in Python. 

My goal is to help blind people with various levels of experience programming.
I hope to do this with articles  on topics I think can be useful.
The articles will likely be inspired by my own expereinces and from hearing from other blind developers and the challenges they've faced.
And the content will likely be some high level comments (including opinions) from me with links to go deeper and really learn something.

If you have a topic you'd like to understand better, feel free to leave a comment (see below).
If I think I can add value to what's already online, I might give it a shot.

## Code Examples

All code examples should be found under the ``` src ``` directory in the codinginblind repo.
What you read in the docs is imported from files in the ``` src ``` directory using an mkdocs extension.

### Python

With each code example block, there should be a "copy to clipboard" button.
If you click that and paste that code into the Python REPL, it should run and you can read the output.
With that in mind, I'm not planning to list the output along with the examples.

## High Level Points

This section is intended for either highlighting important points or calling out something I think is interesting but don't intend to write a whole article about it. 

### Always use a Virtual Environment in Python

Sure, this is my opinion and Python will work without a virtual environment.
By starting with one from the beginning though, you'll likely save yourself some headaches later.
To better appreciate their value, check out this
[great article on virtual environments](https://realpython.com/python-virtual-environments-a-primer/).

### F-Strings in Python

Python 3.6 brought us the lovely f string.
Syntactically, it's a string preceded by the letter 'f'. 
For example, you'll see code like:
``` python
ret = function_one()
print(f"return value from function_one is {ret}")
```

For a deep understanding of what f strings are, and their benefits, read this
[article on f strings from RealPython](https://realpython.com/python-f-strings/).

## No Line Numbers in Example Code

I'm using the material theme for mkdocs (shuld be a link at the bottom of every page).
I could use a plugin to add line numbers for coding examples,
then reference those line numbers in detailed explanations.
As a screen reader user though, and working with Python where indentation level is very significant,
having line numbers breaks the ability of the screen reader to indicate the level of indentation.

I try to provide as much context when describing code examples.
Feel free to leave a comment if something isn't clear enough.

## Comments?

Do you have feedback on any of the articles?
Feel free to open an issue in the 
[codinginblind github repo](https://github.com/joeldodson/codinginblind/issues).
