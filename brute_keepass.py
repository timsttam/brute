#!/usr/bin/python

import sys
import itertools
import libkeepass

words=[]
INFILE= sys.argv[1]
FOUND=0

def unlock(INFILE, secret):
   with libkeepass.open(INFILE, password=secret, unprotect=False) as kdb:
      print (kdb.pretty_print())
      kdb.unprotect()
      print (kdb.pretty_print())


print ("Enter each word to use in the brute-force, enter ctrl+d when done")
for line in sys.stdin:
   words.append(line.rstrip())

print("Trying brute force %s with the following words: %s" % (INFILE,words))

while FOUND==0:
   for i in range(3,6):
      for attempt in itertools.permutations(words,i):
         print("Trying password %s" % ''.join(attempt))
         try:
            unlock(INFILE, ''.join(attempt))
            FOUND=1
            break
         except KeyboardInterrupt:
            raise
         except: 
            continue
   FOUND=1

