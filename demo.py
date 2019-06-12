#! /usr/bin/env python
# -*-coding:utf-8 -*

from __future__ import print_function
import sys
import os
HOME = os.environ["HOME"]
import numpy as np
import pandas as pd
from epath import EPath



def demo_basic():
    """
    demo showing basic usage and latex/csv manipulations

    """
    image_fname = EPath("/tmp/image.png")
    # let's change the extension
    image_fname2 = image_fname.replace_suffix(".png22")
    # change dir
    image_fname3 = image_fname2.replace_parents("/someotherdir/a/b")
    print(image_fname)
    print(image_fname2)
    print(image_fname3)


    home = EPath("/tmp")
    experiment_dir = home.join("experiments")
    experiment_dir.mkdir()

    # create a file name in the exp dir
    fname = experiment_dir.join("mydatafile.data")

    df = pd.DataFrame()
    df["count"] = np.arange(10)

    # fname.writedf_tocsv(df)

    # file name is
    print(fname)
    # stem is
    print(fname.stem())
    print(fname.suffix())
    print(fname.basename())

    # add data after stem
    fname2 = fname.add_after_stem("01010jlkjlkj_LKlKlkj")
    df["count2"] = np.arange(10, 20)
    fname2.writedf_tocsv(df)
    fname2.write_tex(df.to_latex())

    image_fname = EPath(HOME).join("Images/lena.png")
    image = image_fname.imread()


def demo_path_manipulations():
    file_name = EPath("/tmp/my_file.txt")

    for i in range(10):
        for j in range(10):
            # some processing here...
            p = file_name.add_after_stem("{}_{}".format(i, j))
            print(p)

    p_final = file_name.add_before_stem("awesome_experiment")
    print(p_final)

    # moving to another dir
    p_final2 = p_final.replace_parents("/tmp/somedir/somedir2")
    print(p_final2)

    # joining
    p_final3 = p_final.parent().join("../proc/omgdontsavehere")
    print(p_final3)


def demo_experimental_feature_setitem():
    """
    Experimental feature with __setitem__

    """
    image_fname = EPath("/tmp/image.png")
    npath = image_fname/"ff"/"jlkj"

    print("New path : ", npath)
    def brackets(s):
        return "[{}]".format(s)

    print(npath[0])
    print(npath[1])
    print(npath[2])
    print(npath[3])

    # this does not work... yet.
    # print(npath[1:3])

def main():
    demo_path_manipulations()


if __name__ == '__main__':
    sys.exit(main())