# Dictionaries
band = {
    "Vocals": "Plant",
    "Guitar": "Page"
}

band2 = dict(Vocals= "Plant", Guitar = "Page")
print(band)
print(band2)
print(type(band))
print(len(band))

# Access items in a dictionary

print(band["Vocals"])
print(band.get("Guitar"))

# List all Keys
print(band.keys())

# list all values
print(band.values())

# list of key values pairs as tuples
print(band.items())

# Verify a key exists
print("Guitar" in band)
print("Triangle" in band)

# Change values in a dictionary
band["Vocals"] = "Coverdale"
band.update({"Bass": "Corey"})

print(band)

# Removing items from a dictionary
print(band.pop("Bass"))
print(band)

band["Drums"] = "Logan"
print(band)

print(band.popitem()) # tuple
print(band)

# Delet and clear dictionary items

band["Drums"] = "Logan"
del band["Drums"]
print(band)

band2.clear()
print(band2)

del band2

# Copying dictionaires

# band2 = band # creates a reference, dont do this
# print("Bad copy")
# print(band)
# print(band2)

# band2["Drums"] = "Logan"
# print(band)

band2 = band.copy() # use this for a copy of a dictionary
band2["Drums"] = "Logan"
print("Good copy")
print(band)
print(band2)

# or use dictionary constructor function
band3 = dict(band)
print("Good copy")
print(band3)

# Nested Dictionaries

member1 = {
    "Name": "Plant",
    "Instrument": "VoCals"
}
member2 = {
    "Name": "Plant",
    "Instrument": "Guitar"
}
band = {
    "member1": member1,
    "member2": member2
}
print(band)
print(band["member1"]["Name"])

# sets

nums = {1, 2, 3, 4}

nums2 = set((1, 2, 3, 4))

print(nums)
print(nums2)
print(type(nums))
print(len(nums))

# no duplicates are allowed in a set
nums = {1, 2, 2, 3}
print(nums)

# True value is a dupe of 1, False is a dupe of 0

nums = {1, True, 2, 3, False, 0}
print(nums)

# YOu can check if a value is in a set 
print(2 in nums)

# but you cannot refer to an element in the set with an index position or key 

# add a new element to a set

nums.add(8)
print(nums)

# add elements from one set to another

morenums = {5, 6, 7, 9}
nums.update(morenums)
print(nums)

# you can use update with lists, tuples, and dictionaries as well

# merge to sets to create a third new one

one = {1, 2, 3}
two = {4, 5, 6}

mynewset = one.union(two)
print(mynewset)

# keep only the duplicates from the sets

one = {1, 2, 3}
two = {2, 3, 6}

one.intersection_update(two)
print(one)

# keep everything except the duplicates

one = {1, 2, 3}
two = {2, 3, 6}

one.symmetric_difference_update(two)
print(one)