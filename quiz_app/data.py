import requests

parameters={
    "amount":10,
    "type":"boolean",
    "category":18
}
question_data1 = requests.get(url="https://opentdb.com/api.php?amount=10&category=18&type=boolean",params=parameters);
question_data1.raise_for_status()
data=question_data1.json()
question_data=data["results"]
