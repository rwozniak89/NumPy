# import pandas as pd
#
# ages_list = [21, 20, 25, 22]
# names_list = ['Anna', 'Bob', 'Maria', 'Jack']
# print(ages_list)
# print(names_list)
# ages_series = pd.Series(ages_list)
# print(ages_series)
# ages_series = pd.Series(ages_list, index=names_list, name='Age')
# print(ages_series)
#
# # Anna     21
# # Bob      20
# # Maria    25
# # Jack     22
# # Name: Age, dtype: int64
#
#
# student_ages_dict = {'Anna': 21, 'Bob': 20, 'Maria': 25, 'Jack': 22}
#
# ages_series = pd.Series(student_ages_dict, name='Ages')
# print(ages_series)
#
# # Anna     21
# # Bob      20
# # Maria    25
# # Jack     22
# # Name: Ages, dtype: int64
#
# # ages_series.index = ['A', 'B', 'M', 'J']
# # print(ages_series)
#
# # A    21
# # B    20
# # M    25
# # J    22
# # Name: Ages, dtype: int64
#
# #Modifying a Series object
#
# ages_series['Jack'] = 23
# print(ages_series)
#
# # Anna     21
# # Bob      20
# # Maria    25
# # Jack     23
# # Name: Ages, dtype: int64
#
# new_ages_series = ages_series.drop(index='Maria')
# print(new_ages_series)
#
# # Anna    21
# # Bob     20
# # Jack    23
# # Name: Ages, dtype: int64
#
# print(ages_series)
#
# # Anna     21
# # Bob      20
# # Maria    25
# # Jack     23
# # Name: Ages, dtype: int64
#
# ages_series.drop(index='Maria', inplace=True)
# print(ages_series)
#
# ages_series['Maria'] = 25
# print(ages_series)
#
# # Anna     21
# # Bob      20
# # Jack     23
# # Maria    25
# # Name: Ages, dtype: int64
#
# algebra_dict = {'Bob': 90, 'Anna': 50, 'Maria': 100, 'Jack': 90}
#
# algebra_series = pd.Series(algebra_dict, name='algebra')
# print(algebra_series)
#
# average = 0.5*(algebra_series + ages_series)
# print(average)
#
# test = pd.Series(['a', 'b', 1])
# print(test)
#
# def add_records(olympics):
#     olympics[2021] = 'Tokyo'
#     olympics[2024] = 'Paris'
#     olympics[2028] = 'Angeles'
#
# add_records(test)
# print(test)
#
# foods = ['bagel', 'pasta', 'rice']
# calories = [310, 110, 140]
# def create_series(foods, calories):
#    return pd.Series(calories, index=foods, name='Calorie content')
#
# print(create_series(foods, calories))
#
# #DataFrame
# import pandas as pd
#
# students = pd.read_csv('students.csv')
# print(students)
#
# students = pd.read_csv('students.csv', usecols=[0,2],header=0, names=['name', 'age'])
# print(students)
#
# students = pd.read_csv('students.csv', usecols=[0,2],header=0, names=['name', 'age'], index_col=0 )
# print(students)
#
# students_list = [['Anna', 'Smith', 21],
#                  ['Bob', 'Jones', 20],
#                  ['Maria', 'Williams', 25],
#                  ['Jack', 'Brown', 22]]
#
# students = pd.DataFrame(students_list, columns = ['First name', 'Family Name', 'Age'])
# print(students)
#
# students_number = [100, 200, 300, 400]
# students = pd.DataFrame(students_list,
#                         columns = ['First name', 'Family Name', 'Age'],
#                         index = students_number)
# print(students)
#
# # This is a nested dictionary representing the students table
# students_dict = {'First name': {100: 'Anna',
#                                 200: 'Bob',
#                                 300: 'Maria',
#                                 400: 'Jack'},
#
#                  'Family name': {100: 'Smith',
#                                  200: 'Jones',
#                                  300: 'Williams',
#                                  400: 'Brown'},
#                  'Age': {100: 21,
#                          200: 20,
#                          300: 25,
#                          400: 22}}
#
# students = pd.DataFrame(students_dict)
# print(students)
#
# print(students.shape)
# # (4, 3)
#
# print(students.head(2))
# print(students['Age'])
# print(students[['First name', 'Age']])
# print(students[['Age']])
# print(students['Age'])
#
#
# print(students[['Age']].values)
# print(students['Age'].values)
#
# students.to_csv('student_names.csv', sep='\t', columns=['First name', 'Family name'], index=False)
#
# print(students.shape[0])

#Theory: Introduction to classification

