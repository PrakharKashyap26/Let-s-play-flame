# Get input from the user

a = input("Enter the first name: ").lower()

b = input("Enter the second name: ").lower()

# Combine the names

s = a + b

# Remove common letters

s_list = list(s)

for i in set(s):

# Use set to avoid modifying the list while iterating

    if s.count(i) > 1:

        for _ in range(s.count(i)):

            s_list.remove(i)

# Calculate the number of unique letters remaining
 
f = len(s_list)

# FLAMES relationships

flame = ["Friend", "Love", "Affair", "Marriage", "Enemy", "Sibling"]
while len(flame)>1:
    index = (f - 1) % len(flame)
    flame.pop(index)
print("the relationship is : ", flame [0])