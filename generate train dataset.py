import numpy as np
import time
import pandas as pd
from keras.preprocessing import sequence


DATA_ROOT = 'data/'
FUNCTION = 'mf' # Choose between three branches of GO: bp, mf, cc 


MAXLEN = 1000 # Size of sequence embeddings
REPLEN = 256 # Size of network embedding 


def get_gene_ontology(filename='go.obo'):
    # Reading Gene Ontology from OBO Formatted file
    go = dict()
    obj = None
    with open('data/' + filename, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line == '[Term]':
                if obj is not None:
                    go[obj['id']] = obj
                obj = dict()
                obj['is_a'] = list()
                obj['part_of'] = list()
                obj['regulates'] = list()
                obj['is_obsolete'] = False
                continue
            elif line == '[Typedef]':
                obj = None
            else:
                if obj is None:
                    continue
                l = line.split(": ")
                if l[0] == 'id':
                    obj['id'] = l[1]
                elif l[0] == 'is_a':
                    obj['is_a'].append(l[1].split(' ! ')[0])
                elif l[0] == 'name':
                    obj['name'] = l[1]
                elif l[0] == 'is_obsolete' and l[1] == 'true':
                    obj['is_obsolete'] = True
    if obj is not None:
        go[obj['id']] = obj
    for go_id in list(go):
        if go[go_id]['is_obsolete']:
            del go[go_id]
    for go_id, val in go.items():
        if 'children' not in val:
            val['children'] = set()
        for p_id in val['is_a']:
            if p_id in go:
                if 'children' not in go[p_id]:
                    go[p_id]['children'] = set()
                go[p_id]['children'].add(go_id)
    return go


#Gene ontology code of labels
go = get_gene_ontology('go.obo')
func_df = pd.read_pickle(DATA_ROOT + FUNCTION + '.pkl')
functions = func_df['functions'].values


def load_data():
    df = pd.read_pickle(DATA_ROOT + 'train' + '-' + FUNCTION + '.pkl')
    n = len(df)
    index = df.index.values
    valid_n = int(n * 0.8)
    train_df = df.loc[index[:valid_n]]
    valid_df = df.loc[index[valid_n:]]
    test_df = pd.read_pickle(DATA_ROOT + 'test' + '-' + FUNCTION + '.pkl')
    

    def reshape(values):
        values = np.hstack(values).reshape(
            len(values), len(values[0]))
        return values

    def normalize_minmax(values):
        mn = np.min(values)
        mx = np.max(values)
        if mx - mn != 0.0:
            return (values - mn) / (mx - mn)
        return values - mn

    def get_values(data_frame):
        labels = reshape(data_frame['labels'].values)
        #sequence data
        ngrams = sequence.pad_sequences(
            data_frame['ngrams'].values, maxlen=MAXLEN)
        ngrams = reshape(ngrams)
        #network data
        rep = reshape(data_frame['embeddings'].values)
        data = (ngrams, rep)
        return data, labels

    train = get_values(train_df)
    valid = get_values(valid_df)
    test = get_values(test_df)

    return train, valid, test, train_df, valid_df, test_df


print("Preparing data...")
train, valid, test, train_df, valid_df, test_df = load_data()

# train_x, val_x and test_x are tuples which include sequence and network embeddings respectively
train_x, train_y = train
val_x, val_y = valid
test_x, test_y = test


