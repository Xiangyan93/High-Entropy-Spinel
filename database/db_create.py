#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from itertools import combinations, product
sys.path.append('..')
from database.models import *


def IsValidList(v):
    Nmax = max(v)
    if Nmax == 1:
        return True

    factors = list(range(2, Nmax + 1))
    for i in v:
        for j in factors:
            if i % j != 0:
                factors.remove(j)
        if not factors:
            return True
    return False


def add_samples(N=1):
    """
    :param N: The maximum existences of each ion.
    """
    atom_dict = {12: 'Mg', 13: 'Al', 20: 'Ca', 22: 'Ti', 23: 'V', 24: 'Cr',
                 25: 'Mn', 26: 'Fe', 27: 'Co', 28: 'Ni', 29: 'Cu', 30: 'Zn',
                 38: 'Sr', 56: 'Ba'}
    # contain 5-11 types of metal atom
    for i in range(5, 11):
        print("\nProcessing %i-components" % i)
        compositions = [c for c in list(product(range(1, N+1), repeat=i)) if IsValidList(c)]
        for j, an in enumerate(list(combinations(atom_dict.values(), i))):
            sys.stdout.write('\r %i / %i' % (j, len(list(combinations(atom_dict.values(), i)))))
            for c in compositions:
                sample = Sample(**dict(zip(an, c)))
                session.add(sample)
            session.commit()
            exit()
    session.commit()
    return 0


if __name__ == '__main__':
    add_samples(1)
