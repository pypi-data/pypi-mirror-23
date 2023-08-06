yamlord
=======

A wrapper for the `yaml` module to easily read and write `OrderedDict` objects
to and from `YAML` formatted files.

Install
-------

.. codeblock:: bash
    pip install yamlord

Usage
-----

The usage is straightforward: make and `OrderedDict` then write it to a
specified path, or read a `YAML` file from a specified path to an
`OrderedDict`. That's it.

.. codeblock:: python

    from collections import OrderedDict
    import yamlord

    # Make an Ordered dict for testing
    d = OrderedDict()
    d['a'] = 1
    d['b'] = ['str1', 'str2']

    # Write OrderedDict to YAML file
    yamlord.write_yaml(d, './test.yaml')

    # Read YAML file to OrderedDict
    d = yamlord.read_yaml('./test.yaml')
