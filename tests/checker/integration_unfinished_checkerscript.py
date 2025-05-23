#!/usr/bin/env python3

import os
import time

from ctf_gameserver import checkerlib


if __name__ == '__main__':

    pidfile_path = os.environ['CHECKERSCRIPT_PIDFILE']    # pylint: disable=invalid-name
    with open(pidfile_path, 'w', encoding='ascii') as pidfile:
        pidfile.write(str(os.getpid()))

    checkerlib.get_flag(1)

    while True:
        time.sleep(10)
