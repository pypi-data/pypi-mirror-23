=========
MetaSetup
=========

A package for configuring settings and initializing objects.

-------
Summary
-------

With ``metasetup``, there are no configuration files, just python modules which import
and modify settings. This means, that these modules can be used as a "meta" layer on top
of normal configuration files, or to programatically configure the settings themselves.
To access the settings for a particular module, one need only import it with ``metasetup``
as a prefix (e.g. ``from metasetup.my_package import my_module``) and use its attributes.

------------------------
Installation and Testing
------------------------

Install ``metasetup`` using ``pip``:

.. code-block:: text
    
    pip install metasetup

Run the tests with ``pytest``:

.. code-block:: text
    
    py.test metasetup

For a developer's installation:

1. clone this github repository
2. ``cd`` into the parent directory
3. run ``$ pip install -e .``

-----------
Basic Usage
-----------

For demonstration purposes, we can create a contrived scenario in which the python module
configuring settings and the one being configured are the same. Consider a python file
called ``my_module.py`` with the following contents:

.. code-block:: python

    # We define an object which should be configured

    from metasetup import Configurable, import_settings

    class MyClass(Configurable):
        """The class whose instances we are about to configure"""
        pass

    # Import the settings we wish to configure (we could also use `import_settings`)

    from metasetup.my_module import MyClass as MyClassSettings

    # Then, modify the settings as we please

    MyClassSettings.x = 1
    print(MyClassSettings)

    # Finally, we can create an instance of our class and configure it

    mc = MyClass()
    mc.configure()
    print(mc.x)

    # Vualá! The instances of our class can be configured.
