import typing as t
from verma.core.domain import BumpLevelSelector


class BumpLevelSelectorBuilder:

    _patch_patterns: t.List[str] = []
    _minor_patterns: t.List[str] = []
    _major_patterns: t.List[str] = []

    def use_patch_patterns(self, patterns: t.List[str]):
        self._patch_patterns.extend(patterns)

        return self

    def use_minor_patterns(self, patterns: t.List[str]):
        self._minor_patterns.extend(patterns)

        return self

    def use_major_patterns(self, patterns: t.List[str]):
        self._major_patterns.extend(patterns)

        return self

    def build(self) -> BumpLevelSelector:
        return BumpLevelSelector(
            patch_patterns=self._patch_patterns,
            minor_patterns=self._minor_patterns,
            major_patterns=self._major_patterns
        )