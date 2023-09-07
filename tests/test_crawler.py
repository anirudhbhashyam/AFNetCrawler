from afnetcrawler import crawler

import numpy as np

import pandas as pd

import pytest


pytest_plugins = ('pytest_asyncio',)


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "country, first_row, last_row",
    [
        (
            "Armenia",
            [1, "A*01", "Armenia Ghegharkunik", 0.1180, 242, "See"],
            [552, "DRB1*16:02", "Armenia combined Regions", 0.01, 100, "See"],
        ),
        (
            "Cook Islands",
            [1, "DPA1*01:03:01", "Cook Islands", 0.54, 50, "See"],
            [99, "DRB1*15:02:01", "Cook Islands", 0.06, 50, "See"],
        ),
    ],
)
async def test_country_frequency_data_retrieval(country: str, first_row: tuple[str | float], last_row:[str | float]) -> None:
    df = pd.concat(
        [
            data
            async for data in crawler.get_frequency_data_by_country(country)
        ]
    )
    first_row_got = df.iloc[0].dropna().to_list()
    last_row_got = df.iloc[-1].dropna().to_list()
    assert first_row == first_row_got
    assert last_row == last_row_got
