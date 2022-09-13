class usuario:
	def __init__(self, nombre):
		self.nombre = nombre
		self.LibrosP = []
	def Librosp(self, libro, ListaDeLibros):
		if ListaDeLibros.count(libro):
			ListaDeLibros.remove(libro)
			self.LibrosP.append(libro)
		else:
			print("Disculpa, el libro no esta disponible por el momento o el nombre fue  mal escrito")
#Arriba podemos permitirle al usuario que busque el libro deseado, y si este no coincide con los nombres de la lista de libros entonces se le informara que el libro no esta disponible o el nombre fue mal escrito.


	def DevolverLibro(self, libro, ListaDeLibros):
		if self.LibrosP.count(libro):
			self.LibrosP.remove(libro)
			ListaDeLibros.append(libro)
		else:
			print("No hay registros de que este libro haya sido prestado,")
			ListaDeLibros.append(libro)
#Arriba se le permite al usuario devolver el libro que haya tomado prestado, si este  no aparece en los registros de libros prestados entonces se le informara al usuario que este libro no es parte de la biblioteca o al menos no hay registro de que haya sido prestado.

class Biblioteca:
	def __init__(self, Libros):
		self.ListaDeLibros = Libros
		

	def agrLibro(self, libro):
		self.ListaDeLibros.append(libro)


	def removerLibro(self, libro):
		self.ListaDeLibros.remove(libro)


	def MostrarLibros(self):
		print(self.ListaDeLibros)
#Estos son metodos que le permiten al bibliotecario o al encargado de libros, ver una lista completa de todos los libros disponibles y tambien se le permite agregar o remover los libros que el desee de esta lista.
