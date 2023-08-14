from sys import argv

print('the number of cmd line arg:',len(argv))
print ('the list of arguments:',argv)
print('cmd line arguments one bye one...')
for x in argv:
   print(x)
   