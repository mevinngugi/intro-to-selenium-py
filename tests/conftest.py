# This module contains shared fixtures.
# A function that includes both the set up and cleanup methods in one body

import json
import pytest
import selenium.webdriver


@pytest.fixture
def config(scope="session"):

    # Read the config.jason file
    # Read once for the entire test session
    with open("config.json") as config_file:
        config = json.load(config_file)  # Pharse the read config file into a dictionary

    # Assert values are acceptable
    assert config["browser"] in ["Firefox", "Chrome", "Headless Chrome"]
    assert isinstance(config["implicit_wait"], int)
    assert config["implicit_wait"] > 0

    # Return the config as a dictionary
    return config


@pytest.fixture
def browser(config):

    # Initialize the WebFriver instance
    if config["browser"] == "Firefox":
        b = selenium.webdriver.Firefox()
    elif config["browser"] == "Chrome":
        b = selenium.webdriver.Chrome()
    elif config["browser"] == "Headless Chrome":
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument("headless")
        b = selenium.webdriver.Chrome(options=opts)
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported.')

    # Make its calls wait for elements to appear
    b.implicitly_wait(config["implicit_wait"])

    # Return the WebDriver instance for the setup
    yield b

    # Quit the WebDriver instance for the cleanup
    b.quit()
