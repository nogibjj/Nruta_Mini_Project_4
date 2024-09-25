from main import multiply


def test_multiply():
    """testing out multiply function"""
    assert multiply(2, 2) == 4
    assert multiply(4, 2) == 8


if __name__ == "__main__":
    test_multiply()
