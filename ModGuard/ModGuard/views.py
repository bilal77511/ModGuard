import json
from django.http import JsonResponse
from . import apifunctions as api


def single_message(request, message):

     # Call the API to analyze the comment.
    mesres = api.analyze_comment(message)
    print(mesres)
    
    # Assuming mesres[0].text is a string in JSON format, parse it to a dictionary.
    try:
        res = json.loads(mesres[0].text)  # This line changed to parse the JSON string.
    except json.JSONDecodeError:
        # If parsing fails, return an error message.
        return JsonResponse({'error': 'Failed to decode the API response'}, status=400)
    return JsonResponse(res)

def message_list(request):
    messages = [
        {
            "toxicornot": "toxic",
            "stateofmind": "raciest",
            "description": "the person thinks some people should not vote"
        },
        # Add more messages here if needed
    ]
    return JsonResponse(messages, safe=False)
