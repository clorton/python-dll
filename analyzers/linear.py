import numpy as np

class Analyzer:
    def __init__(self):
        return

    def analyze(self, model):

        print(f"Analyzer: {model.output.mean()=}")
        print(f"Analyzer: {model.output.std()=}")

        return
