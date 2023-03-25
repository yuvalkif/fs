Genetic Algorithm-based Feature Selection
This project implements a genetic algorithm for feature selection. The goal is to find the most relevant and informative features in a dataset, while minimizing redundancy and irrelevant features.

Requirements
Python 3.7.6
pandas
numpy
pyitlib
tkinter
Usage
To run the genetic algorithm, use the genetic_feature_selection file. Here are the parameters that can be adjusted:

estimator: an instance of an estimating class for use as fitness function (e.g. mutual information)
num_of_generations: the number of maximum generations
num_of_chromosomes: number of chromosomes to be used, which is the size of the population
num_best_chromosomes: number of best chromosomes to be kept for the next generation
num_rand_chromosomes: number of random chromosomes from current population to be kept for next population
num_crossover_children: number of chromosomes to be made by crossover
features_names: list of the names of the features
operator_probability: the chance for mutation to occur
class_vector: pandas series of the class column
The evolve(data_vector) function can be used to run the algorithm.

To calculate the fitness score for a set of features, use the fitness_function file. Here are the parameters that can be adjusted:

data_vector: pandas dataframe of the features columns
class_vector: pandas series of the class column
explore_rate: a float between 0-1, it's the chance to choose random feature instead of the dominant one
The calculate_score(features_names) function can be used to calculate the fitness score.

The gui file can be used to run a graphical user interface. Here are the parameters that can be adjusted:

Number of generations: number of iterations of the algorithm
Total number of chromosomes: number of feature sets in each iteration
Number of best chromosomes: number of top ranked feature sets which will get copied to the next iteration
Number of random chromosomes: number of random feature sets which will get copied to the next iteration
Number of crossover chromosomes: number of chromosomes to be made by crossover
Mutation chance: the chance for each gene to flip value
Input Dataset
The input dataset should be a pandas dataframe with the following requirements(you can use wdbc dataset attached to this repo):

Class column is the last column
NA eliminating
Categorical to numeric (ints)
(Optional) Discretize to bins
(Optional) Normalize values
