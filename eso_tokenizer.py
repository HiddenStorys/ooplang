from tokenize import*
from io import BytesIO

file_content = open("testingdoc.py", "rb")

def operator(op): 
    return {
        '+' : operator.add,
        '-' : operator.sub, 
        '*' : operator.mul,
        '/' : operator.div,
        '%' : operator.mod,
        '^' : operator.xor
    }[op]

def fileIn(s): 
    tokenized_file = tokenize(s.readline)

    return tokenized_file
    #for item in tokenized_file:
     #   print(item)
    
#fileIn(file_content)
def printTokenizedFile(s):
    for item in tokenized_file: 
        print(item)

tokenized_file = fileIn(file_content)
#printTokenizedFile(tokenized_file)

def checkLocation(token_file): 
    in_function = False
    dent_level = 0
    level_changed = False 

    for item in token_file: 

        if item.string == "def": 
            in_function = True 
            print("found function")

        elif item.type == 5 and in_function: 
            dent_level +=1
            level_changed = True
            print("climbed level")

        elif item.type == 6 and in_function:
            dent_level -= 1 
            level_changed = True
            print("fell level")
        
        if dent_level == 0 and in_function and level_changed: 
            in_function = False
            print("exited function")

        if not in_function: 
            print("nothing here")

def pullEquations(token_file): 
    in_line = False 
    withinEq = False
  #  parenthesis = False
    numberList = []

    for item in token_file:
        if item.type == 4 and not in_line:
            in_line = True
        elif item.type == 4 and in_line:
            if (numberList[len(numberList) - 1] != "BREAK"):
                numberList.append("BREAK")
            in_line = False
           # parenthesis = False
            withinEq = False

        if item.type == 53 and item.string == '=':
            withinEq = True     
        
        if item.type == 2 or (withinEq and item.type == 53 and (item.string == "+" or item.string == "-" or item.string == "/" or item.string == "*" or item.string == "(" or item.string == ")")):
            numberList.append(item.string)
          

    print(numberList) #this is not empty
    return numberList


def runEquation(equation_list):
    i = -1
    merge = False
    mergeNumberOne = 0
    mergeNumberTwo = None
    mergeList = []

    for item in equation_list: 
        i+=1

        if item == 'BREAK': 
            merge = True
            mergeNumberTwo = i
        
        if merge: 
            mergeList.append([''.join(equation_list[mergeNumberOne:mergeNumberTwo])]) 
            print("List")
            print(mergeList)
            mergeNumberOne = mergeNumberTwo + 1
            merge = False


numberList = pullEquations(tokenized_file)
print (numberList)
runEquation(numberList)

#figures out if it's in a function and the location within that function 