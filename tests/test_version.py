# Example test file.

from numpy.testing import assert_equal
import skcolumbia

def test_version_good():
    assert_equal(skcolumbia.__version__, "0.1")
