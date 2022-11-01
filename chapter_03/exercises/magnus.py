some_word = input()
honi_blocks = []

for character in some_word:
  if (not honi_blocks or honi_blocks[-1] == 'I') and character == 'H':
    honi_blocks.append(character)
  elif honi_blocks and honi_blocks[-1] == 'H' and character == 'O':
    honi_blocks.append(character)
  elif honi_blocks and honi_blocks[-1] == 'O' and character == 'N':
    honi_blocks.append(character)
  elif honi_blocks and honi_blocks[-1] == 'N' and character == 'I':
    honi_blocks.append(character)

honi_string = ''.join(honi_blocks)
print(honi_string.count('HONI'))
