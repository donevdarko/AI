import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'

from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import MinMaxScaler

from dataset_script import dataset


if __name__ == '__main__':

    features = [row[:-1] for row in dataset]
    labels = [row[-1] for row in dataset]
    transformed_features = [[row[0] + row[-1]] + row[1:-1] for row in features]

    new_dataset = [f + [l] for f, l in zip(transformed_features, labels)]

    C = int(input())
    P = int(input())

    good_data = [row for row in new_dataset if row[-1]=="good"]
    bad_data = [row for row in new_dataset if row[-1]=="bad"]

    n_good = len(good_data)
    n_bad = len(bad_data)

    good_split = n_good * P // 100
    bad_split = n_bad * P // 100

    if C == 0:
        good_train = good_data[:good_split]
        good_test = good_data[good_split:]
        bad_train = bad_data[:bad_split]
        bad_test = bad_data[bad_split:]
    else:
        good_split = n_good * (100-P) // 100
        bad_split = n_bad * (100-P) // 100

        good_train = good_data[good_split:]
        good_test = good_data[:good_split]
        bad_train = bad_data[bad_split:]
        bad_test = bad_data[:bad_split]

    train_set = good_train + bad_train
    test_set = good_test + bad_test

    X_train = [row[:-1] for row in train_set]
    Y_train = [row[-1] for row in train_set]
    X_test = [row[:-1] for row in test_set]
    Y_test = [row[-1] for row in test_set]

    cls1 = GaussianNB()
    cls1.fit(X_train, Y_train)
    acc1 = cls1.score(X_test, Y_test)

    scaler = MinMaxScaler(feature_range=(-1, 1))
    X_train_scaler = scaler.fit_transform(X_train)
    X_test_scaler = scaler.transform(X_test)

    cls2 = GaussianNB()
    cls2.fit(X_train_scaler, Y_train)
    acc2=cls2.score(X_test_scaler, Y_test)

    print(f"Tochnost so zbir na koloni: {acc1}")
    print(f"Tochnost so zbir na koloni i skaliranje: {acc2}")

