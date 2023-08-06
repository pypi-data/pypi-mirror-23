from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import shutil

import numpy as np
from parsable import parsable

from treecat.config import make_default_config
from treecat.format import pickle_dump
from treecat.format import pickle_load
from treecat.structure import TreeStructure
from treecat.structure import sample_tree
from treecat.training import train_model
from treecat.util import set_random_seed

parsable = parsable.Parsable()

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(REPO, 'data', 'generated')


def generate_dataset(num_rows, num_cols, num_cats=4, rate=1.0):
    """Generate a random dataset.

    Returns:
      A pair (ragged_index, data).
    """
    set_random_seed(0)
    ragged_index = np.arange(0, num_cats * (num_cols + 1), num_cats, np.int32)
    data = np.zeros((num_rows, num_cols * num_cats), np.int8)
    for v in range(num_cols):
        beg, end = ragged_index[v:v + 2]
        column = data[:, beg:end]
        probs = np.random.dirichlet(np.zeros(num_cats) + 0.5)
        for n in range(num_rows):
            count = np.random.poisson(rate)
            column[n, :] = np.random.multinomial(count, probs)
    return {'ragged_index': ragged_index, 'data': data}


def generate_dataset_file(num_rows, num_cols, num_cats=4, rate=1.0):
    """Generate a random dataset.

    Returns:
      The path to a gzipped pickled data table.
    """
    path = os.path.join(DATA, '{}-{}-{}-{:0.1f}.dataset.pkz'.format(
        num_rows, num_cols, num_cats, rate))
    if os.path.exists(path):
        return path
    print('Generating {}'.format(path))
    if not os.path.exists(DATA):
        os.makedirs(DATA)
    dataset = generate_dataset(num_rows, num_cols, num_cats, rate)
    pickle_dump(dataset, path)
    return path


def generate_tree(num_cols):
    tree = TreeStructure(num_cols)
    K = tree.complete_grid.shape[1]
    edge_logits = np.random.random([K])
    edges = [tuple(edge) for edge in tree.tree_grid[1:3, :].T]
    edges = sample_tree(tree.complete_grid, edge_logits, edges, steps=10)
    tree.set_edges(edges)
    return tree


def generate_fake_model(num_rows,
                        num_cols,
                        num_cats,
                        num_components,
                        dataset=None):
    tree = generate_tree(num_cols)
    assignments = np.random.choice(num_components, size=(num_rows, num_cols))
    assignments = assignments.astype(np.int32)
    if dataset is None:
        dataset = generate_dataset(num_rows, num_cols, num_cats)
    ragged_index = dataset['ragged_index']
    data = dataset['data']
    N = num_rows
    V = num_cols
    E = V - 1
    C = num_cats
    M = num_components
    vert_ss = np.zeros((V, M), dtype=np.int32)
    edge_ss = np.zeros((E, M, M), dtype=np.int32)
    feat_ss = np.zeros((V * C, M), dtype=np.int32)
    meas_ss = np.zeros([V, M], np.int32)
    for v in range(V):
        vert_ss[v, :] = np.bincount(assignments[:, v], minlength=M)
    for e, v1, v2 in tree.tree_grid.T:
        pairs = assignments[:, v1].astype(np.int32) * M + assignments[:, v2]
        edge_ss[e, :, :] = np.bincount(pairs, minlength=M * M).reshape((M, M))
    for v in range(V):
        beg, end = ragged_index[v:v + 2]
        data_block = data[:, beg:end]
        feat_ss_block = feat_ss[beg:end, :]
        for n in range(N):
            feat_ss_block[:, assignments[n, v]] += data_block[n, :]
            meas_ss[v, assignments[n, v]] += data_block[n, :].sum()
    model = {
        'tree': tree,
        'assignments': assignments,
        'suffstats': {
            'ragged_index': ragged_index,
            'vert_ss': vert_ss,
            'edge_ss': edge_ss,
            'feat_ss': feat_ss,
            'meas_ss': meas_ss,
        },
    }
    return model


def generate_fake_ensemble(num_rows, num_cols, num_cats, num_components):
    dataset = generate_dataset(num_rows, num_cols, num_cats)
    ensemble = []
    config = make_default_config()
    config['model_num_clusters'] = num_components
    config['seed'] = 0
    for sub_seed in range(3):
        sub_config = config.copy()
        sub_config['seed'] += sub_seed
        set_random_seed(sub_config['seed'])
        model = generate_fake_model(num_rows, num_cols, num_cats,
                                    num_components, dataset)
        model['config'] = sub_config
        ensemble.append(model)
    return ensemble


def generate_model_file(num_rows, num_cols, num_cats=4, rate=1.0):
    """Generate a random model.

    Returns:
      The path to a gzipped pickled model.
    """
    path = os.path.join(DATA, '{}-{}-{}-{:0.1f}.model.pkz'.format(
        num_rows, num_cols, num_cats, rate))
    if os.path.exists(path):
        return path
    print('Generating {}'.format(path))
    if not os.path.exists(DATA):
        os.makedirs(DATA)
    dataset_path = generate_dataset_file(num_rows, num_cols, num_cats, rate)
    dataset = pickle_load(dataset_path)
    config = make_default_config()
    config['learning_annealing_epochs'] = 5
    model = train_model(dataset['ragged_index'], dataset['data'], config)
    pickle_dump(model, path)
    return path


@parsable
def clean():
    """Clean out cache of generated datasets."""
    if os.path.exists(DATA):
        shutil.rmtree(DATA)


if __name__ == '__main__':
    parsable()
