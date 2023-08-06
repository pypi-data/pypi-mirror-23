Regenmaschine: A Simple Python Library for RainMachine™
=======================================================

.. image:: https://img.shields.io/pypi/v/regenmaschine.svg
  :target: https://pypi.python.org/pypi/regenmaschine

.. image:: https://travis-ci.org/bachya/regenmaschine.svg?branch=master
  :target: https://travis-ci.org/bachya/regenmaschine

.. image:: https://img.shields.io/badge/SayThanks-!-1EAEDB.svg
  :target: https://saythanks.io/to/bachya

Regenmaschine (German for "rain machine") is a simple, clean, well-tested Python
library for interacting with `RainMachine smart sprinkler controllers
<http://www.rainmachine.com/>`_. It gives developers an easy API to manage their
controllers over a LAN or via RainMachine's cloud API.

💧 Installation
===============

.. code-block:: bash

  $ pip install regenmaschine

💧 Usage
========

Authentication
--------------

First, we need to authenticate. Authentication can be done against the local
device or the cloud API:

.. code-block:: python

  import regenmaschine as rm

  # Using the local API:
  auth = rm.Authenticator.create_local('<DEVICE_IP_ADDRESS>', '<PASSWORD>')

  # Using the remote API:
  auth = rm.Authenticator.create_remote('<EMAIL ADDRESS>', '<PASSWORD>')

If authentication is successful, this :code:`auth` object can then be used to
create a client:

.. code-block:: python

  client = rm.Client(auth)

Diagnostics
-----------

More info on responses, etc: `<http://docs.rainmachine.apiary.io/#reference/diagnostics>`_

.. code-block:: python

  client.diagnostics.current() # Returns current diagnostic info
  client.diagnostics.log()     # Returns entire device log

Programs
--------

More info on responses, etc: `<http://docs.rainmachine.apiary.io/#reference/programs>`_

.. code-block:: python

  client.programs.all()     # Returns all program info
  client.programs.get(1)    # Returns info about a single program
  client.programs.next()    # Returns the next run date/time for all programs
  client.programs.running() # Returns all running programs
  client.programs.start(7)  # Starts a program
  client.programs.stop(7)   # Stops a program

Restrictions
------------

More info on responses, etc: `<http://docs.rainmachine.apiary.io/#reference/restrictions>`_

.. code-block:: python

  client.restrictions.current()   # Returns currently active restrictions
  client.restrictions.hourly()    # Returns restrictions over the next hour
  client.restrictions.raindelay() # Returns all restrictions due to rain
  client.restrictions.universal() # Returns the global list of restrictions

Stats
-----

More info on responses, etc: `<http://docs.rainmachine.apiary.io/#reference/daily-stats>`_

.. code-block:: python

  client.stats.on_date('6/29/2017')           # Returns all stats for a date
  client.stats.on_date('2017-06-29')          # Returns all stats for a date
  client.stats.on_date('1 week ago')          # Returns all stats for a date
  client.stats.upcoming()                     # Returns expected stats for the next 7 days
  client.stats.upcoming(include_details=True) # Deeper look at the next 7 days

Watering
--------

More info on responses, etc: `<http://docs.rainmachine.apiary.io/#reference/watering>`_

.. code-block:: python

  # log() can have any number of the parameters shown here:
  client.watering.log()                 # Returns log of all watering
  client.watering.log(details=True)     # Returns comprehensive log of all watering
  client.watering.log('6/29/2017', 2)   # Returns log for 6/27-6/29
  client.watering.log('2017-06-29', 2)  # Alternate view of log()
  client.watering.log('2 days ago', 3)  # Returns log 2-5 days ago

  client.watering.queue()               # Returns the active queue of watering activities
  client.watering.runs('6/29/2017', 2)  # Alternate view of log()
  client.watering.runs('2017-06-29', 2) # Alternate view of log()
  client.watering.runs('2 days ago', 3) # Alternate view of log()
  client.watering.stop_all()            # Immediately stops all programs and zones

Weather Services
----------------

More info on responses, etc: `<http://docs.rainmachine.apiary.io/#reference/weather-services>`_

.. code-block:: python

  client.parsers.current() # Returns current weather services being used

Zones
-----

More info on responses, etc: `<http://docs.rainmachine.apiary.io/#reference/zones>`_

.. code-block:: python

  client.zones.all()                            # Returns all zone info
  client.zones.all(advanced_properties=True)    # Returns advanced info for all zones
  client.zones.get(2)                           # Returns advanced info about a single zone
  client.zones.get(2, advanced_properties=True) # Returns info about a single zone
  client.zones.start(3, <number_of_seconds>)    # Starts a zone for X seconds
  client.zones.stop(3)                          # Stops a zone

Exceptions
----------

Regenmaschine relies on two other libraries:
`Requests <https://github.com/requests/requests>`_ and
`Maya <https://github.com/kennethreitz/maya>`_; as such, Regenmaschine may
raise any of the exceptions that they provide.

Beyond that, Regenmaschine defines a few exceptions of its own:

* :code:`BrokenAPICall`: returned when an API call only works on the local or remote
  APIs, but not both
* :code:`InvalidAuthenticator`: returned when invalid authentication data is fed
  into :code:`rm.Authenticator.load()` or :code:`rm.Authenticator.loads()`

Authentication Caching
----------------------

Although there doesn't appear to be a limit to the number of times RainMachine
will allow authentication to occur, for speed/efficiency, it is often desirable
to use the same credentials long-term. The :code:`auth` object can be dumped
and saved in any number of manners:

.. code-block:: python

  # Outputs a dict:
  auth_json = auth.dump()

  # Outputs a string version of the dict:
  auth_str = auth.dumps()

At any point, this authentication can be loaded back into a Regenmaschine
client:

.. code-block:: python

  # Outputs a dict:
  auth.load(auth_json)

  # Outputs a string version of the dict:
  auth.loads(auth_str)

*Beware:* the dumped :code:`auth` object contains the access token needed to
query the API, as well as the information needed to reconstruct the client.
Therefore, it should be cached and stored securely.

💧 Contributing
===============

#. Check for open features/bugs or initiate a discussion on one.
#. Form the repository and make your changes on a new branch.
#. Write a test that covers your new functionality.
#. Run tests: :code:`make test`
#. Build new docs: :code:`make docs`
#. Add yourself to AUTHORS.rst.
#. Submit a pull request!
