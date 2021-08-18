.. _how-to-bug-report:

*************************************
How to Write a Good Python Bug Report
*************************************

Before you report
-----------------

Before opening a bug report on the python bug tracker at
https://bugs.python.org, affectionately nicknamed the "bpo", there are a few
steps you should take. In many cases, the line between bug and behavior can be
blurry, especially in large legacy codebases like the CPython interpreter and
the Python Standard Library. As you go forward, remember that Python is
maintained (almost) entirely by volunteers. Every bug report consumes volunteer
time, and as you think about joining the Python volunteer community with your
bug report, do us a favor and make sure your report has merit!

As a first step, if you are uncertain about whether you might have found a bug
or not, send an email to the python-ideas mailing list at
python-ideas@python.org.  You will not need to wait long before someone will
respond with insight about the problem you are facing.

Solve Surprising Behavior through Documentation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Bear in mind that changing "undesireable behavior" is frequently not possible.
This project is very sensitive towards regressions, and we know that even our
huge regression test suite cannot cover all of the ways Python users are
(ab)using our project in the wild. If the language or a standard library
behaved in a surprising way, a patch to our documentation is usually
the path forward if the problem is purely behavior and not otherwise
problematic.

To that end, documentation is not rocket science! As the person affected by
the confusing thing, you have an intimate understanding of the confusion
better than anyone else. Consider drafting a documentation patch to accompany
your bug report. Pythonistas are picky about their documentation, so it
will certainly get nitpicked, and you will need to follow up with revisions,
but documentation contributions are always in demand, and it is a great way
to start contributiong. It might even save the Python developer ahead of
you from falling into the same trap that led you to be reading this article!


Research Similar Issues on the BPO
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Duplicate issues are posted to the bug tracker *every day.* Don't be that
person. To be fair, the link to the advanced search field on the bug tracker
is very tiny, but you can open it up easily `right here
<https://bugs.python.org/issue?@template=search&status=1>`_

If you find several related issues that have hit a dead end, it doesn't mean
there is nothing you can do. Read the past conversations, try to think of a
path forward, and make a suggestion! At the very least, leave a comment on
the most relevant and/or recent thread expressing that the issue is affecting
you. The bug tracker issues are sorted by activity, so this will ping
everyone in the thread via email and also move the issue to the top of the
bug tracker. Usually, this revives the conversation, so make sure that your
follow-up comment is contentful and suggests a path forward! For example:

   This issue is affecting me as well. In my use case, I encountered this
   problem when I was trying to do ____ real world task. After reading
   the past discussion, I believe that we might be able to move this
   issue forward by ______. While researching, I also noticed that
   this is related to bpo-###, bpo-###, and bpo-###.


How to report a bug
-------------------

Bug reports for the CPython interpreter, the Python standard library, and
Python's official documentation at docs.python.org are submitted to the
Python bug tracker at https://bugs.python.org.

For issues with other Python repositories that do not fit the categories above,
like pip, setuptools, virtualenv, et cetera, there are other places to file
your report; like the python packaging authority. Most of those repositories
are on GitHub.


Other details you should heed
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Fill all the fields on the bug tracker (Components, Versions, Type)
- Be patient – we are volunteers and there are a lot of open issues. If you
  want it fixed fast, include a patch. Even then, it will take a few days or
  sometimes weeks between reviews from a Core Dev
- Look at the problem like a Core Dev as you write up the bug report
   - could your proposed fix introduce regressions elsewhere?
   - can this be fixed with better documentation?


Writing a clear title
---------------------

How would you describe the bug using approximately 10 words? This is the
first part of your bug report a triager or developer will see.

A good summary should quickly and uniquely identify a bug report. It
should explain the problem, not your suggested solution.

-  Good: "shutil.chown should not be defined in Windows"
-  Bad: "windows shutil.chown"

-  Good: "Support UUIDv6, UUIDv7, and UUIDv8 from the new version of RFC4122"
-  Bad: "RFC4122"


Provide a Minimal Reproducible Example
--------------------------------------

If you can, include a minimal reproducible example of the problem that you
are facing. Here is what that means for Python:

* Minimal: find a way to demonstrate the bug with a single Python script
* Complete: do not import third party libraries in your reproduction script.
  This makes it easier for others to run the script, and it means that you
  are more likely closer to the root of the issue.
* Reproducible: be confident that Python is installed correctly on your
  system, and ask for help before filing a bug report if you are not sure.
  Send a message to python-list@python.org, #python irc chat, etc.



For specific types of bugs
^^^^^^^^^^^^^^^^^^^^^^^^^^

- If you identify a bug as a crash, that means a segmentation fault or similar
  critical crash in the python interpreter itself. Please try to use a
  C debugger like lldb or gdb to attach a full backtrace.


Enhancement Requests and PEPs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Note that very small enhancements are approved through the bug tracker, but
larger changes will require writing a Python Enhancement Proposal (PEP), and
completing a review process with the Python Steering Council. If you are
thinking of asking for something big, do not submit a bug report.  Instead,
start with a discussion on python-ideas@python.org, then begin drafting a PEP
if you are serious about persuing the idea.
