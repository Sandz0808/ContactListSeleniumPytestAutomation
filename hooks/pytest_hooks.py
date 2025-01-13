import os

current_test_info = {}


def pytest_runtest_call(item):
    # Capture the test function and class name
    test_file = os.path.basename(item.fspath)
    test_class = item.cls.__name__ if item.cls else None
    test_function = item.name

    # Store the details in a dictionary
    current_test_info['test_file'] = test_file
    current_test_info['test_class'] = test_class
    current_test_info['test_function'] = test_function


def get_current_test_info():
    """Returns the currently running test's information."""
    return current_test_info