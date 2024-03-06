import json

from rest_framework.response import Response
from rest_framework.decorators import api_view

from openai import OpenAI

client = OpenAI(
    api_key="{PLACE YOUR KEY HERE}",
)

@api_view(['GET'])
def getData(request):
    return Response({
        'error': 'false',
        'result': 'API Works :)'
    })

@api_view(['POST'])
def postData(request):
    query = "Extract the following fields \"color,neck type,sleeve length\" as a JSON object in this format {color:,neckType:,sleeveLength:}.";

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": " ".join([request.data["prompt"], query]),
            }
        ],
        model="gpt-3.5-turbo",
    )
    return Response(json.loads(chat_completion.choices[0].message.content))