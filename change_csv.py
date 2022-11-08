import sys
import os

f = open("test.csv", "r")
all_text = f.read()
all_lines = all_text.split('\n')

mypath = './' # put path to images here

onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
onlyfilenames = [str(f).split('.')[0] for f in onlyfiles]

new_text = ''

for line in all_lines:
	if line.split(',')[0] in onlyfilenames:
		new_text += line + '\n'

f2 = open("reduced_test.csv", "w")
f2.write(new_text)
f.close()
f2.close()