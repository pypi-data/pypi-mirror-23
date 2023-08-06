FFfilter
========

Filters media files by testing criteria against header metadata
extracted by `ffprobe <https://ffmpeg.org/ffprobe.html>`__.

Install
-------

.. code:: bash

    pip install fffilter

Dependencies
------------

-  **FFfilter** uses
   `subprocess <https://docs.python.org/3/library/subprocess.html>`__ to
   access the system installation of **ffprobe**.
-  `colorama <https://pypi.python.org/pypi/colorama>`__ will be
   automatically installed by **pip**.

Use
---

Command-line tool
~~~~~~~~~~~~~~~~~

``-s`` ``--show`` *[key]*
^^^^^^^^^^^^^^^^^^^^^^^^^

**Returns a tab-separated list of all values of [key].**

.. code:: bash

    # Return the value(s) of display_aspect_ratio
    fffilter /path/to/file --show display_aspect_ratio

.. code:: bash

    # Return a list of files, surfacing all possible values of given keys
    # (note that '-' must be first argument when receiving piped input if using --show)
    find . -name '*.mp4' | fffilter - --show codec_name codec_type display_aspect_ratio

``-m`` ``--match`` *[key]* *[value]*
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Lists files which match all criteria:**

-  matching files are listed on ``stdout``
-  non-matching files are listed on ``stderr``, printed over a red
   background

Simply pass key and value pairs to repeating occurrences of the
``--match`` parameter.

.. code:: bash

    # Return absoulte path for file if its header declares 4:3 aspect
    fffilter /path/to/file --match display_aspect_ratio 4:3

.. code:: bash

    # Filter a list of files for h.264-encoded full-HD mp4s
    find . -name '*.mp4' | fffilter --match codec_name h264 --match height 1080 --match width 1920 -

Module
~~~~~~

.. code:: python

    from fffilter import fffilter

    path = 'media/some_file.mp4'

    # The show() method requires a path and a list of keys
    d = fffilter.show(path, ['codec_type', 'display_aspect_ratio'])

    # The match() method requires a path and either key=value pairs or a packed dictionary: **{'key':'value'}
    m = fffilter.match(path, codec_type='video', display_aspect_ratio='16:9')

    print(d)
    print(m)

::

    {'display_aspect_ratio': [u'16:9'], 'codec_type': [u'audio', u'video']}
    True

You can also call ``ffprobe(path)`` to access a dictionary of the
complete headers:

.. code:: bash

    headers = fffilter.ffprobe(path)
    print(headers)

::

    {u'streams': [{u'pix_fmt': u'yuv420p', u'sample_aspect_ratio': u'1:1', u'refs': 1, u'codec_type': u'video', u'coded_height': 720
    ...

Disclaimer
----------

This Python Package is not affiliated with
`FFmpeg <https://ffmpeg.org/>`__ or
`FFprobe <https://ffmpeg.org/ffprobe.html>`__.

Credits
-------

**FFfilter** was written by `Edward
Anderson <https://twitter.com/anderson_edw>`__, British Film Institute.

Licence
-------

`Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA
4.0) <https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode>`__
