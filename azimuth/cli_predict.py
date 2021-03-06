import argparse
import io
import sys

import numpy as np
from azimuth.model_comparison import predict
import contextlib


@contextlib.contextmanager
def redirect_stdout(target):
    original = sys.stdout
    try:
        sys.stdout = target
        yield
    finally:
        sys.stdout = original

# Lightweight CLI wrapper for running model predictions on sequence data
if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--sequences', dest='sequences', action='store', type=str, nargs='+', required=True)
    options = parser.parse_args()

    # Capture and suppress print output from model, so that we can cleanly return results on stdout
    f = io.StringIO()
    with redirect_stdout(f):
        # Run model
        predictions = predict(np.array(options.sequences), None, None)

    # Print predictions to stdout for further use
    for seq, pred in zip(options.sequences, predictions):
        print("{} -> {}".format(seq, pred))
