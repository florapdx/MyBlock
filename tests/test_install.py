import unittest

class test_imports(unittest.TestCase):

	def test_Django(self):
		import django

	def test_South(self):
		import south

	def test_psycopg2(self):
		import psychopg2

	def test_tastypie(self):
		import tastypie

"""
# Test something that depends on settings
class test_Something(unittest.TestCase):

	def test_Thing(self):
		from django.conf import settings
		settings.configure(SETTING={
			'this': {
				that
	}})
	import <dependency>
"""
if __name__ == "__main__":
	unittest.main()
