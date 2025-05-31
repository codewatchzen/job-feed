import json

def generate_html():
    with open("docs/jobs.json") as f:
        jobs = json.load(f)

    html = """
    <html>
    <head>
        <title>Software Engineer Jobs</title>
        <style>
            body { font-family: Arial, sans-serif; padding: 20px; }
            .job { margin-bottom: 20px; padding: 10px; border-bottom: 1px solid #ccc; }
            .title { font-size: 18px; font-weight: bold; }
            .company { font-size: 14px; color: #555; }
        </style>
    </head>
    <body>
        <h1>Latest Software Engineer Jobs</h1>
    """

    for job in jobs:
        html += f"""
        <div class="job">
            <div class="title"><a href="{job['url']}" target="_blank">{job['title']}</a></div>
            <div class="company">{job['company']}</div>
        </div>
        """

    html += "</body></html>"

    with open("docs/index.html", "w") as f:
        f.write(html)

if __name__ == "__main__":
    generate_html()
