MicroPython micro:bit REPL
==========================

This script lets you run commands directly onto a connected micro:bit device.
Put simply, you get to program the micro:bit in real time, just like we used
to with the old BBC micro from the 1980's. This encourages exploration,
experimentation and a sense of adventure. It's also a good way to play with
the device to learn about its capabilities.

The script detects the port to which the micro:bit is connected and uses
PySerial to make a connection to the micro:bit's Read Evaluate Print Loop
(REPL).

For more information about what a REPL, is check out this Wikipedia article:

https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop

Getting Started
---------------

When you run the script it will try to be as helpful as possible in working out
why it can't connect. In most cases it will try to print some helpful advice.

Once connected the script will stop the program running on the micro:bit in
order to drop you into the REPL itself. You type Python commands next to the
prompt ('>>>').

You can use the TAB key to auto-complete words. For example, if you
type `microbit.sc` then hit TAB, MicroPython will helpfully complete the
word for you, like this: `microbit.screen`.

You can move forwards and backwards through your command history by using the
up arrow key (to move back through your command history) and down arrow key
(to move forwards through your command history). The left and right arrow
keys allow you to move through the text of your command without deleting it.

Use the TAB and arrow key commands! They save a lot of typing and look really
cool.

Unplugging the device and pressing the reset button will re-start the program
as the version you originally flashed onto the device.

Useful Commands
---------------

A good place to start is to type `help()`. From here you should be able
to explore the device and the MicroPython version of Python 3.

All the micro:bit's hardware is available to program via the `microbit`
module. To start using it type the command `import microbit`. Do fun things
such as `microbit.display.scroll('Hello, World!')` and watch the device react
in real-time.

Type the command `dir()` to see a list of all the things currently
available to you - this includes the various classes and functions for the
program you may have already flashed onto the micro:bit.

Find Out More
-------------

To learn more about the amazing MicroPython visit: http://micropython.org/

The BBC micro:bit's (non-Pythonic) home is: http://microbit.co.uk/

To learn about the Python language visit: http://python.org/
