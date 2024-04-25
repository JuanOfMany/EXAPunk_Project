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
            value2 = split_line[3]
        destination = split_line[-1]
        if operation == 'COPY':
            self.copy(value, destination)

         if operation = 'ADDI':
             self.add(value, value2, destination)
          
    #     if operation = 'SUBI':

    #     if operation = 'MULTI':

    #     if operation = 'DIVI':

    #     if operation = 'MODI':

    def copy(self, value, destination):
        setattr(self, destination, value)
        # print('X, F, T:', self.X, self.F, self.T)

    def isNum(value)
        if value not isdigit():
            value_result = getattr(self, 'value')
            return value_result
        return value
    
    def add(self, value, value2, destination):
        sum = isNum(value) + isNum(value2)
        setattr(self, sum, destination)
        
         
        print('X, F, T:', self.X, self.F, self.T)

testExa = Exa()
testExa.read(sys.argv[1])
