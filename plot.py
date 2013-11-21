'''
Plot a single lephare .spec file

Usage: plot.py specfile types
  specfile - path to specfile
  types - space seperated list of solutions to plot. Example: GAL-1 GAL-2 STAR
'''

from matplotlib import pyplot as plt
import sys
import argparse
from SedData import LephSpecData as lsd

def plot(args=sys.argv):
  parser = argparse.ArgumentParser()
  parser.add_argument('FILE',nargs=1)
  parser.add_argument('TYPES',nargs='*')
  args = parser.parse_args()
  
  

if __name__=="__main__":
  plot()