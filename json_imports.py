import json

file = open('friends_json.txt','r')
file_content = json.loads(file)  #reads file and turns it to dictionary

file.close()

