=====================
Hey Summit API Client
=====================


.. image:: https://img.shields.io/pypi/v/heysummit.svg
        :target: https://pypi.python.org/pypi/heysummit

.. image:: https://img.shields.io/travis/fzipi/heysummit.svg
        :target: https://travis-ci.com/fzipi/heysummit

.. image:: https://readthedocs.org/projects/heysummit/badge/?version=latest
        :target: https://heysummit.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/fzipi/hey-summit/shield.svg
     :target: https://pyup.io/repos/github/fzipi/hey-summit/
     :alt: Updates



Hey Summit API is a requests based client to the Hey Summit API.


* Free software: Apache 2.0 License
* Documentation: https://api-docs.heysummit.com/#introduction


Features
--------

All features from the HeySummit API are implemented. Sadly the API seems unversioned at this point so I cannot guarantee stability.

Examples
--------

The only required argument is the HeySummit API token.

This is an example usage::

  import argparse

  from heysummit.api import HeySummit, HeySummitException

  def list_attendees():
      attendees = hey.get_all_attendees()

      print("There are {n} attendees".format(len(attendees)))
      for attendee in attendees:
          print("id: {id}, email: {email}".format(
                  id=attendee['id'], email=attendee['email']
                  )
          )

  def get_events():
      events = hey.get_events(is_live=True)

      for event in events:
        print(event)

  # main

  # Parse Arguments
  parser = argparse.ArgumentParser(description='HeySummit interaction script.')
  parser.add_argument('-t', '--token', type=str, help='API Token. Example: jdoe.', required=True)

  args = parser.parse_args()

  hey = HeySummit(token=args.token)

  print(hey.get_all_attendees(event=5573))

  talks = hey.get_talks(event=5573, is_active=True)

  for talk in talks:
      print(talk)


