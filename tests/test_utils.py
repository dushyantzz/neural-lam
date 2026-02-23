L1:# Third-party
L2:import pytest
L3:
L4:# First-party
L5:from neural_lam import utils
L6:
L7:
L8+@pytest.mark.parametrize("fraction", [0.5, 1.0, 2.0])
L9+def test_fractional_plot_bundle_scales_width_linearly(fraction):
L10+    """
L11+    The figure width should scale linearly with the given fraction while the
L12+    height stays unchanged.
L13+    """
L14+
L15+    base_bundle = utils.fractional_plot_bundle(1.0)
L16+    bundle = utils.fractional_plot_bundle(fraction)
L17+
L18+    base_width, base_height = base_bundle["figure.figsize"]
L19+    new_width, new_height = bundle["figure.figsize"]
L20+
L21+    assert pytest.approx(new_width) == base_width * fraction
L22+    assert pytest.approx(new_height) == base_height
L23+
L24+
L25+@pytest.mark.parametrize("bad_fraction", [0.0, -0.1, -1.0])
L26+def test_fractional_plot_bundle_raises_for_non_positive_fraction(bad_fraction):
L27+    """
L28+    Non-positive fractions are invalid and should raise a ValueError with a
L29+    helpful error message.
L30+    """
L31+
L32+    with pytest.raises(ValueError) as excinfo:
L33+        utils.fractional_plot_bundle(bad_fraction)
L34+
L35+    assert "fraction must be a positive float" in str(excinfo.value)
L36+
L37+
L38+def test_fractional_plot_bundle_returns_valid_bundle():
L39+    """
L40+    The returned bundle should at least contain a 'figure.figsize' entry with
L41+    a two-element tuple of floats.
L42+    """
L43+
L44+    bundle = utils.fractional_plot_bundle(1.0)
L45+
L46+    assert "figure.figsize" in bundle
L47+
L48+    figsize = bundle["figure.figsize"]
L49+    assert isinstance(figsize, tuple)
L50+    assert len(figsize) == 2
L51+    assert all(isinstance(v, (float, int)) for v in figsize)

