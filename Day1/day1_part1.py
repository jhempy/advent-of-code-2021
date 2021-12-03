f = open("input.txt", "r")
previous = 0
increases = 0
message = '--'
for x in f:
  depth = int(x)
  if (previous > 0 and depth > previous):
    increases = increases + 1
    message = '(increased)'
  previous = depth
  print(depth, message, increases)
  message = '--'
f.close()