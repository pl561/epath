.. Epath documentation master file, created by
   sphinx-quickstart on Sun Jul  7 08:40:25 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Epath's documentation!
=================================
.. toctree::
   :maxdepth: 2
   :caption: Contents:

   modindex
   demoindex

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

What is Epath?
**************  
This module contains tools for manipulating Linux paths. EPath is the main class and proposes lots of features.

In practice, it is possible to never manipulate the path string ever again.  From the first line of codes to a highly developped project, this module 
gives an easier and more convenient time for programming. 

The number of bugs is also greatly reduced : at least once in his life, everyone has mistyped a file path 

Install required modules
************************
::
    
    pip-install pathlib
    pip-install opencv-python

Simple example
**************
::
        
    import cv2
    from epath import EPath
    path = EPath("image.png")
    image = path.imread()
    blured_image = cv2.blur(image, (5, 5)
    new_path = path.add_after_stem("_filtered")
    new_path.imwrite(blured_image) 

How functions globally work
*************************** 
::

    example file path  : /a/b/dir/image.jpg.png
    basename()         : image.jpg.png
    stem()             : image.jpg
    stem().stem()      : image
    parent()           : /a/b/dir
    suffix()           : .png 


Future features
****************
   
   * support urls to manipulate downloadable files, images, etc
   * compatibility with Python 3
   * compatibility with Windows



