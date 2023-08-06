Changelog
=========

dev
---

* -

0.5.2 (2017-07-26)
------------------

* Added a `setup.py` check that the user runs at least the minimal required
  Python version (Python 3.3). This makes `pip` raise a helpful error message
  instead of a meaningless exception.
* Made tests for the `retdec.conn` module work with the latest version of
  `responses` (0.6.0).

0.5.1 (2016-09-24)
------------------

* Emit a warning instead of an error when a call graph, control-flow graph, or
  archive fails to be generated. This makes the ``decompiler`` tool continue
  downloading all the requested outputs instead of giving up on the first
  failure.
* Fixed the use of environment variable ``RETDEC_API_URL`` to override the
  default API URL. Previously, the URL was not overridden, even when given.

0.5 (2016-09-15)
----------------

* Added support for decompilation of files in archives (`ar` format). Archives
  are statically linked libraries, commonly ending with `.a` or `.lib`. To
  decompile a file from an archive, use the `bin` mode and pass either the
  index of the file in the archive (`ar_index`) or its name (`ar_name`). New
  since RetDec 2.2.
* Added a new optional parameter ``output_format`` to the ``fileinfo`` service.
  You can use it to obtain the output in the JSON format. New since RetDec 2.2.
* Added support for decompilation of files in the Intel HEX format. To
  decompile such files, use the ``bin`` mode and pass the architecture and
  endianness of the machine code inside the file. New since RetDec 2.2.
* The ``raw_entry_point`` and ``raw_section_vma`` parameters in ``raw``
  decompilations no longer accept the ``default`` value. In both cases, you
  have to explicitly pass an address. New since RetDec 2.2.
* The ``raw_endian`` parameter was renamed to ``endian``. Use of the original
  name is still supported, but it is deprecated. New since RetDec 2.2.
* It is no longer possible to force an architecture when decompiling a file in
  the ``bin`` mode. The architecture is now detected automatically from the
  input file. New since RetDec 2.2.
* It is no longer required to set ``file_format`` in raw decompilations. When
  given, it will be ignored. New since RetDec 2.2.
* Compiler-optimization levels can now be also specified without the leading
  dash (e.g. you can pass ``O1`` instead of ``-O1``). New since RetDec 2.2.
* Dropped support for Python 3.2 (the ``requests`` module, which is used for
  HTTPS communication, no longer supports it).

0.4 (2016-08-04)
----------------

* Added support for decompilation of raw machine code (the ``raw`` mode).
* Added support for generating and downloading of control-flow graphs.
* Added support for generating and downloading of a call graph.
* Added support for selecting the format of the generated call and control-flow
  graphs.
* Added support for selecting a different style for naming of variables.
* Added support for selecting the type of optimizations to be performed by the
  decompiler.
* Added support for decompilation of unreachable functions.
* Added support for disabling the emission of addresses in the generated code.
* Added support for selecting functions to be decompiled.
* Added support for selecting address ranges to be decompiled.
* Added support for choosing what should be decoded in selective decompilation.
* Improved error messages in exceptions.

0.3 (2016-07-17)
----------------

* Added access to warnings in decompilation phases and their emission in the
  ``decompiler`` tool.
* Added obtaining of the compiled version of the input C file (provided that
  the input was a C file).
* Added support for selecting the compiler to be used when compiling C source
  files.
* Added support for selecting the optimizations to be used when compiling C
  source files.
* Added support for selecting whether C files should be compiled with debugging
  information.
* Added support for selecting whether compiled C files should be stripped.
* Added support for printing script versions via the ``-V``/``--version``
  parameter.

0.2 (2016-06-12)
----------------

* Added support for passing a PDB file to decompilations.
* Added support for selecting the target high-level language.
* Added support for selecting the architecture.
* Added support for selecting the file format.
* Added a new method to the ``Test`` service: ``echo()``. It echoes back the
  parameters passed via the `test/echo
  <https://retdec.com/api/docs/test.html#parameter-passing>`_ service.
* Added a `summary
  <https://retdec-python.readthedocs.io/en/latest/status.html>`_ of the
  supported parts of the `retdec.com API
  <https://retdec.com/api/docs/index.html>`_ into the `documentation
  <https://retdec-python.readthedocs.io/en/latest/>`_.
* ``Decompiler.start_decompilation()`` and ``Fileinfo.start_analysis()`` raise
  ``MissingParameterError`` when the input file is not given.
* Re-formatted the progress-log output from the ``decompiler`` tool to ensure
  that the ``[OK]`` parts are aligned properly.

0.1 (2015-09-13)
----------------

Initial release.
