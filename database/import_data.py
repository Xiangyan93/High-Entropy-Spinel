#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import pandas as pd
from tqdm import tqdm
import sys
sys.path.append('..')
from database.models import *


def import_data(atom_list, target, property='target', atom_ratio=None,
                remark=None):
    atom_dict = {12: 'Mg', 13: 'Al', 20: 'Ca', 22: 'Ti', 23: 'V', 24: 'Cr',
                 25: 'Mn', 26: 'Fe', 27: 'Co', 28: 'Ni', 29: 'Cu', 30: 'Zn',
                 38: 'Sr', 56: 'Ba'}
    name = [atom_dict[a] for a in atom_list]
    if atom_ratio is None:
        atom_ratio = [1] * len(name)
    s = session.query(Sample).filter_by(**dict(zip(name, atom_ratio))).first()
    if s.property == None:
        s.property = json.dumps({property: target})
    else:
        p = json.loads(s.property)
        if property in p:
            assert (target == p[property])
        else:
            s.property = json.dumps(dict(p, **{property: target}))
    if remark is not None:
        s.remark = remark
    session.commit()
    return 0


def main():
    import argparse
    parser = argparse.ArgumentParser(
        description='Import the data from txt file into the database.',
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        '-i', '--input', type=str, help='Input data in csv format.'
    )
    parser.add_argument(
        '--remark', type=str, help='Mark the data with arbitrary string.',
        default=None
    )
    parser.add_argument(
        '--property', type=str, help='The target property name.'
    )
    args = parser.parse_args()
    df = pd.read_csv(args.input, sep='\s+')
    df['atom_list'] = df['atom_list'].apply(
        lambda x: list(map(int, x.split(','))))
    print(df)
    df.progress_apply(lambda x: import_data(x['atom_list'], x[args.property],
                                            property=args.property,
                                            remark=args.remark),
                      axis=1)


if __name__ == '__main__':
    tqdm.pandas()
    main()
