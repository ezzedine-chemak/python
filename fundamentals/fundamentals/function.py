# 1 :
x = [ [5,2,3], [15,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Bryant'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Andres', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 30} ]

# 2: iterateDictionary
def iterateDictionary(some_list):
    for dictionary in some_list:
        for key, value in dictionary.items():
            print(f"{key} - {value}")

print (iterateDictionary(students))

# 3 : iterateDictionary2(key_name, some_list)

def iterateDictionary2(key_name, some_list) :
    for dictionary in some_list:
        if key_name in dictionary :
            print(dictionary[key_name])
        else :
            print(f"{key_name}not found")


print(iterateDictionary2('first_name',students))


# 4:printInfo(some_dict)
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
print(dojo.items())

def printInfo(some_dict) :
    for key, value_list in some_dict.items():
        print(f" {len(value_list)}  {key}")
        for value in value_list:
            print(f"{value}")

print(printInfo(dojo))