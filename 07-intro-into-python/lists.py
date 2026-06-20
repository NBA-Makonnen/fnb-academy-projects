#Lists

fruits = ["Apple", "Banana", "Cherry"]

print(fruits[0])

fruits[1] = "Blueberry"

print(fruits[1])

#Append, Insert, Remove & Sort

fruits = ["Apple", "Banana", "Cherry"]

fruits.append("Kiwi")
print(fruits)

fruits.insert(1, "Orange")
print(fruits)

fruits.remove("Kiwi")
print(fruits)

fruits.sort(reverse=True)
print(fruits)