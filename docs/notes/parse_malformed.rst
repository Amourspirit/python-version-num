.. attention::
    Malformed strings are converted as integers as well.

    If a string has non-alphnumeric characters then the non-alphnumeric characters are stripped away.

.. code-block:: python

    from verr import Version

    v = Version.parse('10.1')
    print(v) # 10.1

    v = Version.parse('10_000.(%2/1)')
    print(v) # 10000.21

    v = Version.parse('0xab12.0x_1c2d]')
    print(v) # 43794.7213

    v = Version.parse('"12_^.0x_1c2d]')
    # dec 12
    # hex 0x1c2d
    print(v) # 12.7213

