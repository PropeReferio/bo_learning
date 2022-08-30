from dataclasses import dataclass, field


class A:
    def __init__(self) -> None:
        self._length = 0


class B:
    def __init__(self, x: int, y: str = "hello", l: list[int] | None = None) -> None:
        self.x = x
        self.y = y
        self.l = [] if not l else l


class C:
    def __init__(self, a: int = 3) -> None:
        self.a = a
        self.b = a + 3


@dataclass(frozen=True)
class AData:
    length: int = 0


@dataclass
class BData:
    x: int
    y: str = "hello"
    lst: list[int] | None = None

    @property
    def l(self):
        return [] if not self.lst else self.lst


@dataclass
class CData:
    a: int = 3

    @property
    def b(self):
        return self.a + 3
