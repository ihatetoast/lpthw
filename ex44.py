class Parent(object):
	def implicit(self):
		print "PARENT implicit()"
	def override(self):
		print "PARENT override()"
	def altered(self):
		print "PARENT altered()"

class Child(Parent):
	def override(self):
		print "CHILD override()"
	def altered(self):
		print "CHILD BEFORE parent altered"
		super(Child, self).altered()
		print "CHILD AFTER parent altered"


dad = Parent()
son = Child()

print "IMPLICIT:"
dad.implicit()
son.implicit()

print "OVERRIDE:"

dad.override()
son.override()

print "ALTERED:"
dad.altered()
son.altered()
