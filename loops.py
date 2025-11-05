value = 1
# while value <= 10:
#     print(value)
#     if value == 5:
#         break
#     value += 1 

# while value <= 10:
#     value += 1
#     if value == 5:
#         continue
#     print(value)
# else:
#     print("Value is now equal to " + str(value))

# for x in names:
#     print(x)

# for x in "mississippi":
#     print(x)

# for x in names:
#     if x == "Logan":
#         break
#     print(x)

# for x in names:
#     if x == "Logan":
#         continue
#     print(x)

# for x in range(4):
#     print(x)

# for x in range(2, 4):
#     print(x)

for x in range(5,105,5):
    print(x)
else:
    print("glad that\'s over")

names = ["Corey", "Logan", "Silas"]

actions = ["Works", "Dads", "Codes"]

# for name in names:
#     for action in actions:
#         print(name + " " + action + ".")

for action in actions:
    for name in names:
        print(name + " " + action + ".")