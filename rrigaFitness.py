from pyitlib import discrete_random_variable as metrics
import math
import random
'''
@params variable1 and variable2 are numpy array of feature/class values
'''

def Symmetric_uncertainty(X, Y):
    result = 0
    try:
        ''' when cloumns have dominant values entropy is close to 0 and cannot use SU, instead MI can be used since multivalued cloumn not exist'''
        result = (2*metrics.information_mutual(X, Y))/(metrics.entropy(X) + metrics.entropy(Y))
    except:
        result = metrics.information_mutual(X, Y)
    finally:
        return result + 1

def Normlized_Interaction_Gain_3way(X, Y, Z):
    interaction_gain = metrics.information_mutual_conditional(X,Z,Y) - metrics.information_mutual(X,Z)
    try:
        result = (interaction_gain)/((metrics.entropy(X) + metrics.entropy(Y)))
    except:
        result = interaction_gain
    finally:
        return result + 1

'''
Relevancy Reduncancy Interaction Genetic algorithm fitness function

@param  (REQUIRED)features_vectors pandas dataframe 
        (REQUIRED)class_vector pandas series
        (REQUIRED)features_names of the features in the subset
        (OPTIONAL) weights a list[3] of weights for interacton, relevancy, and redundancy
@return set score

'''
class RRIGA_Fitness_Function:
    def __init__ (self, features_vectors, class_vector, explore_rate=0.2):
        self.features_vectors = features_vectors
        self.class_vector = class_vector
        self.set_score = 0
        self.explore_rate = explore_rate
        self.int_class_vector = class_vector.astype(int)
        self.__init_dicts__()


    def __init_dicts__(self):
        self.data_score_tracing_dict = dict()
        self.feature_class_symmetric_dict = dict()
        self.feature_feature_symmetric_dict = dict()
        self.data_score_tracing_dict = dict()
        self.ig_dict = dict()

    def get_data_score(self, feature_names):
        return self.data_score_tracing_dict.get(''.join(feature_names))

    def calculate_score(self, features_names):
        # start = time.time()
        names_str = ''.join(features_names)
        feature_score = self.data_score_tracing_dict.get(names_str)
        if feature_score != None:
            return feature_score
        feature_score = 0

        self.set_score = 0
        data = self.features_vectors[features_names]
        max_su = 0
        dominant_feature = None
        dominant_feature_name = None
        int_dominant_feature = 0
        randomize = False
        '''Randomize the dominant feature at a explore_rate chance'''
        if random.random() <= self.explore_rate:
            explore_dominant_feature_index = random.randint(0,len(features_names)-1)
            randomize = True

        curr_feature_idx = 0
        for feature_i in data.iteritems():
            i_name = feature_i[0]
            int_feature_i = feature_i[1].values.astype(int)
            symmetric_i_to_class = self.feature_class_symmetric_dict.get(feature_i[0])

            if symmetric_i_to_class == None:
                symmetric_i_to_class = Symmetric_uncertainty(int_feature_i, self.int_class_vector.values.astype(int))
                self.feature_class_symmetric_dict[i_name] = symmetric_i_to_class

            feature_i_score = symmetric_i_to_class

            if(randomize and explore_dominant_feature_index == curr_feature_idx):
                max_su = feature_i_score
                dominant_feature = feature_i
                dominant_feature_name = i_name
                int_dominant_feature = int_feature_i
                break

            if(feature_i_score > max_su):
                max_su = feature_i_score
                dominant_feature = feature_i
                dominant_feature_name = i_name
                int_dominant_feature = int_feature_i

            curr_feature_idx += 1


        set_score = max_su

        for feature_j in data.iteritems():
            if dominant_feature == feature_j:
                continue
            j_name = feature_j[0]

            int_feature_j = feature_j[1].values.astype(int)

            ig_i_j_class = self.ig_dict.get(dominant_feature_name + j_name)
            symmetric_j_to_i = self.feature_feature_symmetric_dict.get(j_name + dominant_feature_name)
            symmetric_j_to_class = self.feature_class_symmetric_dict.get(j_name)

            if symmetric_j_to_i == None:
                symmetric_j_to_i = self.feature_feature_symmetric_dict.get(dominant_feature_name + j_name)
                if symmetric_j_to_i == None:
                    symmetric_j_to_i = Symmetric_uncertainty(int_dominant_feature, int_feature_j)
                self.feature_feature_symmetric_dict[j_name + dominant_feature_name] = symmetric_j_to_i
                self.feature_feature_symmetric_dict[dominant_feature_name + j_name] = symmetric_j_to_i

            if ig_i_j_class == None:
                ig_i_j_class = self.ig_dict.get(j_name + dominant_feature_name)
                if ig_i_j_class == None:
                    ig_i_j_class = Normlized_Interaction_Gain_3way(int_dominant_feature, int_feature_j, self.int_class_vector.values.astype(int))
                    self.ig_dict[dominant_feature_name + j_name] = ig_i_j_class
                    self.ig_dict[j_name + dominant_feature_name] = ig_i_j_class

            if symmetric_j_to_class == None:
                symmetric_j_to_class = Symmetric_uncertainty(int_feature_j, self.int_class_vector)
                self.feature_class_symmetric_dict[j_name] = symmetric_i_to_class
                '''symmetric_uncertainty range [1,2] IW range [0,2]'''
            set_score *= ((symmetric_j_to_class*ig_i_j_class)/symmetric_j_to_i)

        # print(len(features_names))
        self.data_score_tracing_dict[''.join(features_names)] = set_score
        # print(time.time() - start)
        return float(self.set_score)
