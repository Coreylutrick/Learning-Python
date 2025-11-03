users = ["Corey", "Matt", "Logan"]

data = ["Corey", 31, True]

emptylist = []

print("Corey" in emptylist)

print(users[0])
print(users[-1])
print(users[-2])

print(users.index("Logan"))

print(users[0:2])
print(users[1:])
print(users[-3:3])

print(len(data))

users.append("Katherine")
print(users)

users += ["Lori", "George"]
print(users)

users.extend(["Silas"])
print(users)

# users.extend(data)
# print(users)

users.insert(0, "Rani")
print(users)

users[2:2] = ["Brian", "Melissa"]
print(users)

users[1:3] = ["Grammy", "Coco"]
print(users)

users.remove("Melissa")
print(users)

print(users.pop())
print(users)

del users[0]
print(users)

# del data
data.clear() 
print(data)

users[1:2] = ["corey"]
users.sort()
print(users)

users.sort(key=str.lower)
print(users)

nums = [2, 40, 6, 80, 10]
nums.reverse()
print(nums)

# nums.sort(reverse=True)
# print(nums)

print(sorted(nums, reverse=True))
print(nums)

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

print(type(nums))

mylist = list([1, "Bob", True])
print(mylist)

# Tuples

mytuple = tuple(("Corey", 31, True))

anothertuple = (1, 4, 2, 8, 2, 2)

print(type(mytuple))
print(type(anothertuple))

newlist = list(mytuple)
newlist.append("neil")
newtuple = tuple(newlist)
print(newtuple)

(one, *two, hey) = anothertuple
print(one)
print(two)
print(hey)

print(anothertuple.count(2))