from exercises.class_to_dataclass import A, B, C, AData, BData, CData
import pytest


class TestA:
    def test_a(self):
        a = A()
        assert a._length == 0

    def test_a_data(self):
        a_data = AData()
        assert a_data.length == 0

    def test_a_and_data_a_are_same(self):
        a = A()
        a_data = AData()
        assert a._length == a_data.length

    def test_no_arguments(self):
        with pytest.raises(TypeError):
            a = A(1)
            test_a = TestA(5)


class TestB:
    def test_b(self):
        b = B(5)
        assert b.y == "hello"
        assert b.l == []

        b_2 = B(5, l=[1,2,3])
        assert b_2.y == "hello"
        assert len(b_2.l) == 3

    def test_b_data(self):
        b = BData(5)
        assert b.y == "hello"
        assert b.l == []

        b_2 = BData(5, lst=[1, 2, 3])
        assert b_2.y == "hello"
        assert len(b_2.l) == 3

    def test_are_same(self):
        b = B(5)
        b_data = B(5)
        assert b.x == b_data.x
        assert b.y == b_data.y
        assert b.l == b_data.l

        # TODO add parametrize, test all possibilities


class TestC:
    def test_c(self):
        c = C()
        assert c.a == 3
        assert c.b == c.a + 3

        c_2 = C(15)
        assert c_2.b == c_2.a + 3

        with pytest.raises(TypeError):
            c_3 = C(15, 18)

    def test_c_data(self):
        c = CData()
        assert c.a == 3
        assert c.b == c.a + 3

        c_2 = CData(15)
        assert c_2.b == c_2.a + 3

        with pytest.raises(TypeError):
            c_3 = CData(15, 18)

    def test_are_same(self):
        c = C(5)
        c_data = CData(5)
        assert c.a == c.a
        assert c.b == c_data.b
