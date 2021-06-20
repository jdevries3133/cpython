====================
My Segfault Insanity
====================

Core Dumps vs Python Backtrace
==============================

The core dump backtrace implies that the interpreter is parsing and reading
into token structures when it explodes. Meanwhile, the python backtrace
has the last line being evaluated as::

    import sys
    str(type(sys).__new__(type(sys)))

Obviously a pretty inocuous line!


Is It Really Segfaulting?
=========================

The shell clearly says, "Segmentation Fault (core dumped)." However, running
the core dump through to the end leads to the process recieving a ``SIGABRT``
after an ``assert`` that seems like it *would* fail. This raises the
question, why is a segmentation fault happening at all? The core dump makes
it look more like a failing assertion.
