#QUESTION 1
import random
x = random.randint(1,20) #random number picking
while True:
    num= int(input("Enter a number between 1-20 :"))
    if num>0 and num<21: #preventing wrong range 
        if num == x :
            print("Correct Answer")
            break
        elif num > x:
            print(num,"is greater than the correct answer.")
        elif num < x:
            print(num,"is smaller than the correct answer.")
    else:
        print("Invalid number")

#QUESTION 2
def find_target(given,target): #creating function
    for i in range(len(given)): #finding the position
        if given[i]>= target: #target gets place of the given one 
            return i
      
    return len(given) #end of the list 
given = [1, 3, 5, 6]
target = 3
print(find_target(given,target))
        
 
#OUESTION 3
a = int(input("Number 1 : " ))
b = int(input("Number 2 : "))
Output = a + b
print("Input:","a=","'",a,"'",",","b=","'",b,"'")
print("Output:",Output)

#QUESTION 4 
def single_one(numbers): #creating function
    for i in numbers:
        if numbers.count(i) == 1: #finding the single one by counting
            return i
numbers = [5, 1, 0, 1, 2,0,2] #example
print ("The single number is:", single_one(numbers))
    
#QUESTION 5 
def repeated_DNA(s):
    frequency = {}
    result  = []
    for i in range(len(s)-9): #length of the substrings
        substrings = s[i:i+10] #possible substrings
        frequency[substrings] = frequency.get(substrings,0)+1 #counting repeating ones 
        if frequency[substrings]>= 2 : 
            result.append(substrings) #adding repeated ones to the result 
            
    return result
s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
result = repeated_DNA(s)
print("Repeated sequences:", result) 
    
            