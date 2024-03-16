import anthropic
import json
import os
client = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),
)

def analyze_comment(comment):
    message = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=1000,
        temperature=0.0,
        system="""You are a moderator, and I want your review on this comment. For comment, please:

        1. Categorize it as either 'positive' or 'negative'.
        2. Identify the state of mind (e.g., racist, threatening, harmless,sexist) behind the comment.
        3. Provide a small description explaining why you categorized the comment as postive or negative and also the state of mind.

        Return your analysis in JSON format, following this example:

        {
            "comment": "I think Asian people should not vote in our country",
            "behaviour": "negative",
            "stateofmind": "racist",
            "description": "The person thinks some people should not vote based on their race or ethnicity, which is a racist and discriminatory view."
        }
        """,
        messages=[
            {"role": "user", "content": comment}
        ]
    )

    return message.content

message="i hate when people try to kill animals for eating purpose if i was incharge of it i would have killed them"
result = analyze_comment(message)
print(result)