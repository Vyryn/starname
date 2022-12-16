==================================
Starname: Generate pronounceable star names from star designations
==================================

The ``starname`` module lets you generate random, pronounceable pseudo-words for a star's designation.
- The psudo-name for a given star doesn't change unless its letters and numbers change
- Names are (mostly) pronounceable
- Dashes, spaces, capitalization and other funky characters a name can pick up when copy pasting across the web are ignored
- Names are tested to be as short as possible while having a less than 1 in a million chance of duplicating
- Names should be evenly distributed throughout the namespace, and sensitive to change
  - WISE17412553 will have an entirely different name from WISE17412543


``starname`` is adapted from Gregory Haskins's ``gibbrish`` library_
.. _library: https://github.com/greghaskins/starname/blob/master/setup.py



Usage
-----

``starname`` creates a deterministic pseudo-word as a more memorable name than, say, WD 1054-226.

  >>> from starname import starname
  >>> star = Starname()
  >>> star.generate("WD 1054-226")
  'Qaiocoptoops'
  >>> star.generate("wd1054226")
  'Qaiocoptoops'
  >>> star.generate("SCR 1845-6357")
  'Puentlyiarkaurs'


It also works as a console script::

  ~$ starname WD1054-226
  Qaiocoptoops
  ~$ starname "WISE 1741+2553&"
  Swoudaueldimp
  ~$ starname wise17412553
  Swoudaueldimp
  ~$ starname wise17412543
  Druirfoskoegs

Installation
------------

To install the ``starname`` module and console script globally, clone this repository and run:

  ~$ python setup.py install

Updates
-------

- (2022.12.15)
   - Initial release

Contributions
-------------

Contributions welcome. Additional tests that ensure naming consistency and more precisely define uniqueness are appreicated.