Feature Selection by Genetic Algorithm based on Filter Fitness Function
This project implements a genetic algorithm-based feature selection method using a filter fitness function. The algorithm is designed to select a subset of relevant features from a given dataset.

Requirements
This project requires Python 3.7.6 and the following libraries:

pandas
numpy
pyitlib
tkinter
Files
This project includes the following files:

genetic_feature_selection: contains the implementation of the genetic algorithm-based feature selection method.
fitness_function: contains the implementation of the filter fitness function.
gui: contains the implementation of the graphical user interface.
Usage
Genetic Feature Selection
To use the genetic algorithm-based feature selection method, import the genetic_feature_selection module and create an instance of the GeneticSelector class.

python
Copy code
from genetic_feature_selection import GeneticSelector

estimator = # an instance of an estimating class for use as fitness function e.g Mutual Information
num_of_generations = # the number of maximum generations
num_of_chromosomes = # number of chromosomes to be used, which is the size of the population
num_best_chromosomes = # number of best chromosomes to be kept for the next generation
num_rand_chromosomes = # number of random chromosomes from current population to be kept for next population
num_crossover_children = # number of chromosomes to be made by crossover
features_names = # list of the names of the features
operator_probability = # the chance for mutation to occur 
class_vector = # pandas series of the class column 

selector = GeneticSelector(estimator, num_of_generations, num_of_chromosomes,  num_best_chromosomes, num_rand_chromosomes,
                           num_crossover_children, features_names, operator_probability, class_vector)
data_vector = # pandas dataframe of the features columns 
best_features = selector.evolve(data_vector)
Fitness Function
To use the filter fitness function, import the fitness_function module and create an instance of the RRIGA_Fitness_Function class.

python
Copy code
from fitness_function import RRIGA_Fitness_Function

features_vectors = # pandas dataframe of the features columns
class_vector = # pandas series of the class column
explore_rate = # a float between 0-1, its the chance to choose random feature instead of the dominant one

function = RRIGA_Fitness_Function(features_vectors, class_vector, explore_rate)
features_names = # list of the names of the features to calculate the fitness score on
score = function.calculate_score(features_names)
GUI
To use the graphical user interface, run the main() function in the gui module.

python
Copy code
from gui import main

main()
Input Dataset
The input dataset should be a pandas dataframe with the following requirements:

The class column is the last column.
NA values should be eliminated.
Categorical features should be converted to numeric (ints).
(Optional) Features can be discretized into bins.
(Optional) Feature values can be normalized.
GUI Usage
To use the graphical user interface:

Use "browse" to select a clean dataset as specified above.
Enter the following parameters:
Number of generations: number of iterations of the algorithm.
Total number of chromosomes: number of feature sets in each iteration.
Number of best chromosomes: number of top ranked feature sets which will get copied to the next iteration.
Number of random chromosomes: number of random feature sets which will get copied to the next iteration