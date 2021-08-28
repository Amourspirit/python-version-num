Version.try_parse
=================

**Hex** strings are accepted in **try_parse**.
Hex strings are required to be prefixed with ``0x``.

.. tip::
    Hex strings are *not* case sensitive.

.. code:: python

    from verr import Version

    v_result = Version.try_parse("22.3")
    if v_result[0] == True:
        v = v_result[1]
        print(v) # 22.3
    else:
        err = v_result[1]
        print(e)

    v_result= Version.try_parse('0xd.0x02.0x001a.0XAB')
    if v_result[0] == True:
        v = v_result[1]
        print(v) # 13.2.26.171
    else:
        err = v_result[1]
        print(e)

:See: :py:meth:`verr.Version.try_parse`