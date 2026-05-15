import csv
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import *

def read_file(path):
    with open(path, 'r') as file:
        csv_reader = csv.reader(file, delimiter=';')

        lines = list(csv_reader)[1:]

    lines = [list(map(float, line[:-1])) + [line[-1]] for line in lines]

    return lines


dataset = read_file('NeuralNetworks/aud/data/vino.csv')

# bad dataset

bad_dataset = [row for row in dataset if row[-1] == "bad"]
bad_split_first = int(0.7*len(bad_dataset))
bad_split_second = int(0.8*len(bad_dataset))
train_set_bad = bad_dataset[:bad_split_first]
val_set_bad = bad_dataset[bad_split_first:bad_split_second]
test_set_bad = bad_dataset[bad_split_second:]

# good dataset

good_dataset = [row for row in dataset if row[-1] == 'good']
good_split_first = int(0.7*len(good_dataset))
good_split_second = int(0.8*len(good_dataset))
train_set_good = good_dataset[:good_split_first]
val_set_good = good_dataset[good_split_first:good_split_second]
test_set_good = good_dataset[good_split_second:]

train_set = train_set_bad + train_set_good
val_set = val_set_bad + val_set_good
test_set = test_set_bad + test_set_good

train_X, train_Y = [row[:-1] for row in train_set], [row[-1] for row in train_set]
val_X, val_Y = [row[:-1] for row in val_set], [row[-1] for row in val_set]
test_X, test_Y = [row[:-1] for row in test_set], [row[-1] for row in test_set]

params = {
    'hidden_layer_sizes': (5,),  # 5 would work too
    'activation': 'relu',
    'solver': 'sgd',
    'batch_size': 'auto',
    'learning_rate': 'constant',
    'learning_rate_init': 1e-3,
    'max_iter': 500,
    'random_state': 0,
    # If using early stopping, target variable mustn't be a string
    # 'early_stopping': True,
    # 'validation_fraction': 0.1,
    # 'verbose': True
}

params_2 = params.copy()
params_2['hidden_layer_sizes'] = (10,)

params_3 = params.copy()
params_3['hidden_layer_sizes'] = (100,)

model_1 = MLPClassifier(**params)
model_2 = MLPClassifier(**params_2)
model_3 = MLPClassifier(**params_3)

model_1.fit(train_X, train_Y)

standardScaler = StandardScaler()
model_2.fit(standardScaler.fit_transform(train_X), train_Y)

minmaxScaler = MinMaxScaler(feature_range=(-1, 1))
model_3.fit(minmaxScaler.fit_transform(train_X), train_Y)

models_and_sets = [(model_1, val_X), (model_2, standardScaler.transform(val_X)), (model_3, minmaxScaler.transform(val_X))]
accs=[]

for i, (model, set) in enumerate(models_and_sets):
    acc = model.score(set, val_Y)
    accs.append(acc)

best_model_index = accs.index(max(accs))
best_model = models_and_sets[best_model_index][0]

test_scaled_sets = [test_X, standardScaler.transform(test_X), minmaxScaler.transform(test_X)]
preds = best_model.predict(test_scaled_sets[best_model_index])

print('Accuracy:', accuracy_score(test_Y, preds))


print('Precision:', precision_score(test_Y, preds, pos_label='good'))
print('Recall:', recall_score(test_Y, preds, pos_label='good'))

