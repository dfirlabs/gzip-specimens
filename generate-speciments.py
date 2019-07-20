#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Script to generate GZIP file specimens."""

from __future__ import print_function
from __future__ import unicode_literals

import argparse
import gzip
import os
import sys


def Main():
  """The main program function.

  Returns:
    bool: True if successful or False if not.
  """
  argument_parser = argparse.ArgumentParser(description=(
      'Generates GZIP file specimens.'))

  options = argument_parser.parse_args()

  specimens_path = 'specimens'
  if not os.path.isdir(specimens_path):
    os.mkdir(specimens_path)

  with open('LICENSE', 'rb') as file_object:
    file_data = file_object.read()

  # Create single member GZIP file.
  path = os.path.join(specimens_path, 'single_member.gz')
  with gzip.open(path, 'wb') as file_object:
    file_object.write(b'GZIP file with a single member\n')
    file_object.write(file_data)

  # Create multi member GZIP file.
  path = os.path.join(specimens_path, 'multi_member.gz')
  with gzip.open(path, 'wb') as file_object:
    file_object.write(b'first member of GZIP file\n')
    file_object.write(file_data)

  with gzip.open(path, 'ab') as file_object:
    file_object.write(b'second member of GZIP file\n')
    file_object.write(file_data)

  with gzip.open(path, 'ab') as file_object:
    file_object.write(b'third member of GZIP file\n')
    file_object.write(file_data)

  with gzip.open(path, 'ab') as file_object:
    file_object.write(b'fourth member of GZIP file\n')
    file_object.write(file_data)

  with gzip.open(path, 'ab') as file_object:
    file_object.write(b'fifth member of GZIP file\n')
    file_object.write(file_data)

  return True


if __name__ == '__main__':
  if not Main():
    sys.exit(1)
  else:
    sys.exit(0)
