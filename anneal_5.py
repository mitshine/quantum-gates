import random
import math
import numpy as np
import time

start = time.time()

T = 400
Tmin = 0.1
alpha = 0.9
numIterations = 1000

def genRandSol():
  a = []
  # Instantiating for the sake of compilation
  for i in range(0, numIterations):
    a.append(random.randint(0,1))
  return a

min_value = []
for i in range(0, numIterations):
  min_value.append(0)

current_solution = genRandSol()
old_value = 0
new_value = 0
new_solution = []
old_solution = min_value

while T > Tmin:
  print("Temperature: ", T)
  for i in range(numIterations):
    # Reassigns global minimum accordingly
    current_solution = genRandSol()
    print("Current Solution: ", current_solution)
    if min_value == current_solution:
      print("Minimum Value and Current Solution are same!")
    else:
      if current_solution not in new_solution:
        print("Current Solution is New Solution!")
        for j in range(numIterations):
          old_value = old_value + old_solution[j]
        for k in range(numIterations):
          new_value = new_value + current_solution[k]
        print("Old Value: ", old_value, ", New Value: ", new_value)
        ap = math.exp((old_value - new_value)/T)
        print("ap: ", ap)
        if ap > random.uniform(0,1):
          print("ap < random_number!")
          new_solution.append(current_solution)
        else:
          current_solution = current_solution
      else:
        print("Already Exists!")
    #else:
    #  print("New Solution is ZERO array!")
    old_solution = current_solution

  T = T * alpha #Decreases T, cooling phase

end = time.time()
elapsed_time = end - start
print("All values list: ", new_solution)
print("Simulation time: ", round(elapsed_time, 3), " seconds")