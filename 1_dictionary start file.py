import random

phonebook = {"Chris": "555−1111", "Katie": "555−2222", "Joanne": "555−3333"}

"""
print()
print("*****  start section 1 - print dictionary ********")
print()


print(phonebook)
print(type(phonebook))
print(len(phonebook))

mydictionary = dict(m=9, n=10)
print(mydictionary)


print()
print("*****  end section 1 ********")
print()





print()
print("*****  start section 2 - search dictionary ********")
print()

# print(phonebook["Chris"])
# print(phonebook["chris"])

name = "chris"
if name in phonebook:
    print(phonebook[name])
else:
    print(f"{name} is not in the phonebook")


print()
print("*****  end section 2 ********")
print()




print()
print("*****  start section 3 - edit/append dictionary ********")
print()

print(phonebook)
phonebook["Chris"] = "555-0123"
phonebook["Joe"] = "555-4444"

print(phonebook)


print()
print("*****  end section 3 ********")
print()




print()
print("*****  start section 4 - delete/remove from dictionary ********")
print()


del phonebook["Chris"]
print(phonebook)

print()
print("*****  end section 4 ********")
print()





print()
print("*****  start section 5 - iterate through keys, values, items ********")
print()


for i in phonebook:
    print(i)

for u in phonebook.values():
    print(u)

for key, value in phonebook.items():
    print(f"the key: {key} and the value: {value}")

for phone_tuple in phonebook.items():
    print(phone_tuple)

# if you give the print statement the key, you get the value:
for i in phonebook:
    print(phonebook[i])


print()
print("*****  end section 5 ********")
print()




print()
print("*****  start section 6 - using get and clear ********")
print()


phone = phonebook.get("chris", "555-1111")  # 555-1111 represents 'key not found' here
print(phone)

phonebook.clear()
print(phonebook)

print()
print("*****  end section 6 ********")
print()



print()
print("*****  start section 7 - using pop method ********")
print()


remove = phonebook.pop("Chris", "not found")
print(remove)
print(phonebook)


print()
print("*****  end section 7 ********")
print()




print()
print("*****  start section 8 - using popitem ********")
print()


a = phonebook.popitem() #pops out just the last item in the library
print(a)
print(phonebook)


print()
print("*****  end section 8 ********")
print()

"""

print()
print("*****  start section 9 - using random and converting to list ********")
print()


list_of_keys = list(phonebook)
print(list_of_keys)
random_key = random.choice(list_of_keys)
print(phonebook[random_key])

print(
    phonebook[random.choice(list(phonebook))]
)  # same as the top. use variables less to save memory


print()
print("*****  end section 9 ********")
print()
