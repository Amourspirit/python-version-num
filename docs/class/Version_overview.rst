=======================
:doc:`Version` Overview
=======================

Represents a version number. This class **cannot** be extended. Sealed Class


Constructor
===========

.. table::

    +--------------------+----------------------------------------+------------------------------------+
    | |ws|               | Name                                   | Description                        |
    +====================+========================================+====================================+
    | |img_method|       | Version()                              | Initializes a new instance of the  |
    |                    |                                        | Version class.                     |
    +--------------------+----------------------------------------+------------------------------------+
    | |img_method|       | Version(ver_str)                       | Initializes a new instance of the  |
    |                    |                                        | Version class using the specified  |
    |                    |                                        | string to be parsed                |
    +--------------------+----------------------------------------+------------------------------------+
    | |img_method|       | Version(ver_dict)                      | Initializes a new instance of the  |
    |                    |                                        | Version class using the specified  |
    |                    |                                        | dict to be parsed. Useful for      |
    |                    |                                        | loading json                       |
    +--------------------+----------------------------------------+------------------------------------+
    | |img_method|       | Version(version)                       | Initializes a new instance of the  |
    |                    |                                        | Version class using the specified  |
    |                    |                                        | version.                           |
    +--------------------+----------------------------------------+------------------------------------+
    | |img_method|       | Version(major, minor)                  | Initializes a new instance of the  |
    |                    |                                        | Version class using the specified  |
    |                    |                                        | major and minor values.            |
    +--------------------+----------------------------------------+------------------------------------+
    | |img_method|       | Version(major, minor, build)           | Initializes a new instance of the  |
    |                    |                                        | Version class using the specified  |
    |                    |                                        | major, minor, and build values.    |
    |                    |                                        |                                    |
    +--------------------+----------------------------------------+------------------------------------+
    | |img_method|       | Version(major, minor, build, revision) | Initializes a new instance of the  |
    |                    |                                        | Version class with the specified   |
    |                    |                                        | major, minor, build, and revision  |
    |                    |                                        | numbers.                           |
    |                    |                                        |                                    |
    +--------------------+----------------------------------------+------------------------------------+


Properties
==========

.. table::

    +-------------+-------------------+-------------------------------------+
    |  |ws|       | Name              | Description                         |
    |             |                   |                                     |
    +=============+===================+=====================================+
    | |img_prop|  | |major|           | Gets the value of the major         |
    |             |                   | component of the version number for |
    |             |                   | the current Version object.         |
    +-------------+-------------------+-------------------------------------+
    | |img_prop|  | |minor|           | Gets the value of the minor         |
    |             |                   | component of the version number for |
    |             |                   | the current Version object.         |
    +-------------+-------------------+-------------------------------------+
    | |img_prop|  | |build|           | Initializes a new instance of the   |
    |             |                   | Version class using the specified   |
    |             |                   | major and minor values.             |
    +-------------+-------------------+-------------------------------------+
    | |img_prop|  | |rev|             | Gets the value of the revision      |
    |             |                   | component of the version number for |
    |             |                   | the current Version object.         |
    +-------------+-------------------+-------------------------------------+
    | |img_prop|  | |major_rev|       | Gets the high 16 bits of the        |
    |             |                   | revision number.                    |
    |             |                   |                                     |
    |             |                   |                                     |
    |             |                   |                                     |
    +-------------+-------------------+-------------------------------------+
    | |img_prop|  | |minor_rev|       | Gets the low 16 bits of the         |
    |             |                   | revision number.                    |
    |             |                   |                                     |
    |             |                   |                                     |
    |             |                   |                                     |
    +-------------+-------------------+-------------------------------------+
    | |img_prop|  | |elements|        | Gets the number of version elements |
    |             |                   | of the current instance.            |
    |             |                   |                                     |
    +-------------+-------------------+-------------------------------------+

Methods
=======



.. table::

    +----------------+--------------------------------------+-----------------------------------+
    | |ws| |ws|      | Name                                 | Description                       |
    +================+======================================+===================================+
    | |img_method|   | `parse(input)`_                      | Converts the string               |
    | \ |img_static| |                                      | representation of a version       |
    |                |                                      | number to an equivalent Version   |
    |                |                                      | object. Raises errors if input    |
    |                |                                      | has issues.                       |
    |                |                                      |                                   |
    +----------------+--------------------------------------+-----------------------------------+
    | |img_method|   | `try_parse(input)`_                  | Converts the string               |
    | \ |img_static| |                                      | representation of a version       |
    |                |                                      | number to an equivalent Version   |
    |                |                                      | object. Does not raise errors.    |
    |                |                                      |                                   |
    +----------------+--------------------------------------+-----------------------------------+
    | |img_method|   | `to_str()`_                          | Converts the value of the current |
    |                |                                      | Version object to its equivalent  |
    |                |                                      | String representation.            |
    |                |                                      |                                   |
    +----------------+--------------------------------------+-----------------------------------+
    | |img_method|   | `to_str(field_count)`_               | Converts the value of the current |
    |                |                                      | Version object to its equivalent  |
    |                |                                      | String representation. A          |
    |                |                                      | specified count indicates the     |
    |                |                                      | number of elements to return.     |
    |                |                                      |                                   |
    +----------------+--------------------------------------+-----------------------------------+
    | |img_method|   | `to_tuple()`_                        | Converts the value of the current |
    |                |                                      | Version object to its equivalent  |
    |                |                                      | tuple representation.             |
    |                |                                      |                                   |
    +----------------+--------------------------------------+-----------------------------------+
    | |img_method|   | `to_tuple(field_count)`_             | Converts the value of the current |
    |                |                                      | Version object to its equivalent  |
    |                |                                      | tuple representation. A specified |
    |                |                                      | count indicates the number of     |
    |                |                                      | elements to return.               |
    |                |                                      |                                   |
    +----------------+--------------------------------------+-----------------------------------+


.. |ws| unicode:: 0x00A0 0x00A0 0x00A0 0x00A0 0x00A0

.. |img_method| image:: ../_static/img/dev/method.png
                :width: 16 px
                :height: 11 px
.. |img_static| image:: ../_static/img/dev/static.png
.. |img_prop| image:: ../_static/img/dev/property.png

.. comment
    :py:attr: `build <verr.Version.build>`
    .. _major: Version.html#verr.Version.major
    .. _minor: Version.html#verr.Version.minor
    .. _build: Version.html#verr.Version.build
    .. _revision: Version.html#verr.Version.revision
    .. _major_revision: Version.html#verr.Version.major_revision
    .. _minor_revision: Version.html#verr.Version.minor_revision

.. _elements: Version.html#verr.Version.elements
.. _parse(input): Version.html#verr.Version.parse
.. _try_parse(input): Version.html#verr.Version.try_parse
.. _to_str(): Version.html#verr.Version.to_str
.. _to_str(field_count): Version.html#verr.Version.to_str
.. _to_tuple(): Version.html#verr.Version.to_tuple
.. _to_tuple(field_count): Version.html#verr.Version.to_tuple

.. |major| replace:: :py:attr:`~verr.Version.major`
.. |minor| replace:: :py:attr:`~verr.Version.minor`
.. |build| replace:: :py:attr:`~verr.Version.build`
.. |rev| replace:: :py:attr:`~verr.Version.revision`
.. |major_rev| replace:: :py:attr:`~verr.Version.major_revision`
.. |minor_rev| replace:: :py:attr:`~verr.Version.minor_revision`
.. |elements| replace:: :py:attr:`~verr.Version.elements`
