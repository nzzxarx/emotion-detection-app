import requests
import json

def emotion_detector(text_to_analyse):
    # Task 7: Handling blank inputs
    if not text_to_analyse.strip():
        return {
            'anger': None, 'disgust': None, 'fear': None, 
            'joy': None, 'sadness': None, 'dominant_emotion': None
        }

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json=input_json, headers=headers)

    # Task 7: Handling API Error status code
    if response.status_code == 400:
        return {
            'anger': None, 'disgust': None, 'fear': None, 
            'joy': None, 'sadness': None, 'dominant_emotion': None
        }

    # Task 3: Formatting the output
    formatted_response = json.loads(response.text)
    
    # Extraire le dictionnaire des émotions
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    # Trouver l'émotion dominante (la clé avec la valeur maximale)
    dominant_emotion = max(emotions, key=emotions.get)

    return {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }