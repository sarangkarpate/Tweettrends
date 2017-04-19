from ElasticSearchServices import ElasticSearchServices
from TweetHandler import TwitterHandler
import json
#---- Elastic Search Details -------

index = "tweettrends"
collection = {
	"mappings": {
		"finaltweets2": {
			"properties": {
				"id": {
					"type": "string"
				},
				"message": {
					"type": "string"
				},
				"author": {
					"type": "string"
				},
				"timestamp": {
					"type": "string"
				},
				"location": {
					"type": "geo_point"
				},
                "sentiment": {
					"type": "string"
				}
			}
		}
	}
}


#--------------------------------------------------------

try:
    collection_service = ElasticSearchServices()
    collection_service.create_collection(index, collection)
except:
    print "Index already created"

def persistTweet(tweet):
    tweeter = TwitterHandler()
    json_msg = json.loads(tweet['Message'])
    tid = json_msg['id']
    location_data = json_msg['location']
    message = json_msg['message']
    author = json_msg['author']
    timestamp = json_msg['timestamp']
    sentiment = json_msg['sentiment']
    
    response = tweeter.insertTweet(tid, location_data, message, author, timestamp, sentiment)
    # print response
    return response