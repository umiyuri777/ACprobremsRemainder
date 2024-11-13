from bs4 import BeautifulSoup
from playwright.async_api import async_playwright
import random
import asyncio
import re

ACproblems_url = "https://kenkoooo.com/atcoder/#/table/"

async def get_ACproblem() -> list[str]:

    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch()
        context = await browser.new_context()

        # ページを開く
        page = await context.new_page()

        # 指定したURLに遷移
        await page.goto(ACproblems_url)

        # javascriptによってページが変わるまで待機
        await asyncio.sleep(3)

        content = await page.content()

        # BeautifulSoupでHTMLを解析
        soup = BeautifulSoup(content, 'html.parser')

        trs_with_class = soup.find_all(class_="table-problem")
        problem_links = []
        for row in trs_with_class:
            temp = row.find('a')
            if temp == None:
                continue
            problem_url = temp.get('href')
            if re.search(r'abc\d{3}_[1234abcd]', problem_url):
                print(problem_url)
                problem_links.append(problem_url)

    return random.choice(problem_links)

if __name__ == '__main__':
    asyncio.run(get_ACproblem())