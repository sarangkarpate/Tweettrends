# Here is where we can store and seach for tweets from the document

from ElasticSearchServices import ElasticSearchServices

class TwitterHandler:

	def __init__(self):
		self.es = ElasticSearchServices()
		self.index = "tweettrends"
		self.doc_type = "finaltweets2"

	def getTweets(self, keyword):
		body = {
			"query": {
				"match": {
					"_all": keyword
				}
			}
		}

		size = 10000
		result = self.es.search(self.index, self.doc_type, body, size)

		return result

	def getTweetsWithDistance(self, keyword, distance, latitude, longitude):
		distance_string = distance + 'km'
		print 'Searching ', distance_string, ' from location Latitude: ', latitude, ' ; Longitude: ', longitude

		if (type(latitude) != float):
			latitude = float(latitude)

		if (type(longitude) != float):
			longitude = float(longitude)

		body = 	{
				    "query": {
				        "bool": {
				            "must": {
				                "match": {"_all": keyword }
				            },
				        	"filter": {
								"geo_distance": {
									"distance": distance_string,
									"distance_type": "sloppy_arc",
									"location": {
										"lat": latitude,
										"lon": longitude
									}
								}
							}
					    }
				    }            
				}

		size = 10000
		result = self.es.search(self.index, self.doc_type, body, size)

		return result

	def insertTweet(self, t_id, location_data, tweet, author, timestamp, sentiment):
		body = {
			"id": t_id,
			"message": tweet,
			"author": author,
			"timestamp": timestamp,
			"location": location_data,
			"sentiment": sentiment

		}
		result = self.es.store_data(self.index, self.doc_type, body)
		return result

