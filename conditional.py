print(bool(""))
print(bool("non empty string"))
print(bool(0))
print(bool(43))
print(bool([]))
print(bool(["this", "is", 5, (3, 5)]))
print(bool({}))
print(bool({"Name": "Shea", "hair": "brown", "eye color": "blue", "height": (5,11)}))

x = 100
if x < 10:
    print("That makes sense!")
elif x == 100:
    print("Ahh, x is 100.")
else:
    print("This shouldn't be reached!")