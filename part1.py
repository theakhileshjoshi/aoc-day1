###declaring variables
data = None
entry1 = 0
entry2 = 0
num1 = None
num2 = None
lst = []
###taking inputs in the list
for i in range(200):
    data = input()
    lst.append(data)
###using the algorithm for processing the two numbers which gives 2020 on adding up
for i in range(200):
    for j in range(200):
           num1 = int(lst[i])
           num2 = int(lst[j])
           if num1 + num2 == 2020:
               entry1 = num1
               entry2 = num2
               break
               
###printing the multiplication of the two numbers
print(entry1*entry2)
