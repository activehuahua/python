import sys,warnings

if sys.version_info[0]>=3:
    warnings.warn('Need version 3', RuntimeWarning)
else:
     print('Proceed as normal')