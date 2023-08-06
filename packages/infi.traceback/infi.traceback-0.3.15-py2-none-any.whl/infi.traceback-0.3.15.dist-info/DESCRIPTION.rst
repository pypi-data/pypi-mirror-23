Tracebacks in Python are missing some useful debugging information, such is locals() in each stack frame
This module provides several mechanisms for better tracebacks:
* traceback_context. A context that in patches standard's library traceback module to print better tracebacks
* traceback_decorator. A decorator that calls the decorated method inside the traceback_context
* Nose Plugin. The plugin, enabled with '--with-infi-traceback', prints a better traceback for errors and failures
* pretty_traceback_and_exit_decorator. A decorator for console script entry points that prints exceptions and raises SystemExit

