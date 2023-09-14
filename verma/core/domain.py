import re
import typing as t

from verma.core.enums import BumpLevel


class BumpLevelSelector:

    def __init__(
        self,
        patch_patterns: t.List[str],
        minor_patterns: t.List[str],
        major_patterns: t.List[str],
    ):
        self._patch_patterns = patch_patterns
        self._minor_patterns = minor_patterns
        self._major_patterns = major_patterns

    def select(self, message: str) -> BumpLevel:
        level = None

        for major_pattern in self._major_patterns:
            if re.search(major_pattern, message):
                level = BumpLevel.MAJOR
                return level

        for minor_pattern in self._minor_patterns:
            if re.search(minor_pattern, message):
                level = BumpLevel.MINOR
                return level

        for patch_pattern in self._patch_patterns:
            if re.search(patch_pattern, message):
                level = BumpLevel.PATCH
                return level
            
        return level