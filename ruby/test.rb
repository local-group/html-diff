# coding: utf-8
$TESTING=true
require './htmldiff'

STDOUT.write HTMLDiff.diff(ARGV[1], ARGV[2])
