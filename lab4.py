num_users = int(input("enter number of users: "))

users = {} 

for _ in range(num_users):
    username = input("enter username: ")
    num_items = int(input("how many items? "))

    items = []

    for i in range(num_items):
        item = input(f"item {i+1}: ")
        items.append(item)

    users[username] = items

print("\nUSER DATA:")
for user, items in users.items():
    print(f"{user} -> {items}")

item_count = {}
for items in users.values():
    for item in items:
        if item in item_count:
            item_count[item] += 1
        else:
            item_count[item] = 1

common_items = []
unique_items = []

for item, count in item_count.items():
    if count > 1:
        common_items.append(item)
    else:
        unique_items.append(item)

max_count = max(item_count.values())

most_popular = []
for item, count in item_count.items():
    if count == max_count:
        most_popular.append(item)

print("\nCOMMON ITEMS:")
for item in common_items:
    print(item)

print("\nUNIQUE ITEMS:")
for item in unique_items:
    print(item)

print("\nMOST POPULAR ITEM(S):")
for item in most_popular:
    print(item)
