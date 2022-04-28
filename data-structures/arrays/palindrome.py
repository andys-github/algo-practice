# ----------------------------------------------
# Problem Statement
# ----------------------------------------------
# Design an algorithm that checks if a given
# string is palindrome (a string that reads
# same backward and forward)
#
# For example: radar and madam are palindrome,
# whereas elephant and school are not
# ----------------------------------------------

def is_palindrome(string):
  start_index = 0
  end_index = len(string) - 1
  loop_counter = 0
  palindrome_flag = True

  while start_index < end_index:
    loop_counter += 1
    if string[start_index] != string[end_index]:
      palindrome_flag = False
      break
    start_index += 1
    end_index -= 1

  print('Loop: ', loop_counter)
  return palindrome_flag


input_str = 'madam'
print('Input string: ', input_str)
print(f'Is "{input_str}" a palindrome? {is_palindrome(input_str)}')

input_str2 = 'madame'
print('Input string: ', input_str2)
print(f'Is "{input_str2}" a palindrome? {is_palindrome(input_str2)}')
