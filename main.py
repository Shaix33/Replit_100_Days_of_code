food = input("name a food type: ")
plant = input("name a type of plant: ")
cooking = input("name a method of cooking")
burned = input("name a word that describes burnt food: ")
item = input("name a household item: ")

print("""Menu
  {} {} with {} {} 
  on a bed of {}
""".format(cooking, food, burned, plant, item))