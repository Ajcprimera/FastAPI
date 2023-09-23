import json

#leemos el archivo json
file = open("data.json")
data = json.load(file)

file.close()