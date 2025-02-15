"""Test your functions from Week 2 assignment.
"""
import preclass_assignment.functions as fxn

def test_greet(capsys):
    """Check that the greet function prints as expected"""
    # given
    name = 'world'  # who should we greet?
    # when
    fxn.greet(name)  # greet them
    captured = capsys.readouterr()  # capture what would have been printed to screen
    # then
    assert captured.out == 'Hello, world!\n'  # check that the greeting was what we expect

def test_goldilocks(capsys):
    """Check goldilocks returns expected output"""
    from preclass_assignment.functions import goldilocks

    goldilocks(139)
    captured = capsys.readouterr()
    assert captured.out.strip() == "Too small!"

    goldilocks(140)
    captured = capsys.readouterr()
    assert captured.out.strip() == "Just right. :)"

    goldilocks(151)
    captured = capsys.readouterr()
    assert captured.out.strip() == "Too large!"

def test_square_list():
    """Check square_list returns expected output"""
    # given
    inp = [1, 2, 3]  # test input to function
    exp_out = [1, 4, 9]  # expected output
    # when
    out = fxn.square_list(inp)  # actual output
    # then
    assert exp_out == out  # throw error if actual and expected output don't match

def test_fibonacci_stop():
    """Check fibonacci_stop function works as expected."""
    from preclass_assignment.functions import fibonacci_stop
    assert fibonacci_stop(30) == [1, 1, 2, 3, 5, 8, 13, 21]

def test_clean_pitch():
    """Check clean_pitch works as expected."""
    from preclass_assignment.functions import clean_pitch

    x = [-1, 2, 6, 95]
    status = [1, 0, 0, 0]
    assert clean_pitch(x, status) == [-999, 2, 6, 95]
