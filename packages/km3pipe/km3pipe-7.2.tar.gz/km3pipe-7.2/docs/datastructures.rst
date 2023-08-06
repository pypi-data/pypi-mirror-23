Data Structures
===============

.. contents:: :local:

This section describes the basic data structures which a **pump** usually
provides via the **blob** dictionary. The pump is responsible to parse
the data and create a **blob** (a simple Python dictionary) for each
event in the file. When processing a data file with KM3Pipe, a module
chain is being utilised to cycle through the events. Each module within
the chain recieves the original, unaltered data from the pump and
further also additional information created by the preceeding modules.

Hits and McHits
---------------

If you want to analyse the hits or create your own recunstruction, these two
are the the most important ones.
The class used in KM3Pipe to represent a bunch of hits is called
``RawHitSeries`` and ``McHitSeries``.
The ``RawHitSeries`` comes with ``dom_id``, ``channel_id``, ``tot``, ``time``
and ``triggered`` and the ``McHitSeries`` has ``a``, ``origin``, ``time`` and
``pmt_id``.

+---------------+------------+---------------------------------+
| information   | dict key   | container type                  |
+===============+============+=================================+
| Raw Hits      | Hits       | RawHitSeries (np.ndarray-like)  |
+---------------+------------+---------------------------------+
| MC Hits       | McHits     | McHitSeries (np.ndarray-like)   |
+---------------+------------+---------------------------------+

The ``*Series`` classes are basically numpy ndarrays (you can access the
actual numpy array through the ``._arr`` attribute), but you can also iterate
through them (including slicing) and get instances of ``RawHit`` or ``McHit``
will.
Both the ``*Series`` and the elementary hit classes have attributes which can
be accessed through the following getters:

+---------------------+--------------+-----------+-----------+----------+
| information         | getter       | type      | RawHit    | McHit    |
+=====================+==============+===========+===========+==========+
| hit time            | .time        | numeric   | X         | X        |
+---------------------+--------------+-----------+-----------+----------+
| time over threshold | .tot         | numeric   | X         |          |
+---------------------+--------------+-----------+-----------+----------+
| a (number of p.e.)  | .a           | numeric   |           | X        |
+---------------------+--------------+-----------+-----------+----------+
| PMT ID              | .pmt_id      | numeric   |           | X        |
+---------------------+--------------+-----------+-----------+----------+
| Channel ID          | .channel_id  | numeric   | X         |          |
+---------------------+--------------+-----------+-----------+----------+
| DOM ID              | .dom_id      | numeric   | X         |          |
+---------------------+--------------+-----------+-----------+----------+
| trigger information | .triggered   | bool      | X         |          |
+---------------------+--------------+-----------+-----------+----------+
| origin (track ID)   | .origin      | numeric   |           | X        |
+---------------------+--------------+-----------+-----------+----------+

Note that if you access ``.tot`` of a ``RawHitSeries`` for example, you will
get a 1D numpy array containing all the ToTs of the hits (in the order of the
hits). So you can for example quickly have a look at the ToT distribution of
the full event.

In order to obtain the position, direction and the t0 correction, you
need to apply a geometry. KM3Pipe provides the ``Geometry`` class to do this
for you.

To create a geometry from a detector file::

    geo = kp.Geometry(filename="path/to/detector.detx")


To apply the geometry to a set of hits::

    calibrated_hits = geo.apply(hits)

That's it, you will get a ``HitSeries`` instance with ``pos_x``, ``pos_y``,
... and also ``dir_x``, ``dir_y``...
