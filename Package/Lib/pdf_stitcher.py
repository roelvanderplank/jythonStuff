#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright addition: code from original project(Lageos/pdf-stitcher) under copyright of that project
# All changes (lines between "# --- Aanpassing sourcecode" and "# --- Einde aanpassing sourcecode") released under most permissive licence possible
# (whatever that might be)
from __future__ import print_function, division, with_statement
import PyPDF2
# --- Aanpassing sourcecode! ---
# import csv
# I do not need csv anymore, as I happen to KNOW how many pages I will use...
# --- Einde aanpassing sourcecode ---
import sys

# --- Aanpassing sourcecode! ---
__version__ = '0.2'
# --- Einde aanpassing sourcecode ---
# --- Pattern Stitcher ---

def addright(page, right_page, tx=0):
    """Adds page (PageObject) on the right side, tx is an addtional offset"""
    page.mergeTranslatedPage(right_page, page.mediaBox[2] + tx, 0, expand=True)
    return page


def main():
    print('## PDF Stitcher ##')
    print('Version:', __version__)
    tx = 0
    ty = 0
    # --- Aanpassing sourcecode! ---
    tx = -15
    ty = -37
    # --- Einde aanpassing sourcecode ---
    with open(sys.argv[1], 'rb') as input:
        pdf = PyPDF2.PdfFileReader(input)
        print("Number of Pages: %1.2i" % pdf.getNumPages())

        first_page = True
        # --- Aanpassing sourcecode! ---
        # I do not need a csv file, I happen to KNOW which pages to add.
        # Indeed, it is 'n', 'n+1' all the way to the last page, which is 'n+15'
        numberPages = pdf.getNumPages()
        firstPage = numberPages - 15
        print("First page is: %1.2i" % firstPage)
        first_page = True
        rows = []
        for row in range(0,3):
            for page in range(0,3):
                print("Reading page %1.2i" % int(page + row + row + row + row))
                if first_page is True:
                    output = pdf.getPage(int(firstPage + row + row + row + row + page - 1))
                    first_page = False
                else:
                    output = addright(output, pdf.getPage(int(firstPage + row + row + row + row + page -1)), tx)
            rows.append(output)
            first_page = True
            # --- Einde aanpassing sourcecode ---

        print("Stitching lines of pages ...")
        first_line = True
        for row in reversed(rows):
            if first_line is True:
                output = rows[-1]
                first_line = False
            else:
                output.mergeTranslatedPage(row, 0, output.mediaBox[3] + ty, expand=True)

        print("Saving new file...")
        # --- Aanpassing sourcecode! ---
        # As I do not use a 'pattern' file, I only need TWO arguments: inputfile and outputfile. Hence '3'=>'2'
        with open(sys.argv[2], 'wb') as out_file:
        # --- Einde aanpassing sourcecode ---
            pdf_out = PyPDF2.PdfFileWriter()
            pdf_out.addPage(output)
            pdf_out.write(out_file)
    print("Finished.")
    return

if __name__ == "__main__":
    main()
