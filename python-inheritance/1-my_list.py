# tests/1-my_list.txt

# Test instantiation and methods of MyList

>>> MyList = __import__('1-my_list').MyList

>>> my_list = MyList()
>>> my_list.append(1)
>>> my_list.append(4)
>>> my_list.append(2)
>>> my_list.append(3)
>>> my_list.append(5)
>>> print(my_list)
[1, 4, 2, 3, 5]

>>> my_list.print_sorted()
[1, 2, 3, 4, 5]

>>> print(my_list)
[1, 4, 2, 3, 5]

# Test with negative numbers
>>> my_list = MyList()
>>> my_list.append(-1)
>>> my_list.append(-4)
>>> my_list.append(-2)
>>> my_list.append(-3)
>>> my_list.append(-5)
>>> print(my_list)
[-1, -4, -2, -3, -5]

>>> my_list.print_sorted()
[-5, -4, -3, -2, -1]

>>> print(my_list)
[-1, -4, -2, -3, -5]

# Test with an empty list
>>> my_list = MyList()
>>> print(my_list)
[]

>>> my_list.print_sorted()
[]

>>> print(my_list)
[]
