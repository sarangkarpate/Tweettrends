# Importing Natural Language Processing libraries

import sys
from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 as features
import re
#--------------------------------------------------------------------------------------------------

'''reload(sys)
sys.setdefaultencoding('utf8')'''

# sentiment analysis watson username and password
wusername = '1992498e-7c8e-4be1-abc9-7efab727c89b'
wpassword = 'tohP1GX4NKQ3'

natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2017-02-27',
    username=wusername,
    password=wpassword)

def sentimentAnalysis(text):
    try:
        # Remove unwanted special characters from text
        correct_text=re.sub('[^a-zA-Z0-9 \n\.]', '', text)
        # encoded_text = urllib.quote(text)
        response = natural_language_understanding.analyze(
            text=correct_text,
            features=[features.Emotion(), features.Sentiment()])
        # print text
        # emotion_dict = response['emotion']['document']['emotion']
        overall_sentiment = response['sentiment']['document']['label']

        # print ("The overall sentiment of the text is: "+overall_sentiment)
        # print("The emotional quotient of the text is as follows: ")
        # for key in emotion_dict:
        #     print(key + " : " + str(emotion_dict[key]))
        return overall_sentiment

    except Exception, e:
        print 'Sentiment API error ' + str(e)

def clean_tweet(tweet):
    '''
    Utility function to clean tweet text by removing links, special characters
    using simple regex statements.
    '''
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

def tweet_sentiment_analysis(tweet):
    cleansed_tweet = clean_tweet(tweet)
    sentimentRating = sentimentAnalysis(cleansed_tweet)
    return sentimentRating
    