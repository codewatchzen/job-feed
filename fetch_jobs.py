import requests, json, os
from bs4 import BeautifulSoup

def scrape_indeed(query="Software Engineer"):
    url = f"https://www.indeed.com/jobs?q={query.replace(' ', '+')}&limit=20"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Connection": "keep-alive",
        "Referer": "https://www.google.com/"
    }
    r = requests.get(url, headers=headers)
    print("Indeed status:", r.status_code)
    print("Indeed HTML snippet:", r.text[:500])  # Print first 500 chars
    soup = BeautifulSoup(r.text, "html.parser")

    jobs = []
    for div in soup.select("a.tapItem"):
        title = div.select_one("h2.jobTitle")
        company = div.select_one("span.companyName")
        if title and company:
            jobs.append({
                "title": title.text.strip(),
                "company": company.text.strip(),
                "url": "https://www.indeed.com" + div["href"]
            })
    return jobs[:5]

def scrape_lever():
    url = "https://api.lever.co/v0/postings/leverdemo?mode=json"
    r = requests.get(url)
    postings = r.json()
    return [{"title": p["text"], "company": p.get("categories", {}).get("team", "Lever"), "url": p["hostedUrl"]}
            for p in postings if "Software Engineer" in p["text"]][:20]

def scrape_greenhouse():
    url = "https://boards-api.greenhouse.io/v1/boards/greenhouse/jobs"
    try:
        r = requests.get(url)
        data = r.json().get("jobs", [])
        return [{"title": j["title"], "company": "Greenhouse", "url": j["absolute_url"]}
                for j in data if "Software Engineer" in j["title"]][:20]
    except Exception:
        return []

def scrape_all():
    jobs = []
    indeed_jobs = scrape_indeed()
    print(f"Indeed jobs found: {len(indeed_jobs)}")
    jobs.extend(indeed_jobs)

    lever_jobs = scrape_lever()
    print(f"Lever jobs found: {len(lever_jobs)}")
    jobs.extend(lever_jobs)

    greenhouse_jobs = scrape_greenhouse()
    print(f"Greenhouse jobs found: {len(greenhouse_jobs)}")
    jobs.extend(greenhouse_jobs)

    os.makedirs("./docs", exist_ok=True)
    with open("./docs/jobs.json", "w") as f:
        json.dump(jobs, f, indent=2)

if __name__ == "__main__":
    scrape_all()
