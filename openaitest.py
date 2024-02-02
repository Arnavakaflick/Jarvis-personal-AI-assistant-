from openai import OpenAI
apikey = "your own api key"
client = OpenAI(apikey)
response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "user",
      "content": ""
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)


'''
{
  "choices": [
    {
      "text": "Club goers in downtown Philadelphia have been dealing with a virtual patrol of state Liquor Control Enforcement Agents, traversing the area's doorways with handheld devices that search for fake or underage IDs.\n\n\n\nThe handheld device, known as IDENT, allows agents to scan scans the magnetic stripe and bar code of a driver\u2019s license or other form of valid identification, and sends that information to a secure server where it is validated with the information stored in various state and federal databases. It can cross reference a face shot, photograph, and other information to verify that the ID is legitimate. According to the Pennsylvania Liquor Control Board, the devices help agents quickly evaluate hundreds of IDs in a single night. This helps reduce the amount of time it takes to identify a potential patron with a fake or invalid ID, which increases the effectiveness of their presence at the clubs and also helps ensure that those clubs are not selling alcohol to underage people. It also helps agents minimize the hassle and time spent checking customer's IDs one-by-one and potentially allows them to spend more time focusing on other enforcement and regulatory issues.",
      "index": 0,
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 1,
    "completion_tokens": 224,
    "total_tokens": 225
  }
}
'''
