import sys

class Exa():
    def __init__(self, X=0, T=0, F=0):
      self.X = 0
      self.T = 0
      self.F = 0
      print('X, F, T:', self.X, self.F, self.T)

    def read(self, file):
        with open(file) as opened_file:
            for line in opened_file:
               self.operate(line)
      
    def operate(self, line):
        split_line = line.split()
        operation = split_line[0]
        value = split_line[1]
        if len(split_line) > 3:
            value2 = split_line[2]
        destination = split_line[-1]
        if operation == 'COPY':
            self.copy(value, destination)
            print(f'X: {self.X}, F:{self.F}, T:{self.T}')

        if operation == 'ADDI':
             # print('in add:', value, value2, destination)
             self.add(value, value2, destination)
          
        if operation == 'SUBI':
            self.sub(value, value2, destination)

        if operation == 'MULI':
            self.multi(value, value2, destination)

        if operation == 'DIVI':
            self.div(value, value2, destination)

        if operation == 'MODI':
            self.modi(value, value2, destination)

    def copy(self, value, destination):
        setattr(self, destination, value)
        # print('X, F, T:', self.X, self.F, self.T)

    def isNum(self, value):
        if not value.isdigit():
            value_result = getattr(self, value)
            return int(value_result)
        return int(value)
    
    def add(self, value, value2, destination):
        result = self.isNum(value) + self.isNum(value2)
        setattr(self, destination, result)
        print(f'X: {self.X}, F:{self.F}, T:{self.T}')

    def sub(self, value, value2, destination):
        result = self.isNum(value) - self.isNum(value2)
        setattr(self, destination, result)
        print(f'X: {self.X}, F:{self.F}, T:{self.T}')

    def multi(self, value, value2, destination):
        result = self.isNum(value) * self.isNum(value2)
        setattr(self, destination, result)
        print(f'X: {self.X}, F:{self.F}, T:{self.T}')

    def div(self, value, value2, destination):
        result = self.isNum(value) / self.isNum(value2)
        setattr(self, destination, result)
        print(f'X: {self.X}, F:{self.F}, T:{self.T}')

    def modi(self, value, value2, destination):
        result = self.isNum(value) % self.isNum(value2)
        setattr(self, destination, result)
        print(f'X: {self.X}, F:{self.F}, T:{self.T}')
    

testExa = Exa()
testExa.read(sys.argv[1])
