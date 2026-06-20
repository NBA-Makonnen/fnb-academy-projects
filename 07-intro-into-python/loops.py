# for Loops

fruits = ["Apple", "Banana", "Cherry"]

for fruit in fruits:
    print(fruit)

numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number)

# Using a while Loop to count from 1 to 5

count = 1

while count <= 5:
    print(count)
    count += 1 # increments the count by 1

# for Loop Control Statements

fruits = ["Apple", "Banana", "Cherry", "Dates"]


for fruit in fruits:
    if fruit == "Cherry":
        break #exits the loop if cherry is found
    print(fruit)

print()

for fruit in fruits:
    if fruit == "Cherry":
        continue #skips cherry and moves to the iteration
    print(fruit)

print()

for fruit in fruits:
    if fruit == "Cherry":
        pass #placeholder, no action needed for cherry
    print(fruit)

# while Loop Control Statements

count = 0 

while count < 5:
    print(count)
    count += 1
    if count == 3:
        break #exits the loop when the count is reached