# python-bautils

bautils is a Python module implementing some useful helper functions for
working with the Python [bitarray](https://pypi.python.org/pypi/bitarray/)
module. Specifically, bautils supports adding (and, coming soon) other
basic arithmetic operations on bitarrays as if they were arbitrary length
binary numbers, something the bitarray package itself doesn't seem to
support.

It also contains helper methods to convert between the binary arrays
in the pure Python bitstring module 

I opted to put these functions in a new module; none are terribly complicated
to implement, so they're essentially just a set of convenient wrappers.

Unit tests are also a work in progress.

# Credits, Legal

bautils is written by Ben Rosser <rosser.bjr@gmail.com>, and is released
under the MIT License (see LICENSE file).
