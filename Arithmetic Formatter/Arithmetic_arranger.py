# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 23:20:38 2021

@author: Marcial
"""
import re

def arithmetic_arranger(problems, solve=False):
  # First of all, we have to check if there are more than 4 problems in the array
    if (len(problems) > 5):
        return "Error: Too many problems."
  #We define some empty arrays to split the main string (problems) and those arrays will have sense later  
    primero = ""
    segundo = ""
    lineas= ""
    sumx = ""
    string = ""
    for problem in problems:
      if (re.search("[^\s0-9.+-]", problem)):
        if (re.search("[/]", problem) or re.search("[*]", problem)):
          return "Error: Operator must be '+' or '-'."
        return "Error: Numbers must only contain digits."
        
      firstNumber = problem.split(" ")[0]
      operator = problem.split(" ")[1]
      secondNumber = problem.split(" ")[2]
        
      if (len(firstNumber) >= 5 or len(secondNumber) >= 5):
          return "Error: Numbers cannot be more than four digits."
        
      sum= ""
      if (operator == "+"):
          sum = str(int(firstNumber) + int(secondNumber))
      elif(operator == "-"):
          sum = str(int(firstNumber) - int(secondNumber))
        
      length=max(len(firstNumber), len(secondNumber)) + 2
      top = str(firstNumber).rjust(length)
      bottom = operator + str(secondNumber).rjust(length-1)
      line= ""
      res=str(sum).rjust(length)
        
      for s in range(length):
        line += "-"
        
      if problem != problems[-1]:
        primero += top + '    '
        segundo += bottom + '    '
        lineas += line + '    '
        sumx += res + '    '  
      else:
        primero += top
        segundo += bottom
        lineas += line
        sumx += res
            
    if solve:
      string = primero + "\n" + segundo + "\n" + lineas + "\n" + sumx
    else:
      string = primero + "\n" + segundo + "\n" + lineas
    return string