# cyberglove

Python driver for CyberGlove

## Installing

    pip install cyberglove

All the scripts needed are installed with the pip package.
They are installed in the normal PATH, so run them directly.

## Calibration

**Short version:**

    gather_recordings.py
    fit_mapping.py
    show_calibrated.py

**Explanation:**

Run `gather_recordings.py` and follow the instructions in the viewer.
This will save a file with glove/pose recordings,
and then fit a calibration model to the data.

The first script will take care of running fitting too,
but if you need to manually run fitting run `fit_mapping.py`.

Finally, run `show_calibrated.py` to test out the calibration.
