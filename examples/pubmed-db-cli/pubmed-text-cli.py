#pip install pymed Bio
import argparse
import pandas as pd
from pymed import PubMed
from Bio import Entrez

def search_pubmed(search_term, max_results, include_pubmed_id, include_title, include_abstract):
    pubmed = PubMed(tool="MyTool", email="aalamel@clemson.edu")
    results = pubmed.query(search_term, max_results=max_results)
    article_list = []
    for article in results:
        article_dict = article.toDict()
        if include_pubmed_id:
            pubmed_id = article_dict['pubmed_id'].partition('\n')[0]
        else:
            pubmed_id = ""
        if include_title:
            title = article_dict['title']
        else:
            title = ""
        if include_abstract:
            abstract = article_dict['abstract']
        else:
            abstract = ""
        article_list.append({'pubmed_id': pubmed_id, 'title': title, 'abstract': abstract})
    df = pd.DataFrame(article_list)
    return df

def main():
    parser = argparse.ArgumentParser(description="PubMed Search CLI")
    parser.add_argument("search_term", help="Keyword(s) to search in PubMed database")
    parser.add_argument("-m", "--max_results", type=int, default=100, help="Maximum number of results (default: 100)")
    parser.add_argument("-p", "--pubmed_id", action="store_true", help="Include PubMed ID in the output")
    parser.add_argument("-t", "--title", action="store_true", help="Include title in the output")
    parser.add_argument("-a", "--abstract", action="store_true", help="Include abstract in the output")
    parser.add_argument("-o", "--output", default="output.csv", help="Output CSV file name (default: output.csv)")
    args = parser.parse_args()

    df = search_pubmed(args.search_term, args.max_results, args.pubmed_id, args.title, args.abstract)
    df.to_csv(args.output, index=False)
    print(f"Results saved to {args.output}")

if __name__ == "__main__":
    main()
