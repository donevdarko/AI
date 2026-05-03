import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'
from submission_script import *
from dataset_script import dataset

import numpy as np
from sklearn.preprocessing import OrdinalEncoder
from sklearn.naive_bayes import CategoricalNB

if __name__ == '__main__':
    percent = int(input())
    record = input().split()

    X = [row[:-1] for row in dataset]
    Y = [row[-1] for row in dataset]

    encoder = OrdinalEncoder()
    encoder.fit(X)

    X_encoded = encoder.transform(X)

    split_index = int(len(X_encoded)*percent/100)
    train_X = X_encoded[:split_index]
    train_Y = Y[:split_index]
    test_X = X_encoded[split_index:]
    test_Y = Y[split_index:]

    classifier = CategoricalNB()
    classifier.fit(train_X, train_Y)


    accuracy = classifier.score(test_X, test_Y)
    print(accuracy)

    record_encoded = encoder.transform([record])
    prediction = classifier.predict(record_encoded)
    probabilities = classifier.predict_proba(record_encoded)

    print(prediction[0])
    print(probabilities)

    submit_train_data(train_X, train_Y)
    submit_test_data(test_X, test_Y)
    submit_classifier(classifier)
    submit_encoder(encoder)

