import sys

class Exa():
    def __init__(self, X=0, T=0, F=0):
      self.X = 0
      self.T = 0
      self.F = 0

    def read(self, file):
        with open(file) as opened_file:
            for line in opened_file:
               self.operate(line)
      
    def operate(self, line):
        split_line = line.split()
        operation = split_line[0]
        value = split_line[1]
        destination = split_line[2]
        if operation == 'COPY':
        #   self[destination] = value
            print('COPY')
    #     if operation = 'ADDI':
    #         val1 + val2 = exampleVal
          
    #     if operation = 'SUBI':

    #     if operation = 'MULTI':

    #     if operation = 'DIVI':

    #     if operation = 'MODI':

    def copy(self, value, destination):
       destination = value

testExa = Exa()
testExa.read(sys.argv[1])
