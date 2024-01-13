import os.path
import urllib.parse
import boto3

RAW_AUDIO_BUCKET_NAME = os.environ['RAW_AUDIO_BUCKET_NAME']
TRANSCRIBED_AUDIO_BUCKET_NAME = os.environ['TRANSCRIBED_AUDIO_BUCKET_NAME']
AUDIO_LANGUAGE_CODE = os.environ['AUDIO_LANGUAGE_CODE']

transcribe_client = boto3.client('transcribe')

def transcribe_audio(event):
    fileName = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])
    objectUrl = 'https://s3.amazonaws.com/{0}/{1}'.format(RAW_AUDIO_BUCKET_NAME, fileName)   
    print("Audio to transcribe: " + fileName)
    response = transcribe_client.start_transcription_job(
            TranscriptionJobName=fileName,
            LanguageCode=AUDIO_LANGUAGE_CODE,
            MediaFormat='mp3',
            Media={
                'MediaFileUri': objectUrl
            },
            OutputKey=fileName.replace(".mp3", ".json"),
            OutputBucketName=TRANSCRIBED_AUDIO_BUCKET_NAME
            )
    print("Successfully transcribed audio to bucket: " + TRANSCRIBED_AUDIO_BUCKET_NAME)

def lambda_handler(event, context):
    try:
        transcribe_audio(event)
    except Exception as e:
        print('Exception when transcribing audio')
        print(e)
