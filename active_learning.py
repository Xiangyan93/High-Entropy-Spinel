#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tqdm import tqdm
import sys
import pandas as pd
import numpy as np
from xgboost import XGBClassifier, XGBRegressor
from hes.args import ActiveLearningArgs
from hes.database.models import *


def get_X_y(p: str, atom_dict: Dict[int, str]):
    samples = []
    samples_test = []
    for sample in session.query(Sample):
        if sample.info is None:
            samples_test.append(sample)
        elif json.loads(sample.info).get(p) is not None:
            samples.append(sample)
        else:
            samples_test.append(sample)
    # training
    atom_list = [sample.get_atom_list() for sample in samples]
    remark = [sample.remark if sample.remark is not None else 'None'
              for sample in samples]
    prop = [json.loads(sample.info)[p] for sample in samples]
    df = pd.DataFrame({'atom_list': atom_list, p: prop,
                       'remark': remark})
    for an, name in atom_dict.items():
        df[name] = df.atom_list.apply(lambda x: x.count(an) / len(x))
    # test
    atom_list = [sample.get_atom_list() for sample in samples_test]
    df_test = pd.DataFrame({'atom_list': atom_list})
    for an, name in atom_dict.items():
        df_test[name] = df_test.atom_list.apply(lambda x: x.count(an) / len(x))
    return df[atom_dict.values()], df[p], df_test[atom_dict.values()]


def active_learning(args: ActiveLearningArgs):
    # stable
    X, y, X_test = get_X_y(p='Stabilized', atom_dict=args.atom_dict)
    clf = XGBClassifier(n_estimators=100, use_label_encoder=False).fit(X, y)
    X_stable = X_test[clf.predict_proba(X_test)[:, 0] < 0.5]
    df = X_stable.copy()
    df['proba_0'] = clf.predict_proba(X_stable)[:, 0]
    df['proba_1'] = clf.predict_proba(X_stable)[:, 1]
    df['proba_2'] = clf.predict_proba(X_stable)[:, 2]
    #
    X, y, _ = get_X_y(p='T90', atom_dict=args.atom_dict)
    model = XGBRegressor().fit(X, y)
    y_pred = model.predict(X_stable)
    df['T90_pred'] = y_pred
    idx = np.argsort(y_pred)[:args.n_samples]
    df = df.iloc[idx]
    df.to_csv('al.csv', index=False, float_format='%.4f')


if __name__ == '__main__':
    active_learning(args=ActiveLearningArgs().parse_args())
