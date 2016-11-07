#!/usr/bin/env python2
import sys
import re
import os

def mysplit(sentence):
    limit = int(sys.argv[1])
    count = 0
    str = ''
    for word in re.split('\\s(?=\\w)', sentence):
        new_count = count + len(word) + 1
        if new_count > limit:
            yield str
            str = ''
            new_count = new_count - count

        str += word + ' '
        count = new_count

    if str:
        yield str

if len(sys.argv) != 2:
    print 'Usage: xxx.py length_of_a_sentence'
    sys.exit(1)

limit = sys.argv[1]
if limit <= 0:
    sys.exit(1)

while True:
    try:
        sys.stdout.write('>')
        paragraph = sys.stdin.read()
        paragraph = re.sub('(?<=\w)-\n', '', paragraph)
        paragraph = paragraph.replace('\n', ' ')
        os.system('clear')
        for sentence in [s+'.' for s in re.split('\\.\\s', paragraph)]:
            if re.match('\\s*\\.', sentence):
                continue

            print '--------------'
            os.system('clear')
            print ''

            for line in mysplit(sentence):
                print line

            raw_input()
    except EOFError as e:
        print '-- QUIT --'
    except BaseException as e :
        print ''
        break
