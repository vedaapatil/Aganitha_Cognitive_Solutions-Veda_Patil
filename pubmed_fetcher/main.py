import argparse
from pubmed_fetcher.fetch import fetch_papers, filter_papers, save_to_csv

def main():
    parser = argparse.ArgumentParser(description="Fetch research papers from PubMed.")
    parser.add_argument("query", help="The query to search PubMed")
    parser.add_argument("-f", "--file", type=str, help="Filename to save results (CSV).")
    parser.add_argument("-d", "--debug", action="store_true", help="Print debug information.")

    args = parser.parse_args()

    try:
        papers = fetch_papers(args.query, debug=args.debug)
        filtered_results = filter_papers(papers)

        if args.file:
            save_to_csv(filtered_results, args.file)
        else:
            for result in filtered_results:
                print(result)
    except Exception as e:
        print(f"Error: {e}")
