fruits = ['apple','banana','cherry','date','elderberry']
# "{}{}".format('First fruit:', fruits[0])
# "{}{}".format('Last fruit:', fruits[-1])

print('First fruit: '+ fruits[0])
print('Last fruit: '+ fruits[-1])
print("{}{}".format('Fruits from index 1 to 2: ', fruits[1:3]))


person = ("Rahul", 25, 5.9)
print("{}{}".format("Age: ", person[1]))

car = {"make":"Toyota", "model":"Camry", "year":2020,"color":"Blue"}
print("Car model: "+ car["model"])
car["owner"] = "Rahul"
# print("{}{}".format("Updated car dictionary: ", car))
print('Updated car dictionary:', car)