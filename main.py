from extraction.web_scraper import fetch_webpage


url = "https://books.toscrape.com/"

result = fetch_webpage(url)


if result["success"]:
    soup = result["soup"]

    print("Website fetched successfully.")
    print("Status code:", result["status_code"])

    print("Page title:", soup.title.get_text(strip=True))

    headings = soup.find_all("h3")

    print("\nBook titles:")

    for heading in headings:
        book_link = heading.find("a")

        if book_link:
            print(book_link.get("title"))

else:
    print("Error:", result["error"])
    print("Status code:", result["status_code"])