import sys

import pandas as pd 
import numpy as np

class Machine:
    def __init__(self, path):
        self._populate_Machine(path)
        self._populate_inputs()

    def _populate_Machine(self, path):  
        """Populating Machine"""
        #open file
        ifl = open(path, 'r')

        #grabing first 3 lines
        self.alphabet = ifl.readline().splitlines()
        self.alphabet = self.alphabet[0]

        self.numOfStates = ifl.readline().splitlines()
        self.numOfStates = int(self.numOfStates[0])

        self.aStates = ifl.readline().splitlines()
        self.aStates = int(self.aStates[0])

        #reading from the rest of the file
        self.table = []

        tempTable = ifl.readlines()
        temp = []
        for row in tempTable:
            row = row.strip("\n")
            row = row.replace("{","")            
            row = row.split("}")
            del row[-1]

            for col in row:
                col = col.split(",")
                print("col: ", col)
                temp.append(col)
            
            self.table.append(temp.copy())
            temp.clear()

        #close file
        ifl.close()

    def _populate_inputs(self):
        """populating inputs"""
        self.inputs = []

        infl = open(sys.argv[2], 'r')
        temp = infl.readlines()

        for row in temp:
            row = row.strip("\n")
            self.inputs.append(row)

        #close file
        infl.close()

    def run(self):
        """"""
        temp = []
        qlist = [0]
        
        print("qlist: ", qlist)
        for input in self.inputs:
            print("\ninput: ", input)

            for letter in input:
                print("letter: ", letter)

                for value in qlist.copy():
                    #index = qlist.index(value)
                    
                    if self.table[value][0][0] in qlist:
                        pass
                    else:
                        qlist.append(int(self.table[value][0][0]))
    
                for v in qlist.copy():
                    #i = qlist.index(v)
                    print("qlist: ", qlist)
                    print("v: ", v)
                    print("letter: ", letter)

                    for l in range(0, len(self.alphabet)):
                        print("some: ", self.alphabet[l], l+1)
                        if letter == self.alphabet[l]:
                            print("------------------------------------")
                            temp.append(self.table[qlist[v]][l+1][0])
                            print("temp: ", temp)
                    
                for w in temp:
                    print("w: ", w)
                    if self.table[w][0][0] in qlist:
                        pass
                    else:
                        temp.append(self.table[int(w)][0])
                    
                print("temp: ", temp)


if __name__ == '__main__':
    #GUARD
    if len(sys.argv) != 4:
        print("<file.txt> <input.txt> <out.txt>")
        quit()

    m1 = Machine(sys.argv[1])
    #print variables
    print("alphabet: ", m1.alphabet)
    print("numOfStates: ", m1.numOfStates)
    print("aStates: ", m1.aStates)
    print("table: ", m1.table)
    print("inputs", m1.inputs)

    #m1.run()