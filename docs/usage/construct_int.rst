Constructor via int
===================

**Example:** Constructor including hex strings.

.. code:: python

    from verr import Version

    v = Version(11, 22, 33, 44)
    print(v.major) # 11
    print(v.minor) # 22
    print(v.build) # 33
    print(v.revision) # 44
    print(v) # 11.22.33.44
    print(v.elements) # 4

    v = Version(11, 22)
    print(v.major) # 11
    print(v.minor) # 22
    print(v.build) # 0
    print(v.revision) # 0
    print(v.elements) # 2
    print(v.to_tuple()) # (11, 22)
    print(v.to_str()) # 11.22

.. include:: ../notes/hex_note.rst
.. include:: ../notes/parse_malformed.rst

**See Also:** :doc:`../class/Version`
