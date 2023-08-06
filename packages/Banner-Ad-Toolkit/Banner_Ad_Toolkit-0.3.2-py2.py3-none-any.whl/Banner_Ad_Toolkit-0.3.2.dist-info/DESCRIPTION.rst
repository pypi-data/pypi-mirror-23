Banner Ad Toolkit
=================

Author: Tim Santor tsantor@xstudios.agency

Overview
========

Banner ad development is, at its core, a very repetitive task. You
constantly do the same thing over and over. This toolkit aims to ease a
bit of that repetitive work and while the tasks it does are relatively
small, the speed and ease at which you can do them ends up saving you
precious time.

The workflow described below is one developed over many years of doing
banner ad design and development. While it may seem additional work at
first, I promise you will find that doing each and every campaign in
this way will greatly speed up your workflow. Now on to the good
stuff...

Requirements
============

-  Python 2.7.x
-  ImageMagick
-  pngquant
-  `ImageAlpha <https://pngmini.com/>`__
-  `ImageOptim <https://imageoptim.com/>`__

-  `nasm <http://www.nasm.us/>`__ - download latest tar.gz source code
-  `mozjpeg <https://github.com/mozilla/mozjpeg/releases>`__ - download
   latest tar.gz source code

   ::

       ./cjpeg -quality 60 -quant-table 2 -sample 1x1 -outfile ../crushed.jpg ../backup.jpg

**NOTE**: Image Optimization only works on a Mac at this time.

Install ``nasm`` and ``mozjpeg`` from source (optional)
=======================================================

1. Run ``./configure && make`` in the unzipped source directory
2. Hope you don’t get a million compilation errors.
3. If it succeeds, you’ll be able to run ``./cjpeg`` in this directory
4. You can run ``sudo make install`` if you want ``cjpeg`` installed
   system-wide.

Installation
============

You can install directly via pip:

::

    pip install Banner-Ad-Toolkit

Or from the BitBucket repository (master branch by default):

::

    git clone https://bitbucket.org/tsantor/banner-ad-toolkit
    cd banner-ad-toolkit
    sudo python setup.py install

Usage
=====

File Structure (Optional)
-------------------------

While not required, using the following project structure is recommended
as the command line defaults follow this convention which ends up making
the commands require less input from the user.

::

    PROJECT
    ├── HTML5
    │   ├── Prefix_160x600_Suffix
    │   │   ├── backup.jpg
    │   │   ├── script.js
    │   │   ├── style.css
    │   │   └── index.html
    │   ├── Prefix_300x250_Suffix
    │   │   ├── backup.jpg
    │   │   ├── script.js
    │   │   ├── style.css
    │   │   └── index.html
    │   ├── Prefix_300x600_Suffix
    │   │   ├── backup.jpg
    │   │   ├── script.js
    │   │   ├── style.css
    │   │   └── index.html
    │   ├── Prefix_728x90_Suffix
    │   │   ├── backup.jpg
    │   │   ├── script.js
    │   │   ├── style.css
    │   │   └── index.html
    ├── PSD
    └── adkit.ini

**NOTE**: When running any adkit command, ensure you run it from the
root of your project folder where the ``adkit.ini`` resides (see
recommended File Structure above)

Quickstart
----------

To quickly get up and running by generating a ``adkit.ini`` which allows
us to configure how adkit runs.

::

    adkit-quickstart

    NOTE: You will still need to edit the generated file, this just
    helps save some typing.

Generate HTML
-------------

Once you save out all your image assets for your HTML5 ads, get a jump
start on HTML creation. Simply run the following command:

::

    adkit-html doubleclick

**NOTE**: For all available commands, run ``adkit-html -h``.

Generate CSS
------------

Once you save out all your image assets for your HTML5 ads, get a jump
start on CSS creation. Simply run the following command:

::

    adkit-css doubleclick

**NOTE**: For all available commands, run ``adkit-css -h``.

Generate JS
-----------

Once you save out all your image assets for your HTML5 ads, get a jump
start on JS creation. Simply run the following command:

::

    adkit-js doubleclick

**NOTE**: For all available commands, run ``adkit-js -h``.

Optimize Images
---------------

If you want to optimize all images used in your ads, simply run the
following command:

::

    adkit-optimize

**NOTE**: For all available commands, run ``adkit-optimize -h``

Upload HTML5 Ads
----------------

If you want to upload all HTML5 ads to your server for client preview,
simply run the following command:

::

    adkit-upload

**NOTE**: For all available commands, run ``adkit-upload -h``

Package Ad Zips
---------------

If you want to package each HTML5 ad as a zip, simply run the following
command:

::

    adkit-zip

**NOTE**: For all available commands, run ``adkit-zip -h``

Ad Validation
-------------

You can check your ads for errors against popular target campaign
managers here:

-  `DCM <https://h5validator.appspot.com/dcm>`__
-  `AdWords <https://h5validator.appspot.com/adwords>`__
-  `DoubleClick <https://www.google.com/doubleclick/studio>`__
-  `Sizemek <https://platform.mediamind.com>`__

    Note: Each campaign manager has its own criteria for how ads should
    be built.

Issues
======

If you experience any issues, please create an
`issue <https://bitbucket.org/tsantor/banner-ad-toolkit/issues>`__ on
Bitbucket.


