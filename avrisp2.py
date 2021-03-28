#!/usr/bin/env /usr/bin/python3

import optparse as op
import os
import log

def get_cmdline_avrisp2():
    return "-c avrisp2"

def get_cmdline_target(target):
    if(target == "None"):
        log.errexit("Target not specified!")
    return " -m " + target

def get_cmdline_erase():
    return " -e"

def get_cmdline_program(ifile):
    if(os.path.isfile(ifile)):
        ext = os.path.splitext(ifile)[1].split('.')[1]
        print(ext)
        switcher = {
            'elf': 'e',
            'bin': 'b',
            'hex': 'i'
        }
        fmt = switcher.get(ext, "none")
        if(fmt == "none"):
            log.errexit("Invalid file format! Run 'man avrdude'!")
        ret = " -U flash:w:" + ifile + ":" + fmt
    else:
        log.errexit("Invalid path of input file!")
    return ret

def get_cmdline_verify(ifile):
    if(os.path.isfile(ifile)):
        ext = os.path.splitext(ifile)[1].split('.')[1]
        print(ext)
        switcher = {
            'elf': 'e',
            'bin': 'b',
            'hex': 'i'
        }
        fmt = switcher.get(ext, "none")
        if(fmt == "none"):
            log.errexit("Invalid file format! Run 'man avrdude'!")
        ret = " -U flash:v:" + ifile + ":" + fmt
    else:
        log.errexit("Invalid path of input file!")
    return ret

def avrisp2():
    switches = op.OptionParser()
    switches.add_option("-e", "--erase", dest="erase", default=False, action="store_true", help="Switch to erase target")
    switches.add_option("-i", "--in-file", dest="file", help="Path of the binary file to flash target")
    switches.add_option("-l", "--log", dest="log", default=0, help="Console logging level [1, 2], default 0")
    switches.add_option("-p", "--program", dest="program", default=False, action="store_true", help="Switch to program flash of target, provide input file using -i")
    switches.add_option("-t", "--target", dest="target", help="Target Code as per avrdude")
    switches.add_option("-v", "--verify", dest="verify", default=False, action="store_true", help="Switch to verify program on flash of target, provide input file using -i")

    (option, args) = switches.parse_args()
    ifile = str(option.file)
    target = str(option.target)

    if(option.erase and (option.program or option.verify)):
        log.errexit("Incorrect switches are provided. Please run with -h switch!")

    cmd = get_cmdline_avrisp2()
    cmd+= get_cmdline_target(target)
    if(option.erase):
        cmd += get_cmdline_erase()
    elif(option.program):
        cmd += get_cmdline_program(ifile)
    elif(option.verify):
        cmd += get_cmdline_verify(ifile)
    else:
        log.errexit("Something is worng! Try running again with -h switch")

    os.system("sudo avrdude " + cmd)

    return

if __name__ == "__main__":
    avrisp2()