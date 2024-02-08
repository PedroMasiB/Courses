from time_calculator import add_time


def char_finder(character, intput_string):
  for i in intput_string:
    if i == character:
      return True
  return False


try:
  start_input = input(
    "Insert the starting time using the 12-hour format (hh:mm AM/PM): ")
  #start_input = "12:30 Pm"
  #duration_input = "24:5"
  aux = start_input.split(' ')
  while not char_finder(':', aux[0]):
    print('Error: The starting time format introduced is incorrect. Try again')
    start_input = input('Insert the starting time: ')
    aux = start_input.split(' ')

  start_list = aux[0].split(':') + [aux[1].upper()]

  while not start_list[0].isdigit():
    print("Error: the starting hour must be natural number")
    start_list[0] = input('Insert the hour again: ')
  while not start_list[1].isdigit() or int(start_list[1]) >= 60:
    print("Error: the starting minutes must be a natural number lower than 60")
    start_list[1] = input('Insert the minutes again: ')
  while not start_list[2] == 'PM' and not start_list[2] == "AM":
    print("Error: you must specify if it's PM or AM")
    option = input("1: PM\t2: AM\n")
    if option == '1':
      start_list[2] = "PM"
    elif option == '2':
      start_list[2] == 'AM'

  duration_input = input(
    "Insert the duration time using the format 'hours:minutes': ")
  while not char_finder(':', duration_input):
    print('Error: The duration time format introduced is incorrect. Try again')
    duration_input = input('Insert the starting time: ')
  duration_list = duration_input.split(':')
  while not duration_list[0].isdigit():
    print("Error: the duration hour must be natural number")
    duration_list[0] = input('Insert the hour again: ')
  while not duration_list[1].isdigit() or int(duration_list[1]) >= 60:
    print(
      "Error: the duration minutes must be a natural number and lower than 60")
    duration_list[1] = input('Insert the minutes again: ')

  start_input = ":".join(start_list)
  duration_input = ":".join(duration_list)

except:
  print('Error')

result = add_time(start_input, duration_input, 'Monday')
print(result)
