import os
import requests
from xml.etree import ElementTree as ET
from transformers import pipeline

def fetch_pubmed_articles(query, max_results=5):
    # Step 1: Search for PubMed IDs
    search_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    search_params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": max_results
    }
    response = requests.get(search_url, params=search_params)
    pmids = response.json().get("esearchresult", {}).get("idlist", [])
    if not pmids:
        return []

    # Step 2: Fetch article details for those IDs
    fetch_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    fetch_params = {
        "db": "pubmed",
        "id": ",".join(pmids),
        "retmode": "xml"
    }
    fetch_response = requests.get(fetch_url, params=fetch_params)
    root = ET.fromstring(fetch_response.text)

    # Step 3: Summarize each abstract
    articles = []
    for article in root.findall(".//PubmedArticle"):
        title = article.findtext(".//ArticleTitle", default="No Title")
        abstract = article.findtext(".//Abstract/AbstractText", default="No Abstract")
        pmid = article.findtext(".//PMID", default="Unknown")
        url = f"https://pubmed.ncbi.nlm.nih.gov/{pmid}"

        summary = "Not available"
        if abstract and len(abstract.split()) > 10:
            try:
                result = summarizer(abstract, max_length=60, min_length=20, do_sample=False)
                summary = result[0]["summary_text"]
            except Exception as e:
                summary = f"⚠️ Summarization failed ({str(e)[:40]}...)"

        articles.append({
            "title": title.strip(),
            "abstract": abstract.strip(),
            "summary": summary.strip(),
            "url": url
        })
    return articles

if __name__ == "__main__":
    query = os.environ.get("QUERY", "AI in heart surgery")
    print(f"\n🔍 PubMed AI Agent Query: {query}\n")

    # Init model just once (so it's not re-loaded per summary)
    summarizer = pipeline(
        "summarization",
        model="t5-base",
        tokenizer="t5-base"
    )

    try:
        results = fetch_pubmed_articles(query)
        if not results:
            print(" No results found.")
        for i, article in enumerate(results, 1):
            print(f"\n--- Article {i} ---")
            print(f" Title   : {article['title']}")
            print(f" Abstract: {article['abstract']}")
            print(f" Summary : {article['summary']}")
            print(f" URL     : {article['url']}")
    except Exception as e:
        print(f"❌ Error: {str(e)}")
