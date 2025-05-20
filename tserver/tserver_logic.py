# tserver_logic.py
import requests
from bs4 import BeautifulSoup
import logging

def fetch_recent_testworld_notices(max_count=10):
    url = "https://maplestory.nexon.com/Testworld/News/Update"
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        notices = soup.select("#container .contents_wrap .news_board ul li")[:max_count]

        notice_data = []
        for notice in notices:
            link_tag = notice.select_one("p > a")
            date_tag = notice.select_one("div.heart_date dd")

            if link_tag and date_tag:
                title = link_tag.get_text(strip=True)
                href = link_tag['href']
                full_url = f"https://maplestory.nexon.com{href}"
                date = date_tag.get_text(strip=True)
                notice_data.append((date, title, full_url))

        if not notice_data:
            return []

        latest_date = notice_data[0][0]
        filtered = [(title, url) for date, title, url in notice_data if date == latest_date]

        return filtered

    except requests.exceptions.RequestException as e:
        logging.error(f"공지사항 크롤링 오류: {e}")
        return []
