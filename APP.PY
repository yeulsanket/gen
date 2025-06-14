GROQ_API_KEY = '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'

from groq import Groq

client = Groq(
    api_key=GROQ_API_KEY,
)
while True  :
  chat_completion = client.chat.completions.create(
    messages=[{
      'role' : 'user',
      'content' : 'i am pritam'
    },
          
            {
            "role": "system",
            "content": input("you:")
            },

    ],
    model="llama-3.3-70b-versatile",
    stream=False,
)
  print(chat_completion.choices[0].message.content)
