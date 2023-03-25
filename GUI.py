import tkinter as tk
import pandas as pd
from tkinter import filedialog as fd
from algorithms import rrigaFitness
from algorithms import genetic_feature_selection as genetic_selector


class Browse(tk.Frame):


    def __init__(self, master, initialdir='', filetypes=()):
        super().__init__(master)
        self.dataset_path = tk.StringVar()
        self.num_of_generations = tk.StringVar()
        self.num_of_chromosomes = tk.StringVar()
        self.num_best_chromosomes = tk.StringVar()
        self.num_rand_chromosomes = tk.StringVar()
        self.num_crossover_children = tk.StringVar()
        self.operator_probability = tk.StringVar()
        self._initaldir = initialdir
        self._filetypes = filetypes
        self._create_widgets()
        self._display_widgets()

    def _create_widgets(self):
        self.entry_dataset_path = tk.Entry(self, textvariable=self.dataset_path, font=("bold", 10))
        self.num_of_generations = tk.Entry(self, textvariable=self.num_of_generations, font=("bold", 10))
        self.num_of_chromosomes = tk.Entry(self, textvariable=self.num_of_chromosomes, font=("bold", 10))
        self.num_best_chromosomes = tk.Entry(self, textvariable=self.num_best_chromosomes, font=("bold", 10))
        self.num_rand_chromosomes = tk.Entry(self, textvariable=self.num_rand_chromosomes, font=("bold", 10))
        self.num_crossover_children = tk.Entry(self, textvariable=self.num_crossover_children, font=("bold", 10))
        self.operator_probability = tk.Entry(self, textvariable=self.operator_probability, font=("bold", 10))
        self._button_prediction = tk.Button(self, text="Browse dataset",bg="black",fg="white", command=self.browsePredict)
        self._label_p1=tk.Label(self, text="clean dataset path")
        self._label_p3=tk.Label(self, text="number of generations")
        self._label_p4=tk.Label(self, text="total number of chromosomes")
        self._label_p5=tk.Label(self, text="number of best chromosomes")
        self._label_p6=tk.Label(self, text="number of random chromosomes")
        self._label_p7=tk.Label(self, text="number of crossover chromosomes")
        self._label_p8=tk.Label(self, text="mutation chance")
        self._select=tk.Button(self,text="Select",bg="black",fg="white", command=self.select)
        self._label=tk.Label(self, text="Genetic Feature Selection.", bg="black", fg="white",height=3, font=("bold", 14))



    def _display_widgets(self):
        self._label.pack(fill='y')
        self._label_p1.pack(fill='y')
        self.entry_dataset_path.pack(fill='x', expand=True)
        self._button_prediction.pack(fill='x', expand=True)
        self._label_p3.pack(fill='y')
        self.num_of_generations.pack(fill='x', expand=True)
        self._label_p4.pack(fill='y')
        self.num_of_chromosomes.pack(fill='x', expand=True)
        self._label_p5.pack(fill='y')
        self.num_best_chromosomes.pack(fill='x', expand=True)
        self._label_p6.pack(fill='y')
        self.num_rand_chromosomes.pack(fill='x', expand=True)
        self._label_p7.pack(fill='y')
        self.num_crossover_children.pack(fill='x', expand=True)
        self._label_p8.pack(fill='y')
        self.operator_probability.pack(fill='x', expand=True)
        self._select.pack(fill='y')

    def select(self):
        newwin = tk.Toplevel(root)
        newwin.geometry("500x500")
        label = tk.Label(newwin, text="Best Features", bg="black", fg="white",height=3, font=("bold", 14))
        label.pack()
        entry_dataset_path = self.entry_dataset_path.get()
        num_of_generations = self.num_of_generations.get()
        num_of_chromosomes = self.num_of_chromosomes.get()
        num_best_chromosomes = self.num_best_chromosomes.get()
        num_rand_chromosomes = self.num_rand_chromosomes.get()
        num_crossover_children = self.num_crossover_children.get()
        operator_probability = self.operator_probability.get()
        try:
            # loader = wdbcLoader.WdbcLoader()
            # features_values, class_values, features_names, class_name, self.split = loader.get_data()
            dataset = pd.read_csv(entry_dataset_path)
            features_values = dataset[dataset.columns[0:-1]]
            class_values = dataset[dataset.columns[-1]]
            selector = genetic_selector.GeneticSelector(
                estimator=rrigaFitness.RRIGA_Fitness_Function(features_vectors=features_values, class_vector=class_values),
                num_of_generations=int(num_of_generations),
                num_of_chromosomes=int(num_of_chromosomes),
                num_best_chromosomes=int(num_best_chromosomes),
                num_rand_chromosomes=int(num_rand_chromosomes),
                num_crossover_children=int(num_crossover_children),
                operator_probability=float(operator_probability),
                features_names=features_values.columns.values,
                class_vector=class_values)
            selector.evolve(features_values.copy())
            best_features = selector.best_features

            T = tk.Text(newwin, height=25, width=60)
            # for list in best_features:
            '''  this will return single best feature set   '''
            T.insert('end',str(best_features[0])+"\n")
            T.pack()

            '''  this will return last generation ranked feature sets  '''
            # for list in best_features:
                #     T.insert('end',str(list)+"\n")
                #     T.pack()
        except :
            raise ValueError('please insert valid parameters')

        newwin.mainloop()

    def browseModel(self):

        self.dataset_path.set(fd.askdirectory())

    def browsePredict(self):
        self.dataset_path.set(fd.askopenfilename(initialdir=self._initaldir))



if __name__ == '__main__':
    root = tk.Tk()
    labelfont = ('times', 10, 'bold')
    root.geometry("500x500")
    filetypes = (
        ('*.csv')
    )
    file_browser = Browse(root, initialdir="\\", filetypes=filetypes)
    file_browser.pack(fill='y')
    root.mainloop()