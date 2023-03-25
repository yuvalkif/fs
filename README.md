## **Genetic Algorithm Feature Selection with Interactions (Filter Approach)**
This project implements an experimental approach for Genetic Algorithm Feature Selection that considers interactions using a filter approach.

Requirements
Python 3.7.6
pandas
numpy
pyitlib
tkinter
Usage

Open a command prompt or terminal window and navigate to the directory where the files are stored.

Run the gui.py file by typing python gui.py and pressing Enter.

Click on the "Browse" button to select a dataset. The dataset must be in a CSV format with the class column as the last column, and must be cleaned (i.e., with no missing values, you can use the wdbc dataset attached).

Enter the number of generations, total number of chromosomes, number of best chromosomes, number of random chromosomes, number of crossover chromosomes, and mutation chance. Make sure that the total number of chromosomes is greater than the number of best chromosomes, the number of random chromosomes, and the number of crossover chromosomes.

Click on the "Start" button to start the genetic algorithm. The program will run for the specified number of generations, and the best feature sets will be displayed in the table on the right side of the GUI.

Click on the "Export" button to save the best feature sets to a CSV file.

You can also select a feature set from the table and click on the "Visualize" button to visualize the data using only the selected features
