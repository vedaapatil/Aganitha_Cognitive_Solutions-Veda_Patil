import requests
import re
import csv
from typing import List, Dict

def fetch_papers(query: str, debug: bool = False) -> dict:
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmax": 10,
        "usehistory": "y",
        "retmode": "json"
    }
    response = requests.get(base_url, params=params)
    if debug:
        print(f"Request URL: {response.url}")
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Error fetching data from PubMed API.")

def get_paper_details(pmid: str) -> dict:
    # Placeholder function to simulate paper details
    return {
        "title": f"Title for {pmid}",
        "pub_date": "2023-01-01",
        "authors": [
            {"name": "Dr. Jane Doe", "affiliation": "Some Biotech Company"},
            {"name": "Prof. John Smith", "affiliation": "Some University"},
        ],
        "corresponding_email": "jane.doe@biotech.com"
    }

def filter_papers(papers: dict) -> List[Dict[str, str]]:
    filtered = []
    for paper in papers.get("esearchresult", {}).get("idlist", []):
        details = get_paper_details(paper)
        authors = details.get("authors", [])
        company_affiliations = []
        non_academic_authors = []

        for author in authors:
            affiliation = author.get("affiliation", "")
            if re.search(r"pharma|biotech", affiliation, re.IGNORECASE):
                company_affiliations.append(author["name"])
            elif "university" not in affiliation.lower() and "lab" not in affiliation.lower():
                non_academic_authors.append(author["name"])

        if company_affiliations:
            filtered.append({
                "PubmedID": paper,
                "Title": details["title"],
                "Publication Date": details["pub_date"],
                "Non-academicAuthor(s)": ", ".join(non_academic_authors),
                "CompanyAffiliation(s)": ", ".join(company_affiliations),
                "Corresponding Author Email": details.get("corresponding_email", "")
            })
    return filtered

def save_to_csv(results: List[Dict[str, str]], filename: str):
    headers = ["PubmedID", "Title", "Publication Date", "Non-academicAuthor(s)", "CompanyAffiliation(s)", "Corresponding Author Email"]
    with open(filename, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        for result in results:
            writer.writerow(result)
