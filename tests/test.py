#!/usr/bin/env python
#coding: utf-8

import os
import argparse
import subprocess

import toml

def decode_utf8(s):
    return s.decode('utf-8')

def test(exe_path, case):
    message = decode_utf8(case['message'])
    a       = decode_utf8(case['a'])
    b       = decode_utf8(case['b'])
    should  = decode_utf8(case['should'])

    print u'this: {}'.format(a)
    print u'that: {}'.format(b)
    output = subprocess.check_output([exe_path, a, b]).decode('utf-8')
    print u'----: {}'.format(should)
    print u'====: {}'.format(output)
    assert output == should, message


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
            print 'Config path: {}'.format(path)
            with open(path) as f:
                config = toml.load(f)
                for exe_path in args.exes:
                    print 'Executeable file: {}'.format(exe_path)
                    for case in config['cases']:
                        test(exe_path, case)
            print '----------'


if __name__ == "__main__":
    main()
