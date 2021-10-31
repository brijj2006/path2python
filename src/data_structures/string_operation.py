import textwrap


def print_numbers():
    n = 9
    answer = ''

    for i in range(1, n + 1):
        answer = answer + str(i)

    print(answer)


print_numbers()

# 123456789


'''Task
You are given a string .
Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.'''


def check_string():
    str = "#$%@^&*kjnk svskjnbui h 4oi3hheuh /dfh uidshvhdsuihv suihc 0hrem89m4c02mw4xo;,wh fwhncoishmxlxfkjsahnxu83v 08 n8OHOIHIOMOICWHOFCMHEOFMCOEJMC0J09C 03J J3L;JMFC3JM3JC3'JIOO9MMJ099U N090N9 OOHOLNHNLLKNLKNKNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333000000000000000000000000000000000000000000000000000000000000000000000000000"

    print(True if any(k in "0123456789" or k.lower() in "abcdefghijklmnopqrstuvwxyz" for k in str) else False)
    print(True if any(k.lower() in "abcdefghijklmnopqrstuvwxyz" for k in str) else False)
    print(True if any(k in "0123456789" for k in str) else False)
    print(True if any(k in "abcdefghijklmnopqrstuvwxyz" for k in str) else False)
    print(True if any(k in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" for k in str) else False)


check_string()

# True
# True
# True
# True
# True

'''You are given a string  and width .
Your task is to wrap the string into a paragraph of width .

Function Description

Complete the wrap function in the editor below.

wrap has the following parameters:

string string: a long string
int max_width: the width to wrap to
Returns

string: a single string with newline characters where the breaks should be'''


def wrap(string, max_width):
    i = 0
    j = 0
    text = ''
    final_text = ''
    for char in string:
        text = text + char
        i = i + 1
        j = j + 1
        if i == max_width:
            i = 0
            # print(text)
            final_text = final_text + text + '\n'
            text = ''
        if j == len(string):
            final_text = final_text + text
            # print(text)
    return final_text


text = wrap('ABCDEFGHIJKLIMNOQRSTUVWXYZ', 4)
print(text)


# ABCD
# EFGH
# IJKL
# IMNO
# QRST
# UVWX
# YZ

# Second Solution
def wrap_text():
    text = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ'
    width = 4
    print(textwrap.fill(text, width))


wrap_text()


def join_string():
    line = 'this is a string'
    line = line.split(" ")
    line = '-'.join(line)
    print(line)


# this-is-a-string
join_string()

'''
Sample Input
STDIN           Function
-----           --------
abracadabra     s = 'abracadabra'
5 k             position = 5, character = 'k'

Sample Output
abrackdabra
'''


def mutate_string(string, position, character):
    string = list(string)
    string[position] = character
    string = ''.join(string)
    print(string)


# abrackdabra
mutate_string('abracadabra', 5, 'k')

'''the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. 
String traversal will take place from left to right, not from right to left

Sample Input

ABCDCDC
CDC

Sample Output

2
'''


def count_substring(string, sub_string):
    count = 0
    for char in range(len(string) - len(sub_string) + 1):
        if string[char:char + len(sub_string)] == sub_string:
            count = count + 1

    print('substring occurance in string is {} times'.format(count))


count_substring('ABCDCDC', 'CDC')
