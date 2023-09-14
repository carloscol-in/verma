import git
import typing as t

from verma.core import BumpLevelSelectorBuilder
from verma.core.enums import BumpLevel


def select_bump_level_by_commit_message(
        message: str,
        patch_patterns: t.List[str],
        minor_patterns: t.List[str],
        major_patterns: t.List[str]
    ) -> BumpLevel:

    selector = (
        BumpLevelSelectorBuilder()
            .use_patch_patterns(patch_patterns)
            .use_minor_patterns(minor_patterns)
            .use_major_patterns(major_patterns)
            .build()
    )

    level = selector.select(message)

    return level
