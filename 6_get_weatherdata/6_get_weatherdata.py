import json

with open('./6_sampleAPI.json') as data_file:
    data = json.load(data_file)
    toCelsius = data['main']['temp'] - 273
    print(toCelsius)


