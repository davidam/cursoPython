import json

student = {"101":{"class":'V', "Name":'Rohit',  "Roll_no":7},
                    "102":{"class":'V', "Name":'David',  "Roll_no":8},
                    "103":{"class":'V', "Name":'Samiya', "Roll_no":12}}
        
print(json.dumps(student))
print(json.dumps(student, sort_keys=True))
print(json.dumps(student, indent=4))
