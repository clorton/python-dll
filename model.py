import importlib
import sys
from pathlib import Path

import numpy as np


class Model:
    ...


def run(analyzers: list[str], directory: Path = Path(__file__).parent.absolute):

    # "Run" our model - generate 129 samples of a 13Hz sine wave.
    model = Model()
    x = np.linspace(0, 1, 129)                  # 129 samples of 1 second
    model.dx = x[1] - x[0]                      # Sample spacing
    model.fs = 1 / model.dx                     # Sampling rate (samples per unit)
    model.output = np.sin(13 * 2 * np.pi * x)   # 13Hz

    for analyzer in analyzers:
        # take, e.g., "fourier.Frequency" and split into "fourier" (the .py file)
        # and "Frequency" the name of the Python class
        module_name, component_name = analyzer.split(".")

        sys.path.insert(0, str(directory))              # Temporarily add the DLL directory to the path
        module = importlib.import_module(module_name)   # programmatically import the module, e.g. "fourier", by name
        sys.path.pop(0)                                 # Undo path environment variable change
        klass = getattr(module, component_name, None)   # Get the class constructor from the module, e.g. "Frequency"
        component = klass()                             # Create an instance of the class
        component.analyze(model)                        # Call its analyze() method

    return


if __name__ == "__main__":
    # Ask to call two "analyzers" located in "../analyzers"
    run(["fourier.Frequency", "linear.Analyzer"], (Path(__file__).parent / "analyzers").absolute())
