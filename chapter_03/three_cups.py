swaps = input()
ball_position = 1

for swap_type in swaps:
  if swap_type == 'A' and ball_position == 1:
    ball_position = 2
  elif swap_type == 'A' and ball_position == 2:
    ball_position = 1
  elif swap_type == 'B' and ball_position == 2:
    ball_position = 3
  elif swap_type == 'B' and ball_position == 3:
    ball_position = 2
  elif swap_type == 'C' and ball_position == 1:
    ball_position = 3
  elif swap_type == 'C' and ball_position == 3:
    ball_position = 1

print(ball_position)
