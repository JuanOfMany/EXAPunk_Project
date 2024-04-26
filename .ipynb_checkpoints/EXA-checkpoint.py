import sys

class Exa():
    def __init__(self, X=0, T=0, F=0):
      self.X = 0
      self.T = 0
      self.F = 0
      self.marks = {}
      self.file = []

    # added file lines to list separated by \n and stripped
        # need to use list to properly implement jumping
            # specifically looped jumping
    def read(self, file):
        with open(file) as opened_file:
            for line in opened_file:
                self.file.append(line.strip())
            total_line_count = len(self.file)
            opened_file.seek(0)
            for line_num, line in enumerate(opened_file):
                operate_return = self.operate(line, line_num)
                
                if operate_return:
                    type_of_jump = operate_return[0]
                    mark_to_jump = operate_return[1]
                    # do some jumps
                    if type_of_jump == 'JUMP':
                        for num in range(self.marks[mark_to_jump], total_line_count):
                            self.operate(opened_file[num], num)

                    if type_of_jump == 'TJMP':
                        if (getattr(self, 'T')):
                            for num in range((self.marks[mark_to_jump]) + 1, total_line_count):
                                self.operate(self.file[num], num)

                    if type_of_jump == 'FJMP':
                        if not getattr(self, 'T', self.marks[mark_to_jump]):
                            print('fjmp', mark_to_jump)
                            for num in range(self.marks[mark_to_jump], total_line_count):
                                self.operate(self.file[line_num], num)

      
    def operate(self, line, line_num):
        print('line:', line.strip(), 'line_num:', line_num)
        split_line = line.split()
        operation = split_line[0]
        value = split_line[1]
        if len(split_line) > 3:
            value2 = split_line[2]
        destination = split_line[-1]
        if operation == 'COPY':
            self.copy(self.isNum(value), destination)

        if operation == 'ADDI':
             self.add(value, value2, destination)
          
        if operation == 'SUBI':
            self.sub(value, value2, destination)

        if operation == 'MULI':
            self.multi(value, value2, destination)

        if operation == 'DIVI':
            self.div(value, value2, destination)

        if operation == 'MODI':
            self.modi(value, value2, destination)

        if operation == 'TEST':
            value2 = split_line[3]
            operator = split_line[2]
            self.test(self.isNum(value), operator, self.isNum(value2))

        if operation == 'MARK':
            self.marks[value] = line_num

        if operation == 'JUMP':
            for num in range((self.marks[value]) + 1, len(self.file)):
                self.operate(self.file[num], num)

        if operation == 'TJMP':
            if (getattr(self, 'T') != 0):
                for num in range((self.marks[value]) + 1, len(self.file)):
                    self.operate(self.file[num], num)

        if operation == 'FJMP':
            if (getattr(self, 'T')) == 0:
                for num in range((self.marks[value]) + 1, len(self.file)):
                    self.operate(self.file[num], num)

        print(f'X: {self.X}. T: {self.T}')

    def isNum(self, value):
        if not value.isdigit():
            value_result = getattr(self, value)
            return int(value_result)
        return int(value)

    def copy(self, value, destination):
        setattr(self, destination, value)
    
    def add(self, value, value2, destination):
        result = self.isNum(value) + self.isNum(value2)
        setattr(self, destination, result)

    def sub(self, value, value2, destination):
        result = self.isNum(value) - self.isNum(value2)
        setattr(self, destination, result)

    def multi(self, value, value2, destination):
        result = self.isNum(value) * self.isNum(value2)
        setattr(self, destination, result)

    def div(self, value, value2, destination):
        result = self.isNum(value) // self.isNum(value2)
        setattr(self, destination, result)

    def modi(self, value, value2, destination):
        result = self.isNum(value) % self.isNum(value2)
        setattr(self, destination, result)
        
    def test(self, value1, operator, value2):
        match operator:
            case "=":
                if value1 == value2:
                    setattr(self, 'T', 1)
                else:
                    setattr(self, 'T', 0)
                    
            case ">":
                if value1 > value2:
                    setattr(self, 'T', 1)
                else:
                    setattr(self, 'T', 0)
                    
            case "<":
                if value1 < value2:
                    setattr(self, 'T', 1)
                else:
                    setattr(self, 'T', 0)
                    
        

testExa = Exa()
testExa.read(sys.argv[1])
