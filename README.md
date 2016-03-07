# jythonStuff
Stuff needed to 'wrap' the python code using jython, in such a way that it can be used as a Java jar file!

Content of this repository:
- Stuff from jython (http://www.jython.org/)
For licence etc, please see http://www.jython.org/
- An updated Main.java, where the original is given in https://wiki.python.org/jython/JythonFaq/DistributingJythonScripts
Changes are minimal (only changed a few lines, these are commented).
As to licence issues: original licence, see https://wiki.python.org/jython/JythonFaq/DistributingJythonScripts
Any adaptation by myself: 'as free a licence as possible', given any licence issues from either Jython or the creators of the original Main.java.
- Two .py files:one called /Package/entrypoint.py which simply calls the other. This 'entrypoint.java' is suggested in the wiki page above.
The other .py file is in /Package/Lib: it is pdf_stitcher.py
This .py file is documented and copied from one of my other repositories: https://github.com/roelvanderplank/fork-of-pdf-stitcher
- A complete PyPFD2 libaray.
This is a (as of this moment yet UNaltered) fork of the original PyPDF2. See https://github.com/roelvanderplank/Fork-of-PyPDF2.


