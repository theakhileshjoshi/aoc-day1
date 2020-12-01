###Declaring Variables
data = None
entry1 = 0
entry2 = 0
entry3 = 0
num1 = None
num2 = None
num3 = None
lst = []
###taking input
for i in range(200):
    data = input()
    lst.append(data)
###processing
for i in range(200):
    for j in range(200):
       for k in range(200):
           num1 = int(lst[i])
           num2 = int(lst[j])
           num3 = int(lst[k])
           if num1 + num2 + num3 == 2020:
               entry1 = num1
               entry2 = num2
               entry3 = num3
               break
               
###printing the multiplication
print(entry1*entry2*entry3)
