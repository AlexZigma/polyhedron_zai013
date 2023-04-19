from pytest import approx
from math import sqrt
from shadow.polyedr import Polyedr


def invisible_area(self):
    self.make_shadows()
    return self.invisible_area()


setattr(Polyedr, 'test_invisible_area', invisible_area)


class TestPolyedr:

    def test_polyedr_1(self):
        assert Polyedr(f"data/test1.geom").test_invisible_area() == 0

    def test_polyedr_2(self):
        assert Polyedr(f"data/test2.geom").test_invisible_area() == 1

    def test_polyedr_3(self):
        assert Polyedr(f"data/test3.geom").test_invisible_area() == 1

    def test_polyedr_4(self):
        assert Polyedr(f"data/test4.geom").test_invisible_area() == \
            approx(sqrt(2)/2)

    def test_polyedr_5(self):
        assert Polyedr(f"data/test5.geom").test_invisible_area() == 2

    def test_polyedr_6(self):
        assert Polyedr(f"data/test6.geom").test_invisible_area() == 0

    def test_polyedr_7(self):
        assert Polyedr(f"data/test7.geom").test_invisible_area() == 0

    # python3 -B -m pytest -p no:cacheprovider tests/test_polyedr.py
