# 🧰 Software Engineer Job Feed (Free & Open)

A simple, no-cost job board that scrapes and lists the latest **Software Engineer** openings from multiple popular sites — auto-updated daily and hosted on **GitHub Pages**.

🔗 View Jobs: [https://your-username.github.io/job-feed/](https://your-username.github.io/job-feed/)

---

## 🔍 How It Works

- 🕷 Scrapes jobs from:
  - Indeed
  - Lever
  - Greenhouse
- 💾 Stores as `docs/jobs.json`
- 🖥 Converts to `docs/index.html`
- 🔁 GitHub Actions runs daily
- 🌐 GitHub Pages hosts the site

---

## 🚀 Setup Locally

```bash
git clone https://github.com/your-username/job-feed.git
cd job-feed
pip install -r requirements.txt
python fetch_jobs.py
python generate_html.py
