import requests
import json

def emotion_detector(text_to_analyze):
    '''Analyze text, detect the emotions in it, and find the dominant emotion'''

    #HTTPs request for IBM Watson's Emotion Detector
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobject = { "raw_document": { "text": text_to_analyze } }
     
    response = requests.post(url, json = myobject, headers=header)  
  
    #return None values if status code is 400 or 500 (invalid input, for example)
    if response.status_code == 400 or response.status_code == 500:
        return{'anger': None, 
        'disgust': None,
        'fear' : None,
        'joy':None,
        'sadness': None,
        'dominant_emotion': None} 
    else:
        #convert the JSON content to a dictionary
        formatted_response = json.loads(response.text)

        #extract the list of emotion scores
        emotion_scores = formatted_response['emotionPredictions'][0]['emotion']
    
        #find the dominant emotion in the list
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    
        #add the dominant emotion in the list of emotions
        emotion_scores['dominant_emotion'] = dominant_emotion
        return emotion_scores
    