#!/usr/bin/env python
"""
A simple shim around PySerial that detects the correct port to which the
micro:bit is connected and attempts to make a serial connection to it in order
to bring up the Python REPL.
"""
from __future__ import print_function
import re
import sys
import serial
import serial.tools.miniterm
from serial.tools.list_ports import comports
from serial.tools.miniterm import Console, Miniterm, key_description


MICROBIT_PID = 516     # 0x0204
MICROBIT_VID = 3368    # 0x0D28
BAUDRATE = 115200
PARITY = 'N'
ARM = 'https://developer.mbed.org/handbook/Windows-serial-configuration'
EXIT_CHAR = chr(0x1D)    # GS/CTRL+]

# Regular expression to match the device id of the micro:bit
RE_VID_PID = re.compile("VID:PID=([0-9A-F]+):([0-9A-F]+)", re.I)


def find_microbit():
    """
    Returns the port for the first micro:bit found connected to the computer
    running this script. If no micro:bit is found, returns None.
    """
    for port, desc, opts in comports():
        match = RE_VID_PID.search(opts)
        if match:
            vid, pid = match.groups()
            vid, pid = int(vid, 16), int(pid, 16)
            if vid == MICROBIT_VID and pid == MICROBIT_PID:
                return port
    if sys.platform.startswith('win'):
        # No COM port found, so give an informative prompt.
        sys.stderr.write('Have you installed the micro:bit driver?\n')
        sys.stderr.write('For more details see: {}\n'.format(ARM))
    return None


def connect_miniterm(port):
    try:
        ser = serial.Serial(port, BAUDRATE, parity=PARITY, rtscts=False, xonxoff=False)
        return Miniterm(
            ser,
            echo=False,
            #convert_outgoing=2,
            #repr_mode=0,
        )
    except serial.SerialException as e:
        if e.errno == 16:
            # Device is busy. Explain what to do.
            sys.stderr.write(
                "Found micro:bit, but the device is busy. "
                "Wait up to 20 seconds, or "
                "press the reset button on the "
                "back of the device next to the yellow light; "
                "then try again.\n"
            )
        elif e.errno == 13:
            print("Found micro:bit, but could not connect.".format(port), file=sys.stderr)
            print(e, file=sys.stderr)
            print('On linux, try adding yourself to the "dialout" group', file=sys.stderr)
            print('sudo usermod -a -G dialout <your-username>', file=sys.stderr)

        else:
            # Try to be as helpful as possible.
            sys.stderr.write("Found micro:bit, but could not connect via" +
                             " port %r: %s\n" % (port, e))
            sys.stderr.write("I'm not sure what to suggest. :-(\n")
        sys.exit(1)


def main():
    """
    The function that actually runs the REPL.
    """
    port = find_microbit()
    print('port', port)
    if not port:
        sys.stderr.write('Could not find micro:bit. Is it plugged in?\n')
        sys.exit(1)
    miniterm = connect_miniterm(port)
    # Emit some helpful information about the program and MicroPython.
    shortcut_message = 'Quit: {} | Stop program: Ctrl+C | Reset: Ctrl+D\n'
    help_message = 'Type \'help()\' (without the quotes) then press ENTER.\n'
    sys.stderr.write(shortcut_message.format(key_description(EXIT_CHAR)))
    sys.stderr.write(help_message)
    # Start everything.
    miniterm.exit_character = EXIT_CHAR
    miniterm.set_rx_encoding('utf-8')
    miniterm.set_tx_encoding('utf-8')
    miniterm.start()
    miniterm.serial.write(b'\x03')  # Connecting stops the running program.
    try:
        miniterm.join(True)
    except KeyboardInterrupt:
        pass
    sys.stderr.write('\nEXIT - see you soon... :-)\n')


if __name__ == '__main__':
    main()
