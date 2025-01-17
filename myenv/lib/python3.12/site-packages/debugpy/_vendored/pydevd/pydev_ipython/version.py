"""
Utility for version comparison
"""


class _Version:
    def __init__(self, s):
        parts = s.split(".")
        version_parts = []
        for p in parts:
            try:
                version_parts.append(int(p))
            except ValueError:
                version_parts.append(p)

        self._version_parts = tuple(version_parts)

    def __ge__(self, v):
        this_parts = self._version_parts
        other_parts = v._version_parts

        while len(this_parts) < len(other_parts):
            this_parts = this_parts + (0,)

        return this_parts >= other_parts


def check_version(found_version, expected_min_or_eq_to_version):
    """check version string found_version >= expected_min_or_eq_to_version

    If dev/prerelease tags result in TypeError for string-number comparison,
    it is assumed that the dependency is satisfied.
    Users on dev branches are responsible for keeping their own packages up to date.
    """
    try:
        return _Version(found_version) >= _Version(expected_min_or_eq_to_version)
    except TypeError:
        return True


if __name__ == "__main__":
    assert check_version("1.2.3", "1.2.3")
    assert check_version("1.2.4", "1.2.3")
    assert check_version("1.2", "1.2.bar")
    assert check_version("1.3", "1.2.bar")
    assert check_version("1.3", "1.2b")
    assert not check_version("1.2", "1.3")
    assert not check_version("1.2.0", "1.2.1")
    assert not check_version("1.2", "1.2.1")
    print("Ok, checks passed")
