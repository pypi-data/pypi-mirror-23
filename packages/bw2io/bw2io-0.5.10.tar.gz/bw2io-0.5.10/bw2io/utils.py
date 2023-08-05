# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
from eight import *

from numbers import Number
from stats_arrays import *
import codecs
import csv
import hashlib
import json
import os
import pprint
import sys

PY3 = sys.version_info >= (3, 0)

DEFAULT_FIELDS = ('name', 'categories', 'unit',
                  'reference product', 'location')

def default_delimiter():
    if PY3:
        return ";"
    else:
        return b";"


def activity_hash(data, fields=None, case_insensitive=True):
    """Hash an activity dataset.

    Used to import data formats like ecospold 1 (ecoinvent v1-2) and SimaPro, where no unique attributes for datasets are given. This is clearly an imperfect and brittle solution, but there is no other obvious approach at this time.

    The fields used can be optionally specified in ``fields``.

    No fields are required; an empty string is used if a field isn't present. All fields are cast to lower case.

    By default, uses the following, in order:
        * name
        * categories
        * unit
        * reference product
        * location

    Args:
        * *data* (dict): The :ref:`activity dataset data <database-documents>`.
        * *fields* (list): Optional list of fields to hash together. Default is ``('name', 'categories', 'unit', 'reference product', 'location')``.
        * *case_insensitive* (bool): Cast everything to lowercase before computing hash. Default is ``True``.

    Returns:
        A MD5 hash string, hex-encoded.

    """
    lower = lambda x: x.lower() if case_insensitive else x

    def get_value(obj, field):
        if isinstance(data.get(field), (list, tuple)):
            return lower("".join(data.get(field) or []))
        else:
            return lower(data.get(field) or "")

    fields = fields or DEFAULT_FIELDS
    string = u"".join([get_value(data, field) for field in fields])
    return str(hashlib.md5(string.encode('utf-8')).hexdigest())


def es2_activity_hash(activity, flow):
    """Generate unique ID for ecoinvent3 dataset.

    Despite using a million UUIDs, there is actually no unique ID in an ecospold2 dataset. Datasets are uniquely identified by the combination of activity and flow UUIDs."""
    return str(hashlib.md5((activity + flow).encode('utf-8')).hexdigest())


def load_json_data_file(filename):
    DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
    if filename[-5:] != ".json":
        filename = filename + ".json"
    return json.load(open(os.path.join(DATA_DIR, filename), encoding='utf-8'))


def format_for_logging(obj):
    return pprint.pformat(obj, indent=2)


def rescale_exchange(exc, factor):
    """Rescale exchanges, including formulas and uncertainty values, by a constant factor.

    No generally recommended, but needed for use in unit conversions. Not well tested.

    """
    assert isinstance(factor, Number)
    assert (
        factor > 0 or
        exc.get('uncertainty type', 0) in {UndefinedUncertainty.id,
                                           NoUncertainty.id,
                                           NormalUncertainty.id}
    )
    if exc.get('formula'):
        exc['formula'] = "({}) * {}".format(exc['formula'], factor)
    if exc.get('uncertainty type', 0) in (UndefinedUncertainty.id, NoUncertainty.id):
        exc[u'amount'] = exc[u'loc'] = factor * exc['amount']
    elif exc['uncertainty type'] == NormalUncertainty.id:
        exc[u'amount'] = exc[u'loc'] = factor * exc['amount']
        exc[u'scale'] *= factor
    elif exc['uncertainty type'] == LognormalUncertainty.id:
        # ``scale`` in lognormal is scale-independent
        exc[u'amount'] = exc[u'loc'] = factor * exc['amount']
    elif exc['uncertainty type'] == TriangularUncertainty.id:
        exc[u'minimum'] *= factor
        exc[u'maximum'] *= factor
        exc[u'amount'] = exc[u'loc'] = factor * exc['amount']
    elif exc['uncertainty type'] == UniformUncertainty.id:
        exc[u'minimum'] *= factor
        exc[u'maximum'] *= factor
        if 'amount' in exc:
            exc[u'amount'] *= factor
    else:
        raise UnsupportedExchange(
            u"This exchange type can't be automatically rescaled"
        )
    return exc


class UnicodeCSVReader(object):
    """From http://python3porting.com/problems.html#csv-api-changes"""
    def __init__(self, filename, dialect=csv.excel,
                 encoding="utf-8", **kw):
        self.filename = filename
        self.dialect = dialect
        self.encoding = encoding
        self.kw = kw

    def __enter__(self):
        if PY3:
            self.f = open(self.filename, 'rt',
                          encoding=self.encoding, newline='')
        else:
            self.f = open(self.filename, 'rb')
        self.reader = csv.reader(self.f, dialect=self.dialect,
                                 **self.kw)
        return self

    def __exit__(self, type, value, traceback):
        self.f.close()

    def next(self):
        row = next(self.reader)
        if PY3:
            return row
        return [s.decode(self.encoding) for s in row]

    __next__ = next

    def __iter__(self):
        return self
