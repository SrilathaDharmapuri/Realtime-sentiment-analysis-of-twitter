import pickle
import nltk
from termcolor import colored

from classifier import getTrainingAndTestData

classifier = nltk.classify.NaiveBayesClassifier
f = open('my_classifier.pickle0.738619912508', 'rb')
classifier = pickle.load(f)
f.close()

def realtimeAnalyse(tweet, classifier):

    # from classifier.py main function
    feature_set = {'ngram': 1, 'negtn': False}
    tweets = [[tweet, 'neg', 'NO_QUERY', []]]
    (v_train, v_test) = getTrainingAndTestData(tweets, 1, 1, '1step', feature_set)
    test_predict = [classifier.classify(t) for (t, s) in v_train]
    # print ('result ' + str(test_predict[0]))

    if str(test_predict[0]) == 'pos':
        print colored(tweet, 'green')
    elif str(test_predict[0]) == 'neg':
        print colored(tweet, 'red')
    else:
        print colored(tweet, 'blue')

# realtimeAnalyse("this is :(", classifier)
# realtimeAnalyse("this is great :)", classifier)
# realtimeAnalyse("this movie is xD", classifier)