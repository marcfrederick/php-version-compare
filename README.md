# php-version-compare

[![Test](https://github.com/marcfrederick/php-version-compare/actions/workflows/test.yml/badge.svg)](https://github.com/marcfrederick/php-version-compare/actions/workflows/test.yml)
[![PyPI version](https://badge.fury.io/py/php-version-compare.svg)](https://badge.fury.io/py/php-version-compare)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/php-version-compare)](https://pypi.org/project/php-version-compare/)
[![PyPI - License](https://img.shields.io/pypi/l/php-version-compare)](https://pypi.org/project/php-version-compare/)

> ℹ️ **Note**: This project is feature-complete and will only receive updates for bug fixes or compatibility with new
> Python versions. No new features are planned. If you require additional features, please consider forking the project.

A simple Python library for comparing version strings in a manner compatible with PHP's
[version_compare](https://www.php.net/manual/en/function.version-compare.php) function.
Although this implementation is not derived from PHP's code, it passes the same tests to ensure compatibility.

## Installation

To install `php-version-compare`, use pip:

```bash
pip install php-version-compare
```

## Usage

```python
from php_version_compare import version_compare

# Without operator
print(version_compare('1.0', '1.1'))  # Output: -1
print(version_compare('1.1', '1.0'))  # Output: 1
print(version_compare('1.0', '1.0'))  # Output: 0

# With operator
print(version_compare('1.1', '1.0.0', operator='>='))  # Output: True
print(version_compare('1.0.0', '1.1', operator='<='))  # Output: True
print(version_compare('1.0', '1.0', operator='!='))  # Output: False
```

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

### Running Tests

To run tests, make sure you have `tox` installed and run the following command, which will run the tests for all
supported Python versions that are installed on your system:

```bash
tox
```

If you only want to run the tests for a specific Python version, you can specify the version:

```bash
tox -e py39
```

## License

This project is licensed under either of the following, at your option:

- Apache License, Version 2.0 ([LICENSE-APACHE](LICENSE-APACHE) or
  [https://www.apache.org/licenses/LICENSE-2.0](https://www.apache.org/licenses/LICENSE-2.0))
- MIT License ([LICENSE-MIT](LICENSE-MIT) or
  [https://opensource.org/licenses/MIT](https://opensource.org/licenses/MIT))

Which license to use is up to you. This project is dual-licensed for compatibility with both.
When contributing, you agree to license your contributions under the same terms.

## Versioning

This project uses [Semantic Versioning](https://semver.org/). For the versions available, see
the [tags on this repository](https://github.com/marcfrederick/php-version-compare/tags) or the
[releases page](https://github.com/marcfrederick/php-version-compare/releases).
