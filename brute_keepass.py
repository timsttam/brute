#!/usr/bin/python

import sys
import itertools
import libkeepass

words=[]
INFILE= sys.argv[1]

def unlock(INFILE, secret):
   with libkeepass.open(INFILE, password=secret, unprotect=False) as kdb:
      print (kdb.pretty_print())
      kdb.unprotect()
      print (kdb.pretty_print())


print ("Enter each word to use in the brute-force, enter ctrl+d when done")
for line in sys.stdin:
   words.append(line.rstrip())

print("Trying brute force %s with the following words: %s" % (INFILE,words))
for attempt in itertools.permutations(words,5):
   print("Trying password %s" % ''.join(attempt))
   try:
      unlock(INFILE, ''.join(attempt))
      break
   except:
      continue

