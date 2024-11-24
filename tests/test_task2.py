import matplotlib
matplotlib.use('Agg')

import pytest
import import_ipynb
import hw2

import hashlib

VAR_COMP = hw2.VARIANT % 4

def hash_str(string):
  return hashlib.sha256(string.encode('utf-8')).hexdigest()[:8]

def test_companies_loaded():
  assert len(hw2.DF_COMPANIES) == 28

def test_correct_columns():
  ans = ['AAPL', 'ABNB', 'ADBE', 'AMZN', 'CSCO', 'DBX', 'EBAY', 'GOOGL', 'GTLB',
         'HPQ', 'INTC', 'META', 'MSFT', 'MU', 'NFLX', 'NVDA', 'ORCL', 'PINS', 'SHOP',
         'SPOT', 'TCOM', 'TSLA', 'TWLO', 'UBER', 'XIACY']

  res = sorted(list(hw2.DF_COMPANIES.columns))

  assert res == ans

def test_correlation_matrix():
  ans = '95a97af3'

  res = hash_str(str(list(hw2.DF_CORR.values.flatten())))

  assert res == ans

def test_corr_comp():
  ans = ['f6c4ff33', '8ea93a9a', '4a3b5526', '5394df14']

  res = hash_str(str(hw2.LST_COMP_CORR))

  assert res == ans[VAR_COMP]

def test_means():
  ans = ['ce211141', '4b98443c']

  res = hash_str(str(list(hw2.S_MEANS_COMP)))

  assert res in ans
