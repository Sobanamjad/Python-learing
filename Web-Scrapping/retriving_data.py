from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(channel="chrome")
    page = browser.new_page()
    page.goto("https://zerolifestyle.co/pages/smart-watches", wait_until="domcontentloaded", timeout=60000)

    html_content = page.content()

    with open("zero_rendered.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    page.screenshot(path="zero_page.png", full_page=True)

    browser.close()
