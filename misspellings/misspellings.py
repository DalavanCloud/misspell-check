#!/usr/bin/python

import sys
import getopt
import misspellings_lib as misspellings

def usage(msg=None):
  print 'USAGE: misspellings [-f file] [files]'
  print 'Checks files for common spelling mistakes.'
  print '  -f file: File containing list of files to check.'
  print '  -m file: File containing list of misspelled words & corrections.'
  print '  -d     : Dump the list of misspelled words.'
  print '  -s     : Create a shell script to interactively correct the file.'
  print '  files: Zero or more files to check.'
  if msg is not None:
    print 'ERROR: %s' % msg
    sys.exit(1)
  sys.exit(0)


if __name__ == '__main__':
  try:
    flags, files = getopt.getopt(sys.argv[1:], 'f:m:dsvh')
  except getopt.GetoptError, e:
    usage(e)
  dump_ms = False
  ms_file = None
  script_output = False
  for flag, option in flags:
    if flag == '-d':
      dump_ms = True
    elif flag == '-f':
      if option == '-':
        f = sys.stdin
      else:
        try:
          f = open(option, 'r')
        except IOError, e:
          usage(e)
      for line in f:
        files.append(line.strip())
    elif flag == '-h':
      usage()
    elif flag == '-m':
      ms_file = option
    elif flag == '-s':
      pass
    elif flag == '-v':
      print 'Version 1.0'
      sys.exit(0)
    else:
      usage('Unknown option "%s"' % flag)
  ms = misspellings.Misspellings(files=files, misspelling_file=ms_file)
  errors, results = ms.check()
  if not script_output:
    for res in results:
      print '%s[%d]: %s -> %s' % (res[0], res[1], res[2], ','.join(
        ['"%s"' % w for w in ms.suggestions(res[2])]))
    for err in errors:
      print 'ERROR: %s' % err
  else:
    print 'Not implemented yet.'
