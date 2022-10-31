password = input()

uppercase_letters_count = sum(1 for character in password if character.isupper())
lowercase_letters_count = sum(1 for character in password if character.islower())
digits_count = sum(1 for character in password if character.isdigit())

if len(password) >= 8 and len(password) <= 12 and password.isalnum() and (lowercase_letters_count >= 3 and uppercase_letters_count >= 2 and digits_count >= 1):
  print('Valid')
else:
  print('Invalid')
