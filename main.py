import dataset
import scenes_features
import sentence_features
import svm
import random_forest
import extra_features
import feature_vect
import generate_dataset

if __name__ == '__main__':
   #generate_dataset.gen_config4()
   random_forest.random_forest(config=4)
   #svm.svm(config=4)



