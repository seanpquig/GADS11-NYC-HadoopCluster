# -*- coding: utf-8 -*-
#!/usr/bin/python
# Licensed to Cloudera, Inc. under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  Cloudera, Inc. licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Wordcount example, for Hadoop streaming.
#
# Test with:
#  cat test-words | python wordcounter.py map | sort | python wordcounter.py reduce
#  hello 2
#  moon  1
#  sun 1

import sys
import re
import __builtin__

delimiter = ','

def emit(key, value):
  print delimiter.join( (key, value) )

def run_map():
  for line in enumerate(sys.stdin):
    ### Find and only emit lines that are ERRORs

    emit(key, line)
    
def run_reduce():
  """Gathers reduce() data in memory, and calls reduce()."""
  for line in sys.stdin:
    #Remove key from KV pair
    line = line.rstrip()
    key, value = re.split(delimiter, line, 1)
    print value

def main():
  """Runs map or reduce code, per arguments."""
  if len(sys.argv) != 2 or sys.argv[1] not in ("map", "reduce"):
    print "Usage: %s <map|reduce>" % sys.argv[0]
    sys.exit(1)
  if sys.argv[1] == "map":
    run_map()
  elif sys.argv[1] == "reduce":
    run_reduce()
  else:
    assert False

if __name__ == "__main__":
  main()
