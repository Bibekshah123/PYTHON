# fin = open(r"lab10/cities.txt.py", "r")
# line = fin.readline()
# maxpop = 0
# maxcity =""
# while line != "":
#     fields = line.split(';')
#     city = fields[0]
#     country = fields[1]
#     population = (fields[2])
#     if (country.strip() == "UK"):
#         if (int (population.strip()) > maxpop):
#             maxpop = int(population.strip())
#             maxcity = city
#         line = fin.readline()

# if maxpop > 0:
#     print ("No cities in input file. \n")
# else:
#     print (f"Largest city in UK is {maxcity}.") 
