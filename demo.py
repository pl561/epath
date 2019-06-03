#! /usr/bin/env python
# -*-coding:utf-8 -*


import sys
import os
import numpy as np
import pandas as pd
from epath import EPath



def demo():
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

    fname.writedf_tocsv(df)

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




def main():
    demo()


if __name__ == '__main__':
    sys.exit(main())