apple_threes = int(input())
apple_twos = int(input())
apple_ones = int(input())

banana_threes = int(input())
banana_twos = int(input())
banana_ones = int(input())

apple_total = apple_threes * 3 + apple_twos * 2 + apple_ones
banana_total = banana_threes * 3 + banana_twos * 2 + banana_ones

if apple_total > banana_total:
  print('A')
elif apple_total < banana_total:
  print('B')
else:
  print('T')
