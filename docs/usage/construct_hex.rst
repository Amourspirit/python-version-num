Constructor via hex
===================

**Hex** strings are accepted in the constructor.

**Example:** Constructor including hex strings.

.. code:: python

    from verr import Version

    v = Version(1, 2, 3, "0xffbbff0b")
    print(v.major_revision == int("ffbb", 16)) # True
    print(v.minor_revision == int("ff0b", 16)) # True
    print(v) # 1.2.3.4290510603
    print(v.to_str(3)) # 1.2.3
    print(v.to_tuple()) # (1, 2, 3, 4290510603)
    print(v.to_tuple(3)) # (1, 2, 3)
    print(v.elements) # 4

    v = Version('0xd', '0x02', '0x001a', '0XAB')
    print(v)  # 13.2.26.171

.. include:: ../notes/hex_note.rst
.. include:: ../notes/parse_malformed.rst

**See Also:** :doc:`../class/Version`
