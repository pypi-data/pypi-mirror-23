from NeuralNetwork_ import NeuralNetwork
from Pickler_  import Pickler
from Transfer_Calculator_ import Transfer_Calculator as tc
from Predictor_ import Predictor
from Constants import BASE_DIR
from Constants import MODELS_DIR
from Constants import INCEPTION_DIR
from Constants import TRAIN_DIR
from Constants import PRED_DIR
from Constants import TEST_WELLS_DIR
from Constants import TEST_INDL_DIR
import Constants
import os
import pickle

class Main:
    """ Contains the commands for running nnClassify from the command line"""

    @staticmethod
    def __setup():
        if not os.path.exists(BASE_DIR): os.makedirs(BASE_DIR)
        if not os.path.exists(MODELS_DIR): os.makedirs(MODELS_DIR)
        if not os.path.exists(TRAIN_DIR): os.makedirs(TRAIN_DIR)
        if not os.path.exists(PRED_DIR): os.makedirs(PRED_DIR)
        if not os.path.exists(INCEPTION_DIR): os.makedirs(INCEPTION_DIR)
        if not os.path.exists(TEST_WELLS_DIR): os.makedirs(TEST_WELLS_DIR)
        if not os.path.exists(TEST_INDL_DIR): os.makedirs(TEST_INDL_DIR)
        return


    @staticmethod
    def create_model(name):
        Main.__setup()
        model = NeuralNetwork("transfer", num_categories=3)
        print (' ') 
        print ('Starting to save')
        model.save(MODELS_DIR + name)
        print ('Done saving')
        return

    @staticmethod
    def train(trainning_set, name, epochs):
        Main.__setup()
        print ('Loading Model')
        model = NeuralNetwork("load", file_path=MODELS_DIR + name)
        print ('Done Loading Model')
        print (' ') 
        print ('Loading Images Please Be Patient')
        
        if not os.path.exists(TRAIN_DIR + trainning_set + "/labels.p"):
            Pickler.pickleIndividualSet(TRAIN_DIR + trainning_set)
        
        labels = pickle.load(open(TRAIN_DIR 
            + trainning_set + "/labels.p","rb"))

        if not os.path.exists(TRAIN_DIR+ trainning_set + "/transfer_values.p"):
            tc.getTransferValues(TRAIN_DIR + trainning_set + "/images.p",
                    TRAIN_DIR + trainning_set + "/transfer_values.p")

        imgs =  pickle.load(open(TRAIN_DIR
            + trainning_set + "/transfer_values.p","rb"))
        encoding = [Constants.ABNORMAL, Constants.NORMAL, Constants.WEIRD]
        print ('Done Loading Images')
        print (' ')
        print ('Starting to train')
        model = NeuralNetwork("transfer", num_categories=len(encoding))
        history = model.train(MODELS_DIR + name, imgs, labels, epochs)
        print ('Done Training')
        print (' ')
        print ('Starting to save')
        model.save(MODELS_DIR + name)
        print ('Done saving')
        return

    @staticmethod
    def predict(pred_set, name):
        Main.__setup()
        print ('Loading Model')
        model = NeuralNetwork("load", file_path=MODELS_DIR + name)
        print ('Done Loading Model')
        print (' ')
        print ('Starting to predict')
        Predictor.predict_wells(PRED_DIR + pred_set, 
                    [Constants.ABNORMAL,
                        Constants.NORMAL,
                        Constants.WEIRD],
                    model)


    @staticmethod
    def test_wells(test_set, name):
        Main.__setup()
        print ('Loading Model')
        model = NeuralNetwork("load", file_path=MODELS_DIR + name)
        print ('Done Loading Model')
        print (' ') 
        print ('Starting to predict')
        Predictor.test_wells(TEST_WELLS_DIR + test_set,
                [Constants.ABNORMAL,
                    Constants.NORMAL,
                    Constants.WEIRD],
                model)
        return

    @staticmethod
    def test_individual(test_set, name):
        Main.__setup()
        print ('Loading Model')
        model = NeuralNetwork("load", file_path=MODELS_DIR + name)
        print ('Done Loading Model')
        print (' ')
        print ('Loading Images Please Be Patient')

        if not os.path.exists(TEST_INDL_DIR + test_set + "/labels.p"):
            Pickler.pickleIndividualSet(TEST_INDL_DIR + test_set)

        labels = pickle.load(open(TEST_INDL_DIR 
            + test_set + "/labels.p","rb"))
        
        if not os.path.exists(TEST_INDL_DIR + test_set + "/transfer_values.p"):
            tc.getTransferValues(TEST_INDL_DIR + test_set + "/images.p",
                    TEST_INDL_DIR + test_set + "/transfer_values.p")

        imgs =  pickle.load(open(TEST_INDL_DIR
            + test_set + "/transfer_values.p","rb"))
        print ('Done Loading Images')
        print (' ')
        print ('Testing accuracy on individual images')
        accuracy = model.test_individual(imgs,labels)
        print (' ')
        print ("The accuracy on this test set is: " + str(accuracy))
        return



