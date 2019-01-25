## Overview

This project demonstrates import errors that I see when running `pytype` in the pytype\_import\_error directory. 

## Error Example

(directory structure has been modified)

```
Computing dependencies
Analyzing 6 sources with 0 local dependencies
ninja: Entering directory `/foo/pytype-import-error/pytype_import_error/pytype_output'
[1/6] pytype-single --imports_info /foo/pytype-import-error/pytype_import_error/adjacent_module.py
FAILED: /foo/pytype-import-error/pytype_import_error/pytype_output/pyi/pytype_import_error/main.pyi 
pytype-single --imports_info /foo/pytype-import-error/pytype_import_error/pytype_output/imports/pytype_import_error.main.imports --module-name pytype_import_error.main -V 3.7 -o /foo/pytype-import-error/pytype_import_error/pytype_output/pyi/pytype_import_error/main.pyi --analyze-annotated --nofail --quick /foo/pytype-import-error/pytype_import_error/main.py
File "/foo/pytype-import-error/pytype_import_error/main.py", line 1, in <module>: Can't find module 'adjacent_module'. [import-error]
File "/foo/pytype-import-error/pytype_import_error/main.py", line 2, in <module>: Can't find module 'subpackage'. [import-error]
File "/foo/pytype-import-error/pytype_import_error/main.py", line 3, in <module>: Can't find module 'subpackage.helpers'. [import-error]

For more details, see https://github.com/google/pytype/blob/master/docs/errors.md#import-error.
[5/6] pytype-single --imports_info /foo/pytype-import-error/pytype_import_error/subpackage/helpers.py
ninja: build stopped: subcommand failed.
```


## Note

NOTE: if you remove pytype\_import\_error/\_\_init\_\_.py, the import errors disappear
