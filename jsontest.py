import json

d = '''[{ "Glenn", "Sally", "Jen" }]'''

json.loads(d)
print(isinstance(d, list))
