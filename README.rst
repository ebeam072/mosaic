MOSAIC: A modular single-molecule analysis interface
=================================


MOSAIC is a single molecule analysis toolbox that automatically decodes multi-state nanopore data. By modeling the nanopore system with an equivalent circuit, MOSAIC leverages the transient response of a molecule entering the channel to quantify pore-molecule interactions. In contrast to existing techniques such as ionic current thresholding {REFS} or Viterbi decoding {REFS}, this technique allows the estimation of short-lived transient events that are otherwise not analyzed.

Nanometer-scale pores have demonstrated potential use in biotechnology applications, including DNA sequencing {REFS}, single-molecule force spectroscopy {REFS}, and single-molecule mass spectrometry {REFS}. The data modeling and analysis methods implemented in MOSAIC allow for dramatic improvements in the quantification of molecular interactions with the channel in each of these applications.

MOSAIC is written in Python and developed in the Semiconductor and Device Metrology (`SDMD <http://www.nist.gov/pml/div683/about.cfm>`_) division, in the Physical Metrology Laborotory (`PML <http://www.nist.gov/pml/>`_) at the National Institute of Standards and Technology (`NIST <http://www.nist.gov>`_).

**If you use MOSAIC in your work, please cite:**

A. Balijepalli, J., Ettedgui, A. T. Cornio, J. W. F. Robertson K. P. Cheung, J. J. Kasianowicz & C. Vaz, "`Quantifying Short-Lived Events in Multistate Ionic Current Measurements. <http://pubs.acs.org/doi/abs/10.1021/nn405761y>`_" *ACS Nano* 2014, **8**, 1547–1553.



What's new in v1.0b2
=================================

- Fixed threshold update error from 1.0b1.
- Considerably improved automatic open channel state detection.
- The default settings string is now included within the source code.
- Implemented new top-level class ConvertToCSV that allows conversion of data read by any TrajIO object to comma separated files.
- Updated build system and unit testing framework.
- Misc UI updates.




**Disclaimer:**
This software was developed at the National Institute of Standards and Technology by employees of the Federal Government in the course of their official duties. Pursuant to title 17 Section 105 of the United States Code this software is not subject to copyright protection and is in the public domain. Each of these packages is an experimental system. NIST assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability,or any other characteristic. We would appreciate acknowledgement if the software is used. This software can be redistributed and/or modified freely provided that any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.