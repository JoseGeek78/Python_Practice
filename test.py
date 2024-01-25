# Este bucle for itera en sentido decreciente
"""
for i in range(10,2,-1):
    print(i)
    

Este código está anulado y no se ejecuta
for i in range(10,0,-1)
  print(i)

"""
def get_full_name(first_name, last_name):
    full_name = first_name.title() + " " + last_name.title()
    return full_name


print(get_full_name("john", "doe"))