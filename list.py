
index = 0

tasks = [1,2,3]
items = list(range(4))
my_stuff = [float(1),2.23,"3","cztery"]

print(tasks)
print(tasks[0])
print(items)
print(my_stuff)

people = ["Hanna","Louisa","Claudia", "Angela","Geoffrey", "aparna"]

people[0] = "Hannah"
people[4] = "Jeffrey"
people[5] = "Aparna"

while index < len(people):
    print(f"{index+1}. {people[index]}")
    index += 1

for item in people:
    print(item)

print(len(people))
