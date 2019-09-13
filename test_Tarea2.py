import Tarea2
# importa tarea2 que contiene el codigo a probar


def test_exito():
    assert Tarea2.Func(20, 10) == (10, 30, 200)


def test_menor():
    assert Tarea2.Func(10, 20) == -1


def test_literal():
    assert Tarea2.Func('A', 20) == -1
