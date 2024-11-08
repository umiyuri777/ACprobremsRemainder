import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time
from playwright.sync_api import sync_playwright

ACproblems_url = "https://kenkoooo.com/atcoder/#/table/"

def get_ACproblem() -> str:

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        context = browser.new_context()

        # ページを開く
        page = context.new_page()

        # 指定したURLに遷移
        page.goto(ACproblems_url)

        # javascriptによってページが変わるまで待機
        time.sleep(3)

        # BeautifulSoupでHTMLを解析
        soup = BeautifulSoup(page.content(), 'html.parser')

        trs_with_class = soup.find_all(class_="table-problem")

        problem_links = []
        for row in trs_with_class:
            temp = row.find('a')
            if temp == None:
                continue
            problem_url = row.find('a').get('href')
            print(problem_url)
            problem_links.append(problem_url)

        print(problem_links)





get_ACproblem()