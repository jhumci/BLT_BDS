
def solution_1_2_1_5():
    # importing the math library
    import math

    # here the user can define the input
    initial_population_size = 100
    carrying_capacity = 200
    growth_rate = 0.1
    t_in_h = 10


    # here the calculation is made
    final_population_size = carrying_capacity / (1+((carrying_capacity - initial_population_size)/initial_population_size) * math.exp(- growth_rate*t_in_h))

    # here, we print out the results
    print("Started simulation with the following parameters: \n initial population size: {} \n carrying capacity: {} \n growth rate: {}  \n The population after {} time steps is {}".format(initial_population_size, carrying_capacity, growth_rate, t_in_h, final_population_size))


def solution_1_2_2_5():
    dna_sequence = ["A", "U", "C", "C", "G","A", "G", "C", "U", "E", "G","A", "G", "C", "U", "E", "Z", "G","A", "G", "C", "U","U", "G"]
    print("Length of original sequence is {}".format(len(dna_sequence)))

    # Remove only removes the first occurrence of an item
    dna_sequence.remove("E")
    dna_sequence.remove("E")
    dna_sequence.remove("Z")

    print("Length of cleaned sequence is {}".format(len(dna_sequence)))

    codon_list = []

    for starting_point in range(0,len(dna_sequence), 3):

        print(dna_sequence[starting_point:starting_point+3])
        codon_list.append("".join(dna_sequence[starting_point:starting_point+3]))

    print(codon_list)


def solution_1_2_3_4():
    users_wanting_to_enter = ["Adam","Eve","Lilith","Abel","Cain"]
    users_with_clearance = ["Adam","Eve"]

    for user in users_wanting_to_enter:
        if user in users_with_clearance:
            print("Hi, {}! Please enter.".format(user))
        else:
            print("Hi, {}! Please go to the supervisor to register.".format(user))

def solution_1_2_4_5():
    import math

    t = 0
    epsilon = 1

    # here the user can define the input
    initial_population_size = 1
    population_size = 1
    carrying_capacity = 200
    growth_rate = 0.1

    results = []

    while population_size + epsilon  < carrying_capacity:

        last_population_size = population_size

        population_size = carrying_capacity / (1+((carrying_capacity - initial_population_size)/initial_population_size) * math.exp(- growth_rate*t))

        growth = population_size - last_population_size

        print("The population after {0} time steps is {1:.2f}".format(t, population_size))

        t = t + 1  

        new_result = {"Time step" : t, "Population size" : population_size, "Growth" : growth}
        results.append(new_result)

def calculate_logistic_growth(carrying_capacity,initial_population_size,growth_rate,t):

  """returns the population size at a given time t"""
  population_size = carrying_capacity / (1+((carrying_capacity - initial_population_size)/initial_population_size) **(- growth_rate*t))
  return (population_size)

def carry_out_simulation(epsilon, carrying_capacity, initial_population_size, growth_rate):
  """runs the simulation and returns a list with the results"""
  t = 0
  results = []
  population_size = initial_population_size

  print("Started simulation with the following parameters: \n initial population size: {} \n carrying capacity: {} \n growth rate: {}".format(initial_population_size, carrying_capacity, growth_rate))

  while population_size + epsilon  < carrying_capacity:

    last_population_size = population_size

    population_size = calculate_logistic_growth(carrying_capacity,initial_population_size,growth_rate,t)

    growth = population_size - last_population_size

    print("The population after {0} time steps is {1:.2f}".format(t, population_size))

    t = t + 1  

    new_result = {"Time step" : t, "Population size" : population_size, "Growth" : growth}
    results.append(new_result)

  return results 

def find_highest_growth(results):
  """returns the time step with the highest growth """

  last_growth = 0

  for data_point in results:
    growth = data_point["Growth"] 
    is_current_growth_lower_than_before = (last_growth > growth)

    if is_current_growth_lower_than_before:
      print("Found maximum growth of {0:.2f} at {1}!".format(last_data_point["Growth"],last_data_point["Time step"] ))
      break
    last_growth = data_point["Growth"] 
    last_data_point = data_point

from itertools import combinations

def full_comparison(sequence_1, sequence_2, n, threshold):
  """Returns the percentage of subsequences with length n, that are found in sequence_1"""
  comparison_counter = 0
  matches_counter = 0

  # Create the k-mers from sequence 1
  for index in range(0,len(sequence_1) - n + 1):
    search_sequence = sequence_1[index:index+n]
    
    # Create them to the other sequence
    for index in range(0,len(sequence_2) - n + 1):
        comparison_counter = comparison_counter + 1

        # Make a comparison between the m-mers
        similarity_value = compare_sequences(search_sequence,sequence_2[index:index+n])
        
        # Only count the match, if the similarity is higher than the threshold
        if similarity_value >= threshold:
          matches_counter = matches_counter + 1
          #print("Match counter: {}".format(matches_counter))

  print("Made {} comparisons.".format(comparison_counter))
  print("Found {} good matches.".format(matches_counter))

  return matches_counter/(len(sequence_1)-n+1)

def compare_sequences(short_sequence1,short_sequence2):
  """Returns the percentage of matching nucleotides """
  # set a counter for the matches
  matches = 0
  
  # go through the sequences using an index
  for i in range(0,len(short_sequence1)):

    # if they are the same at an index position
    if short_sequence1[i] == short_sequence2[i]:

      #count the match
      matches = matches + 1
      
  # as we want to find the relative number of matches, we normalize them using the sequence length
  return matches/len(short_sequence1)

def solution_1_2_6_3(nukleotid_sequences, n, threshold):

  temp = combinations(nukleotid_sequences, 2)
  for i in list(temp):
  #print (i[0]["Sample Name"] + " vs " + i[1]["Sample Name"])
      match = full_comparison(i[0]["Sequence"], i[1]["Sequence"], n, threshold)
      print("Match for {} and {} in percent: {}".format(i[0]["Sample Name"], i[1]["Sample Name"], match))