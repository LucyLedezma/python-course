### Mi primer scipt de python
## calcular el promedio de edades
alumns = [{'name': 'Maria', 'surname': 'Acosta', 'age': 21}, 
          {'name': 'Martin', 'surname': 'Cáceres', 'age': 23},
          {'name': 'Antonio', 'surname': 'Lopez', 'age': 19},
          {'name': 'Laura', 'surname': 'Benitez', 'age': 21}
         ]
total_age = 0
for i, alumn in enumerate(alumns):
    print(f"Alumn: {alumn['name']} {alumn['surname']}"
          f"age: {alumn['age']}")
    total_age += alumn['age']

mean_age = total_age // len(alumns)

print(f'Mean age: {mean_age}')
