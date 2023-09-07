from bs4 import BeautifulSoup    

import httpx

import pandas as pd

import typing


async def get_frequency_data_by_country(country: str) -> typing.AsyncIterator[pd.DataFrame]:
    async with httpx.AsyncClient(timeout = 200) as client:
        page = 1
        while True:
            response = await client.get(f"http://allelefrequencies.net/hla6006a.asp?hla_country={country}&page={page}")
            response.raise_for_status()
            html_soup = BeautifulSoup(response.text, "html.parser")
            html_table = html_soup.find("table", {"class": "tblNormal"})
            if html_table is None:
                break
            df = pd.read_html(str(html_table))[0]
            if df.empty: 
                break
            print(f"{country}: {page}", end = "\r")
            page += 1
            yield df
