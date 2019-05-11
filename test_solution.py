from solution import Link


def test_links_are_reversible():
    assert Link(3, 5) == Link(5, 3)


def test_pop_specific_value():
    array = [1, 5, 6, 2, 5, 7]
    val = array.remove(5)

    assert val is None
    assert array == [1, 6, 2, 5, 7]


def test_catch_raise():
    array = [1, 5, 6, 2, 5, 7]
    try:
        array.remove(1245)
    except ValueError:
        raise ValueError('asfasdfdas')
        print('ok, caught the error')
