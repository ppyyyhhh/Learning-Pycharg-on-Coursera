import json

data = '''
{
 "name" : "chuck",
  "phone" :{
    "type" : "intl",
    "number" : "+1 734 303 4456"
    },
  "email" :{
    "hide" : "yes"
  }
}'''
# data is a dict() here.
data2 = '''
[
    {"1":"1"
    },
    {"2":"2"
    },
    {"3":"3"
    },  
]'''
#data 2 is a list of dict here.




print(data)


info = json.loads(data)
print("name: ", info["name"])
print("email hide:", info["email"]["hide"])