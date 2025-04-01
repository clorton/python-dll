import importlib.util
from pathlib import Path

def load_module_from_file(filepath):
    filepath = Path(filepath)
    module_name = filepath.stem  # e.g., "my_module" from "my_module.py"
    
    spec = importlib.util.spec_from_file_location(module_name, filepath)
    if spec and spec.loader:
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    else:
        raise ImportError(f"Could not load module from {filepath}")
