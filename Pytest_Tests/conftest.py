import pytest
from selenium import webdriver
import os


@pytest.fixture
def driver(request):
    browser = webdriver.Chrome()
    yield browser

    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        os.makedirs("Screenshots", exist_ok=True)
        browser.save_screenshot(
            f"Screenshots/{request.node.name}.png"
        )

    browser.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, "rep_" + report.when, report)