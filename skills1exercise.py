# Things you should be able to do.

the_number_list = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
the_word_list = [ "What", "about", "the", "Spam", "sausage", "spam", "spam", "bacon", "spam", "tomato", "and", "spam"]

# Write a function that takes a list of numbers and returns a new list with only the odd numbers.
def all_odd(number_list):

    odds = []

    for number in number_list:
       
        if number % 2 != 0:
          odds.append(number)

    return odds
 

#can just put print and then call function after =, but if want to save value in a variable, call function this way.
odd_numbers = all_odd(the_number_list)
print odd_numbers


# Write a function that takes a list of numbers and returns a new list with only the even numbers.
def all_even(number_list):
    
    evens = []

    for number in number_list:
        if number % 2 == 0:
            evens.append(number)

    return evens
even_numbers_list = all_even(the_number_list)
print even_numbers_list


# Write a function that takes a list of strings and a new list with all strings of length 4 or greater.
def long_words(word_list):

    longs = []

    for word in word_list:
        if len(word) > 4:
            longs.append(word)
    return longs

long_words_list = long_words(the_word_list)
print long_words_list


# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(number_list):

    number_list.sort()

    return number_list[0]

print smallest(the_number_list)


# Write a function that finds the largest element in a list of integers and returns it.
def largest(number_list):
    
    number_list.sort()

    return number_list[-1]

print largest(the_number_list)

# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(number_list):

    halvesies_list = []

    for number in number_list:
        halved = float(number) / 2
        halvesies_list.append(halved)
    return halvesies_list

print halvesies(the_number_list)

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):
    
    lengths_of_words = []

    for words in word_list:
        
        length = len(words)
        lengths_of_words.append(length)
    return lengths_of_words

print word_lengths(the_word_list)


# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(number_list):

    for nums in number_list[0:]:
        
        sum(nums)
    return number_list
    


    # for nums in number_list[0:]:
    #     sum (float(nums))
    # return number_list

print sum_numbers(the_number_list)

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(number_list):
    return 0

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(word_list):
    return ""

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(number_list):
    return 0
