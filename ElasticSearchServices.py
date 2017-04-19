# This is the file where we connect to ES + find and insert data

#----------Parsing Configuration File--------------------

myvars = {}
with open("auth.txt") as myfile:
    for line in myfile:
        name, var = line.partition(":")[::2]
        myvars[name.strip()] = var.strip()

#---------Import Elastic Search libraries----------------

from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth

# Our elastic search engine

HOSTADDRESS=myvars['elastic_search_host_address']

awsauth = AWS4Auth(myvars['aws_api_key'], myvars['aws_secret'], "us-west-1", 'es')

class ElasticSearchServices:

    def __init__(self):
        self.es = Elasticsearch(
            hosts=[{'host': HOSTADDRESS, 'port': 443}],
            http_auth=awsauth,
            use_ssl=True,
            verify_certs=True,
            connection_class=RequestsHttpConnection
        )

    def store_data(self, index, doc_type, body):
        results = self.es.index(
    			index=index,
    			doc_type=doc_type,
    			body=body
    		)

        return results

    def create_collection(self, index, body):
        print ("Creating collection...")
        results = self.es.indices.create(
            index=index,
            ignore=400,
            body=body
        )
        return results

    def search(self, index, doc_type, body, size):
    	results = self.es.search(
    			index = index,
    			doc_type = doc_type,
    			body = body,
    			size = size
    		)

    	return results

    def total_hits(results):
    	return results['hits']['total']

