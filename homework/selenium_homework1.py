import pytest
from selenium import webdriver

import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def driver(request):
    driver = None
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    yield driver
    if driver:
        driver.quit()


@pytest.mark.parametrize("driver, url, expected_title", [
    ("chrome", "https://www.amazon.com/", "Amazon"),
    ("chrome", "https://www.apple.com/", "Apple"),
    ("firefox", "https://www.google.com/", "Google")
], indirect=["driver"])
def test_page_title(driver, url, expected_title):
    driver.get(url)
    assert expected_title in driver.title
