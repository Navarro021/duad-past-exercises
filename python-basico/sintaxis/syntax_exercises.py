age = 40
name = "jhonathan"
last_name = "navarro"
european = False
colombian = True
years_living_usa = 6
height = 1.78
weight = 180.54
favorite_movies = ["titanic", "home alone", "avatar"]
favorite_sports = ["tennis","mma","boxeo","rugby"]

string_string = name + last_name
string_int = age + years_living_usa
int_string = age + name
list_list = favorite_movies + favorite_sports
string_list = name + favorite_sports
float_int = height + age
bool_bool = european + colombian

# si quieres ver el resultado puedes descomentar los print y veras el resultado en la consola.

#print(string_string)
#print(string_int)
#print(int_string)
#print(list_list)
#print(string_list)
#print(float_int)
#print(bool_bool)

# string + string → jhonathannavarro
# string + int = 46
# int + string = unsupported operand type(s) for +: 'int' and 'str'
# list + list = ['titanic', 'home alone', 'avatar', 'tennis', 'mma', 'boxeo', 'rugby']
# string + list = TypeError: can only concatenate str (not "list") to str
# float + int = 41.78
# bool + bool = 1