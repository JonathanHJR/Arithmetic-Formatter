import re

def arithmetic_arranger(problems, calculate = False):
    first = ""
    second = ""
    lines = ""
    sums = ""
    arranged_problems = ""

    
    if (len(problems) > 5):
      return "Error: Too many problems."

    for problem in problems:

      firstNumber = problem.split(" ")[0]
      operator = problem.split(" ")[1]
      secondNumber = problem.split(" ")[2]

      if (len(firstNumber)) > 4 or (len(secondNumber)) > 4:
        return "Error: Numbers cannot be more than four digits."
      
      if (re.search("[^\s\d+-.]", problem)): # with [^], matches anything other than those mentioned in this range 
        if (re.search("[*]", problem)) or (re.search("[/]", problem)): # additionally inform that the input operators must also only be '+' or '-' if matched
          return "Error: Operator must be '+' or '-'."
        return "Error: Numbers must only contain digits."

      sum = ""

      if (operator == '+'):
        sum = str(int(firstNumber) + int(secondNumber))
      elif (operator == '-'):
        sum = str(int(firstNumber) - int(secondNumber))

      width = max(len(firstNumber), len(secondNumber)) + 2 # the max length out of the two numbers
      firstline = str(firstNumber).rjust(width) # designing output format
      secondline = operator + str(secondNumber).rjust(width - 1)
      dashline = "" 
      result = str(sum).rjust(width)

      for d in range(width):
        dashline += "-" # add number of dashes corresponding to range of width to empty string assigned to dashline

      if problem != problems[-1]:
        first += firstline + "    "
        second += secondline + "    "
        lines += dashline + "    "
        sums += result + "    "
      else:
        first += firstline
        second += secondline
        lines += dashline
        sums += result

    if calculate:
      arranged_problems = first + "\n" + second + "\n" + lines + "\n" + sums
    else:
      arranged_problems = first + "\n" + second + "\n" + lines
      
    return arranged_problems