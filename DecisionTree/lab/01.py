import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'
from submission_script import *
from dataset_script import dataset  #dataset_script

from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import OrdinalEncoder

# Ova e primerok od podatochnoto mnozestvo, za treniranje/evaluacija koristete ja
# importiranata promenliva dataset
dataset_sample = [['C', 'S', 'O', '1', '2', '1', '1', '2', '1', '2', '0'],
                  ['D', 'S', 'O', '1', '3', '1', '1', '2', '1', '2', '0'],
                  ['C', 'S', 'O', '1', '3', '1', '1', '2', '1', '1', '0'],
                  ['D', 'S', 'O', '1', '3', '1', '1', '2', '1', '2', '0'],
                  ['D', 'A', 'O', '1', '3', '1', '1', '2', '1', '2', '0']]

if __name__ == '__main__':
    # Vashiot kod tuka
    x = int(input())
    criterion = input()

    n = len(dataset)
    test_size = int((100 - x) / 100 * n)
    train_size = n - test_size


    test_set = dataset[:test_size]
    train_set = dataset[test_size:]

    train_X = [row[:-1] for row in train_set]
    train_Y = [row[-1] for row in train_set]
    test_X = [row[:-1] for row in test_set]
    test_Y = [row[-1] for row in test_set]

    encoder = OrdinalEncoder()
    encoder.fit([row[:-1] for row in dataset])

    train_X_enc = encoder.transform(train_X)
    test_X_enc = encoder.transform(test_X)

    params_1 = {
        'criterion': criterion,
        'max_depth': 50,
        'random_state': 0
    }

    classifier = DecisionTreeClassifier(**params_1)
    classifier.fit(train_X_enc, train_Y)

    accuarcy = classifier.score(test_X_enc, test_Y)
    depth = classifier.get_depth()
    leaves = classifier.get_n_leaves()
    importances = classifier.feature_importances_
    most_important = int(importances.argmax())
    least_important = int(importances.argmin())

    print(f"Depth: {depth}")
    print(f"Number of leaves: {leaves}")
    print(f"Accuracy: {accuarcy}")
    print(f"Most important feature: {most_important}")
    print(f"Least important feature: {least_important}")

    
    
    
    
    
    
    # Na kraj potrebno e da napravite submit na podatochnoto mnozestvo,
    # klasifikatorot i encoderot so povik na slednite funkcii
    
    # submit na trenirachkoto mnozestvo
    submit_train_data(train_X_enc, train_Y)
    
    # submit na testirachkoto mnozestvo
    submit_test_data(test_X_enc, test_Y)
    
    # submit na klasifikatorot
    submit_classifier(classifier)
    
    # submit na encoderot
    submit_encoder(encoder)
