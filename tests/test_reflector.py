import pytest

from enigma.reflector import reflector


def test_reflector():
    assert reflector('a') == 'z'
    assert reflector('b') == 'y'
    assert reflector('c') == 'x'
    assert reflector('d') == 'w'
    assert reflector('e') == 'v'
    assert reflector('f') == 'u'
    assert reflector('g') == 't'
    assert reflector('h') == 's'
    assert reflector('i') == 'r'
    assert reflector('j') == 'q'
    assert reflector('k') == 'p'
    assert reflector('l') == 'o'
    assert reflector('m') == 'n'
    assert reflector('n') == 'm'
    assert reflector('o') == 'l'
    assert reflector('p') == 'k'
    assert reflector('q') == 'j'
    assert reflector('r') == 'i'
    assert reflector('s') == 'h'
    assert reflector('t') == 'g'
    assert reflector('u') == 'f'
    assert reflector('v') == 'e'
    assert reflector('w') == 'd'
    assert reflector('x') == 'c'
    assert reflector('y') == 'b'
    assert reflector('z') == 'a'


def test_reflector_wrong_value():
    with pytest.raises(ValueError):
        reflector(1)

    with pytest.raises(ValueError):
        reflector(True)

    with pytest.raises(ValueError):
        reflector(None)

    with pytest.raises(ValueError):
        reflector([])

    with pytest.raises(ValueError):
        reflector({})

    with pytest.raises(ValueError):
        reflector(())

    with pytest.raises(ValueError):
        reflector('')

    with pytest.raises(ValueError):
        reflector(' ')

    with pytest.raises(ValueError):
        reflector('a' * 2)
