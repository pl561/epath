#! /usr/bin/env python
# -*-coding:utf-8 -*

__author__ = "Pascal Lefevre"
__email__ = "plefevre561@gmail.com"

"""This module contains tools for manipulating Linux paths.
EPath is the main class and proposes lots of features.

In practice, it is possible to never manipulate the path string ever again. 
From the first line of codes to a highly developped project, this module 
gives an easier and more convenient time for programming. 

The number of bugs is also greatly reduced : at least once in his life, 
everyone has mistyped a file path 

# simple example:
    import cv2
    from epath import EPath
    path = EPath("image.png")
    image = path.imread()
    blured_image = cv2.blur(image, (5, 5)
    new_path = path.add_after_stem("_filtered")
    new_path.imwrite(blured_image) 


# how functions globally work : 
    example file path  : /a/b/dir/image.jpg.png
    basename()         : image.jpg.png
    stem()             : image.jpg
    stem().stem()
    parent()           : /a/b/dir
    suffix()           : .png 
    
In general, some functions do not really require documentation 
since their names are self explainatory.
    
# future features :
   support urls to manipulate downloadable files, images, etc
"""


import sys
import os
from shutil import copyfile
import pathlib
import cv2
# import image

def replace_dir(path_obj, newdir):
    """modify a pathlib.Path object parent"""
    name = os.path.join(newdir, path_obj.name)
    return name

def replace_suffix(path_obj, suffix):
    """replaces last suffix of path
    eg : image.jpg.png --> image.jpg.newsuffix"""
    if suffix.startswith('.'):
        basename = "".join([path_obj.stem, suffix])
    else:
        basename = "".join([path_obj.stem, '.', suffix])
    return os.path.join(str(path_obj.parent), basename)

def add_before_stem(path_obj, ssuffix):
    """add suffix (ssufix) before stem"""
    basename = "".join([ssuffix, path_obj.stem, path_obj.suffix])
    name = os.path.join(str(path_obj.parent), basename)
    return name

def add_after_stem(path_obj, ssuffix):
    """add suffix (ssufix) after stem"""
    basename = "".join([path_obj.stem, ssuffix, path_obj.suffix])
    name = os.path.join(str(path_obj.parent), basename)
    return name


class EPath:
    """Enhanced Path class with several useful features
    behavior : uses functions, not attributes and returns EPath objects

    odd case : -- import pathtools as pt
               -- ep = pt.EPath("/tmp/ttt/file.a.b.c")
               -- ep.add_after_stem("extra_param_")
               >> '/tmp/ttt/file.a.bextra_param_.c'

    """
    def __init__(self, obj):
        """init function can take different objects such as :
           - str obj
           - pathlib.Path obj
           - EPath obj itself"""
        if isinstance(obj, str):
            if obj.endswith('/'):
                self.path_str = obj[:-1]
            else:
                self.path_str = obj
            self.path_obj = pathlib.Path(self.path_str)
        elif isinstance(obj, pathlib.Path):
            self.path_obj = obj
            self.path_str = str(obj)
        elif isinstance(obj, EPath):
            self.path_obj = obj.path_obj
            self.path_str = obj.path_str
        else:
            raise ValueError("not a str, not a pathlib.Path obj, "
                             "not a EPath !")

    def parent(self):
        """:returns the current path parent"""
        return EPath(str(self.path_obj.parent))

    def stem(self):
        """:returns the current path stem (basename without extension)"""
        return EPath(self.path_obj.stem)

    def stem_noparam(self):
        """:returns the current path stem without stem suffix"""
        return EPath(self.stem().string().split('_')[0])

    def basename(self):
        """:returns the base file name of the current path"""
        return EPath(self.path_obj.name)

    def suffix(self):
        """:returns the suffix (or file extention)"""
        return EPath(self.path_obj.suffix)

    def has_suffix(self):
        """tests for suffix (or extension) existence"""
        if len(self.path_obj.suffix) == 0:
            return False
        else:
            return True

    def add_suffix(self, suffix):
        """:returns a new EPath obj with a new suffix to the current path"""
        if suffix.startswith("."):
            suffix = suffix[1:]
        p = ".".join([self.path_str, suffix])
        return EPath(p)

    def exists(self):
        """tests if path exists on the hdd"""
        return self.path_obj.exists()

    def is_dir(self):
        """tests if path is a directory"""
        return self.path_obj.is_dir()

    def is_file(self):
        """tests if path is a file"""
        return self.path_obj.is_file()

    def is_readable(self):
        """tests for read access"""
        return os.access(self.path_str, os.R_OK)

    def is_writable(self):
        """test for write access"""
        return os.access(self.path_str, os.W_OK)

    def is_executable(self):
        return os.access(self.path_str, os.X_OK)

    def mkdir(self, raiseException=False):
        """silent mkdir"""
        if not self.exists():
            self.path_obj.mkdir()
        else:
            if raiseException:
                self.path_obj.mkdir()

    def touch(self):
        """creates a file at the current path but does
        not erase its content if it exists"""
        self.path_obj.touch()

    def removefile(self):
        """removes the file at the current path"""
        if self.is_file():
            if self.exists():
                return os.remove(self.path_str)
        else:
            raise ValueError("This is not a file !")

    def removedir(self):
        """removes the directory at the current path"""
        if self.is_dir():
            if self.exists():
                return os.rmdir(self.path_str)
        else:
            raise ValueError("This is not a directory !")

    def string(self):
        return self.__str__()

    def replace_parents(self, new_parents, obj=True):
        """replaces all parents by np, if obj is True, returns an object"""
        path = os.path.join(str(new_parents), self.basename().string())
        return EPath(path) if obj else path

    def replace_suffix(self, new_suffix, obj=True):
        """replaces last suffix of path"""
        if new_suffix.startswith('.'):
            basename = "".join([self.stem().string(), new_suffix])
        else:
            basename = "".join([self.stem().string(), '.', new_suffix])
        path = os.path.join(self.parent().string(), basename)
        return EPath(path) if obj else path

    def add_before_stem(self, ssuffix, sep='_', obj=True):
        """add suffix (ssufix) before stem"""
        basename = "".join(
            [
            ssuffix,
            sep,
            self.stem().string(),
            self.suffix().string()
            ])
        path = os.path.join(self.parent().string(), basename)
        return EPath(path) if obj else path

    def add_after_stem(self, ssuffix, sep='_', obj=True):
        """add suffix (ssufix) after stem"""
        basename = "".join(
            [self.stem().string(),
             sep,
             ssuffix,
             self.suffix().string()
             ])
        path = os.path.join(self.parent().string(), basename)
        return EPath(path) if obj else path

    def add_param(self, psuffix, sep='_', obj=True):
        """add parameters suffix after stem"""
        # if dict then name params in psuffix
        # else just put values
        if isinstance(psuffix, dict):
            keys = list(map(str, psuffix.keys()))
            values = list(map(str, psuffix.values()))
            ssuffix = "_".join("".join(item) for item in zip(keys, values))
        elif isinstance(psuffix, list) or isinstance(psuffix, tuple):
            ssuffix = "_".join(map(str, psuffix))
        else:
            raise ValueError("psuffix has not the right type")

        return self.add_after_stem(ssuffix, obj=obj)


    def join(self, extrapath, obj=True):
        """receive a path and append it to the current path
        work similarly as the os.join function"""
        if isinstance(extrapath, list) or isinstance(extrapath, tuple):
            r = os.path.join(self.path_str, *extrapath)
        else:
            r = os.path.join(self.path_str, str(extrapath))
        assert obj in [True, False]
        return EPath(r) if obj else str(r)

    def __add__(self, extrasuffix):
        """concatenate extrasuffix with path_str stem
           eg : /tmp/file + hello --> /tmp/filehello"""
        # assert not extrasuffix.startswith("/"), "use / operator instead"
        r = self.path_str + extrasuffix
        return EPath(r)

    def __div__(self, extrapath):
        """simulates / like linux paths but in Python code
           returns an EPath object"""
        print(extrapath)
        return self.join(EPath(extrapath))
    __floordiv__ = __truediv__= __div__


    def __getitem__(self, item):
        """parents and basename access in a list
           it is basically indexed access to the split path by /"""
        items = self.path_str.split('/')
        if self.path_str.startswith('/'):
            items[0] = '/'
        return EPath(items[item])


    def imread(self, **kwds):
        """reads an image using OpenCV"""
        return cv2.imread(self.path_str, **kwds)

    def imwrite(self, img):
        """write an image (numpy array) using OpenCV"""
        r = cv2.imwrite(self.path_str, img)
        msg = "Could not write img at {}".format(self.path_str)
        assert self.exists(), msg

    def write(self, content, mode=""):
        """write content to the current path"""
        with open(self.path_str, mode=mode) as fd:
            fd.write(content)

    # def write_csv(self, csv_content):
    #     if self.has_suffix():
    #         fname = self.replace_suffix(".csv").string()
    #     else:
    #         fname = self.add_suffix(".csv").string()
    #     with open(fname, mode="w") as fd:
    #         fd.write(csv_content)

    def writedf_tocsv(self, df, sep=";"):
        """receives a pandas.DataFrame object and saves its csv version"""
        if self.has_suffix():
            fname = self.replace_suffix(".csv").string()
        else:
            fname = self.add_suffix(".csv").string()
        df.to_csv(fname, sep=sep)

    def write_tex(self, tex_content, mode="w"):
        """receives a latex string content and modify or add the .tex suffix
        and saves it at the Epath instance location"""
        if self.has_suffix():
            fname = self.replace_suffix(".tex").string()
        else:
            fname = self.add_suffix(".tex").string()
        with open(fname, mode=mode) as fd:
            fd.write(tex_content)

    def copyto(self, dir):
        """copy the file at current path to a new directory dir"""
        if EPath(dir).is_dir():
            copyfile(self.string(), self.replace_parents(dir).string())
        else:
            raise ValueError("cannot copy, not a dir")



    def __str__(self):
        return "{}".format(self.path_str)
    __repr__ = __str__



def main():
    pass


if __name__ == '__main__':
    sys.exit(main())