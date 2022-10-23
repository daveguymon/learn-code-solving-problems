distance = int(input())

amount_of_far = "far, " * distance

trimmed_amount_of_far = amount_of_far.strip(', ')

introduction = "A long time ago in a galaxy " + trimmed_amount_of_far + " away..."

print(introduction)