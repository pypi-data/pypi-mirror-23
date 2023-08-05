================
Utopia framework
================
This package provides the basic framework that organises the rest of the packages that make up the Utopia suite. It provides mechanisms for declaring and loading plugins, and working with citation dictionaries. Whereas it can be useful as is, it is expected to be used alongside other packages that provide the actual functionality of Utopia.

Common packages
---------------

In most cases, the following packages should be installed as well as this framework package.

- **pyutopia-tools** provides utilities to various common resources such as PubMed, Crossref, ArXiv, etc. It also provides access utilities for working with the various Utopia servers. These tools can be used to create bespoke applications.
- **pyutopia-plugins-common** provides plugins that slot into the resolution pipeline (amongst others).