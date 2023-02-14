from pathlib import Path

from rest_framework_mixins.generate import all_mixin_combinations


def test_package_code_equals_generated_code():
    package_code_path = (
        Path(__file__).parent.parent / "rest_framework_mixins" / "__init__.py"
    )
    package_code = package_code_path.read_text()

    generated_code = all_mixin_combinations()

    assert package_code == generated_code
