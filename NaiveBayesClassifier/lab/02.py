import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'
from submission_script import *
from dataset_script import dataset

from sklearn.naive_bayes import GaussianNB


if __name__ == '__main__':
    # Vashiot kod tuka
    record = list(map(float, input().split()))

    class_0_records = [row for row in dataset if row[-1] == '0']
    class_1_records = [row for row in dataset if row[-1] == '1']
    
    split_0 = int(len(class_0_records)*0.85)
    split_1 = int(len(class_1_records)*0.85)

    train = class_0_records[:split_0] + class_1_records[:split_1]
    test = class_0_records[split_0:] + class_1_records[split_1:]

    train_X = [[float(val) for val in row[:-1]] for row in train]
    train_Y = [int(row[-1]) for row in train]

    test_X = [[float(val) for val in row[:-1]] for row in test]
    test_Y = [int(row[-1]) for row in test]

    classifier = GaussianNB()
    classifier.fit(train_X, train_Y)

    acc = classifier.score(test_X, test_Y)

    print(acc)

    prediction = classifier.predict([record])
    prob = classifier.predict_proba([record])

    print(prediction[0])
    print(prob)
    

    # Na kraj potrebno e da napravite submit na podatochnoto mnozestvo,
    # klasifikatorot i encoderot so povik na slednite funkcii
    
    # submit na trenirachkoto mnozestvo
    submit_train_data(train_X, train_Y)
    
    # submit na testirachkoto mnozestvo
    submit_test_data(test_X, test_Y)
    
    # submit na klasifikatorot
    submit_classifier(classifier)
    
    # povtoren import na kraj / ne ja otstranuvajte ovaa linija
