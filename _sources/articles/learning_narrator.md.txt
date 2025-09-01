# Learning Narrator

For several years now, Microsoft has been showing Narrator some love.
It's getting to the point of being a real option for your daily driver.
At the very least, it's a great option for getting unstuck when you run into problems while using other screen readers on Windows.
In this article we'll go through some of the basics and highlight some useful references for later.

If you are brand new to screen readers, this might not be the best resource to get started.
Hopefully you have access to a blindness organization to help learning some basics.
Once you have some screen reader fundamentals down, this resource should be at a good level of depth to get going with Narrator.

Before jumping into using Narrator to get around Windows and interact with various applications,
let's go over some basics.

## Getting Started

### Microsoft's Official Online Documentation 

IN the interest of teaching to fish (not giving out fish), the most important link you should know is 
[Microsoft support's Introduction to Narrator](https://support.microsoft.com/en-us/windows/complete-guide-to-narrator-e4397a0d-ef4f-b386-d8ae-c172f109bdb1)

That page has two important areas, a table of contents with links and descriptions to chapters, followed by highlights of what's new in the latest release.
And it is well structured with semantic HTML.

If you want the table of contents, find the first HTML table then navigate by links to get to each chapter.
Following the table of contents, Each main feature in what's new is summarized under an HTML level 2 heading.

### First, Necessary Keyboard Shortcuts

My first thought when learning a new screen reader is how do I speed up the voice.
But first, how to even get started.

#### Turning on and off Narrator: ```windowsKey+ctrl+enter```

The keyboard command ```windowsKey+ctrl+enter``` toggles Narrator on and off.
That is technically a shortcut that can be disabled.
My experience though, especially at Costco and Best Buy, is that shortcut is enabled by default.

You can also exit Narrator with ```narratorKey+esc```.
I have no idea why there is a separate way to exit.

#### Narrator Modifier Key: ```capsLock``` and ```insert```

Both the ```insert``` key and ```capsLock``` can be used as modifiers for Narrator.
As far as I know, the ```capsLock``` behaves identically to the ```insert``` key.
That's how NVDA works as well;
in either laptop or desktop mode, the ```capsLock``` works identically to the ```insert``` key.
In JAWS, on my 15 inch laptop with a full keyboard (including num pad), 
I found by configuring JAWS to use a desktop keyboard, and enabling ```capsLock``` as the JAWS key, there were slight functional differences between ```capsLock``` and ```insert```.

For simplicity, two versus four syllables, and less typing, I'll use the term ```capsLock``` when referring to the Narrator modifier key.

#### Changing Voice Speed: ```capsLock+minus```, ```capsLock+plus```

The "minus" and "plus" are technically the hyphen and equals keys to the right of the 0 key near the top of the keyboard, below the function keys.
The increase/decrease voice speed is documented as ```ctrl++``` and ```ctrl+-```.
There is no need to hold down the shift key though to get the plus sign, it's simply an easy way to label that key.
If you have a keyboard with a num pad, the num pad plus and minus keys do not alter voice playback speed.

#### Speech History: ```capsLock+x```, ```capsLock+ctrl+x```, ```capsLock+alt+x```

Following are shortcuts to quickly access the last spoken phrase, copy that to the copy and paste buffer, and to enter a buffer containing the last 500 spoken phrases.

- **repeat last spoken phrase: ```capsLock+x```**
- **copy last spoken phrase: ```capsLock+ctrl+x```**
- **enter buffer with last 500 spoken phrases: ```capsLock+alt+x```** -
  You can move around this buffer in the same way you'd move around a text document,
  including the same commands to highlight and copy text.

### Narrator Home

The first time you start Narrator, you'll be presented with the Narrator Home screen.
Home gives access to a quick start guide, what's new section, the feedback form, online documentation, and some basic configuration settings.
There is a checkbox to disable showing Narrator home when Narrator starts.
You can access Narrator Home through Narrator settings, don't fear you'll be missing something if you disable it on startup.

### Give Feedback: ```capsLock+alt+f```

You can access the feedback form at any time using the keyboard shortcut, you don't have to go through Narrator Home.

### configuration: ```windowsKey+ctrl+n```

This will launch you into the accessibility settings.
Many of the settings are collapsed by default.
pay close attention to "show more" buttons, what you're looking for might be buried deeper in those settings.

#### Start Narrator Before and After Sign On

The very first show more button exposes the check boxes to have Narrator started automatically before sign on and after sign on.
If Narrator is your daily driver, you probably want to check both of these boxes.

#### And the Usual Suspects

And of course you can change the voice synthesizer, download new voices, change verbosity, configure braille, and so on.
It's probably a better use of your time to go through the settings than read about them here.

### References for More Learning

Continuing the teaching to fish metaphor, telling learners where they are likely to find fish is a key element to a successful fishing career.
Following are keyboard shortcuts and links useful when trying to remember a certain function, or wanting to discover more features.

#### Keyboard Shortcuts for Help

- **input learning (keyboard input help): ```capsLock+1```** - 
  This is a great way to explore keyboard shortcuts and probably familiar to users of other screen readers.
  It puts you in a mode where everything you type is captured by the screen reader.
  If what you type is a screen reader command, you will hear what that command is.
  You must type ```capsLock+1``` again to exit this mode.
- **all commands search: ```capsLock+f1```** - list of all available keyboard commands. 
  drops you initially into a search box.
  Try typing in words to describe what you're trying to do, for example, "increase",
  will narrow down the list of commands related to increasing something (e.g., voice volume or speed)
  press escape key to exit.
- **available item command help: ```capsLock+f2```** - simlar to ```capsLock+f1``` but limited to commands relevant to the item with focus.
  Also puts you in search box initially.
  Press escape key to exit.

#### Links to Microsoft Resources for Keyboard Shortcuts

Here is where the fish are really biting...

I'll occasionally spend time going through lists of keyboard commands.
I find it a good way to refresh my memory as well s find functionality I didn't know, or forgot, exists.
Here are some links I find useful.

- [Narrator keyboard commands and touch gestures](https://support.microsoft.com/en-us/windows/appendix-b-narrator-keyboard-commands-and-touch-gestures-8bdab3f4-b3e9-4554-7f28-8b15bd37410a) -
  The page has well structured, semantic HTML.
  You can navigate by headings or tables and quickly find commands grouped by functionality.
  It has both standard and legacy keyboard commands.
  I highly recommend going with the standard layout especially if you're getting started.
  If you have experience with other screen readers, the standard commands will be very familiar. 
- [Windows Keyboard Shortcuts](https://support.microsoft.com/en-us/windows/keyboard-shortcuts-in-windows-dcc61a57-8ff0-cffe-9796-cb9706c75eec) -
  This has everything you can imagine.
  The HTML tables are hidden in collapsed regions.
  You can navigate by heading or button to find a topic, then press the button and a table will be revealed.
- [Windows Keyboard Shortcuts for Accessibility](https://support.microsoft.com/en-us/windows/windows-keyboard-shortcuts-for-accessibility-021bcb62-45c8-e4ef-1e4f-41b8c1fc87fd) -
  Good semantic HTML with headings and tables (not in collapsed regions).
  Good sections on Windows Magnifier, followed by a more generic accessibility section.
- [Keyboard Shortcuts for Office 365](https://support.microsoft.com/en-us/office/keyboard-shortcuts-in-microsoft-365-e765366f-24fc-4054-870d-39b214f223fd) -
  Don't look for the shortcuts on this page, it has links to various products (e.g., Outlook, Word, Teams).

## And Now, Using Narrator

We know how to start and stop Narrator, where to configure it, some useful keyboard shortcuts, and where to find more information.
Let's learn how to use it. 