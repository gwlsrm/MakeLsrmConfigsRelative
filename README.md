# MakeLsrmConfigsRelative

Utility `make_config_relative.py` makes paths in [LSRM SpectraLine software](http://lsrm.ru/en/products/list.php?SECTION_CODE=semejjstvo_spectraline_1.7) configurations relative. Utility edits config-files: `lsrm.cnf` and converts internal paths to relative:

e.g. for configuration NaI it will convert path `d:\gw\LSRM\Work\NaI\Data\calibr.cen -> Data\calibr.cen`

So you can move configuration to any directory and work with it in SpectraLine (from v 1.7.9864)



### How to use

```sh
python make_config_relative.py c:\Lsrm\Work
```

Recursively makes paths in all configurations relative.

