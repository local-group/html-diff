#!/usr/bin/env python
#coding: utf-8

import os
import re
import textwrap
import argparse
import subprocess

import toml


def decode_utf8(s):
    return s.decode('utf-8')


def pwrapped(text):
    text = re.sub(r'[ \n\t\r]+', ' ', text)
    return textwrap.fill(text)


def test(exe_path, case):
    message = decode_utf8(case.get('message', 'should work'))
    old     = decode_utf8(case['old'])
    new     = decode_utf8(case['new'])
    diff    = decode_utf8(case['diff'])
    wrap    = case.get('wrap', True)

    print u'[old]: {!r}'.format(old)
    print u'[new]: {!r}'.format(new)
    output = subprocess.check_output([exe_path, old, new]).decode('utf-8')
    if wrap:
        output = pwrapped(output)
        diff = pwrapped(diff)
    print u'[ diff ]: {!r}'.format(diff)
    print u'[output]: {!r}'.format(output)
    assert output == diff, message


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', metavar='DIR', default='./config',
                        help='Test config directory')
    parser.add_argument('exes', metavar='EXE', nargs='+', help='Executable files')
    args = parser.parse_args()
    print 'Args:', args
    print '--------------------'
    for exe_path in args.exes:
        if not os.path.isfile(exe_path):
            parser.error('Not a file path: {}'.format(exe_path))
        if not os.access(exe_path, os.X_OK):
            parser.error('Not executeable file: {}'.format(exe_path))
    return args


def main():
    args = parse_args()
    for directory, _ , files in os.walk(args.config):
        for name in files:
            if not name.endswith('.toml'):
                continue

            path = os.path.join(directory, name)
            print '[Config path]: {}'.format(path)
            with open(path) as f:
                config = toml.load(f)
                for exe_path in args.exes:
                    print '[Executeable file]: {}'.format(exe_path)
                    for case in config['cases']:
                        test(exe_path, case)
                        print '---------------'

                print '--------------------'
    print '[DONE]'


if __name__ == "__main__":
    main()
