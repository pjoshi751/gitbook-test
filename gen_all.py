#!/usr/bin/python3.6
import os

files = os.listdir('./docs') 
files = [f for f in files if f.endswith('.md')]
files.remove('summary.md')
files.sort(key = lambda x: x.lower())
out = open('all.txt', 'wt')
for f in files:  
    words = f.split('.') 
    prefix, suffix = words[0], words[1]
    prefix_space = prefix.replace('-', ' ')
    s = '[%s](%s.md)' % (prefix_space, prefix)
    out.write(s + '\n') 
 
out.close()





