from project import question, write_header, write_data_in_csv, ask, action, number_of_iterations, get_csv, get_number_of_clicks, write_cursor_location
import mock
import builtins



def test_question():
    assert question("yes") == True
    assert question("no") == False


def test_write_header():
    assert write_header("test.csv") == True

def test_write_data_in_csv():
    assert write_data_in_csv([[1, 2]], "test.csv") == True


def test_ask():
    assert ask("yes") == True
    assert ask("no") == False


def test_action():
    assert action([[1, 2]]) == True


def test_number_of_iterations():
    with mock.patch.object(builtins, "input", lambda _: 1):
        assert number_of_iterations() == 1

def test_get_csv():
    with mock.patch.object(builtins, "input", lambda _: "hello.csv"):
        assert get_csv() == "hello.csv"

def test_get_number_of_clicks():
    with mock.patch.object(builtins, "input", lambda _: 5):
        assert get_number_of_clicks() == 5

def test_write_cursor_location():
    assert write_cursor_location(12, 6, "", True) == [[12, 6]]