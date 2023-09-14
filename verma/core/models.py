import dataclasses


@dataclasses.dataclass(frozen=True)
class Version:
    major: int
    minor: int
    patch: int
    prefix: str

    def __str__(self):
        return f'{self.prefix}{self.major}.{self.minor}.{self.patch}'

    def __repr__(self):
        return f'{self.prefix}{self.major}.{self.minor}.{self.patch}'
