from Bio import Entrez

class PubMed:
    def __init__(self, email):
        self.email = email
    def fetch_details(self, ids):
        Entrez.email = self.email
        handle = Entrez.efetch(db='pubmed',
                           retmode='xml',
                           id=','.join(ids))
        return Entrez.read(handle)

    def searchArticles(self, query):
        Entrez.email = self.email
        handle = Entrez.esearch(db='pubmed', retmax=10, term=query)
        record = Entrez.read(handle)
        handle.close()
        return self.fetch_details(record['IdList'])
 
