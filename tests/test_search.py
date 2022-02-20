"""
These tests cover DuckDuckGo searches
"""

import pytest
from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage


@pytest.mark.parametrize("phrase", ["panda", "python", "polar bear"])
def test_basic_duckduckgo_search(browser, phrase):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)

    # Commenting out the the single test phrase for multiple search phrases using the parametrize decorator
    # PHRASE = "panda"

    # Given the DuckDuckGo home page is displayed
    search_page.load()

    # When the user searches for "panda" using the hardcoded PHRASE variable
    # When the user runs multiple searches
    search_page.search(phrase)

    # Then search result query is "panda"
    assert phrase == result_page.search_input_value()

    # And the search result links pertain to "panda"
    # for title in result_page.result_link_titles():
    #    assert PHRASE.lower() in title.lower()

    titles = result_page.result_link_titles()
    matches = [t for t in titles if phrase.lower() in t.lower()]
    assert len(matches) > 0

    # And the search result title contains "panda"
    # Reordered the assertions to avoid Firefox race condition
    assert phrase in result_page.title()
