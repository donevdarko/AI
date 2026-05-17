import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'
from submission_script import *
from dataset_script import dataset

from sklearn.neural_network import MLPClassifier

# Ova e primerok od podatochnoto mnozestvo, za treniranje/evaluacija koristete ja
# importiranata promenliva dataset
dataset_sample = [[180.0, 23.6, 25.2, 27.9, 25.4, 14.0, 'Roach'],
                  [12.2, 11.5, 12.2, 13.4, 15.6, 10.4, 'Smelt'],
                  [135.0, 20.0, 22.0, 23.5, 25.0, 15.0, 'Perch'],
                  [1600.0, 56.0, 60.0, 64.0, 15.0, 9.6, 'Pike'],
                  [120.0, 20.0, 22.0, 23.5, 26.0, 14.5, 'Perch']]


if __name__ == '__main__':
    # Vashiot kod tuka
    col_index = int(input())

    num_neurons = int(input())

    record = list(map(float, input().split()))

    modified_dataset = [row[:col_index] + row[col_index+1:] for row in dataset]

    record_modified = [record]
    record_modified = [row[:col_index] + row[col_index+1:] for row in record_modified]


    split = len(modified_dataset)*80//100
    train = modified_dataset[:split]
    test = modified_dataset[split:]

    train_X = [row[:-1] for row in train]
    train_Y = [row[-1] for row in train]
    test_X = [row[:-1] for row in test]
    test_Y = [row[-1] for row in test]

    classifier = MLPClassifier(hidden_layer_sizes=num_neurons, random_state=0, max_iter=500)

    classifier.fit(train_X, train_Y)

    acc = classifier.score(test_X, test_Y)

    prediction = classifier.predict(record_modified)[0]

    probs = classifier.predict_proba(record_modified)[0]

    print(f"Tochnost: {acc}")
    print(f"Predvidena klasa: {prediction}")
    print(f"Verojatnosti: {probs}")
    
    
    
    
    
    
    # Na kraj potrebno e da napravite submit na podatochnoto mnozestvo
    # i klasifikatorot so povik na slednite funkcii
    
    # submit na trenirachkoto mnozestvo
    submit_train_data(train_X, train_Y)
    
    # submit na testirachkoto mnozestvo
    submit_test_data(test_X, test_Y)
    
    # submit na klasifikatorot
    submit_classifier(classifier)
