# EPath, an Enhanced Path Python module 

## Description
EPath is a module made to improve workflow efficiency and avoid bugs when dealing with multiple file paths.

## Installation or required packages via pip (Python 2.7)
    pip install pathlib
    pip install opencv-python
    pip install pandas
    pip install sphinx


## simple example:
    import cv2
    from epath import EPath
    path = EPath("image.png") # the image file name is "image.png"
    image = path.imread()
    blured_image = cv2.blur(image, (5, 5)
    new_path = path.add_after_stem("_filtered") # the new image file name is "image_filtered.png"
    new_path.imwrite(blured_image)


## How functions work
    example file path  : /a/b/dir/image.jpg.png
    basename()         : image.jpg.png
    stem()             : image.jpg
    stem().stem()      : image
    parent()           : /a/b/dir
    suffix()           : .png 

## How to build documentations
At the project root directory :

    cd docs
    make html

The **entry file** for documentation is docs/build/html/index.html. For those who use firefox :

    firefox docs/build/html/index.html
    
    
## Future features
   support urls to manipulate downloadable files, images, etc
   compatibility with Python 3
   compatibility with Windows
   
## TODO
* Remove pathlib.Path ?
* continue to write docstring for doctest
* develop experimental features such as ``__setitem__``
   
## Bugs, others, implementation choices

Undecided behavior

    import pathtools as pt
    ep = pt.EPath("/tmp/ttt/file.a.b.c")
    ep.add_after_stem("extra_param_")
    gives '/tmp/ttt/file.a.bextra_param_.c'
    
Compatibility issues with dots in paths

    /tmp/file_90.0.txt
    should we replace "." from floating values to "f" ?
    in this case, .0 is not meant to be an extension

Convention : only use "." for extensions/suffixes




