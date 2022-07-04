"""
Simple test, to trigger pipelines
Will be removed
"""

import app.src


def test_version():
    """
    Test le numéro de version du projet
    :return: None
    """
    assert app.src.__version__ == "0.1.0"
