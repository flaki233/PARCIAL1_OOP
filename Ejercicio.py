class usuario:
	def __init__(self, nombre):
		self.nombre = nombre
		self.LibrosP = []
	def Librosp(self, libro, ListaDeLibros):
		if ListaDeLibros.count(libro):
			ListaDeLibros.remove(libro)
			self.LibrosP.append(libro)
		else:
			print("Disculpa, el libro no esta disponible por el momento")

	def DevolverLibro(self, libro, ListaDeLibros):
		if self.LibrosP.count(libro):
			self.LibrosP.remove(libro)
			ListaDeLibros.append(libro)
		else:
			print("No hay registros de que este libro haya sido prestado,")
			ListaDeLibros.append(libro)

class Biblioteca:
	def __init__(self, Libros):
		self.ListaDeLibros = Libros
		

	def agrLibro(self, libro):
		self.ListaDeLibros.append(libro)


	def removerLibro(self, libro):
		self.ListaDeLibros.remove(libro)


	def MostrarLibros(self):
		print(self.ListaDeLibros)
