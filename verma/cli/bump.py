import click
import git
import typing as t

from verma.core.functions import bump_version_by_level
from verma.git.utils import select_bump_level_by_commit_message


@click.command()
@click.option('--patch-pattern', '-p', 'patch_patterns', multiple=True)
@click.option('--minor-pattern', '-m', 'minor_patterns', multiple=True)
@click.option('--major-pattern', '-M', 'major_patterns', multiple=True)
def bump(
        patch_patterns: t.List[str],
        minor_patterns: t.List[str],
        major_patterns: t.List[str]
    ):
    repo = git.Repo()
    message = repo.head.commit.message
    last_tag = repo.tags[-1] if len(repo.tags) > 0 else None
    new_version = 'v0.0.0'

    if last_tag is None:
        click.echo(new_version)
        return
    
    current_version = last_tag.name

    level = select_bump_level_by_commit_message(
        message=message,
        patch_patterns=patch_patterns,
        minor_patterns=minor_patterns,
        major_patterns=major_patterns
    )

    new_version = bump_version_by_level(
        current_version=current_version,
        bump_level=level,
        prefix='v'
    )

    click.echo(new_version)
