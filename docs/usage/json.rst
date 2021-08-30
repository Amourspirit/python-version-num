JSON Usage
==========

.. code:: python

    import json
    from verr import Version

    v1 = Version(1, 2, 3, 4)
    json_str = json.dumps(v1)
    print(json_str) # {"major": 1, "minor": 2, "build": 3, "revision": 4}
    v2 = Version(json.loads(json_str))
    print(v1 == v2) # True

    v1 = Version('0xfd', 22)
    json_str = json.dumps(v1)
    print(json_str)  # {"major": 253, "minor": 22}
    v2 = Version(json.loads(json_str))
    print(v1 == v2)  # True
