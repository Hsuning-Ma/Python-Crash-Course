from die import Die
#   Create a Die with six sides
die = Die()
#   Make some rolls, and store the results in a list
results = []
for roll_num in range(100) :
  result = die.roll()
  results.append(result)
print(results)
