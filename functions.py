import random
import numpy as np
functions = {"first": "ax + b = c", "second": "ax + b = cx + d"}

def first(a, b, c):
  try: 
    a = float(a)
    b = float(b)
    c = float(c)
    atimesx = c - b
    answer = atimesx/a
    return answer
  except ValueError:
    return "You didn't enter numbers!"

def second(a, b, c, d):
  try: 
    a = float(a)
    b = float(b)
    c = float(c)
    d = float(d)
    atimesx = c + d - b
    aminusctimesx = atimesx - c
    answer = aminusctimesx / (a-c)
    return answer
  except ValueError:
    return "You didn't enter numbers!"

def questions(difficulty):
  difficulties = ['easy', 'medium', 'hard']
  if difficulty.lower() not in difficulties:
    return "This is not a difficulty!"
  "ax + b = c"
  if difficulty.lower() == "easy":
    answer = random.randint(1,10)
    a = random.randint(1,10)
    b = random.randint(1,20)
    c = (answer * a) + b
    equation = f"{str(a)}x + {str(b)} = {str(c)}"
    return equation, answer, ",".join([str(a), str(b), str(c)])
  if difficulty.lower() == "medium":
    answer = random.randint(1,20)
    a = random.randint(-10,10)
    b = random.randint(-10,50)
    c = (answer * a) + b
    equation = f"{str(a)}x + {str(b)} = {str(c)}"
    return equation, answer, ",".join([str(a), str(b), str(c)])
  if difficulty.lower() == "hard":
    answer = random.randint(-15,15)
    a = random.randint(-20,20)
    b = random.randint(-50,50)
    c = (answer * a) + b
    equation = f"{str(a)}x + {str(b)} = {str(c)}"
    return equation, answer, ",".join([str(a), str(b), str(c)])

def threevariablesequation(equation1, equation2, equation3, rightside):
  A = np.array([equation1, equation2, equation3])
  b = np.array(rightside)
  allvar = np.linalg.solve(A, b)
  x = allvar[0]
  y = allvar[1]
  z = allvar[2]
  return f"x = {x}, y = {y}, z = {z}"

def twovariablesequation(equation1, equation2, rightside):
  A = np.array([equation1, equation2])
  b = np.array(rightside)
  allvar = np.linalg.solve(A, b)
  x = allvar[0]
  y = allvar[1]
  return f"x = {x}, y = {y}"

def fourvariablesequation(equation1, equation2, equation3, equation4, rightside):
  A = np.array([equation1, equation2, equation3, equation4])
  b = np.array(rightside)
  allvar = np.linalg.solve(A, b)
  x = allvar[0]
  y = allvar[1]
  z = allvar[2]
  w = allvar[3]
  return f"x = {x}, y = {y}, z = {z}, w = {w}"

def slope_intercept(x1,y1,x2,y2):
  a = (y2 - y1) / (x2 - x1)
  b = y1 - a * x1     
  return a,b
