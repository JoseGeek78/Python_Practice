# Este bucle for itera en sentido decreciente
"""
for i in range(10,2,-1):
    print(i)
    

Este código está anulado y no se ejecuta
for i in range(10,0,-1)
  print(i)

"""
def get_full_name(first_name: str, last_name: str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name


print(get_full_name("papa", "hop"))

def get_name_with_age(name: str, age: int):
    name_with_age = name.title() + " is this old: " + str(age)
    return name_with_age
  
print(get_name_with_age("jose", 45))