import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'
from submission_script import *
from dataset_script import dataset

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

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
    n_trees = int(input())
    criterion = input()
    test_record = list(map(float, input().split()))

    X = []
    Y = []

    for row in dataset:
        features = list(row[:-1])
        del features[col_index]
        X.append(features)
        Y.append(row[-1])

    test_record_reduced = list(test_record)
    del test_record_reduced[col_index]

    split_index = int(0.85*len(X))
    train_X = X[:split_index]
    train_Y = Y[:split_index]
    test_X = X[split_index:]
    test_Y = Y[split_index:]

    params = {
        'n_estimators': n_trees,
        'criterion': criterion,
        'random_state': 0
    }

    classifier = RandomForestClassifier(**params)
    classifier.fit(train_X, train_Y)

    predictions = classifier.predict(test_X)
    acc = accuracy_score(test_Y, predictions)

    predicted_class = classifier.predict([test_record_reduced])[0]
    probabilities = classifier.predict_proba([test_record_reduced])[0]

    print(f'Accuracy: {acc}')
    print(predicted_class)
    print(probabilities)
    
    
    
    
    
    # Na kraj potrebno e da napravite submit na podatochnoto mnozestvo
    # i klasifikatorot so povik na slednite funkcii
    
    # submit na trenirachkoto mnozestvo
    submit_train_data(train_X, train_Y)
    
    # submit na testirachkoto mnozestvo
    submit_test_data(test_X, test_Y)
    
    # submit na klasifikatorot
    submit_classifier(classifier)
