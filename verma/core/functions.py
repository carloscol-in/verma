import re

from verma.core.enums import BumpLevel
from verma.core.models import Version


def bump_version_by_level(
        current_version: str,
        bump_level: BumpLevel,
        prefix: str
    ) -> str:
    version = re.search(r'[\d.]+', current_version).group()

    major, minor, patch = (int(n) for n in version.split('.'))

    if bump_level == BumpLevel.MAJOR:
        major += 1
        minor = patch = 0
    elif bump_level == BumpLevel.MINOR:
        minor +=1
        patch = 0
    elif bump_level == BumpLevel.PATCH:
        patch += 1

    return str(
        Version(
            major=major,
            minor=minor,
            patch=patch,
            prefix=prefix
        )
    )
