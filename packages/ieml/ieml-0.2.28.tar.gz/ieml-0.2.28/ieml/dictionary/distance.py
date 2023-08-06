import logging
import os
import pickle
from enum import Enum, unique, IntEnum
from itertools import combinations, product, groupby, chain

import bidict
import numpy as np
from scipy.sparse.csr import csr_matrix

from ieml.dictionary.dictionary import Dictionary
from ieml.dictionary.tools import term

logger = logging.getLogger(__name__)

RelationType = unique(IntEnum('RelationType', {
    'Null': 0,
    'Equal': 1,
    'Crossed': 2,
    'Associated': 3,
    'Twin': 4,
    'Opposed': 5,
    **{'Rank_%d'%i: 6 + i  for i in range(6)},

    **{'Child_%s'%''.join(s): int(11 + (3 ** i - 1) / 2 + j) for i in range(1, 4) for j, s in
       enumerate(product('sam', repeat=i))},

    **{'Father_%s' % ''.join(s): int(50 + (3 ** i - 1) / 2 + j) for i in range(1, 4) for j, s in
       enumerate(product('sam', repeat=i))}
}))


def default_metric(dictionary_version):
    mat = get_matrix('distance', dictionary_version)
    return lambda t0, t1: mat[t0.index, t1.index]


def term_ranking(t):
    order = get_matrix('order', t.dictionary.version)
    terms = [term(int(i)) for i in sorted(order[t.index, :].indices, key=lambda o: order[t.index, o])]
    return [t for t in terms if len(t) == 1], [t for t in terms if len(t) != 1]


def relations_pack(t0, term_list):
    reltypes = get_matrix('relation', t0.dictionary.version)

    res = [(reltypes[t0.index, t1.index], t1) for t1 in term_list]

    return [(RelationType(key).name, [t[1] for t in v]) for key, v in groupby(res, key=lambda t: t[0])]


def test_metric(t0):
    def _str_term(t):
        return "%s - (%s)"%(str(t), t.translations['fr'])

    print("Ranking from %s"%_str_term(t0))
    ss, para = term_ranking(t0)
    ss_pack = relations_pack(t0, ss)
    para_pack = relations_pack(t0, para)

    def _print_pack(p):
        for reltype, v in p:
            print("- %s -"%str(reltype))
            print("\n".join(_str_term(t) for t in v))

    print("SS:")
    _print_pack(ss_pack)
    print("\nParadigms")
    _print_pack(para_pack)
    # print('\n'.join("[%.3f] [%s]: %s"%(r[0], RelationType(reltypes[t0.index, r[1].index]).name,_str_term(r[1])) for r in res))




def get_matrix(name, version):
    file = '/tmp/cache_%s_%s.npy' % (name, str(version))
    if os.path.isfile(file):
        with open(file, 'rb') as fp:
            return pickle.load(fp)
    else:
        logger.log(logging.INFO, "Building distance matrix '%s'."%name)
        mat = MATRIX_BUILD[name](version)
        for k, v in mat.items():
            file_name = '/tmp/cache_%s_%s.npy' % (k, str(version))
            with open(file_name, 'wb') as fp:
                pickle.dump(v, fp)

        return mat[name]

RELATIONS_TYPES = {
    'associated': 0,
    'opposed': 1,
    'crossed': 2,
    'twin': 3,
    'table_5': 4,
    'table_4': 5,
    'table_3': 6,
    'table_2': 7,
    'table_1': 8,
    'table_0': 9
}

def get_relation(t0, t1, prefix=None):
    if prefix is None:
        reltype = min({r for r in t0.relations.to(t1) if r not in ('contained', 'contains')},
                          key=lambda r: RELATIONS_TYPES[r])

        if reltype == 'associated':
            return RelationType.Associated
        elif reltype == 'opposed':
            return RelationType.Opposed
        elif reltype == 'crossed':
            return RelationType.Crossed
        elif reltype == 'twin':
            return RelationType.Twin
        elif reltype.startswith('table_'):
            return RelationType['Rank_%d'%int(reltype[6:7])]
        else:
            raise NotImplemented
    else:
        type = 'Child' if t0.layer < t1.layer else 'Father'
        return RelationType['%s_%s'%(type, prefix)]


RELATION_ORDER_FROM_MAX_RANK = {
    i: ['Equal', 'Associated', 'Opposed', 'Crossed', 'Twin', 'Father1'] for i in range(6)
}

RELATION_ORDER_FROM_MAX_RANK[0] += ['Rank_0', 'Child1', 'Father2', 'Child2', 'Father3', 'Child3', 'Null']
RELATION_ORDER_FROM_MAX_RANK[1] += ['Rank_1', 'Child1', 'Father2', 'Child2', 'Rank_0','Father3', 'Child3', 'Null']
RELATION_ORDER_FROM_MAX_RANK[2] += ['Rank_2', 'Child1', 'Father2', 'Rank_1', 'Child2', 'Rank_0', 'Father3', 'Child3', 'Null']
RELATION_ORDER_FROM_MAX_RANK[3] += ['Rank_3', 'Child1', 'Rank_2', 'Father2', 'Rank_1', 'Child2', 'Rank_0', 'Father3', 'Child3', 'Null']
RELATION_ORDER_FROM_MAX_RANK[4] += ['Rank_4', 'Child1', 'Rank_3', 'Rank_2', 'Father2', 'Rank_1', 'Child2', 'Rank_0', 'Father3', 'Child3', 'Null']
RELATION_ORDER_FROM_MAX_RANK[5] += ['Rank_5', 'Child1', 'Rank_4', 'Rank_3', 'Rank_2', 'Father2', 'Rank_1', 'Child2', 'Rank_0', 'Father3', 'Child3', 'Null']

for i, rellist in RELATION_ORDER_FROM_MAX_RANK.items():
    res = []
    for rel in rellist:
        if rel.startswith('Child'):
            res += [RelationType['Child_%s'%''.join(k)] for k in product('sam', repeat=int(rel[5:6]))]
        elif rel.startswith('Father'):
            res += [RelationType['Father_%s'%''.join(k)] for k in product('sam', repeat=int(rel[6:7]))]
        else:
            res += [RelationType[rel]]

    RELATION_ORDER_FROM_MAX_RANK[i] = {rel: j for j, rel in enumerate(res)}


def get_relation_value(relation, t0):
    return RELATION_ORDER_FROM_MAX_RANK[t0.max_rank][relation]


def _build_distance_matrix(version):
    def _enumerate_ancestors(t, prefix=''):
        for k, v in t.relations.father.items():
            for t1 in v:
                # if t1 is layer 0, we include this etymology only if it is a direct father/child
                if t1.layer == 0 and len(prefix) != 0:
                    continue

                yield (prefix + k, t1)

                if len(prefix) < 2:
                    yield from _enumerate_ancestors(t1, prefix=prefix + k)

    d = Dictionary(version)

    def _put(mat,d, i, j):
        mat[0].append(d)
        mat[1].append(i)
        mat[2].append(j)

    order_matrix = ([], [], [])
    relation_type_matrix = ([], [], [])

    for root in d.roots:
        for t0, t1 in combinations(root.relations.contains, 2):
            rel = get_relation(t0, t1)
            value = get_relation_value(rel, t0)
            _put(order_matrix, value, t0.index, t1.index)
            _put(order_matrix, value, t1.index, t0.index)

            _put(relation_type_matrix, int(rel), t0.index, t1.index)
            _put(relation_type_matrix, int(rel), t1.index, t0.index)

    for layer in d.layers:
        for t0 in layer:
            for prefix, t1 in _enumerate_ancestors(t0):
                rel = get_relation(t0, t1, prefix=prefix)
                _put(relation_type_matrix, int(rel), t0.index, t1.index)
                _put(order_matrix, get_relation_value(rel, t0), t0.index, t1.index)

                rel = get_relation(t1, t0, prefix=prefix)
                _put(relation_type_matrix, int(rel), t1.index, t0.index)
                _put(order_matrix, get_relation_value(rel, t1), t1.index, t0.index)

    for i in range(len(d)):
        _put(relation_type_matrix, int(RelationType.Equal), i, i)
        _put(order_matrix, 0, i, i)

    build_mat = lambda mat: csr_matrix((mat[0], (mat[1], mat[2])), dtype=np.int8)

    # distance_matrix = build_mat(distance_matrix)
    # order_matrix = build_mat(order_matrix)
    relation_type_matrix = build_mat(relation_type_matrix)
    order_matrix = build_mat(order_matrix)
    # 'distance': distance_matrix,
    # 'order': order_matrix,
    return {'relation': relation_type_matrix,
            'order': order_matrix}


MATRIX_BUILD = {
    # 'distance': _build_distance_matrix,
    'order': _build_distance_matrix,
    'relation': _build_distance_matrix,
    # 'ancestor': _build_ancestor_matrix
}
