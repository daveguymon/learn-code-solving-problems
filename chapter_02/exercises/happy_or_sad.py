user_string = input()

happy_emoticon = ':-)'
sad_emoticon = ':-('

happy_frequency = user_string.count(happy_emoticon)
sad_frequency = user_string.count(sad_emoticon)

if happy_frequency == 0 and sad_frequency == 0:
  print('none')
else:
  net_mood_value = happy_frequency + (sad_frequency * -1)

  if net_mood_value > 0:
    print('happy')
  elif net_mood_value < 0:
    print('sad')
  else:
    print('unsure')
