#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
import curses

import time


def main():
    while True:
        time.sleep(0.1)


if __name__ == '__main__':
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        stdscr.keypad(False)
        curses.nocbreak()
        curses.echo()
        curses.endwin()