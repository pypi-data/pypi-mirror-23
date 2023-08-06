# -*- coding: utf-8 -*-

"""
==========================================================
HORUS: Named Entity Recognition Algorithm
==========================================================

HORUS is a Named Entity Recognition Algorithm specifically
designed for short-text, i.e., microblogs and other noisy
datasets existing on the web, e.g.: social media, some web-
sites, blogs and etc..

It is a simplistic approach based on multi-level machine
learning combined with computer vision techniques.

more info at: https://github.com/dnes85/components-models

"""

# Author: Esteves <diegoesteves@gmail.com>
# Version: 1.0
# Version Label: HORUS_NER_2016_1.0
# License: BSD 3 clause
from optparse import OptionParser

from src.horus.components.core import Core


def main():

    op = OptionParser(usage='usage: %prog [options] arguments')

    op.add_option("--input_text", dest="input_text",
                  help="The text to be annotated")

    op.add_option("--input_file", dest="input_file",
                  help="The file to be annotated")

    op.add_option("--ds_format", dest="ds_format", default=0,
                  help="The format to be annotated [0 = free text (default), 1 = Ritter]")

    op.add_option("--output_file", dest="output_file", default="horus_out",
                  help="The output file")

    op.add_option("--output_format", dest="output_format", default="json",
                  help="The output file type")

    (opts, args) = op.parse_args()
    print(__doc__)
    op.print_help()

    if not opts.input_text and not opts.input_file:
        op.error('inform either an [input_text] or [input_file] as parameter!')

    horus = Core(False, 5)
    print horus.version_label
    ret = horus.annotate(opts.input_text, opts.input_file, opts.ds_format, opts.output_file, opts.output_format)
    print ret

if __name__ == '__main__':
    main()
