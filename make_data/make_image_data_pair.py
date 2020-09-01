#!/usr/bin/env python

# Make a bare-bones imitation of a ten-year rainfall sheet
#  use random data.

import os

# All the details are in the tyrImage class
from tyrImage import tyrImage

# Specify where to put the output
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--docn", help="Document name", type=str, required=True)
parser.add_argument(
    "--opdir", help="output directory name", default=None, type=str, required=False
)
parser.add_argument("--xshift", help="pixels", type=int, default=None, required=False)
parser.add_argument("--yshift", help="pixels", type=int, default=None, required=False)
parser.add_argument(
    "--rotate", help="degrees clockwise", type=int, default=None, required=False
)
args = parser.parse_args()
if args.opdir is None:
    args.opdir = ("%s/OCR-fake") % os.getenv("SCRATCH")

# Pass all the image control options to image creation function
a = vars(args)
kwargs = {i: a[i] for i in a if i not in ["docn", "opdir"]}

ic = tyrImage(args.opdir, args.docn, **kwargs)
ic.makeImage()
ic.makeNumbers()
