#lets learn about lists


supplies = ["tent", "sleeping bags", "water", "raspberry pi", "coffee", "knife", "ethernet cable", "flash drive", "beard oil", "marshmallows"]


camp_site = ["Crystal Lake", 404, 95.5, 10, False]


supplies.extend(["toilet paper", "bidet"])

supplies.pop(0)

print("This item was just deleted: " + supplies.pop(0))

supplies.pop(0)

print(supplies)


#supplies.clear() clears everything
#supplies.pop() remove 1 item from the list using index ex.5 
#supplies.remove() remove exact item