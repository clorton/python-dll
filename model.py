import importlib
import sys
from pathlib import Path

import numpy as np


class Model:
    ...


def run(analyzers: list[str], directory: Path = Path(__file__).parent.absolute):
    model = Model()
    x = np.linspace(0, 1, 129)                  # 129 samples of 1 second
    model.dx = x[1] - x[0]                      # Sample spacing
    model.fs = 1 / model.dx                     # Sampling rate (samples per unit)
    model.output = np.sin(13 * 2 * np.pi * x)   # 13 Hz?

    for analyzer in analyzers:
        module_name, component_name = analyzer.split(".")

        sys.path.insert(0, str(directory))
        module = importlib.import_module(module_name)
        sys.path.pop(0)
        klass = getattr(module, component_name, None)
        component = klass()
        component.analyze(model)

    return


if __name__ == "__main__":
    run(["fourier.Frequency", "linear.Analyzer"], Path(__file__).parent / "analyzers")
