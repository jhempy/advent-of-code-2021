f = open("input.txt", "r")
depths = []
last_sum = 0
increases = 0
message = '--'

for x in f:
  depth = int(x)
  depths.append(depth)
f.close()

i = 2
while i < len(depths):
  current_sum = depths[i-2] + depths[i-1] + depths[i]
  if (last_sum > 0 and current_sum > last_sum):
    increases = increases + 1
    message = '(increased)'
  last_sum = current_sum
  print(depths[i-2], depths[i-1], depths[i], current_sum, message, increases)
  message = '--'
  i = i + 1