shopping_list = []
shopping_list.append("milk")
shopping_list.append("cheese")

shopping_list.remove("milk")

for item in shopping_list:
    print(item)

if "milk" in shopping_list:
    print("Delicious!")
if "eggs" not in shopping_list:
    print("well we can't have that!")
    shopping_list.append("eggs")

foods = {}
foods["banana"] = "A delici"
foods["banana"]
del foods["banana"]