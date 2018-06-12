from die import Die
import pygal
#   Create two Dies with six sides
die_1 = Die()
die_2 = Die(10)
#   Make some rolls, and store the results in a list
results = []
for roll_num in range(500000) :
  result = die_1.roll() + die_2.roll()
  results.append(result)
#   Analyze the results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1) :
  frequency = results.count(value)
  frequencies.append(frequency)
#   Visualize the results
hist = pygal.Bar()
hist.title = "Results of rolling a D6 and a D10 for 500000 times"
hist.x_labels = [
  '2', '3', '4', '5', '6', '7',
  '8', '9', '10', '11', '12', '13', '14', '15', '16']
hist.x_title = "Result"
hist.y_title = "Frequency of result"
hist.add("D6 + D6", frequencies)
hist.render_to_file('die_visual.svg')
print(frequencies)
