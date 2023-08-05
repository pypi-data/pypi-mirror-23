# BitField for [motorengine](https://github.com/heynemann/motorengine)
Custom field type for storing and retrieving bit-packed flags as enums.

Inspiration from [`enum.IntFlag` documentation](https://docs.python.org/3.6/library/enum.html#intflag).

## Installation
`motorengine-bitfield` requires a minimum Python version of 3.6.2.

Add the code directly to your project or install from pip with:
```shell
pip install motorengine-bitfield
```

## Examples
```python
from bitfield import BitField

# create an enum to use in our example
class UserFlags(enum.IntFlag):
    IS_ACTIVE                = enum.auto() # least-significant bit
    IS_ADMIN                 = enum.auto()
    HAS_LOGGED_IN            = enum.auto()
    HAS_SEEN_INTRO           = enum.auto()
    SUBSCRIBED_TO_NEWSLETTER = enum.auto() # most-significant bit

# use the enum in our Document mapping
class User(motorengine.Document):
    name  = StringField()
    email = StringField()
    flags = BitField(UserFlags)

# let's test one out!
user = User(
    name='Bit Field',
    email='example@bitfield.py',
    flags=(UserFlags.IS_ACTIVE | UserFlags.SUBSCRIBED_TO_NEWSLETTER),
)

# enum instances are serialized into an integer
user.to_son()
# {'name': 'Bit Field', 'email': 'example@bitfield.py', 'flags': 17}
user = loop.run_until_complete(
    user.save()
)

# and deserialized into the original enum
retrieved_user = loop.run_until_complete(
    User.objects.get(user._id)
)
retrieved_user.flags
# <UserFlags.SUBSCRIBED_TO_NEWSLETTER|IS_ACTIVE: 17>
bool(user.flags & UserFlags.IS_ADMIN)
# False

# a BitField value also be created with plain integers
int_user = loop.run_until_complete(
    User.objects.create(flags=(2**5 - 1))
)
loop.run_until_complete(User.objects.get(int_user._id)).flags
# <UserFlags.SUBSCRIBED_TO_NEWSLETTER|HAS_SEEN_INTRO|HAS_LOGGED_IN|IS_ADMIN|IS_ACTIVE: 31>

# or from strings of binary
str_user = loop.run_until_complete(
    User.objects.create(flags='01101'))
)
loop.run_until_complete(User.objects.get(str_user._id)).flags
# <UserFlags.HAS_SEEN_INTRO|HAS_LOGGED_IN|IS_ACTIVE: 13>
```

## Development
Tests are written with pytest and can be run with `python setup.py test`.

Pull requests always welcome!
