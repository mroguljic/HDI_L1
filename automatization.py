import pexpect
import time
import os	
import csv
import sys
from datetime import datetime



tests=[]
HDI_ID = raw_input("Enter HDI ID: ")
tests.append(HDI_ID)


with open('HDIresults.csv','r') as f:
	csvreader=csv.reader(f,delimiter=',')
	duplicateFlag = False
	for row in csvreader:
		if(row[0]==HDI_ID):
			duplicateFlag = True
			print("An entry for this HDI ID already exists!")
			print(row)	
	if(duplicateFlag):
		continueFlag = raw_input("Do you still want to continue? [y/N]")
		if(continueFlag.lower()!='y'):
			quit()


child = pexpect.spawn('/bin/bash -c "./bin/psi46test test"')
tests.append(datetime.now().strftime("%Y-%m-%d-%H:%M:%S"))
time.sleep(1)
print("Running startmod")
child.send('startmod\n')
time.sleep(3)
os.system("../HDItest-master/LabJack-Code/examples/InitializeDigitalIO")
flag = raw_input("Data signal output ok? (check that signal is visible on both A1- and A1+ with opposite polarities) [Y/n] ")
if(flag.lower()=='n'):
	tests.append('Fail')
else:
	tests.append('Pass')
os.system("../HDItest-master/LabJack-Code/examples/Clock0")
flag = raw_input("Clock 0 ok? [Y/n] ")
if(flag.lower()=='n'):
	tests.append('Fail')
else:
	tests.append('Pass')
os.system("../HDItest-master/LabJack-Code/examples/Clock1")
flag = raw_input("Clock 1 ok? [Y/n] ")
if(flag.lower()=='n'):
	tests.append('Fail')
else:
	tests.append('Pass')
os.system("../HDItest-master/LabJack-Code/examples/Clock2")
flag = raw_input("Clock 2 ok? [Y/n] ")
if(flag.lower()=='n'):
	tests.append('Fail')
else:
	tests.append('Pass')
os.system("../HDItest-master/LabJack-Code/examples/Clock3")
flag = raw_input("Clock 3 ok? [Y/n] ")
if(flag.lower()=='n'):
	tests.append('Fail')
else:
	tests.append('Pass')
os.system("../HDItest-master/LabJack-Code/examples/CTR0")
flag = raw_input("CTR 0 ok? [Y/n] ")
if(flag.lower()=='n'):
	tests.append('Fail')
else:
	tests.append('Pass')
os.system("../HDItest-master/LabJack-Code/examples/CTR1")
flag = raw_input("CTR 1 ok? [Y/n] ")
if(flag.lower()=='n'):
	tests.append('Fail')
else:
	tests.append('Pass')
os.system("../HDItest-master/LabJack-Code/examples/CTR2")
flag = raw_input("CTR 2 ok? [Y/n] ")
if(flag.lower()=='n'):
	tests.append('Fail')
else:
	tests.append('Pass')
os.system("../HDItest-master/LabJack-Code/examples/CTR3")
flag = raw_input("CTR 3 ok? [Y/n] ")
if(flag.lower()=='n'):
	tests.append('Fail')
else:
	tests.append('Pass')


raw_input("Plug D2 to Ch4, trigger on it and set Single Seq")
SDAflag = 'Y'
while(SDAflag.lower()!='n'):
	os.system("../HDItest-master/LabJack-Code/examples/SDA0")
	child.send('tbmsel 31 2\n')
	child.send('select 0\n')
	child.send('dac 1 19\n')
	SDAflag = raw_input("Repeat SDA 0? [Y/n]")
flag = raw_input("SDA 0 ok? [Y/n] ")
if(flag.lower()=='n'):
	tests.append('Fail')
else:
	tests.append('Pass')
SDAflag = 'Y'
while(SDAflag.lower()!='n'):
	os.system("../HDItest-master/LabJack-Code/examples/SDA1")
	child.send('tbmsel 30 1\n')
	child.send('select 4\n')
	child.send('dac 1 19\n')
	SDAflag = raw_input("Repeat SDA 1? [Y/n]")
flag = raw_input("SDA 1 ok? [Y/n] ")
if(flag.lower()=='n'):
	tests.append('Fail')
else:
	tests.append('Pass')
SDAflag = 'Y'
while(SDAflag.lower()!='n'):
	os.system("../HDItest-master/LabJack-Code/examples/SDA2")
	child.send('tbmsel 30 2\n')
	child.send('select 8\n')
	child.send('dac 1 19\n')
	SDAflag = raw_input("Repeat SDA 2? [Y/n]")
flag = raw_input("SDA 2 ok? [Y/n] ")
if(flag.lower()=='n'):
	tests.append('Fail')
else:
	tests.append('Pass')
SDAflag = 'Y'
while(SDAflag.lower()!='n'):
	os.system("../HDItest-master/LabJack-Code/examples/SDA3")
	child.send('tbmsel 31 1\n')
	child.send('select 12\n')
	child.send('dac 1 19\n')
	SDAflag = raw_input("Repeat SDA 3? [Y/n]")
flag = raw_input("SDA 3 ok? [Y/n] ")
if(flag.lower()=='n'):
	tests.append('Fail')
else:
	tests.append('Pass')


raw_input("Turning HV on")
child.send('hvon\n')
raw_input("Raise voltage to -800V and press enter\n")
tests.append(raw_input("Enter the voltage as measured on the HV pin: "))

raw_input("Put the Z-stage in the upper position and press enter\n")

raw_input("Raise voltage to -1100V and press enter")
for remaining in range(60, 0, -1):
    sys.stdout.write("\r")
    sys.stdout.write("{:2d} seconds remaining".format(remaining)) 
    sys.stdout.flush()
    time.sleep(1)
tests.append(raw_input("\rEnter current in nA: "))
raw_input("Turning HV off")
child.send('hvoff\n')
raw_input("Turn off voltage")
print('Exiting psi46test and disengaging relays')
child.send('poff\n')
child.send('exit\n')
os.system("../HDItest-master/LabJack-Code/examples/InitializeDigitalIO")

print(tests)
failFlag = False
for testRes in tests:
	if("fail" in testRes.lower()):
		failFlag = True

if(failFlag==True):
	print("The HDI will be graded as failed based on these results.")
	tests.append("Fail")
	tests.append(raw_input("Comment: "))
else:
	
	print("The HDI will be graded as passed based on these results.")
	changeToFail =	raw_input("Change it to 'Fail'[y/N]? (comment required in that case)")
	if(changeToFail.lower()=='y'):

		comment = ""
		while not comment.replace(" ",""):
			comment = raw_input("Comment: ")
		tests.append("Fail")
		tests.append(comment)
	else:
		tests.append("Pass")
		tests.append(raw_input("Comment: "))


print(tests)
writeFlag = raw_input('Write the results into HDIresults.csv? [y/N]\n')

if(writeFlag.lower()=='y'):
	with open('HDIresults.csv','a') as f:
	  line = ";".join(tests)
	  f.write(line)
	  f.write("\n")
