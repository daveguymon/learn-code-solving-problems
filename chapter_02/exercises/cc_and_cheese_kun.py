units = int(input())
cheesiness = int(input())

satisfaction_level = ''

if units == 3 and cheesiness >= 95:
  satisfaction_level = 'absolutely'
elif units == 1 and cheesiness <= 50:
  satisfaction_level = 'fairly'
else:
  satisfaction_level = 'very'

print('C.C. is ' + satisfaction_level + ' satisfied with her pizza.')
