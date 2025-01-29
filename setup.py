
from setuptools import setup

setup(
    scripts=['bin/cubic_phase_fitter'],
    pbr=True,
    dependency_links = ['https://github.com/MDAnalysis/mdanalysis']
    )
