# Tools (txxlz)

Miscellaneous Python Tools

Requirements:
  Python 3

Installation:

>  pip install txxlz

Usage
```python

from txxlz import Txxlz
txxlz = Txxlz()

# Prepare Json Body for python processing to avoid TypeErrors
>>>txxlz.prepare_json('{"true":true,"null":null,"false":false}')
{"true": True, "null" : None, "false", False}
```
Documentation To be released on 9 April 2019
