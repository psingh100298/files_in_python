file = open('csv_data.txt','r')
lines = file.readlines()
file.close()

lines = [line.strip() for line in lines[1:]]

for line in lines:
    person_data = line.split(',')
    name = person_data[0]
    age = person_data[1]
    university = person_data[2]
    degree = person_data[3]

    print(f'{name.title()} is {age}, studying {degree.capitalize()} at {university.title()}')

sample_csv_value = ','.join(['Rolf','25','Mit','Computer Science'])
print(sample_csv_value)


