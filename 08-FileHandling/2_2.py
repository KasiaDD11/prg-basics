###
# Writes Seven Wonders of the World to a file
#
seven_wonders = [
   "Great Wall of China",
   "Petra",
   "Christ the Redeemer",
   "Machu Picchu",
   "Chichen Itza",
   "Roman Colosseum",
   "Taj Mahal"
]

# Name of the file to write to
file_name = 'seven_wonders.txt'

# Sort data alphabetically
seven_wonders.sort()

with open(file_name, 'w') as file:
      i=1
      for item in seven_wonders:
            file.write(f'{i}. WONDER OF THE WORLD: {item}\n')
            i+=1


            
        