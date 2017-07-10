##########################
# List comprehension 101 #
##########################

numbers = [1, 4, 10, 3, 30, 2, 66, 20, 30]

words = ['jacqueline',
        'Robert',
        'tulipes en fleurs',
        'rue des chemins',
        'palmiers de Dubai',
        'Paris la nuit',
        'bracelet',
        'jantes',
        'bois foncé']

# multiply per 2 all numbers
double_numbres = [n * 2 for n in numbers]
# print(double_numbres)

# convert all numbers into string
numbers_to_string = [str(n) for n in numbers]
# print(numbers_to_string)

# keep words that does not contain blank spaces.
words_without_blank = [w for w in words if not " " in w]
#print(words_without_blank)

# create a new list with even numbers only (nombres pairs).
# Use a conditional structure!
even_numbers = [n for n in numbers if n % 2 == 0]
# print(even_numbers)

# create a new list with numbers and words as tuples.
# should look like: [('jacqueline', 1), ('robert', 4)]
new_list = [(words[i], numbers[i]) for i in range(0, len(numbers))]
#print(new_list)

# A good resource: https://hackernoon.com/list-comprehension-in-python-8895a785550b
