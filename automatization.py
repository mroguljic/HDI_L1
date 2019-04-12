import pexpect
import time
import os	
import csv
import sys

tests=[]
tests.append(raw_input("Enter HDI ID: "))
child = pexpect.spawn('/bin/bash -c "./bin/psi46test test"')
time.sleep(1)
print("Running startmod")
child.send('startmod\n')
time.sleep(3)
os.system("../HDItest-master/LabJack-Code/examples/InitializeDigitalIO")
flag = raw_input("Data signal output ok? [Y/n] ")
if(flag=='n'):
	tests.append('Fail')
else:
	tests.append('Pass')
os.system("../HDItest-master/LabJack-Code/examples/Clock0")
flag = raw_input("Clock 0 ok? [Y/n] ")
if(flag=='n'):
	tests.append('Fail')
else:
	tests.append('Pass')
os.system("../HDItest-master/LabJack-Code/examples/Clock1")
flag = raw_input("Clock 1 ok? [Y/n] ")
if(flag=='n'):
	tests.append('Fail')
else:
	tests.append('Pass')
os.system("../HDItest-master/LabJack-Code/examples/Clock2")
flag = raw_input("Clock 2 ok? [Y/n] ")
if(flag=='n'):
	tests.append('Fail')
else:
	tests.append('Pass')
os.system("../HDItest-master/LabJack-Code/examples/Clock3")
flag = raw_input("Clock 3 ok? [Y/n] ")
if(flag=='n'):
	tests.append('Fail')
else:
	tests.append('Pass')
os.system("../HDItest-master/LabJack-Code/examples/CTR0")
flag = raw_input("CTR 0 ok? [Y/n] ")
if(flag=='n'):
	tests.append('Fail')
else:
	tests.append('Pass')
os.system("../HDItest-master/LabJack-Code/examples/CTR1")
flag = raw_input("CTR 1 ok? [Y/n] ")
if(flag=='n'):
	tests.append('Fail')
else:
	tests.append('Pass')
os.system("../HDItest-master/LabJack-Code/examples/CTR2")
flag = raw_input("CTR 2 ok? [Y/n] ")
if(flag=='n'):
	tests.append('Fail')
else:
	tests.append('Pass')
os.system("../HDItest-master/LabJack-Code/examples/CTR3")
flag = raw_input("CTR 3 ok? [Y/n] ")
if(flag=='n'):
	tests.append('Fail')
else:
	tests.append('Pass')
raw_input("Plug D2 to Ch4, trigger on it and set Single Seq")
os.system("../HDItest-master/LabJack-Code/examples/SDA0")
child.send('tbmsel 31 2\n')
child.send('select 0\n')
child.send('dac 1 19\n')
flag = raw_input("SDA 0 ok? [Y/n] ")
if(flag=='n'):
	tests.append('Fail')
else:
	tests.append('Pass')
os.system("../HDItest-master/LabJack-Code/examples/SDA1")
child.send('tbmsel 30 1\n')
child.send('select 4\n')
child.send('dac 1 19\n')
flag = raw_input("SDA 1 ok? [Y/n] ")
if(flag=='n'):
	tests.append('Fail')
else:
	tests.append('Pass')
os.system("../HDItest-master/LabJack-Code/examples/SDA2")
child.send('tbmsel 30 2\n')
child.send('select 8\n')
child.send('dac 1 19\n')
flag = raw_input("SDA 2 ok? [Y/n] ")
if(flag=='n'):
	tests.append('Fail')
else:
	tests.append('Pass')
os.system("../HDItest-master/LabJack-Code/examples/SDA3")
child.send('tbmsel 31 1\n')
child.send('select 12\n')
child.send('dac 1 19\n')
flag = raw_input("SDA 4 ok? [Y/n] ")
if(flag=='n'):
	tests.append('Fail')
else:
	tests.append('Pass')
raw_input("Turning HV on")
child.send('hvon\n')
raw_input("Raise voltage to 1000V and press enter")
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
child.send('exit\n')
os.system("../HDItest-master/LabJack-Code/examples/InitializeDigitalIO")
tests.append(raw_input("Comment: "))
print(tests)
writeFlag = raw_input('Write the results into HDIresults.csv? [y/N]\n')

if(writeFlag=='y'):
	with open('HDIresults.csv','a') as f:
	  line = ",".join(tests)
	  f.write(line)
	  f.write("\n")