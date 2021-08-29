Version.parse
=============

**Hex** strings are accepted in **parse**.
Hex strings are required to be prefixed with ``0x``.

.. tip::
    Hex strings are *not* case sensitive.

.. code:: python

    from verr import Version

    v = Version.parse("11.22.33")
    print(v.major) # 11
    print(v.minor) # 22
    print(v.build) # 33
    print(v.revision) # 0
    print(v.elements) # 3
    print(v.to_tuple()) # (11, 22, 33)
    print(v.to_str()) # 11.22.33

    v1 = Version.parse("1.2.2")
    v2 = Version.parse("1.2.3")
    print(v1 > v2) # False
    print(v1 <= v2) # True

    v = Version.parse('0xd.0x02.0x001a.0XAB')
    print(v)  # 13.2.26.171

:See: :py:meth:`~verr.Version.parse`