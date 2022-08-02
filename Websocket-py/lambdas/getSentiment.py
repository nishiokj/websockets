import json 

import boto3

def lambda_handler(event,context):
    #call googleAPI
    comprehend = boto3.client(service_name='comprehend', region_name='us-east-1')
    #event['message'] = "that guy is a clown and I do not like him"
    message = event['message']
    #print(event)
    stringMessage = str(message)
    #stringMessage = "I think that the current markets indicate that the stock market will go down. With Powell raising interest rates money will surely tighten in the coming months. This could be bad news for popular indexes"
    obj = comprehend.detect_sentiment(Text=stringMessage, LanguageCode='en')
    
    sentimentScore = obj["SentimentScore"]
    Positive = sentimentScore['Positive']
    Negative = sentimentScore['Negative']
    Neutral = sentimentScore['Neutral']
    Mixed = sentimentScore['Mixed']
    sentiment = obj["Sentiment"]
    
    return {
        'Sentiment' : sentiment,
        'Positive' : Positive,
        'Negative' : Negative,
        'Neutral' : Neutral,
        'Mixed' : Mixed,
        'statusCode': 200
        
    }