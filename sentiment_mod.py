# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 14:38:05 2020

@author: Laksh
"""
#
#import nltk
import random
import pickle
#from nltk.corpus import movie_reviews
from nltk.tokenize import word_tokenize

#from nltk.classify.scikitlearn import SklearnClassifier
#from sklearn.naive_bayes import MultinomialNB , GaussianNB, BernoulliNB
#from sklearn.svm import SVC, LinearSVC, NuSVC
#from sklearn.linear_model import LogisticRegression, SGDClassifier


from nltk.classify import ClassifierI
from statistics import mode


documents_f = open("documents.pickle","rb")
documents = pickle.load(documents_f)
documents_f.close()
    
featuresets_f = open("featuresets.pickle","rb")
featuresets = pickle.load(featuresets_f)
featuresets_f.close()

word_features_f = open("word_features.pickle","rb")
word_features = pickle.load(word_features_f)
word_features_f.close()

random.shuffle(featuresets)
test_set = featuresets[10000:]

nb_f = open("nb.pickle","rb")
nbc = pickle.load(nb_f)
nb_f.close()

Bernoulli_f = open("Bernoulli.pickle","rb")
Bernoullic = pickle.load(Bernoulli_f)
Bernoulli_f.close()

Multinomial_f = open("MNB.pickle","rb")
Multinomialc = pickle.load(Multinomial_f)
Multinomial_f.close()

LinearSVC_f = open("LinearSVC.pickle","rb")
LinearSVCc = pickle.load(LinearSVC_f)
LinearSVC_f.close()

NuSVC_f = open("NuSVC.pickle","rb")
NuSVCc = pickle.load(NuSVC_f)
NuSVC_f.close()

LogisticRegression_f = open("LogisticRegression.pickle","rb")
LogisticRegressionc = pickle.load(LogisticRegression_f)
LogisticRegression_f.close()

SGDClassifier_f = open("SGDClassifier.pickle","rb")
SGDClassifierc = pickle.load(SGDClassifier_f)
SGDClassifier_f.close()


class VoteClass(ClassifierI):
    def __init__(self,*classifiers):
        self._classifiers = classifiers
        
    def classify(self,features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        return mode(votes)
    
    def confidence(self,features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        
        choice_votes = votes.count(mode(votes))
        conf = choice_votes/len(votes)
        return conf


def findfeatures(documents):
    words = word_tokenize(documents)
    features = {}
    for w in word_features: 
        features[w] = (w in words)
    return features


#
#featuresets = [(findfeatures(rev),category) for (rev,category) in documents]
#train_set = featuresets[:10000]



voted_classifier = VoteClass(nbc,Bernoullic,Multinomialc,LinearSVCc,NuSVCc,LogisticRegressionc,SGDClassifierc)
#print("Voted Classifier Accuracy:",(nltk.classify.accuracy(voted_classifier,test_set))*100)
#


def sentiment(text):
    feats = findfeatures(text)
    return voted_classifier.classify(feats),voted_classifier.confidence(feats)

#sentiment("happy")
#





