import matplotlib
matplotlib.use('Agg')

import pytest
import import_ipynb
import hw2

import hashlib

VAR_REG = hw2.VARIANT % 5

def hash_str(string):
  return hashlib.sha256(string.encode('utf-8')).hexdigest()[:8]

def test_data_loaded():
  assert len(hw2.DF_WGI) == 214

def test_data_sorted():
  assert hash_str(str(hw2.DF_SORTED.iloc[0].values)) == 'fc99fc7e'

def test_region_selected():
  var_counts = [30, 32, 19, 18, 48]

  assert var_counts[VAR_REG] == len(hw2.DF_REGION)


def test_minmax():
  ans = ['88b1ab93', '0df87554', '5da75e3e', '38f1341e', 'c09bdd8c']

  res_idx = str(sorted(list(hw2.DF_MINMAX.index)))

  assert hash_str(res_idx) == ans[VAR_REG]

def test_means():
  ans = ['c1dc4c9b', '0312e8ab', 'b9fc5497', '17fa2828', '09e6ec1f']

  res = str(list(hw2.S_MEANS.round(4).values))

  assert hash_str(res) == ans[VAR_REG]

def test_res_table_values():
  ans = [('45dcc784', '5d969b11'),
         ('b12f00e2', '959f5cf1'),
         ('9fade5f4', '02853e67'),
         ('3dac8083', '1520ba4b'),
         ('b4b46deb', '78de7acd')]

  res = hash_str(str(list(hw2.RES_TABLE.values.flatten())))

  assert res in ans[VAR_REG]

def test_res_table_columns():
  ans = ['Region', 'Country', 'Rank 1996', 'Rank 2022', 'Difference']

  res = list(hw2.RES_TABLE.columns)

  assert res == ans

def test_res_table_idx():
  ans = ['mean_2022', 'max_2022', 'min_2022', 'Russia_2022']

  res = list(hw2.RES_TABLE.index)

  assert res == ans

