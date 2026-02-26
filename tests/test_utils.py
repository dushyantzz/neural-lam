# Third-party
import pytest

# First-party
from neural_lam import utils


@pytest.mark.parametrize("fraction", [0.5, 1.0, 2.0])
def test_fractional_plot_bundle_scales_width_linearly(fraction: float) -> None:
    """
    The figure width should scale linearly with the given fraction while the
    height stays unchanged.
    """

    base_bundle = utils.fractional_plot_bundle(1.0)
    bundle = utils.fractional_plot_bundle(fraction)

    base_width, base_height = base_bundle["figure.figsize"]
    new_width, new_height = bundle["figure.figsize"]

    assert pytest.approx(new_width) == base_width * fraction
    assert pytest.approx(new_height) == base_height


@pytest.mark.parametrize("bad_fraction", [0.0, -0.1, -1.0])
def test_fractional_plot_bundle_raises_for_non_positive_fraction(
    bad_fraction: float,
) -> None:
    """
    Non-positive fractions are invalid and should raise a ValueError with a
    helpful error message.
    """

    with pytest.raises(ValueError) as excinfo:
        utils.fractional_plot_bundle(bad_fraction)

    assert "fraction must be a positive float" in str(excinfo.value)


def test_fractional_plot_bundle_returns_valid_bundle() -> None:
    """
    The returned bundle should at least contain a 'figure.figsize' entry with
    a two-element tuple of floats.
    """

    bundle = utils.fractional_plot_bundle(1.0)

    assert "figure.figsize" in bundle

    figsize = bundle["figure.figsize"]
    assert isinstance(figsize, tuple)
    assert len(figsize) == 2
    assert all(isinstance(v, (float, int)) for v in figsize)

