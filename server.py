''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
#Import Flask, render_template, request from the flask framework package
from flask import Flask, render_template, request
#Import the sentiment_analyzer function from the package created
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask("Emotion Detector")
@app.route("/emotionDetector")
def sent_analyzer():
    ''' Receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector() function.
        The output returned shows all the detected emotions, their scores, 
        and the dominant emotion.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)
    #check result is valid
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    response = (f"For the given statement, the system response is "
    f"'anger': {result['anger']}, "
    f"'disgust': {result['disgust']}, "
    f"'fear': {result['fear']}, "
    f"'joy': {result['joy']} and "
    f"'sadness': {result['sadness']}. "
    f"The dominant emotion is {result['dominant_emotion']}.")
    return response

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
