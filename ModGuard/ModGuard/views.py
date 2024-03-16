from django.http import JsonResponse

def single_message(request):
    response_data = {
        "toxicornot": "toxic",
        "stateofmind": "raciest",
        "description": "the person thinks some people should not vote"
    }
    return JsonResponse(response_data)

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
