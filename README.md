This is a Python library and tool to check for misspelled
words in source code.  It does this by looking for words from
a list of common misspellings.  The dictionary it uses to do this
is based on the [Wikipedia list of common misspellings](http://en.wikipedia.org/wiki/Wikipedia:Lists_of_common_misspellings/For_machines)

The list has been slightly modified to remove some changes that cause
a number of false positives.  In particular `ok->OK` was removed (ok is
frequently used in perl tests for instance).

To try it out, merely run the following (using the coreutils
source tree as an example):

    git clone git://git.sv.gnu.org/coreutils ../coreutils
    find ../coreutils -name '*.c' | ./misspellings/misspellings.py -f -
    ../coreutils/src/cat.c[754]: efficency -> "efficiency"
    ../coreutils/src/comm.c[196]: funtion -> "function"
    ../coreutils/src/expr.c[21]: seperate -> "separate"
    ../coreutils/src/pr.c[1416]: accomodate -> "accommodate"
    ../coreutils/src/tac.c[342]: unneccessary -> "unnecessary"
    ../coreutils/src/test.c[97]: supressed -> "suppressed"

This file is in [Markdown syntax](http://daringfireball.net/projects/markdown/syntax)
