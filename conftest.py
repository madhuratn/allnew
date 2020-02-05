def pytest_addoption(parser):

    parser.addoption("--browser",default="Chrome")
    parser.addoption("--url", default="test")
    parser.addoption("--env", default="local")