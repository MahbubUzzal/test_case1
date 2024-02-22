from mock import patch, call

from demo_case01.demo_prac01 import adi, get_greetings, divide, fizz_buzz_logic, _sum


def test_adi_answer():
    expected = 5
    actual = adi(3, 2)
    assert actual == expected


def test_get_greetings():
    expected = 'Welcome home Honey!!!'
    actual = get_greetings('Honey')
    assert actual == expected


def test_divide():
    expected = 10
    actual = divide(20, 2)
    assert actual == expected


def test_fizz_buzz_logic_9():
    given = 9
    expected = 'Fizz'
    actual = fizz_buzz_logic(given)
    assert actual == expected


def test_fizz_buzz_logic_25():
    given = 25
    expected = 'Buzz'
    actual = fizz_buzz_logic(given)
    assert actual == expected


def test_fizz_buzz_90():
    given = 90
    expected = 'FizzBuzz'
    actual = fizz_buzz_logic(given)
    assert actual == expected


# def test_fizz_buzz_n_calls(mocker):
#     given = 5
#     mock_fizz_buzz_logic = mocker.patch('fizz_buzz_logic')
#     fizz_buzz(given)mock_fizz_buzz_logic

def test_numbers_sum():
    given = 10
    expected = 55
    actual = _sum(given)
    assert actual == expected


def test_resl_pyramid():
    given = 10