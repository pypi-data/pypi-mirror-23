UConnRCMPy
==========

Data processing code for the RCM at UConn. See the license file for
information about the license for this code.

CI Status
---------

Travis: |Build Status| AppVeyor: |Build status| Codecov: |codecov|

DOI
---

|DOI|

Change Log
==========

All notable changes to this project will be documented in this file.

The format is based on `Keep a Changelog <http://keepachangelog.com/>`__
and this project adheres to `Semantic
Versioning <http://semver.org/>`__.

`Unreleased <https://github.com/bryanwweber/UConnRCMPy/compare/v3.0.4...HEAD>`__
--------------------------------------------------------------------------------

Added
~~~~~

Fixed
~~~~~

Changed
~~~~~~~

Removed
~~~~~~~

[3.0.5] - 2017-06-21
--------------------

Fixed
~~~~~

-  Exception no longer raised when the EOC time is changed of an
   experiment that was mischaracterized as non-reactive

`3.0.4 <https://github.com/bryanwweber/UConnRCMPy/compare/v3.0.3...v3.0.4>`__ - 2017-06-21
------------------------------------------------------------------------------------------

Fixed
~~~~~

-  EOC time not respected after it had been changed in
   ``change_EOC_time``

`3.0.3 <https://github.com/bryanwweber/UConnRCMPy/compare/v3.0.2...v3.0.3>`__ - 2017-06-16
------------------------------------------------------------------------------------------

Added
~~~~~

-  Function to manually set the EOC time, ``change_EOC_time``

Fixed
~~~~~

-  Comparing T\_EOC between reactive and non-reactive caused a
   ``ValueError``
-  Add ``copy`` argument to ``AltExperiment`` class initializer
-  Fix how adding cases is handled in ``AltCondition``

Changed
~~~~~~~

Removed
~~~~~~~

`3.0.2 <https://github.com/bryanwweber/UConnRCMPy/compare/v3.0.1...v3.0.2>`__ - 2017-04-19
------------------------------------------------------------------------------------------

Added
~~~~~

-  CITATION file
-  PyPI packages

Fixed
~~~~~

-  Deploy doctr to the root directory (see
   `drdoctr/doctr#157 <https://github.com/drdoctr/doctr/issues/157>`__
   and
   `drdoctr/doctr#160 <https://github.com/drdoctr/doctr/issues/160>`__)

Changed
~~~~~~~

-  DOI badges point to latest DOI from Zenodo
-  Relicensed to BSD 3-Clause

`3.0.1 <https://github.com/bryanwweber/UConnRCMPy/compare/v3.0.0...v3.0.1>`__ - 2017-02-21
------------------------------------------------------------------------------------------

Added
~~~~~

-  Copy keyword in Experiment init to avoid auto-copy to clipboard
-  Regression tests for Experiment, including ignition delay, p\_EOC,
   and T\_EOC estimate
-  ``kwargs`` are passed through to the Experiment init in
   ``add_experiment``

Fixed
~~~~~

-  ``copy=False`` kwarg passed to ``add_experiment`` in tests fixes
   tests on Travis
-  Load CTI file instead of from source string to avoid
   `Cantera/cantera#416 <https://github.com/Cantera/cantera/issues/416>`__

Changed
~~~~~~~

-  Butterworth filter is now first order
-  Butterworth filter cutoff frequency is no longer corrected
-  End point for linear fit of filter residuals is chosen automatically
-  Derivative is smoothed with moving average

`3.0.0 <https://github.com/bryanwweber/UConnRCMPy/compare/v2.1.0...v3.0.0>`__ - 2017-02-07
------------------------------------------------------------------------------------------

Added
~~~~~

-  Print warning when the simulated TCs don't match
-  Python 3.6 builds on Travis
-  Conda builds on Travis/Appveyor upload to anaconda.org when a tag is
   pushed.
-  Appveyor builds for Windows tests/packaging
-  Prompt user for filter frequency when auto-setting fails
-  Label for raw pressure line
-  Refactor ``Simulation`` class to new module
-  Conda recipe
-  Summary output from ``Condition``
-  String input to ``Experiment``
-  Add types to the docs for constants
-  ``__repr__`` for all classes
-  Text-file output from relevant trace-type classes
-  ``reactive_file`` is an attribute of ``Condition`` as a property
-  This CHANGELOG file
-  Automatic filter cutoff frequency selection and override functions
-  Upload docs to gh-pages with
   `doctr <https://github.com/drdoctr/doctr>`__
-  Disable Cantera thermo warnings after loading a CTI file for the
   first time
-  ``volume-trace.yaml`` file is automatically written
-  Version information is stored in ``_version.py``

Fixed
~~~~~

-  Travis builds now fail appropriately
-  Added MANIFEST.in and modified setup.py to include test data files
-  Replot lines when filtering frequency is changed
-  Fix docs after ``dataprocessing`` -> ``conditions``/``experiments``
   module split
-  Unsuppress thermo warnings before loading a new CTI file
-  Properly set ``reactive_case`` and ``nonreactive_case``, and other
   attributes important for the ``VolumeTrace`` generation
-  Filter frequency has to be set after the experiment sampling
   frequency is calculated
-  Writing the ``volume-trace.yaml`` file now has filenames instead of
   ``Path`` reprs
-  Time in figure legend has a colon

Changed
~~~~~~~

-  Catch ``FileNotFoundError``\ s instead of ``OSError``\ s when files
   are missing
-  Raise exceptions if CTI arguments are specified incorrectly to
   ``Experiment``
-  Convert all time axes on figures to ms
-  Split the dataprocessing module into experiments and conditions
   modules
-  Use slices to compute the derivative of the experimental pressure
   trace
-  A CTI filename is required as input when Condition is instantiated
-  The creation of the volume trace is controlled by instance attributes
   rather than ``volume-trace.yaml``
-  Minimum version of Cantera is 2.3.0

Removed
~~~~~~~

-  CanSen dependency is no longer required
-  Voltage traces are no longer smoothed, and the smoothing function has
   been removed

`2.1.0 <https://github.com/bryanwweber/UConnRCMPy/compare/v2.0.2...v2.1.0>`__ - 2016-05-31
------------------------------------------------------------------------------------------

Added
~~~~~

-  Docs for ``dataprocessing``
-  Matplotlib to intersphinx
-  Alternate class for processing experimental data ``AltExperiment``
-  The year is stored in the ``experiment_parameters`` dictionary
-  Plot the P0 fit line on nonreactive plots
-  Axis labels on figures

Fixed
~~~~~

-  Default documentation role is ``py:obj``
-  Import from ``experiment`` module should be ``dataprocessing`` module
-  Wrong version in docs
-  Get the non-reactive experiment to plot in ``create_volume_trace``
-  The zeroed time and pressure trace should come from the
   ``pressure_trace`` instance in ``process_folder``
-  Include offset in pressure trace timing calculations
-  Documentation typos in filtering function and finding PC
-  Using a float as an index to a NumPy array is deprecated, so don't do
   that

Changed
~~~~~~~

-  Use online Cantera docs for intersphinx
-  The exception generated if calculation of TC fails is printed
-  ``parse_file_name`` is a method of ``Experiment``
-  Reduce the search increment for finding PC from 100 to 50

Removed
~~~~~~~

-  ``PressureFromVolume`` and ``VolumeFromPressure`` state can no longer
   be set by P and v

`2.0.2 <https://github.com/bryanwweber/UConnRCMPy/compare/v2.0.1...v2.0.2>`__ - 2016-01-24
------------------------------------------------------------------------------------------

Added
~~~~~

-  ``Condition`` is imported in ``__init__.py``

`2.0.1 <https://github.com/bryanwweber/UConnRCMPy/compare/v2.0.0...v2.0.1>`__ - 2016-01-23
------------------------------------------------------------------------------------------

Fixed
~~~~~

-  Wrong figure name used in ``compare_to_sim``
-  Derivative of simulated pressure trace was computed incorrectly

Changed
~~~~~~~

-  Only get the parameters needed from the YAML file, instead of loading
   the whole thing every time
-  Simulations are plotted with the time-axis in ms and with the zero at
   EOC

`2.0.0 <https://github.com/bryanwweber/UConnRCMPy/compare/v1.0.7...v2.0.0>`__ - 2016-01-23
------------------------------------------------------------------------------------------

Added
~~~~~

-  Sphinx documentation

Fixed
~~~~~

-  Clipboard pasting works on OS X and Windows

Changed
~~~~~~~

-  Refactor most functionality into classes
-  Remove ``ParsedFilename`` class
-  Remove old, unused, modules including ``nonreactive.py``,
   ``volume_trace.py``, and ``experiments.py``->``dataprocessing.py``
-  Set the overall and first stage ignition delays, and the TC of
   nonreactive experiments to 0

`1.0.7 <https://github.com/bryanwweber/UConnRCMPy/compare/v1.0.6...v1.0.7>`__ - 2016-12-01
------------------------------------------------------------------------------------------

Added
~~~~~

-  Low-pass filtering function for the voltage signal
-  First stage ignition delay is automatically calculated

Fixed
~~~~~

-  Errors in computing the temperature are caught now, instead of
   crashing the analysis
-  Eliminate deprecation warning about ``ReactorNet.step()`` by checking
   the version of Cantera being used

Changed
~~~~~~~

-  Change offset for ignition delay calculation from 5 ms to 2 ms
-  Use FFT convolve from ``scipy`` instead of ``convolve`` from
   ``numpy`` because the FFT was 100x faster
-  The voltage is low-pass filtered and then moving-average smoothed,
   rather than just being smoothed
-  Increase the smoothing window for the derivative from 5 to 151
-  The compression time from the YAML file is used as the end time when
   fitting the initial period of the pressure trace

`1.0.6 <https://github.com/bryanwweber/UConnRCMPy/compare/v1.0.5...v1.0.6>`__ - 2015-07-18
------------------------------------------------------------------------------------------

Added
~~~~~

-  Option to specify ``end_time`` or ``end_temp`` to the simulation in
   the class constructor

`1.0.5 <https://github.com/bryanwweber/UConnRCMPy/compare/v1.0.4...v1.0.5>`__ - 2015-07-16
------------------------------------------------------------------------------------------

Added
~~~~~

-  Option to plot results in the ``ign_loop`` script

`1.0.4 <https://github.com/bryanwweber/UConnRCMPy/compare/v1.0.3...v1.0.4>`__ - 2015-07-16
------------------------------------------------------------------------------------------

Fixed
~~~~~

-  Bugs related to missing ``pathlib`` imports in traces files

`1.0.3 <https://github.com/bryanwweber/UConnRCMPy/compare/v1.0.2...v1.0.3>`__ - 2015-07-16
------------------------------------------------------------------------------------------

Added
~~~~~

-  New dependency on the ``pathlib`` module, requiring Python >= 3.4

Fixed
~~~~~

-  The path to search for files to process in ``ign_loop`` is computed
   at runtime rather than import-time
-  Fix typo in ``ParsedFilename`` docs

`1.0.2 <https://github.com/bryanwweber/UConnRCMPy/compare/v1.0.1...v1.0.2>`__ - 2015-07-16
------------------------------------------------------------------------------------------

Fixed
~~~~~

-  Ignore the build directory

Changed
~~~~~~~

-  Rename class ``PressureTrace`` to ``ExperimentalPressureTrace``
-  The smoothing function sets the first ``(span-1)/2`` data points
   equal to the value there
-  Refactor ``voltage`` variable name to be ``signal``
-  Smooth the voltage first, then compute the pressure, rather than the
   other way around

`1.0.1 <https://github.com/bryanwweber/UConnRCMPy/compare/v1.0.0...v1.0.1>`__ - 2015-07-16
------------------------------------------------------------------------------------------

Added
~~~~~

-  Filename for the reactive experiment is loaded from the
   ``volume-trace.yaml`` file

Fixed
~~~~~

-  Minimize code inside with-statement for YAML file
-  Ignore ``dist`` folder from Git

Changed
~~~~~~~

-  The name of the script to run an analysis of a folder is changed from
   ``process-ignition-loop`` to ``ignloop``

`1.0.0 <https://github.com/bryanwweber/UConnRCMPy/compare/0408b7df57a059e42e946caad4273f808507b9fa...v1.0.0>`__ - 2015-06-28
----------------------------------------------------------------------------------------------------------------------------

Added
~~~~~

-  Basic functionality of class-based interface to process data

Citation of UConnRCMPy
======================

|DOI|

To cite UConnRCMPy in a scholarly article, please use

    B. W. Weber, R. Fang, and C.J. Sung. (2017) UConnRCMPy v3.0.2
    [software]. Zenodo. https://doi.org/10.5281/zenodo.594918

A BibTeX entry for LaTeX users is

.. code:: tex

    @software{uconnrcmpy,
      title = {{{UConnRCMPy}}},
      url = {https://github.com/bryanwweber/UConnRCMPy},
      version = {3.0.3},
      author = {Weber, Bryan William and Fang, Ruozhou and Sung, Chih-Jen},
      date = {2017-04},
      doi = {10.5281/zenodo.594918}
    }

The DOI for the latest version can be found in the badge at the top. If
you would like to cite a specific, older version, the DOIs for each
release are:

-  v3.0.4:
   `10.5281/zenodo.815568 <https://doi.org/10.5281/zenodo.815568>`__
-  v3.0.3:
   `10.5281/zenodo.810181 <https://doi.org/10.5281/zenodo.810181>`__
-  v3.0.2:
   `10.5281/zenodo.556469 <https://doi.org/10.5281/zenodo.556469>`__
-  v3.0.1:
   `10.5281/zenodo.321427 <https://doi.org/10.5281/zenodo.321427>`__
-  v3.0.0:
   `10.5281/zenodo.269678 <https://doi.org/10.5281/zenodo.269678>`__

.. |Build Status| image:: https://travis-ci.org/bryanwweber/UConnRCMPy.svg?branch=master
   :target: https://travis-ci.org/bryanwweber/UConnRCMPy
.. |Build status| image:: https://ci.appveyor.com/api/projects/status/xxs56c4iqy9akeam?svg=true
   :target: https://ci.appveyor.com/project/bryanwweber/uconnrcmpy
.. |codecov| image:: https://codecov.io/gh/bryanwweber/UConnRCMPy/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/bryanwweber/UConnRCMPy
.. |DOI| image:: https://zenodo.org/badge/36095263.svg
   :target: https://zenodo.org/badge/latestdoi/36095263
