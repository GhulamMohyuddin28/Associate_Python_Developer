# Create a list of strings: mutants
mutants = ['charles xavier', 
            'bobby drake', 
            'kurt wagner', 
            'max eisenhardt', 
            'kitty pryde']

# Create a list of tuples: mutant_list
mutant_list = list(enumerate((mutants)))

# Print the list of tuples
print(mutant_list)

# Unpack and print the tuple pairs
for index1 in enumerate(mutants):
    print(index1, mutants)

# Change the start index
for index2 in enumerate(mutants, start=1):
    print(index2, mutants)
