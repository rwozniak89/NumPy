# # NumPy (short for Numerical Python) is a Python library fundamental for scientific computing. It supports a variety of high-level mathematical functions and is broadly used in data science, machine learning, and big data applications. With its help, you will be able to perform linear algebra calculations easily, as well as statistical, logical, and other operations, making use of numerous built-in functions.
# #
# # Most parts of NumPy that require high execution speed are written in C, which makes the operations much faster than the corresponding ones in Python itself. Owing to its efficiency and convenience, the library has gained vast popularity among data scientists who work with large datasets and need to perform speed computations.
# # Installation
# #
# # Firstly, to start working with NumPy, we need to install it, which can be easily done with pip:
# #
# # pip install numpy
# #
# # You can read more about the installation on the official page of the scientific python distribution.
# #
# # Then, import the library before starting your work:
#
# import numpy as np
#
# # NumPy arrays
# #
# # The core NumPy object is an n-dimensional array, also known as ndarray. The simplest way to create a NumPy array is to convert a Python list:
#
# first = np.array([1, 2, 3, 4, 5])
# print(first)                       # [1 2 3 4 5]
# print(type(first))                 # <class 'numpy.ndarray'>
#
# # In the example above, first is a one-dimensional array that is treated as a vector. As you can see, when printed, it is rendered without commas, as opposed to Python lists.
# #
# # Similarly, we can create a two-dimensional Numpy array from the corresponding Python list. Two- and more dimensional arrays are treated as matrices.
#
# second = np.array([[1, 1, 1],
#                    [2, 2, 2]])
#
# print(second)    # [[1 1 1]
#                  #  [2 2 2]]
#
# # NumPy arrays vs Python lists
# #
# # As you can see, NumPy arrays resemble a Python built-in list data type. However, there are a few crucial differences:
# #
# #     Unlike Python lists, NumPy arrays can only contain elements of the same type, usually numbers, due to the specifics of application fields.
# #     NumPy arrays are much more memory-efficient and much faster than Python lists when working with large datasets.
# #     Arithmetic operations differ when executed on Python lists or NumPy arrays.
# #
# # Let's take a look at arithmetic operations that can be applied both to arrays and to lists. All differences in them can be explained by the fact that Numpy arrays are created for computing and treated as vectors and matrices, while Python lists are a datatype made just to store data.
# #
# # To illustrate it, we'll create two lists and two arrays containing the same elements:
#
# list_a = [1, 2, 3, 4]
# array_a = np.array(list_a)
#
# list_b = [11, 22, 33, 44]
# array_b = np.array(list_b)
#
# # First, let's find their sum. The addition of two arrays returns their sum as when we add two vectors.
#
# print(array_a + array_b)  # [12 24 36 48]
#
# # For this reason, we can't add up arrays of different lengths, a ValueError will appear.
#
# array_c = np.array([111, 222])
# # print(array_a + array_c)        # ValueError
#
# # When we try to add a list and an array, the former is converted to an array, so the result is also a sum of vectors.
#
# print(list_a + array_a)   # [2 4 6 8]
#
# # However, when applied to lists, addition just merges them together.
#
# print(list_a + list_b)    # [1, 2, 3, 4, 11, 22, 33, 44]
#
# # Similarly, if we try to multiply a list by n, we'll get the list repeated n times, while with an array, each element will be multiplied by n:
#
# print(list_a * 3)   # [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
# print(array_a * 3)  # [3 6 9 12]
#
# # Learning sizes
# #
# # There're a number of ways to learn more about an array without printing it.
#
# first = np.array([1, 2, 3, 4, 5])
# second = np.array([[1, 1, 1],
#                    [2, 2, 2]])
#
# # To find out the dimensions size, use shape. The first number of the output indicates the number of rows and the second — the number of columns.
#
# print(second.shape)  # (2, 3)
#
# print(second.shape[0])  # (2, 3)
#
# array = np.array([[1,  2,  3],
#                   [4,  5,  6],
#                   [7,  8,  9],
#                   [10, 11, 12]])
#
# print('array', array.shape)  # (2, 3)
#
# # If the NumPy array has only one dimension, the result will be a bit different:
#
# print(first.shape)   # (5,)
#
# # In this case, the first number is not the number of rows but rather the number of elements in the only dimension, and the empty place after the comma means that there's no second dimension.
# #
# # The length of the shape tuple is the number of axes, ndim.
# #
# print(first.ndim)   # 1
# print(second.ndim)  # 2
#
# # The function len() returns the array's length, and size gives us the number of elements in the array.
#
# print(len(first), first.size)    # 5 5
# print(len(second), second.size)  # 2 6
#
# # Note that in the first case they return the same value, while in the second case the numbers differ. The thing is, len() works as it would work with regular lists, so if we regard the two-dimensional array above as a list containing two nested lists, it becomes clear that for finding its length only the nested lists are counted. Size, on the contrary, counts each single element in all nested lists.
#
# # Another thing to point out is that both length and size can also be got from its shape: length is actually the length of the first dimension, so it equals shape[0], and size is the total number of elements, which equals the product of all elements in the shape tuple.
#
# # Recap
# #
# # In this topic, we've learned the basics of NumPy:
# #
# #     what is NumPy and what it can be used for,
# #     how to install and import the library,
# #     arrays, the basic datatype of Numpy,
# #     the difference between NumPy arrays and Python lists,
# #     ways to get information about an array's content.
# #
# # Now, let's practice the acquired knowledge so that you'll be able to use it in the future.
#
# first = np.array(['1sss', 2, 3, 4, 5])
# print(first)
#
#
# import numpy as np
#
#
#
# def collect_info(array):
#     return (f'Shape: {array.shape}; dimensions: {array.ndim}; length: {len(array)}; size: {array.size}')
#
# def print_collect_info(array):
#     print(collect_info(array))
#
#
# threeD = np.array([[[1, 1, 1], [2, 2, 2]],
#                    [[3, 3, 3], [4, 4, 4]]])
#
# print_collect_info(threeD)
# print(threeD)
# n = np.zeros((3, 2, 6, 1))
# print_collect_info(n)
# print(n)
# #"Shape: (2, 2, 3); dimensions: 3; length: 2; size: 12".
# #"Shape: (2, 2, 3); dimensions: 3; length: 2; size: 12

# As you know, when we add an array and a list, the latter is treated also as an array. However, we may not want the addition to return the same result for a list and an array as it does for two arrays, because an argument being a list instead of an array might be a mistake.
#
# Write a function that will take two arguments:
#
#     two arrays,
#     an array and a list,
#     two lists.
#
# In the first case, sum them and return the result. In the second case, return a string with the warning One argument is a list, and in the last case, return Both arguments are lists, not arrays.
#
# All lists and arrays will be one-dimensional and of the same size.

# import numpy as np
#
# a1 = np.array([[1,2],[3,4]])
# a2 = a1
# l1 = [1,2,3,4]
# l2 = l1
#
# def custom_sum(arg1, arg2):
#     if type(arg1) == type(np.array(0)) and type(arg2) == type(np.array(0)):
#         return  arg1 + arg2
#     elif (type(arg1) == type(np.array(0)) and type(arg2) == type(list('1'))) or (type(arg2) == type(np.array(0)) and type(arg1) == type(list('1'))) :
#         return  'One argument is a list'
#     elif type(arg1) == type(list('1')) and type(arg2) == type(list('1')):
#         return 'Both arguments are lists, not arrays'
#     else:
#         return 0;
#
#
# print( custom_sum(a1,a2))
# print(custom_sum(a1,l1))
# print(custom_sum(l1,a1))
# print(custom_sum(l1,l2))
#
# import numpy as np
#
# def custom_sum(arg1, arg2):
#     if isinstance(arg1, np.ndarray) and isinstance(arg2, np.ndarray):
#         return arg1 + arg2
#     elif (isinstance(arg1, np.ndarray) and isinstance(arg2, list)) or (isinstance(arg1, list) and isinstance(arg2, np.ndarray)):
#         return 'One argument is a list'
#     elif isinstance(arg1, list) and isinstance(arg2, list):
#         return 'Both arguments are lists, not arrays'
#     return None
#
#
# import numpy as np
#
#
# def custom_sum(arg1, arg2):
#     lists = len([arg for arg in (arg1, arg2) if type(arg) == list])
#     if lists == 2:
#         return 'Both arguments are lists, not arrays'
#     elif lists == 1:
#         return 'One argument is a list'
#     else:
#         return arg1 + arg2


#
# import numpy as np
#
# arr = np.array([[1, 5, 6],
#                 [0, 5, 7],
#                 [9, 0, 3]])
# print(arr.ndim)
#


# the following line reads the input and converts it into a list; do not modify it, please
# hidden = list(input())
#
# # your code here
# #for i in hidden:
# print(len(hidden))
#
# def is_even(number):
#     return number % 2 == 0
#
# print(is_even(1))
#
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
#            21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
#            41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
#            61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
#            81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
#
# n =  [e for e in numbers if e % 5 == 0]
# print(n)

# import random
# random.seed(1)
# print(random.choice([1, 2, 3, 4, 5])) #2
#
#
# n = int(input())
# if n <0:
#     print("negative")
# elif n>0:
#     print("positive")
# else:
#     print("zero")

# raise_to_power = lambda x, y: x ** y
#
# print(raise_to_power(2, 3))
#
# def func2(x):
#     if x % 2 == 0:
#         return 'even'
#     else:
#         return 'odd'
#
# func = lambda x: x % 2 == 0
#
#
# func = lambda x: 'even' if x % 2 == 0 else 'odd'
#
# print(func(2))


# print("The ship's name is 'Brave'.")
# #print('Cat's paws.')
# print('The word "Ciao" means "hello" in Italian.')
# #print("And "Ciao" is Italian "Bye".")
#
# print(r"""
# Switching on the camera in the camel habitat...
#  ___.-''''-.
# /___  @    |
# ',,,,.     |         _.'''''''._
#      '     |        /           \
#      |     \    _.-'             \
#      |      '.-'                  '-.
#      |                               ',
#      |                                '',
#       ',,-,                           ':;
#            ',,| ;,,                 ,' ;;
#               ! ; !'',,,',',,,,'!  ;   ;:
#              : ;  ! !       ! ! ;  ;   :;
#              ; ;   ! !      ! !  ; ;   ;,
#             ; ;    ! !     ! !   ; ;
#             ; ;    ! !    ! !     ; ;
#            ;,,      !,!   !,!     ;,;
#            /_I      L_I   L_I     /_I
# Look at that! Our little camel is sunbathing!""")
#
# input_str = input()
#
# # your code here
# input_str = list(input_str)
# print(input_str)

# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# # put your python code here
# print(alphabet[16])
#
# # Save the input in this variable
# ticket = input()
#
# # Add up the digits for each half
# half1 = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
# half2 = int(ticket[3]) + int(ticket[4]) + int(ticket[5])
#
# # Thanks to you, this code will work
# if half1 == half2:
#     print("Lucky")
# else:
#     print("Ordinary")



#
# # write your code here
# n = int(input('Please enter the number of the habitat you would like to view:'))
# if n == 0:
#     print(camel)
# elif n == 1:
#     print(lion)
# elif n == 2:
#     print(deer)
# elif n == 3:
#     print(goose)
# elif n == 4:
#     print(bat)
# elif n == 5:
#     print(rabbit)
#
# print("""---
# You've reached the end of the program. To check another habitat, please restart the watcher.""")
#
#
# In this topic, we continue discussing NumPy. We will focus on new ways of creating arrays, as well as on methods of their indexing and slicing. The introduction to NumPy showed the simplest way to create an array — converting a Python list using np.array(). But there are other ways we may need to know.
# Array range and evenly spaced array
#
# The first function that helps to create arrays in NumPy, is np.arange(). It is similar to the built-in range() generator of numbers, but np.arange() returns an array. Let's have a look at the example.
#
# import numpy as np
#
# array_1 = np.arange(5)
# print(array_1)  # [0 1 2 3 4]
# #
# # [Click and drag to move]
# #
# # You can also create an array by specifying a start element, a stop element, and a step: np.arange(start, stop, step). The default step value equals to 1. Note that the start element is included in the range while the stop element is not.
#
# array_2 = np.arange(5, 9)
# array_3 = np.arange(5, 6, 0.1)
# print(array_2)  # [5 6 7 8]
# print(array_3)  # [5. 5.2 5.4 5.6 5.8]
# #
# # [Click and drag to move]
# #
# # If you want to space all the elements in your array evenly, np.linspace() can help you. It takes the start value, the end value, and the num parameter which is the total number of elements. The default num value is 50, so in the second example below, there will be 50 elements in the array array_5, evenly spaced between 21 and 23. As opposed to the np.arange() function, the end value in np.linspace() is always included in the array.
#
# array_4 = np.linspace(21, 23, num=10)
# array_5 = np.linspace(21, 23)
# print(array_4)   # [21.  21.5 22.  22.5 23. ]
# print(array_5)  # [21.         21.04081633 21.08163265 21.12244898 ... 22.95918367 23.
#
# # Arrays filled with ones and zeros
# #
# # Sometimes we need an array consisting of only zeroes or only ones. In NumPy, there are easy ways to create them. np.zeros() and np.ones() create new dimensioned arrays filled with the corresponding values.
#
# array_6 = np.ones((3, 2))
# array_7 = np.zeros(7)
# print(array_6)
# # [[1. 1.]
# #  [1. 1.]
# #  [1. 1.]]
# print(array_7)  # [0. 0. 0. 0. 0. 0. 0.]
#
# # [Click and drag to move]
# #
# # The np.zeros_like() and np.ones_like() functions are similar to the previous ones, but they return an array of ones or zeros with the same shape and type as the given arrays.
#
# x = np.array([[1, 1, 1], [2, 2, 2]])
# y = np.array([1, 2, 3, 4, 5])
# array_8 = np.ones_like(x)
# array_9 = np.zeros_like(y)
# print(array_8)
# # [[1 1 1]
# #  [1 1 1]]
# print(array_9)  # [0 0 0 0 0]
# #
# # Converting NumPy arrays to Python lists
# #
# # Finally, when you do not need to work with arrays anymore, you can easily transform them into lists. NumPy provides the array.tolist() function.
#
# array_10 = np.array([[1, 2], [3, 4]])
# lst1 = array_10.tolist()
# print(lst1)  # [[1, 2], [3, 4]]
# #
# # [Click and drag to move]
# #
# # If we attempt to use the list(array) function on numpy arrays, it will also return a list but its elements will be numpy arrays.
#
# array_11 = np.array([[5, 2], [7, 4]])
# lst2 = list(array_11)
# print(lst2)  # [array([5, 2]), array([7, 4])]
# print(type(lst2[0]))  # <class 'numpy.ndarray'>
# print('ndexing in arrays')
# # Indexing in arrays
# #
# # Now, once we know how to create arrays, it is time to learn how to get access to their elements. Just like with Python lists, we can access the elements using indices. If you use a one-dimensional array in your program, there is no difference with how list indices work. However, when you face an n-dimensional array, do not forget about some key operations.
# #
# # Let's have a look at the example and discuss it.
#
# array_12 = np.array([[1, 12, 31], [4, 45, 64], [0, 7, 89]])
# print(array_12)
# print(array_12[2, 2])  # 89
# print(array_12[0, 2])  # 89
# print(array_12[2][2])  # 89
# #
# # [Click and drag to move]
# #
# # First of all, we created a two-dimensional array. Suppose, we are interested in getting the last value. The idea of multidimensional indexing is quite easy: if you have two dimensions, the first value addresses the row of your array, the second one addresses the index of the value you are searching for. You can see that the result of array_12[2, 2] and array_12[2][2] is the same. The first case is more efficient, however, because when we write array_12[2][2], a new temporary array is created after the first index that is subsequently indexed by 2.
# #
# # Similarly, if you have three dimensions, you need to print three values to execute multidimensional indexing, etc. Let's look at the three-dimensional example below.
#
# array_13 = np.array([[[1, 12, 31], [4, 45, 64], [0, 7, 89]]])
# print(array_13)
# print(array_13[0, 1, 1])  # 45
# print(array_13[0][1][1])  # 45
# #
# # [Click and drag to move]
# #
# # If you print an index that is out of the bounds, it will cause an error in your program.
#
# def collect_info(array):
#     return (f'Shape: {array.shape}; dimensions: {array.ndim}; length: {len(array)}; size: {array.size}')
#
# print(collect_info(array_12))
# print(collect_info(array_13))
#
# # Slicing in arrays
# #
# # NumPy arrays can also be sliced like lists in Python. Slicing a one-dimensional array is the same as slicing a Python list, so our main task is to understand how to slice n-dimensional arrays. Look at the example below:
#
# array_14 = np.array([[100, 101, 102],
#                  [103, 104, 105],
#                  [106, 107, 108],
#                  [109, 110, 111]])
# print(collect_info(array_14))
# print(array_14[1:3, 1])   # [104 107]
#
# print(array_14[:, 1:])   # [104 107]
# # [Click and drag to move]
# #
# # We start by creating a two-dimensional array array_14 with four rows. When we write array_14[1:3, 1], the first part addresses the slice of the rows to be taken into account, then the second part chooses an element of each row. As a result, we have a new one-dimensional array.
# #
# # Let's have a look at some more examples. array_15 below is a three-dimensional array. Just like in Python, we can use the negative index to choose elements from the end — the last two-dimensional array [[11, 12, 13, 14, 15], [16, 17, 18, 19, 20]] in this case. Then we just make a full copy of the array with the help of the : operator, and at last, in each row, we choose a particular slice.
#
# array_15 = np.array([[[1, 2, 3, 4, 5],
#                  [6, 7, 8, 9, 10]],
#                  [[11, 12, 13, 14, 15],
#                  [16, 17, 18, 19, 20]]])
# print(collect_info(array_15))
# print(array_15[-1, :, 1:4])
# # [[12 13 14]
# #  [17 18 19]]
# #
# # [Click and drag to move]
# #
# # In array_16 we extract every row and element with a given step.
#
# # two-dimensional array
# array_16 = np.array([[1, 2, 3, 4, 5],
#                  [5, 4, 3, 2, 1],
#                  [6, 7, 8, 9, 10],
#                  [10, 9, 8, 7, 6],
#                  [11, 12, 13, 14, 15]])
# print(collect_info(array_16))
# print(array_16[::2, ::2])
# # [[ 1  3  5]
# #  [ 6  8 10]
# #  [11 13 15]]
#
# # [Click and drag to move]
# #
# # As you can see, slicing operations are the same as with Python lists. But here, we apply them with the dimensions in mind. This can lead to some errors, especially with high-dimensional arrays, so we need to be very careful.
# # Conclusion
# #
# # In this topic, we have learned how to:
# #
# #     create arrays using different methods,
# #     transform arrays into lists,
# #     index and slice multidimensional arrays.
# #
# # Now it's high time to move on to some practical tasks. Practice makes perfect!
# # #Now let's work with a new array.
# #
# # array = np.array([[4,5,6],
# #                   [3,2,1],
# #                   [7,8,9],
# #                   [12,11,10]])
# #
# # #Match each slicing with its result.
# # array[-2, -1] #9
# # array[:2, ::2] #[[4 6] [3 1]]
# # array[2, 1] #8
# # array[::2, 1:] #[[5 6] [8 9]]
# #
# # array = np.linspace(20, 42, num=11)
# # print(array)
# # print(array[4])
# #
# # import numpy as np
# #
# #
# # a = np.array([[1, 3, 4],
# #               [45, 66, 76],
# #               [0, 9, 4],
# #               [12, 14, 90],
# #               [39, 71, 83],
# #               [27, 20, 5]])
# # # your code here
# # a1 = int(input())
# # a2 = int(input())
# # def print_element(x, y):
# #     return a[x, y]
# # print(print_element(a1, a2))
# # Write a code that extracts a part of the following array. The first integer in the input is a step for extracting a subarray, the second integer is a step for rows in the subarray, and the last integer is an index for the elements in the rows. Print the resultant array.?
# import numpy as np
# a = np.array([[[10, 11, 12], [13, 14, 15], [16, 17, 18]],
#               [[20, 21, 22], [23, 24, 25], [26, 27, 28]],
#               [[30, 31, 32], [33, 34, 35], [36, 37, 38]],
#               [[40, 41, 42], [43, 44, 45], [46, 47, 48]],
#               [[50, 51, 52], [53, 54, 55], [56, 57, 58]],
#               [[60, 61, 62], [63, 64, 65], [66, 67, 68]],
#               [[70, 71, 62], [73, 74, 65], [76, 77, 78]],
#               [[80, 81, 62], [83, 84, 85], [86, 87, 88]]])
# print(collect_info(a))
#
# # a1 = int(input())
# # a2 = int(input())
# # a3 = int(input())
# a1,a2,a3 = 2,2,1
# def print_element(x, y, z):
#     return a[::x, ::y, z]
# print(print_element(a1, a2, a3))
#
# print(np.zeros((5,2)))
#
# import numpy as np
# size = int(input())
# value = int(input())
# print(np.full((size, size), value)*1.0)
#
# import numpy as np
#
#
# side = int(input())
# dim = (side, side)
# fillup = int(input())
# print(np.ones(dim) if fillup == 1 else np.zeros(dim))
#
# import numpy as np
#
# a = int(input())
# b = float(input())
# c = np.zeros((a, a))
# c[...] = b
#
# print(c)
#
# import numpy as np
#
# b= np.arange(15,25, 6)
# print(b)
# a1 = np.linspace(15, 25, num=6)
# print(a1)
#
# a = np.linspace(15, 25, 6)[-2]
#
# print(a)
#
# import numpy as np
# array = np.linspace(15, 25, 6)
# print(array[-2])
#
# Theory: Data types in NumPy
#
# In this topic, we are going to get acquainted with NumPy data types. You have already learned some basic data types provided in Python: string for text data, float for floating-point numbers, etc. NumPy and Python data types share some common features, but at the same time, NumPy data has some unique peculiarities. We will discuss the basic NumPy data types and methods of working with them.
# Types of data in NumPy
#
# Imagine that you strive to know everything about all data types in NumPy and you wonder how to do it. In this case np.sctypeDict can help you. It prints a dictionary in which all the keys are different data types.
# import numpy as np
# print(np.sctypeDict)
# {'?': <class 'numpy.bool_'>, 0: <class 'numpy.bool_'>, 'byte': <class 'numpy.int8'>, 'b': <class 'numpy.int8'>, 1: <class 'numpy.int8'>, 'ubyte': <class 'numpy.uint8'>, ...}
#
# Of course, such a dictionary is not the most convenient way to explore the data types. The summary of the main types with their brief descriptions is shown below. The most widely-used types are the ones that represent integers and floating numbers, but there are other types, too. It is worth mentioning that NumPy data types are the same as in C programming language because NumPy itself is a wrapper on C, which makes NumPy operations so fast.
#
# 1. Integer data
#
# For integer numbers, there are a lot of specific data types in NumPy.
# Data type 	Description
# int_ or int32 or int64 	Integer type set by default (depends on a user's operation system)
# int8 	Integers ranging from -128 to 127
# int16
#
# Integers ranging from -32 768 to 32 767
# int32 	Integers ranging from -2 147 483 648 to 2 147 483 647
# int64 	Integers ranging from -9 223 372 036 854 775 808 to 9 223 372 036 854 775 807
# uint8 	Non-negative integers ranging from 0 to 255
# uint16 	Non-negative integers ranging from 0 to 65 535
# uint32 	Non-negative integers ranging from 0 to 4 294 967 295
# uint64 	Non-negative integers ranging from 0 to 18 446 744 073 709 551 615
#
# Mind different ranges of numbers. As we have mentioned, NumPy specifies the size of the data: the thing is, one byte (or 8 bits) is required to decode integers from -128 to 127. If we take only positive ones, the range is from 0 to 255, respectively. For larger integers, we need two bytes (16 bits), four bytes (32 bits), or eight bytes (64 bits).
#
# The range thresholds are determined by different powers of two. In case of int8, it is 2(8-1) = 128. One bit is reserved for the negative / positive sign, so it's 27 rather than 28. Also, one place is taken by zero, so the upper boundary is 128 - 1 = 127. Similarly, for the upper limit for int64, 9 223 372 036 854 775 807 = 2(64-1) - 1.
#
# It is important to note that -3, for instance, can have either int8, int16, int32, or int64 data type. On the other hand, 3 can represent any of int and uint formats, it all depends on what you are working with.
#
# 2. Float data
#
# For float values, there are the following data types:
# Data type 	Description
# float16
#
# Half-Precision Floating-Point Format (2 Bytes)
# float32
#
# Single-Precision Floating-Point Format (4 bytes)
# float_or float64
#
# Double-Precision Floating-Point Format (8 bytes)
# float128
#
# Quadruple-Precision Floating-Point Format (16 bytes)
#
# It is necessary to clarify the types of precisions. Half-precision floating-point format provides results that are not that accurate. If you want to obtain more decimal spaces, you need to use the single-precision, double-precision, or quadruple-precision formats. It is shown in the example below.
#
# n = 22/7
# print(np.float16(n))  # 3.143
# print(np.float32(n))  # 3.142857
# print(np.float64(n))  # 3.142857142857143
# #
# # For other purposes, you can use boolean, complex, or string data. bool_ is for boolean data in NumPy, it works the same way as the boolean type in Python. For complex numbers, there are several data types: complex64, complex_ (complex128), and complex256. String data is represented by str_ (standard Python string) and unicode_ (Unicode string), and bytes as bytes_ (a sequence of encoded bytes which is ready to be stored in the memory of a program). You can read more about these data types in the official NumPy documentation.
# #
# #  Specifying data types
# #
# # In NumPy, the np.dtype class stores different objects of the data type. Below there are some sample queries:
#
# print(np.float64)  # <class 'numpy.float64'>
# print(np.str_)     # <class 'numpy.str_'>
# #
# # To find out the data type of an existing array, use array.dtype:
#
# array_1 = np.array([[5, 6], [15, 0]])
# array_2 = np.array([[2.5, 5.7], [1.2, 6.9]])
# array_3 = np.array([[2, 34], [78.9, 4.5]])
# print(array_1.dtype)  # int64
# print(array_2.dtype)  # float64
# print(array_3.dtype)  # float64
# print(array_3)  # float64
# #
# # Be aware of the array_3 variable. It contains an array with different types of data — integers and floats. When combining data, NumPy will convert all the data into one type, so that all the integers become floating numbers.
# #
# # When creating an array, you can specify the type of data in the array with the help of the dtype argument:
#
# array_4 = np.array([[1, 2], [3, 4]], dtype=np.float32)
# print(array_4)
# # [[1. 2.]
# #  [3. 4.]]
#
# array_5 = np.arange(7, dtype=np.float64)
# print(array_5)  # [0. 1. 2. 3. 4. 5. 6.]
#
# array_6 = np.arange(7, dtype=np.int64)
# print(array_6)  # [0 1 2 3 4 5 6]
# #
# # Changing data types
# #
# # To transform one data type into another, use the np.<type> function:
#
# print(np.bool(1))  # True
# print(np.float64(35))  # 35.0
# #
# # If you want to do it with an array rather than with single values, use the array.astype() function. It copies the array and converts it into the specified type.
#
# array_7 = np.array([[-129, 45], [34, 129]], dtype=np.int64)
# print(array_7)
# # [[-129   45]
# #  [  34  129]]
#
# print(array_7.astype(np.float64))
# # [[-129.   45.]
# #  [  34.  129.]]
#
# print(array_7.astype(np.str_))
# # [['-129' '45']
# #  ['34' '129']]
#
# print(array_7.astype(np.bool_))
# # [[ True  True]
# #  [ True  True]]
# #
# # In the example above, you can see that we can easily transform our array_7 into float, string, or boolean data. However, if we try to change the type to int8, a problem will arise:
# # data type. Be careful with this, it can lead to errors!
# print(array_7.astype(np.int8))
# # [[ 127   45]
# #  [  34 -127]]
#
# As you can remember, int8 can store integers from -128 to 127 that take up to one byte. When we try to convert into int8 numbers that are not in its range, NumPy will not display a memory error, but instead, it just starts counting from the very beginning. -129 was changed to 127, the first positive integer. Similarly, 129 was changed to the second negative integer.
#
# What happens in the example above, is called an integer overflow. It occurs when an arithmetic operation attempts to create a number outside of the range that can be represented within a given

# Conclusion
#
# NumPy provides a great number of data types compared to basic Python data types. In this topic we've learned:
#
#     main types of data in NumPy;
#     how to specify data types when you create arrays;
#     how to print the data type of an existing array;
#     the way of changing data types in arrays.
#
# The next step is practicing your skills!


# import numpy as np
#
# array = np.array([[0, 2, 1998],
#                   [12, 0, 1212],
#                   [21, 0, 0],
#                   [7, 0, 2019]])
#
# # print((array[int(input()), :]).astype(np.bool_))
#
#
# import numpy as np
#
# # array = np.array([[212, 215, 434, 2, 0],
# #                   [6, 447, 0, 4, 143],
# #                   [10, 478, 601, 602, 3]], dtype=np.float64)
# #
# # print((array[int(input()), ::int(input())]).astype(np.int8))
#
# print(np.bool_(int(input())))

# Standard functions with one-dimensional arrays
#
# The easiest way to explain the basics of array operations is to show a few examples with one-dimensional arrays. You will learn to use them on multi-dimensional arrays later in this topic.
#
# Let's start with finding the sum of the array elements. Similarly to basic addition in Python, we use the method sum() that returns the sum of all values in the given array:
# import numpy as np
#
# array_1 = np.array([1, 2, 3, 4, 5])
# print(array_1.sum())  # 15
# #
# # The method array.prod() returns the product of the array elements. It is similar to multiplication in Python:
#
# print(array_1.prod())  # 120
# #
# # array.max() and array.min() return the maximum or minimum value in the array, respectively:
#
# print(array_1.max())  # 5
# print(array_1.min())  # 1
# #
# # Finally, array.argmax() and array.argmin() return the indexes of the maximum or minimum values in the array.
#
# print(array_1.argmax())  # 4
# print(array_1.argmin())  # 0
#
# Be careful with data types in your array! All operations described in this topic work only with integers and floats.
#
# Statistical functions with one-dimensional arrays
#
# NumPy also provides tools to implement statistical calculations. Take a look at the main statistical functions and their descriptions:
# NumPy methods and functions 	Descriptions
# array.std() or np.std(array) 	Computation of the Standard Deviation
# array.mean() or np.mean(array) 	Computation of the Arithmetic Mean
# array.var() or np.var(array) 	Computation of the Variance
# np.median(array) 	Computation of the Array Element Median
# np.average(array) 	Computation of the Array Element Average
#
# You can see the examples of these operations below:
#
# array_2 = np.array([3, 56, 78, 32, 65, 0, 9])
# print(array_2.std())  # 29.576604101960076
# print(array_2.mean())  # 34.714285714285715
# print(array_2.var())  # 874.7755102040816
# print(np.median(array_2))  # 32.0
# print(np.average(array_2))  # 34.714285714285715
#
# import numpy as np
# from scipy import stats
#
# a = np.array([[1, 3, 4, 2, 2, 7],
#               [5, 2, 2, 1, 4, 1],
#               [3, 3, 2, 2, 1, 1]])
# m = stats.mode(a)
# print(m)
# a = np.array([1,1,1,2,2,2,2,3,3,4])
# m = stats.mode(a)
# print(m)
#
# Axes in arrays
#
# You already know that axes in the arrays have their dimensions. But what exactly is an axis? To put it short, an axis is a direction along the columns and rows of your array. One-dimensional arrays have only one row. Consider an example for the array np.array([56, 78, 96]):
#
# Now, let's take a look at another example with the two-dimensional array np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]). Here, enumeration starts with columns. Here, the columns are Axis 0, and the rows are Axis 1:
#
# Working with two-dimensional arrays is rather simple, but how do we analyze axes in a three-dimensional array? It is easier than you might think: just imagine a coordinate system. Once again, let's look at an example. We have an array np.array([[[7, 8], [2, 10]], [[13, 0], [1, 2]]]) .
#
# Our array consists of two subarrays, each consisting of two columns and two rows. Axis 1 here represents the vertical axis, Axis 2 represents the horizontal axis, and Axis 0 is the so-called Z axis that corresponds to the depth of the array.
#
# So, the pairs [7, 13], [8, 0], [2, 1], and [10, 2] will be analyzed along the Axis 0, the pairs [7, 2], [8, 10], [13, 1], and [0, 2] will be analyzed along the Axis 1, and the pairs [7, 8], [2, 10], [13, 0], and [1, 2] will be analyzed along the Axis 2.
#
# Arrays with four or more dimensions require some imagination to represent their structure, but it works the same way: you just add one more axis to your coordinate system.
#
# There is a cool trick to remember which index corresponds to which axis. When we have only one axis (that is, a row), it is always Axis 0. When a column appears, it becomes Axis 0, and the row switches to Axis 1. Finally, in the example above, the new axis becomes Axis 0, and the other two shift to Axis 1 (columns) and Axis 2 (rows). The same logic also works for multi-dimensional arrays with more than three dimensions.
#
# Specifying axes for operations in multidimensional arrays
#
# Why are axes so important in NumPy? Sometimes you need to specify the axis you are working with, for example, when you carry out some operations with your array. This section contains some particular examples.
#
# # There is no need to specify Axis 0 in one-dimensional arrays, but if you do, no errors will occur.
# import numpy as np
# array_3 = np.array([1, 2, 3])
# print(array_3.sum())  # 6
# print(array_3.sum(axis=0))  # 6
# #
# # Mind the number of axes you're dealing with. If you print an index that is out of bounds of a certain array dimension, this will cause an error.
# #
# # Let's analyze a new two-dimensional array. If we don't specify any axes, the operations will be carried out on all elements, just like with a one-dimensional array:
#
# array_4 = np.array([[1, 2, 3],
#                     [4, 5, 6],
#                     [7, 8, 9]])
# print(np.mean(array_4))  # 2.581988897471611
# print(array_4.sum())  # 45
# #
# # If you want to carry out an operation with a particular axis, use the axis=X command, where X is the index of the desired axis:
#
# print(np.mean(array_4, axis=0))  # [4. 5. 6.]
# print(array_4.sum(axis=1))  # [ 6 15 24]
# print(array_4[:,1])
# #
# # As you can see, np.mean(array_4, axis=0) with the specified axis calculates the mean values for the elements in each column. For example, the mean of the first column is 4, because (1 + 4 + 7) / 3 = 4. Similarly, array_4.sum(axis=1) calculates the sum of all values in each row. For the first row, the sum is 1 + 2 + 3 = 6.
# #
# # Now let's take a look at another situation that may occur when we work with a three-dimensional array:
# print('array_5')
# array_5 = np.array([[[1, 2], [3, 4]],
#                     [[5, 6], [7, 8]]])
# print(array_5.sum(axis=0))
# print(array_5.sum(axis=1))
# print(array_5.sum(axis=2))
# # [[ 6  8]
# #  [10 12]]
# print(array_5.max(axis=1))
# # [[3 4]
# #  [7 8]]
# print(array_5.mean(axis=2))
# # [[1.5 3.5]
# #  [5.5 7.5]]
# #
# # array_5.sum(axis=0) and array_5.max(axis=1) work the same way as the example above; they calculate the sum of all values in each row and the maximum value in each column, respectively. As for array_5.mean(axis=2), it adds each pair [1, 2], [3, 4], [5, 6], [7, 8], calculates every mean, and returns a new array with these mean values.
# # Conclusion
# #
# # In this topic, we have learned:
# #
# #     how to carry out operations with one-dimensional arrays;
# #     why axes are important and how they work;
# #     how to specify axes when you're dealing with operations in NumPy.
# #
# # Now that you have this knowledge, it's time to test it and make sure you can put it to practice.
#
# array = np.array([[7, 80, 15], [6, 9, 4], [9, 4, 3]])
# print(array.prod(axis=0))
# print(array.prod(axis=1))
#
# array = np.array([[34, 0, 5], [77, 1, 4], [89, 44, 3]])
# print('array', array)
# print(array.sum(axis=0))
# print(array.min(axis=0))
# print(array.prod(axis=1))
# print(array.mean(axis=1))
#
#
# # import numpy as np
# #
# # a = np.array([int(input()), int(input()), int(input())])
# # print(a.max())
# # print(a.argmax())
# #
# # import numpy as np
# # array = np.array([int(input()) for _ in range(3)])
# # print(array.max(), array.argmax(), sep='\n')
# #
# # import numpy as np
# # a = [input() for _ in range(3)]
# # array = np.array(a, dtype=np.int)
# # print(array.max(), array.argmax(), sep='\n')
#
# import numpy as np
#
#
# array = np.array([[[13, 14], [34, 35]], [[9, 9], [5, 0]]])
# print(array.sum(axis=0))
# print(array.sum())

# Basic arithmetic operations on arrays
#
# First of all, do not forget to import the module:

import numpy as np
#
# The first operations we are going to cover are basic mathematical operations: addition, subtraction, multiplication, division, and exponentiation. They all are element-wise; this means that the operations are applied to pairs of corresponding elements in two arrays and the results are placed in a new array.
# # Addition
#
# To
# calculate
# the
# sum
# of
# two
# arrays, you
# can
# use
# the
# np.add()
# function.
#
# a1 = np.array([1, 2, 3])
# a2 = np.array([4, 5, 6])
# a3 = np.add(a1, a2)
# print(a3)  # [5 7 9]
# print(a1+a2)  # [5 7 9]

# There is also
# an
# opportunity
# to
# add
# two - dimensional
# arrays or arrays
# with more than two dimensions.Another way of using addition is a1 + a2.
#
# a1 = np.array([[1, 2], [3, 4]])
# a2 = np.array([[5, 6], [7, 8]])
# a3 = a1 + a2
# print(a3)
# print(a1 + a2)
# [[ 6  8]
#  [10 12]]

# Now
# mind
# another
# example:
#
# a1 = np.array([[1, 2], [3, 4]])
# a2 = np.array([[5, 6, 7], [8, 9, 10]])
# a3 = np.add(a1, a2)
# # ValueError: operands could not be broadcast together with shapes (2,2) (2,3)
#
# The
# thing is, the
# first
# array
# has
# two
# columns,
# while the second one has three columns, so the ValueError is raised because of the incompatibility of different shapes.
# Now
# let
# 's analyze another example.
#
# a1 = np.array([[1, 2], [3, 4]])
# a2 = np.array([5, 6])
# a3 = np.add(a1, a2)
# print(a3)
# [[ 6  8]
#  [ 8 10]]

# The
# operands
# have
# different
# shapes, but
# there
# are
# no
# errors.So, what
# happens in this
# case? The
# shape
# of
# the
# first
# operand is (2, 2), the
# shape
# of
# the
# second
# one is (2,).To
# make
# them
# compatible and apply
# an
# element - wise
# addition, NumPy
# uses
# broadcasting.Broadcasting
# can
# be
# described as a
# set
# of
# rules
# for applying element - wise operations on arrays of different shapes.When you work with two arrays, NumPy always compares their sizes and turns them into one shape, if possible.In the example, broadcasting goes as follows: as
# the
# last
# dimensions
# have
# an
# equal
# number
# of
# elements, it
# takes
# the
# second
# operand and expands
# it
# to
# a
# larger
# size:
#
# In
# other
# words, the
# broadcasting
# procedure
# replicates[5
# 6] and adds
# it
# to[1
# 2] and [3 4].The
# resultant
# array
# has
# the(2, 2)
# shape.
#
# There is another
# example
# for you:
#
# a1 = np.array([[[1, 2, 3]], [[4, 5, 6]]])
# a2 = np.array([[7], [8]])
# a3 = np.add(a1, a2)
# print(a3)
# [[[ 8  9 10]
#   [ 9 10 11]]
#
#  [[11 12 13]
#   [12 13 14]]]

# The
# shape
# of
# the
# first
# operand is (2, 1, 3), the
# second
# one
# has
# the(2, 1)
# shape.What
# does
# broadcasting
# do in this
# case? Dimensions
# with the size equal to 1 are expanded to match dimensions in the first array: 7 is replicated, so
# it
# can
# be
# added
# to[1
# 2
# 3]; 8 is also
# replicated and added
# to[1
# 2
# 3].Then, 7 is added
# to[4
# 5
# 6], and so is 8.
# The
# shape
# of
# the
# resultant
# array is (2, 2, 3).
#
# At
# the
# end
# of
# the
# day, broadcasting
# tries
# to
# match
# different
# sizes
# so
# that
# arithmetic
# operations
# can
# be
# performed.Most
# of
# the
# examples
# below
# will
# include
# broadcasting, too, so
# that
# you
# can
# understand
# how
# it
# works
# better.You
# can
# read
# more
# about
# broadcasting in the
# official
# Numpy
# guidelines.
#
# Subtraction
#
# To
# subtract
# arrays, we
# can
# use
# np.subtract():
# print('a3 = np.subtract(a1, a2)')
# a1 = np.array([[2, 7], [8, 13]])
# a2 = np.array([5])
# a3 = np.subtract(a1, a2)
# print(a3)
# print(a1 - a2)
# [[-3  2]
#  [ 3  8]]
#
# In
# this
# case, the
# only
# element
# of
# the
# second
# array is also
# replicated.Mind
# that
# you
# can
# type
# a1 - a2
# instead
# of
# np.subtract(a1, a2).Moreover, you
# can
# subtract
# the
# integer
# 5
# instead
# of
# the
# NumPy
# array[5], the
# result
# will
# stay
# the
# same.
#
# Multiplication
#
# np.multiply()
# will
# multiply
# arguments
# of
# arrays
# element - wise:

# a1 = np.array([[[1, 2, 3], [3, 4, 5]], [[5, 6, 7], [7, 8, 9]]])
# a2 = np.array([[-1, 0, 7], [12, 14, 5]])
# a3 = np.multiply(a1, a2)
# print(a3)
# [[[ -1   0  21]
#   [ 36  56  25]]
#
#  [[ -5   0  49]
#   [ 84 112  45]]]

# As
# you
# can
# see, the
# shape
# of
# the
# resultant
# array is equal
# to
# the
# shape
# of
# the
# bigger
# array.Again, writing
# a1 * a2 is equal
# to
# np.multiply(a1, a2).
# Division
#
# np.divide()
# allows
# us
# to
# divide
# two
# arrays:
#
# a1 = np.array([[[-6, 12, 3]], [[2, 15, 3]]])
# a2 = np.array([[2], [4]])
# a3 = np.divide(a1, a2)
# print(a3)
# # [[[-3.    6.    1.5 ]
# #   [-1.5   3.    0.75]]
# #
# #  [[ 1.    7.5   1.5 ]
# #   [ 0.5   3.75  0.75]]]
# print('a3 = np.divide(a1, a2)')
# a1 = np.array([[[-6, 3]], [[2, 3]]])
# a2 = np.array([[2], [4]])
# a3 = np.divide(a1, a2)
# print(a3)
# # You
# # can
# # also
# # use
# # a1 / a2
# # instead
# # of
# # np.divide(a1, a2).
# #
# # Exponentiation
# # np.power()
# # raises
# # elements
# # of
# # the
# # first
# # array
# # to
# # powers
# # from the second
# #
# # array.It is also
# # an
# # element - wise
# # operation.
#
# a1 = np.array([[1, 2], [3, 4]])
# a2 = np.array([[5, 6], [7, 8]])
# a3 = np.power(a1, a2)
# print(a3)
# # [[    1    64]
# #  [ 2187 65536]]
#
# # a1 ** a2 is another
# # way
# # to
# # do
# # so.
# #
# # To sum up, NumPy allows us to implement basic arithmetic operations on several arrays. If array shapes are different, sometimes it is still possible to perform operations on them, with the help of broadcasting.
#
# # rray multiplication vs matrix product
# #
# # When discussing multiplication in NumPy, we should distinguish two different operations: np.multiply() and np.matmul(). Let's take a look at the example:
#
# a1 = np.array([[1, 2], [5, 8]])
# a2 = np.array([[4, 6], [7, 3]])
#
# a3 = np.multiply(a1, a2)
# print(a3)
# print(a1 * a2)
# # [[ 4 12]
# #  [35 24]]
#
# a4 = np.matmul(a1, a2)
# print(a4)
# # [[18 12]
# #  [76 54]]
# #
# a4 = np.dot(a1, a2)
# print(a4)
#
# # As far as we know, np.multiply() is applied when we want to compute element-wise multiplication. By contrast, np.matmul() is used for obtaining the matrix product of two arrays, it is not an element-wise operation. You can also change np.matmul(a1, a2) to a1 @ a2 which is the same way to obtain the matrix product.
#
# Array transposing
#
# Finally, it is worth mentioning that NumPy provides a way for transposing a matrix using np.transpose() or the alternative array.T:
# import numpy as np
# a1 = np.array([[1, 2], [3, 4]])
# a2 = np.transpose(a1)
# print(a2)
# # [[1 3]
# #  [2 4]]
#
# a3 = a1.T
# print(a3 == a2)  # True
#
# # It can also be implemented if the number of rows and the number of columns are not equal:
#
# a1 = np.array([[1, 2], [3, 4], [5, 6]])
# a2 = a1.T
# print(a2)
# # [[1 3 5]
# #  [2 4 6]]
#
# # However, if you deal with a one-dimensional array, the same array will be returned:
#
# a1 = np.array([1, 2, 3, 4])
# a2 = np.transpose(a1)
# print(a2)
# # [1 2 3 4]

# Conclusion
#
# In this topic, we have learned:
#
#     how to use basic arithmetic procedures for two arrays;
#     the basics of broadcasting in NumPy;
#     the difference between array multiplication and matrix product;
#     how to transpose arrays.
#
# Now it is time for you to practice!

import numpy as np
#
# import numpy as np
#
# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# a = np.array([[a, b], [c, d]])
# print(a.T)
#
# import numpy as np
#
# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# e, f = int(input()), int(input())
# a1 = np.array([[a, b], [c, d]])
# a2 = np.array([e, f])
# print(a1/a2)
#
# import numpy as np
#
# a, b, c, d = 1, 4, 3, 8
# e, f = 5, 6
# a1 = np.array([[a, b], [c, d]])
# a2 = np.array([e, f])
# print(a1@a2)
# print((a1/a2).T)
# print(a1/a2)
# print(a2/a1)
#
# print(a1.T/a2)
#
# np.reshape, np ravel # spłaszczanie
# np.stack

# Theory: Boolean operations on arrays
#
# n previous topics, we have discussed some array operations. NumPy, however, has many other useful functions. We can use comparison operators such as <, > or == on an array in NumPy, and the result of these operations will be another array with Boolean data type elements. In this topic, we will cover the main aspects of these operations.
# Integer comparison
#
# You can compare elements in your array with a given integer using the following comparison operators: <, >, <=, >=, ==, !=.

# a1 = np.array([1, 2, 3, 4, 5])
# print(a1 < 4)
# # [ True  True  True False False]
#
# # As you can see, the resulting array contains True and False values. The first three elements are less than 4, so we have three True values. The last two elements are bigger, so the two False values.
# #
# # We can use these comparisons with multidimensional arrays as well. Again, each element is compared to an integer, then the True or False value is returned.
#
# a1 = np.array([[11, 22], [33, 44], [55, 66]])
# print(a1 >= 44)
# # [[False False]
# #  [False  True]
# #  [ True  True]]
#
# # Other operators are used in the same way.
# # Array comparison
# #
# # Using the operations above, we can compare two arrays as well:
#
# a1 = np.array([[12, 23], [16, 40], [15, 16]])
# a2 = np.array([[12, 73], [96, 10], [25, 16]])
# print(a1 >= a2)
# # [[ True False]
# #  [False  True]
# #  [False  True]]
#
# # Two arrays must have the same shape or they must be broadcastable for comparisons. In the example below, the second array is broadcastable to the shape of the first one. The comparison is element-wise.
#
# a1 = np.array([[12, 23], [16, 40], [15, 76]])
# a2 = np.array([[12, 73]])
# print(a1 < a2)
# # [[False  True]
# #  [False  True]
# #  [False False]]
# #
# # If arrays don't meet the mentioned requirements, a ValueError will be raised.
#
# a1 = np.array([[12, 23], [16, 40], [15, 76]])
# a2 = np.array([[12, 73, 3]])
# # print(a1 > a2)
# # Traceback (most recent call last):
# #   File "main.py", line 5, in
# #     print(a1 > a2)
# # ValueError: operands could not be broadcast together with shapes (3,2) (1,3)
#
# # The result of the operations with integers and arrays is always a Boolean array.
# # Operators and functions of comparison
# #
# # Apart from comparison operators, NumPy has functions that have the same purpose as the operators. The table below shows them in full.
# # Operators 	Functions
# # > 	np.greater()
# # < 	np.less()
# # >= 	np.greater_equal()
# # <= 	np.less_equal()
# # == 	np.equal()
# # != 	np.not_equal()
# #
# # Have a look at the code below; we use the np.greater() function instead of the operator. It is a complete equivalent of the expression a1 > a2:
#
# a1 = np.array([3, 8, 79])
# a2 = np.array([1, 0, 75])
# print(np.greater(a1, a2))
# # [ True  True  True]
#
# # Similarly, you can use an integer for comparison in the functions:
#
#
# a1 = np.array([3, 8, 79])
# print(np.less(a1, 56))
# # [ True  True  False]
# #
# # The operators are equal to the functions. You can use any of these two approaches in your programs.
# # Logic functions
# #
# # If you want to check whether any or all the values in an array fulfill a specific condition, np.any() and np.all() can be used:
#
# a1 = np.array([3, 8, 9])
# print(np.any(a1 < 4))  # True
#
# # The code above checks whether the array contains at least one element that is less than 4. The condition is fulfilled, so the True value is returned. If we change np.any() to np.all(), the True value will be obtained if all the elements in the array meet the requirement:
#
# a1 = np.array([3, 8, 9])
# print(np.all(a1 < 4))  # False
#
# # In the array, the elements "8" and "9" don't fulfill the condition, so the result of np.all() is False.
# # Selecting elements in an array
# #
# # Sometimes we may want to select elements in the given array based on some condition. There is the np.where() function for that. It accepts a Boolean array. The Boolean array defines a criterion for selecting elements. Let's look at the example:
#
# a1 = np.array([19, 92, 53, 44, 35])
# spec = np.where(a1 > 37)
# print(a1[spec])  # [92 53 44]
# #
# # We need to create an array, then a spec variable in which we specify that the elements in a1 should be greater than 37. To understand this idea better, let's compare the two following lines of the code:
#
# print(a1 > 37)  # [False  True  True  True False]
# print(np.where(a1 > 37))  # (array([1, 2, 3]),)
#
# # a > 37 returns a list of True and False values, whereas np.where() returns a tuple with the indexes of elements that are True. Finally, getting back to our example. We print the a1[spec] array; we used the spec variable to isolate values that are True.
#
# # Note that np.where() can accept a list of Boolean values right away, instead of an operation that will return a list. It works the same as in the examples above:
#
# a1 = np.array([19, 92, 53, 44, 35])
# spec = np.where([False, True, True, True, False])
# print(a1[spec])  # [92 53 44]
# #
# # We can also apply np.where() to two arrays by merging them. Take a look at the following example:
#
# num = np.array([1, 2, 3, 4, 5])
# a1 = np.array(['red', 'orange', 'green', 'yellow', 'white'])
# a2 = np.array(['black', 'brown', 'purple', 'pink', 'blue'])
# a3 = np.where(num > 2, a1, a2)
# print(a3)  # ['black' 'brown' 'green' 'yellow' 'white']

# Let's discuss how this array was obtained. The first variable, num, contains integers from 1 to 5. Then we create two arrays of the same shape, with which we will work further. After that, np.where() accepts a Boolean array with True and False values, obtained from comparing each num element with 2. For every True value it chooses a corresponding element from a1, whereas for every False value a corresponding element from a2 is chosen. That's why the resulting array is ['black' 'brown' 'green' 'yellow' 'white']: the first two elements in num were False, the next three were True.
# Conclusion
#
# In this topic, we have learned:
#
#     how to use comparison operators for arrays;
#     how to check if any or all array values fulfill a condition;
#     how to select specified elements using a condition.
#
# Now let's practice new knowledge so that it will be easier for you to use it in the future.

# import numpy as np
#
# a = int(input())
# b = int(input())
# c = int(input())
#
# ar = np.array([a, b, c])
# print(ar <= 67)

# import numpy as np
#
# a = 1##int(input())
# b = 22#int(input())
# c = 55#int(input())
# d = 66#int(input())
# ar = np.array([a, b, c, d])
# spec = np.where(ar >= 45)
# print(ar[spec])

# import numpy as np
#
# a = int(input())
# b = int(input())
# c = int(input())
# ar = np.array([a, b, c])
# print(np.all(ar > 15))
#
# import numpy as np
#
# a = 6##int(input())
# b = 7#int(input())
# c = 9#int(input())
# d = 0#int(input())
# ar1 = np.array([a, b])
# ar2 = np.array([c, d])
#
# a1 = np.array([a<c, b<d])
# print(a1)  # [92 53 44]
#
# x = np.array([a, b])
# y = np.array([c, d])
#
# print(x < y)
#
# ar1 = np.array([a, b])
# ar2 = np.array([c, d])
#
# # print(np.less(ar1, ar2))
#
# import numpy as np
# # In previous topics, we have discussed a great number of operations on NumPy arrays and matrices, but some of them are still not explained. For instance, sometimes you need to find a rank or a determinant of a matrix, to decompose a matrix, etc. In these situations, the linalg (linear algebra) submodule can help you: it offers various methods to apply linear algebra on NumPy arrays. In this topic, we are going to cover important functions of this module. As the linalg submodule is a part of NumPy, just import the library to start using the submodule.
# # Determinant of a matrix
# #
# # While working with a matrix, sometimes you need to compute its determinant. In this case, you can use the np.linalg.det() function and just pass your NumPy array to it. In the example below, the function accepts a two-dimensional array.
#
#
#
# arr = np.array([[1, 3], [2, 4]])
# print(np.linalg.det(arr))  # -2.0
# #
# # Note that the function accepts the square matrix. If the matrix is not square, an error will be raised.
# #
# # This function can also compute determinants for several matrices of the same shape. Mind the next example.
#
# arr = np.array([[[1, 2], [3, 2]],
#                 [[4, 7], [1, 8]]])
# print(np.linalg.det(arr))  # [-4. 25.]
# #
# # In this example, the array contains several subarrays with the same shape: [[1, 2], [3, 2]] and [[4, 7], [1, 8]]. If the shapes of the subarrays were different, there would be an error. The determinants are computed separately for each array. The result is the NumPy array of obtained determinants.
# # Inverse of a matrix
# #
# # In this section, we are going to discuss how to deal with an inverse of a matrix. In linalg, the np.linalg.inv() function allows us to obtain the inverse of the matrix. In the example below, we create a square matrix using np.array() and then pass it to np.linalg.inv() for computing the inverse of the matrix.
#
# arr1 = np.array([[2, 1, 3], [1, 2, 4], [2, 4, 6]])
# arr2 = np.linalg.inv(arr1)
# print(arr2)
# arrIdent = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
# arr1i = arr1 * arr2
# print(arr1i)
# # [[ 0.66666667 -1.          0.33333333]
# #  [-0.33333333 -1.          0.83333333]
# #  [ 0.          1.         -0.5       ]]
# #
# # To check if the obtained matrix is really inverse, we can use the np.dot() function: if the result is an identity matrix, it means that arr2 is an inverse of the matrix.
#
# print(np.dot(arr1, arr2))
# # [[1. 0. 0.]
# #  [0. 1. 0.]
# #  [0. 0. 1.]]
# #
# # Now we know how to work with the function, but there is one more feature we should mention. Have a look at the following snippet:
#
#
#
# # arr = np.array([[-1, 1.5], [2/3, -1]])
# # print(np.linalg.inv(arr))
# # Traceback (most recent call last):
# # ...
# # numpy.linalg.LinAlgError: Singular matrixIf it is impossible to decompose the gi
# #
# # In this example, we get an error. What happened? The matrix that we have passed to the function, has a zero determinant. If its determinant is zero, our matrix is not invertible. It is known as a singular matrix. Remember: if you try to pass any singular matrix to the function in your program, the LinAlgError will be raised.
# # Eigenvalues of an array
# #
# # In linear algebra, you can often deal with eigenvalues and eigenvectors. NumPy also allows computing eigenvalues and eigenvectors of a square matrix with a help of the np.linalg.eig() function.
#
# arr = np.array([[1, 2], [3, 4]])
# w, v = np.linalg.eig(arr)
#
# print(np.linalg.eig(arr))
# # (array([-0.37228132,  5.37228132]), array([[-0.82456484, -0.41597356],
# #        [ 0.56576746, -0.90937671]]))
#
# print(w)
# # [-0.37228132  5.37228132]
#
# print(v)
# # [[-0.82456484 -0.41597356]
# #  [ 0.56576746 -0.90937671]]
# #
# # Let's comment on the results. The function eig() returns a tuple that consists of two arrays. The first array w contains the eigenvalues. In the second array v there's a matrix, columns of which are eigenvectors, such that the column v[:,i] is the eigenvector corresponding to the eigenvalue w[i]. To ensure that the values are correct, let's check the equality of dot products: for instance, the dot product of the original array and the first eigenvector must be equal to the dot product of the first eigenvalue and the first eigenvector.
#
# print(np.dot(arr, v[:, 0]))  # [ 0.30697009 -0.21062466]
# print(np.dot(w[0], v[:, 0]))  # [ 0.30697009 -0.21062466]
# #
# # As you can see, the eigenvalues and eigenvectors we have obtained are correct.
# # Singular value decomposition
# #
# # In NumPy's linalg, there is a possibility to implement singular value decomposition which is known as SVD. We'll explain it briefly below. Let's have a look at the picture:
# #
# # In linear algebra, SVD is a procedure of representing your matrix as a dot product of three matrices. The first matrix consists of columns that are known as left-singular vectors. The second matrix is a diagonal one. Each element on its diagonal is a singular value of the original matrix. The last matrix is a matrix with right-singular vectors. Singular values and vectors are obtained with the help of eigenvalues and eigenvectors. SVD is a very useful method, especially for machine learning: if you have a huge array of data, it allows you to compress it efficiently.
# #
# # Right now, we are interested in programming rather than in theoretical approaches. In NumPy, the np.linalg.svd() function provides the procedure of SVD:
#
# arr = np.array([[1, 2, 3], [4, 5, 6], [0, 3, 2], [7, 2, 5]])
# svd_matr = np.linalg.svd(arr)
# print(svd_matr)
# # (array([[-0.2733616 , -0.27938277,  0.86441813, -0.31622777],
# #        [-0.67416854, -0.36789866, -0.10073405,  0.63245553],
# #        [-0.21105836, -0.56855365, -0.48187252, -0.63245553],
# #        [-0.65285878,  0.68069273, -0.1021412 , -0.31622777]]),
# #  array([12.81712466,  4.14874014,  0.71363215]),
# #  array([[-0.58827915, -0.45692452, -0.66719384],
# #        [ 0.72645468, -0.66105233, -0.18781218],
# #        [-0.35523405, -0.59517208,  0.72081826]]))
# #
# # The result of SVD is a tuple. The first array in the tuple is the array with left singular vectors. The second array contains three singular values. The third array has right singular vectors.
# #
# # If it is impossible to decompose the given array, the LinAlgError will be raised.
# #
# # A rank of a matrix
# #
# # A rank of a matrix is the maximum number of linearly independent rows or columns. The rows and columns are linearly independent if no column or row of a matrix can be defined as a linear combination of other columns or rows. Imagine, we have the following matrix.
# #
# # This matrix has 2 rows and 4 columns. In linear algebra, the rank of a matrix doesn't exceed the minimum number of rows/columns. In this case, it will definitely not exceed 2. There are a lot of ways for calculating ranks in linear algebra, but we will not focus on them right now.
# #
# # Let's look at automatic ways to compute the rank of a matrix in NumPy. The np.linalg.matrix_rank() function helps to do it:
#
# arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# rank = np.linalg.matrix_rank(arr)
# print(rank)  # 2
# #
# # The function can also compute ranks for several matrices of the same shape:
#
# arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# rank = np.linalg.matrix_rank(arr)
# print(rank)  # [2 2]
# #
# # The result is a NumPy array with ranks for each submatrix: [[1, 2], [3, 4]] and [[5, 6], [7, 8]].
# # Conclusion
# #
# # So far, we have had a quick look at the submodule linalg in NumPy. Now you know:
# #
# #     how to compute the determinant of a square array with the help of np.linalg.det();
# #     how to find an inverse of a matrix using np.linalg.inv();
# #     how to use np.linalg.eig() for computing eigenvectors and eigenvalues;
# #     how to get SVD of a matrix with the help of np.linalg.svd();
# #     how to find the rank of a matrix using np.linalg.matrix_rank().
# #
# # Of course, we couldn't cover all the functions that exist in this submodule. If you are eager to find out more information, read the following documentation.
#
# import numpy as np
#
# a = 1#int(input())
# b = 2#int(input())
# c = 3#int(input())
# d = 4#int(input())
#
# arr = np.array([[a, b], [c, d]])
# rank = np.linalg.matrix_rank(arr)
# print(rank)
#
#
# # put your code here
# print(a < 10 or a > 250)
#
# i = 0
# while i < 5:
#     print('*')
#     if i % 2 == 0:
#         print('**')
#     if i > 2:
#         print('***')
#     i = i + 1
# # Carl asks you to count the sum of the first k natural numbers. Read k from the input, then add up numbers from 1 to k and print your answer.
# k = int(input())
# i = 1
# sum = 0
# while i <= k:
#     #sum += int(input())
#     sum += i
#     i += 1
# print(sum)
# # Kudos! Carl gives credit to you and suggests another solution: you can replace your loop with the formula (k * (k + 1)) // 2.
#
# animals = [camel, lion, deer, goose, bat, rabbit]
#
# # write your code here
# while True:
#     n = input('Please enter the number of the habitat you would like to view:')
#
#     if (n == 'exit'):
#         break
#     n = int(n)
#
#     if n == 0:
#         print(camel)
#     elif n == 1:
#         print(lion)
#     elif n == 2:
#         print(deer)
#     elif n == 3:
#         print(goose)
#     elif n == 4:
#         print(bat)
#     elif n == 5:
#         print(rabbit)
#
# print("See you later!")
