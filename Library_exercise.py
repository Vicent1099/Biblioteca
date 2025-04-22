class Libro:
    def __init__(self, titulo, autor, isbn, disponible=True): #propiedades de la clase
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible

    def agregar(self, lista): #se tiene que indicar el libro a la que se le va a agregar el libro
        lista.append(self)
        print(f"Libro '{self.titulo}' agregado") #solo indica si se ha agregado

    def prestar(self):
        if self.disponible: #si disponible = True
            self.disponible = False #lo cambia a False
            print(f"Libro '{self.titulo}' prestado")
        else:
            print(f"El libro '{self.titulo}' está prestado") # si ya era False se indica este mensaje

    def devolver(self):
        if self.disponible == False: #si no está disponible
            self.disponible = True#lo cambia a disponible
            print(f"Libro '{self.titulo}' devuelto")
        else:
            print(f"El libro '{self.titulo}' ya estaba disponible")#mensaje si ya estaba disponible 

    def mostrar(self):
        estado = "Sí" if self.disponible else "No" #se crea una variable "estado", si está disponible se guarda el str "Sí" o "No", en caso contrario
        print(f"Título: {self.titulo}, Autor: {self.autor}, ISBN: {self.isbn}, Disponible: {estado}")#se indica las características del libro y se usa la variable estado, en la línea anterior declarada

    @staticmethod#se crea una función dentro de una clase sin self ni todas las propiedades de la clase
    def buscar(lista, isbn): #definimos método con una lista y el código ISBN 
        for libro in lista: #itera la lista
            if libro.isbn == isbn:#compara el isbn de cada libro con el isbn que se pide en el método buscar
                estado = "Sí" if libro.disponible else "No" #idem línea 27, de la función mostrar
                print(f"Título: {libro.titulo}, Autor: {libro.autor}, ISBN: {libro.isbn}, Disponible: {estado}")
                return#sale del bucle si se encuentra y evita que se lea la siguientes líneas
        print(f"No se encontró el libro con el código {isbn}.")#si se encontrara el libro y no estuviera return, se activaría esta línea


biblioteca = [# para hacer pruebas sin necesidad de usar agregar()
    Libro("Cien años de soledad", "Gabriel García Márquez", "9788437604947", disponible=True),
    Libro("1984", "George Orwell", "9780451524935", disponible=False),
    Libro("El Principito", "Antoine de Saint-Exupéry", "9780156012195", disponible=True),
    Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "9788467033767", disponible=False),
    Libro("Crónica de una muerte anunciada", "Gabriel García Márquez", "9788437604948", disponible=True),
    Libro("El señor de los anillos", "J.R.R. Tolkien", "9788445000667", disponible=False)
]
print("\nBienvenido al Sistema de Gestión de Biblioteca")
def menu():#función de menú para que vuelva a aparecer el menú
    print("\nEscoja su opción: ")
    print("1. Agregar libro")
    print("2. Prestar libro")
    print("3. Devolver libro")
    print("4. Mostrar libros")
    print("5. Buscar libro")
    print("6. Salir del sistema")
    print("7. Desplegar el menú\n")
menu()
num=0 # permite entrar al bucle automáticamente
while num != 6:#si el usuario indica el valor 6, se sale del programa
    try:#se añade un bloque try-except si el usuario marca un float o str
        num = int(input("\nElige una opción: "))#se pide el valor del menú deseado al usuario
    except ValueError: #se añade un bloque try-except si el usuario marca un float o str
        print("\nHas indicado un valor no válido, las opciones son del 1 al 6.\n")
        menu()
    if num == 1: #opción de agregar
        titulo1 = input("Indique el título: ")#pide las propiedades del libro
        autor1 = input("Indique el autor: ")
        isbn1 = input("Indique el ISBN: ") #pide el ISBN en str
        libro1 =Libro(titulo1,autor1,isbn1,True)#se agrega el libro con las características pedidas
        libro1.agregar(biblioteca)#uso del método agregar en la biblioteca
        

    elif num == 2:#opción de prestar el libro
        isbn2 = input("Indique el ISBN: ")#pide el ISBN en str
        libro_encontrado = False#se crea una variable booleana False
        for libro in biblioteca:#busca cada libro en la lista
            if libro.isbn == isbn2:#si coincide el ISBN de algún libro de la biblioteca con el indicado por el usuario:
                libro_encontrado = True#como se ha encontrado para la variable a True
                libro.prestar()#uso del método prestar
                break#se sale del bucle
        if not libro_encontrado:#si la variable sigue siendo False
            print("No se encontró ningún libro con el ISBN\n", isbn2)

    elif num == 3:#opción de devolver el libro
        isbn3 =input("Indique el ISBN: ")#pide al usuario el ISBN
        libro_encontrado = False#idem opción de prestar libro
        for libro in biblioteca:
            if libro.isbn == isbn3:
                libro_encontrado = True
                libro.devolver()#uso del método devolver
        if not libro_encontrado:
            print("No se encontró ningún libro con el ISBN: ", isbn3)

    elif num == 4:#oopción de mostrar todos los libros
        print("\n Libros disponibles:\n")
        for libro in biblioteca:#itera cada libro en la biblioteca con un bucle for
            libro.mostrar()#uso del método mostrar para cada libro en la biblioteca

    elif num == 5:#opción de buscar libro por ISBN
        isbn4 = input("Indique el ISBN: ")#pide el ISBN 
        Libro.buscar(biblioteca, isbn4)#con el método buscar busca el ISBN en la lista biblioteca

    elif num == 6:
        print("Saliendo del programa...")

    elif num == 7:#mensaje si se quiere salir del programa
        menu()
    
    elif num <= 0 or num >= 7:#si se indica un valor por encima o debajo del 1 al 6, así se vuelve a solicitar el valor del menú
        print("\nHas indicado un valor no válido, las opciones son del 1 al 6.\n")
        menu()


