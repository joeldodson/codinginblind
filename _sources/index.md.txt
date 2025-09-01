# Coding In Blind

## It's a play on words

Most people reading this page have probably heard the term "going in blind."
It generally means going into something without any, or very little, prior knowledge.
It's figurative, for most people.

This is a site initially created for the blind software developer community.
My intent is to write posts, with examples, and maybe even make videos showing coding with a screen reader.
It might end up just being stuff I've done and want to remember how I did it, so I write an article.

## Why the .vip domain?

Yes, to be sure, everyone these days is a very important person.
In blindness communities however, VIP is often used as Visually Impaired Person.

As I was scrolling through NameCheap to determine if anyone else was using codinginblind, I found all the usual domains were available.
I thought, how about .io, it's cooler than .com.
Or maybe go retro with .net.
Then I scrolled to .vip and thought, "HA! It's got to be that one."

## Intent: What Am I Trying to do Here 

There is certainly no lack of online information available to learn most anything (for better or worse).
And much of that information is accessible (as in a11y) to some useful degree.
I don't intend to write, for example, a Python tutorial.
Or something like an in depth article on, say, what is scope and how does it work in Python. 

My goal is to help blind people with various levels of experience programming.
I hope to do this with articles  on topics I think can be useful.
The articles will likely be inspired by my own experiences and from hearing from other blind developers and the challenges they've faced.
And the content will likely be some high level comments (including opinions) from me with links to go deeper and really learn something.

If you have a topic you'd like to understand better, feel free to leave a comment (see below).
If I think I can add value to what's already online, I might give it a shot.

## High Level Points

This section is intended for either highlighting important points or calling out something I think is interesting but don't intend to write a whole article about.

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

I'm using the pydata-sphinx-theme with sphinx (should be a link at the bottom of every page) to create this site.
I could use a plugin to add line numbers for coding examples,
then reference those line numbers in detailed explanations.
As a screen reader user though, and working with Python where indentation level is very significant,
having line numbers breaks the ability of the screen reader to indicate the level of indentation.

I try to provide sufficient context when describing code examples.
Feel free to leave a comment if something isn't clear enough.

## Comments?

Do you have feedback on any of the articles?
Feel free to open an issue in the 
[codinginblind github repo](https://github.com/joeldodson/codinginblind/issues).

``` {toctree}
:maxdepth: 3
:hidden: false
:caption: Table of Contents

Articles<articles/index.md>
About<about.md>
```
