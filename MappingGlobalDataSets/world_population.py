import json
import pygal
from countries_codes import get_country_code
#   Load the data into a list
filename = "population_data.json"
with open(filename) as f :
  pop_data = json.load(f)
#   Buidl a dictionary of population data
cc_populations = {}
#   Print the 2010 population for each country
for pop_dict in pop_data :
  if pop_dict["Year"] =="2010" :
    country_name = pop_dict["Country Name"]
    population = int(float(pop_dict["Value"]))
    code = get_country_code(country_name)
    if code :
      cc_populations[code] = population
    #   print(code + ": " + str(population))
    # else :
    #   print("Error - " + country_name)
    # #print(country_name + ": " + str(population))
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items() :
  if pop < 10000000 :
    cc_pops_1[cc] = pop
  elif pop < 1000000000 :
    cc_pops_2[cc] = pop
  else :
    cc_pops_3[cc] = pop
#   See how many countries are in each level.
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))
wm = pygal.maps.world.World()
wm.title = "World Population in 2010, by County"
wm.add("0-10m", cc_pops_1)
wm.add("10m-10n", cc_pops_2)
wm.add(">10b", cc_pops_3)
# wm.add("2010", cc_populations)
wm.render_to_file("world_population.svg")
