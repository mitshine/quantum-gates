import random

count = 0
arr1 = []
arr2 = []
while (count < 100):
  arr1 = []
  for i in range(0, 100):
      k = random.randint(0, 1) # decide on a k each time the loop runs
      #print(k)
      arr1.append(k)
      if(i == 99):
          if arr1 not in arr2:
             arr2.append(arr1)
             count = count + 1
          else:
             arr2 = arr2
      print("count: ", count, "\narray1 length: ", len(arr1))
      #if(len(arr2) == 50):
      #    name = input('What is your name?\n')
      f = open("output_anneal_2.txt", "w")
      f.write(str(arr2)+"\n")
      f.close()

arr2_1 = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1]

x = len(arr2_1)

print(x)

