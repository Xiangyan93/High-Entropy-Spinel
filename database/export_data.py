#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import pandas as pd
from tqdm import tqdm
import sys
sys.path.append('..')
from database.models import *


def main():
    import argparse
    parser = argparse.ArgumentParser(
        description='Import the data from txt file into the database.',
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        '--property', type=str, help='The target property name.'
    )
    args = parser.parse_args()
    samples = session.query(Sample).filter(Sample.property!=None)
    atom_list = [sample.get_atom_list() for sample in samples]
    remark = [sample.remark if sample.remark is not None else 'None'
              for sample in samples]
    p = [json.loads(sample.property)[args.property] for sample in samples]
    df = pd.DataFrame({'atom_list': atom_list, args.property: p,
                       'remark': remark})
    df.atom_list = df.atom_list.apply(lambda x: ','.join(list(map(str, x))))
    df.to_csv('data.txt', sep=' ', index=False)


if __name__ == '__main__':
    tqdm.pandas()
    main()
