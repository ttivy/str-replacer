# Description
Replace many strings at once.

# Installation
```Bash
$ pip install git+https://github.com/ttivy/str-replacer.git
```
or
```Bash
$ git clone https://github.com/ttivy/str-replacer.git
$ cd str-replacer
$ python setup.py install
```

# Requirements
- [pyahocorasick](https://github.com/WojciechMula/pyahocorasick)

# Usage
```Python
import replacer

replacements = {
    'src': '<dst>',
    'SRC': '<DST>',
}
r = replacer.Replacer(replacements)

r.replace('abcsrcdefABCSRCDEF')
# abc<dst>defABC<DST>DEF
```
