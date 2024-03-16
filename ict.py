# -*- coding: utf-8 -*-
"""ict.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-PAKaVstIYQP_pANT0Rizdl94XKdgKH8
"""

class Calculator:
  def __init__(self, num1, num2):
    self.num1 = num1
    self.num2 = num2

  def add(self):
    return self.num1 + self.num2

  def subtract(self):
    return self.num1 - self.num2

  def multiply(self):
    return self.num1 * self.num2

  def divide(self):
    return self.num1 / self.num2

num1 = float(input("Enter the first number: "))

num2 = float(input("Enter the second number: "))

calc = Calculator(num1, num2)

operation = input("Enter the operation (1.add, 2.sub, 3.mul, 4.div): ")

if operation == "1":
  print(calc.add())
elif operation == "2":
  print(calc.subtract())
elif operation == "3":
  print(calc.multiply())
elif operation == "4":
  print(calc.divide())
else:
  print("Invalid operation")

class Calculator:
  def __init__(self, num1, num2):
    self.num1 = num1
    self.num2 = num2

  def add(self):
    return self.num1 + self.num2

  def subtract(self):
    return self.num1 - self.num2

  def multiply(self):
    return self.num1 * self.num2

  def divide(self):
    return self.num1 / self.num2

expression = input("Enter the expression : ")

operator = expression[1]
operands = expression.split(operator)

num1 = float(operands[0])
num2 = float(operands[1])

calc = Calculator(num1, num2)

if operator == "+":
  print(calc.add())
elif operator == "-":
  print(calc.subtract())
elif operator == "*":
  print(calc.multiply())
elif operator == "/":
  print(calc.divide())
else:
  print("Invalid operation")