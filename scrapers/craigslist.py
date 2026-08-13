def craigslist(self, query):
    url = f"https://calgary.craigslist.org/search/sss?query={query}"
    try:
        r = requests.get(url, timeout=5)
        soup = BeautifulSoup(r.text, "html.parser")
        items = []

        for ad in soup.select(".result-row"):
            title_el = ad.select_one(".result-title")
            price_el = ad.select_one(".result-price")

            title = title_el.get_text(strip=True) if title_el else ""
            price = price_el.get_text(strip=True).replace("$", "") if price_el else "0"
            link = title_el["href"] if title_el and title_el.has_attr("href") else ""

            items.append({
                "title": title,
                "price": price,
                "platform": "craigslist",
                "url": link
            })

        return items
    except Exception:
        return []
