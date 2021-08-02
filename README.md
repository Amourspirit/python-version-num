# Version Class

Represents a version number. This class cannot be extended.
Sealed Class

## Installation

You can install the Version Class from [PyPI](https://pypi.org/project/verr/):

```python
pip install verr
```

## Constructors

|                                                                 | Name                                   | Description                                                                                                   |
|-----------------------------------------------------------------|----------------------------------------|---------------------------------------------------------------------------------------------------------------|
| ![Img-Method.gif](https://i.postimg.cc/QCSwCbL3/Img-Method.gif) | Version()                              | Initializes a new instance of the Version class.                                                              |
| ![Img-Method.gif](https://i.postimg.cc/QCSwCbL3/Img-Method.gif) | Version(ver_str)                       | Initializes a new instance of the Version class using the specified string to be parsed                       |
| ![Img-Method.gif](https://i.postimg.cc/QCSwCbL3/Img-Method.gif) | Version(version)                       | Initializes a new instance of the Version class using the specified version.                                  |
| ![Img-Method.gif](https://i.postimg.cc/QCSwCbL3/Img-Method.gif) | Version(major, minor)                  | Initializes a new instance of the Version class using the specified major and minor values.                   |
| ![Img-Method.gif](https://i.postimg.cc/QCSwCbL3/Img-Method.gif) | Version(major, minor, build)           | Initializes a new instance of the Version class using the specified major, minor, and build values.           |
| ![Img-Method.gif](https://i.postimg.cc/QCSwCbL3/Img-Method.gif) | Version(major, minor, build, revision) | Initializes a new instance of the Version class with the specified major, minor, build, and revision numbers. |

## Properties

|                                                                     | Name           | Description                                                                                    |
|---------------------------------------------------------------------|----------------|------------------------------------------------------------------------------------------------|
| ![Img-Property.gif](https://i.postimg.cc/kMykTn2p/Img-Property.gif) | major          | Gets the value of the major component of the version number for the current Version object.    |
| ![Img-Property.gif](https://i.postimg.cc/kMykTn2p/Img-Property.gif) | minor          | Gets the value of the minor component of the version number for the current Version object.    |
| ![Img-Property.gif](https://i.postimg.cc/kMykTn2p/Img-Property.gif) | build          | Initializes a new instance of the Version class using the specified major and minor values.    |
| ![Img-Property.gif](https://i.postimg.cc/kMykTn2p/Img-Property.gif) | revision       | Gets the value of the revision component of the version number for the current Version object. |
| ![Img-Property.gif](https://i.postimg.cc/kMykTn2p/Img-Property.gif) | major_revision | Gets the high 16 bits of the revision number.                                                  |
| ![Img-Property.gif](https://i.postimg.cc/kMykTn2p/Img-Property.gif) | minor_revision | Gets the low 16 bits of the revision number.                                                   |

## Methods

|                                                                                                                                | Name                | Description                                                                                                                                               |
|--------------------------------------------------------------------------------------------------------------------------------|---------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![Img-Method.gif](https://i.postimg.cc/QCSwCbL3/Img-Method.gif)![Img-Static.png](https://i.postimg.cc/zGMmT0yD/Img-Static.png) | parse(input)        | Converts the string representation of a version number to an equivalent Version object. Raises errors if input has issues.                                |
| ![Img-Method.gif](https://i.postimg.cc/QCSwCbL3/Img-Method.gif)![Img-Static.png](https://i.postimg.cc/zGMmT0yD/Img-Static.png) | try_parse(input)    | Converts the string representation of a version number to an equivalent Version object. Does not raise errors.                                            |
| ![Img-Method.gif](https://i.postimg.cc/QCSwCbL3/Img-Method.gif)                                                                | to_str()            | Converts the value of the current Version object to its equivalent String representation.                                                                 |
| ![Img-Method.gif](https://i.postimg.cc/QCSwCbL3/Img-Method.gif)                                                                | to_str(field_count) | Converts the value of the current Version object to its equivalent String representation. A specified count indicates the number of components to return. |

## Usage

```python
from verr import Version

v = Version(1, 2, 3, 4)
print(v.major) # 1
print(v.minor) # 2
print(v.build) # 3
print(v.revision) # 4
print(v) # 1.2.3.4

v = Version.parse("1.2.3")
print(v.major) # 1
print(v.minor) # 2
print(v.build) # 3

v1 = Version.parse("1.2.2")
v2 = Version.parse("1.2.3")
print(v1 > v2) # False
print(v1 <= v2) # True

v = Version(1,2,3, int("ffbbff0b", 16))
print(v.major_revision == int("ffbb", 16)) # True
print(v.minor_revision == int("ff0b", 16)) # True
print(v) # 1.2.3.4290510603
print(v.to_str(3)) # 1.2.3

v_result = Version.try_parse("22.3")
if v_result[0] == True:
  v = v_result[1]
  print(v) # 22.3
else:
  err = v_result[1]
  print(e)
```
