fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# new_list = [i for i in fruits]
# print(new_list)

# new_list = [i for i in fruits if 'a' in i]
# print(new_list)

new_list = [i if i != 'kiwi' else 'something' for i in fruits]
print(new_list)
