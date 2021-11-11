#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Database engine
"""
from typing import Dict, Iterator, List, Optional, Union, Literal, Tuple
import os
import json
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine, exists, and_
from sqlalchemy import Column, Integer, Float, Text, Boolean, String, ForeignKey, UniqueConstraint
CWD = os.path.dirname(os.path.abspath(__file__))

Base = declarative_base()
metadata = Base.metadata

db_file = 'sqlite:///%s/../../data/hes.db' % CWD

engine = create_engine(db_file, echo=False)
Session = sessionmaker(engine)
session = Session()


class Sample(Base):
    __tablename__ = 'sample'
    id = Column(Integer, primary_key=True)
    composition = Column(Text)
    remark = Column(Text)
    info = Column(Text)

    def get_atom_list(self):
        atom_list = []
        return atom_list

    @property
    def is_stabilized(self) -> Optional[int]:
        if self.property is None:
            return None
        else:
            return json.loads(self.property)['Stabilized']


metadata.create_all(engine)
