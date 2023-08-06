DType-Decorate
==============

The DType-Decorate module defines two different decorators at the current state. These decorators can be used to
constrain the attributes of the decorated function to specific data types. This can help to keep functions clean
especially when they are written for a specific context. This is usually the case for scientific applications,
where functionality is often more important than clean code.


Installation
~~~~~~~~~~~~

You can either use `pip` to install the version from PyPI or git to install the probably more recent version from
github.

.. code-block:: bash

  git clone http://github.com/mmaelicke/dtype-decorate.git
  cd dtype-decorate
  pip install -r requirements.txt
  python setup.py install


.. code-block:: bash

  pip install dtype-decorate


Usage
~~~~~

There are two decorators so far: `accept` and `enforce`. `accept` will restrict the attribute data types to the
the defined ones, while `enforce` will try to convert the given attribute to a desired data type.
Both can also be used together, where `accept` does only make sense to be used after `enforce`.

Define a function that does only accept an `int` and a `float`.

.. code-block:: python

  @accept(a=int, b=float)
  def f(a, b):
    pass

You can also specify more than one data type allowed. Any attribute not given in the decorator will just be
ignored.

.. code-block:: python

  @accept(a=(int, float))
  def f(a, be_any_type)
    pass

  f(5, 'mystr')   # will run fine
  f('mystr', 5)   # will raise a TypeError

The `accept` decorator can also handle None type and callables like functions or lambda. These have to be specified
as a string.

.. code-block:: python

  @accept(a='None', b=('None', 'callable'))
  def f(a, b):
    pass

  f(None, None)           # will run fine
  f(None, lambda x: x)    # will run fine
  f(5, None)              # will raise a TypeError