
import boto3

def lambda_handler(event,context):
    comprehend = boto3.client(service_name='comprehend', region_name='us-east-1')
    message = event['message']
    stringMessage = str(message)
    obj = comprehend.detect_sentiment(Text=stringMessage, LanguageCode='en')
    sentimentScore = obj["SentimentScore"]
    Positive = sentimentScore['Positive']
    Negative = sentimentScore['Negative']
    Neutral = sentimentScore['Neutral']
    Mixed = sentimentScore['Mixed']
    sentiment = obj["Sentiment"]
    
    return {
        'Sentiment' : sentiment,
        'PositiveConfidence' : Positive,
        'NegativeConfidence' : Negative,
        'NeutralConfidence' : Neutral,
        'MixedConfidence' : Mixed,
        'statusCode': 200
        
    }