import re

def arithmetic_arranger(problems, show=False):
    firstLine = ""
    secondLine = ""
    thirdLine = ""
    fourthLine = ""
    if len(problems) > 5 :
        return 'Error: Too many problems.'
    for problem in problems :
        operand = problem.split()
        if operand[1] != '+' and operand[1] != '-' :
            return "Error: Operator must be '+' or '-'."
        if operand[0].isdigit() == False or operand[2].isdigit() == False :
            return "Error: Numbers must only contain digits."
        if len(operand[0]) > 4 or len(operand[2]) > 4 :
            return "Error: Numbers cannot be more than four digits."
        if len(operand[0]) > len(operand[2]) :
            greater = len(operand[0])
        else :
            greater = len(operand[2])
        if problem == problems[-1] :
            firstLine += " " * (greater - len(operand[0]) + 2) + operand[0] 
            secondLine += operand[1] + " " * (greater - len(operand[2]) + 1) + operand[2] 
            thirdLine += "-"*(greater + 2) 
            if operand[1] == '+' :
                result = int(operand[0]) + int(operand[2])
            else :
                result = int(operand[0]) - int(operand[2])
            fourthLine += " "*(greater + 2 - len(str(result))) + str(result) 
        else :
            firstLine += " " * (greater - len(operand[0]) + 2) + operand[0] + " "*4
            secondLine += operand[1] + " " * (greater - len(operand[2]) + 1) + operand[2] + " "*4
            thirdLine += "-"*(greater + 2) + " "*4
            if operand[1] == '+' :
                result = int(operand[0]) + int(operand[2])
            else :
                result = int(operand[0]) - int(operand[2])
            fourthLine += " "*(greater + 2 - len(str(result))) + str(result) + " "*4
    if show :
        return firstLine + "\n" + secondLine + "\n" + thirdLine + "\n" + fourthLine 
    else :
        return firstLine + "\n" + secondLine + "\n" + thirdLine