class Parent :

	def __init__ (self, last_name, eye_color) :

		print "Parent constructor Called"

		self.last_name = "Cyrus"
		self.eye_color = "Blue"

	def show_info(self) :

		print "Last Name : " + self.last_name
		print "Eye Color : " + self.eye_color



# Sintaxis Herencia
# class <name_child> (<parent_name>)
# Esta clase hereda de la clase Parent

class Child(Parent) :

	def __init__ (self, last_name, eye_color, number_of_toys) :

		print "Child constructor Called"
		# we are reusing the constructor of the father class
		Parent.__init__(self, last_name, eye_color)
		self.number_of_toys = number_of_toys

	# method overriding or polimorfismo
	def show_info(self) :

		print "Last Name : " + self.last_name
		print "Eye Color : " + self.eye_color
		print "Number of Toys : " + str(self.number_of_toys)


billy_cirus = Parent("Cyrus", "Blue")
miley_cirus = Child("Cyrus", "Green", 5)


# we are calling the child show info method
miley_cirus.show_info()