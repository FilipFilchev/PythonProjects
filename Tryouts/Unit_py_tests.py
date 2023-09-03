# import unittest

# class TestStringMethods(unittest.TestCase):
#     def test_upper(self):
#         self.assertEqual('foo'.upper(), 'FOO')

#     def test_isupper(self):
#         self.assertTrue('FOO'.isupper())
#         self.assertFalse('Foo'.isupper())

#     def test_split(self):
#         s = 'hello world'
#         self.assertEqual(s.split(), ['hello', 'world'])
#         with self.assertRaises(TypeError):
#             s.split(2)

# if __name__ == '__main__':
#     unittest.main()

# """
# ----------------------------------------------------------------------
# Ran 3 tests in 0.002s

# OK


# or run python -m unittest 
# """



def test_upper():
    assert 'foo'.upper() == 'FOO'

def test_isupper():
    assert 'FOO'.isupper()
    assert not 'Foo'.isupper()

def test_split():
    s = 'hello world'
    assert s.split() == ['hello', 'world']
    try:
        s.split(2)
        assert False, "Expected TypeError"
    except TypeError:
        pass

"""
collected 3 items                                                                                                                   

Unit_py_test.py ...                                                                                                           [100%]

========================================================= 3 passed in 0.02s =========================================================
"""