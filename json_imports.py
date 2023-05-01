import json

file = open('friends_json.txt','r')
file_contents = json.load(file)   #reads file and turns it to dictionary

file.close()

print(file_contents['friends'][0])

cars = [
    {'make':'ford', 'model':'fiesta'},
    {'make':'ford', 'model':'focus'}

]

file = open('cars_json.txt','w')
json.dump(cars,file)
file.close()

my_json_string = '[{"name":"Alfa Romeo", "released":1950}]'
incorrect_car = json.loads(my_json_string)
print(incorrect_car[0]['name'])

