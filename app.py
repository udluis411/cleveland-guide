from anthropic import Anthropic

client = Anthropic()

with open("guide.txt", "r") as f:
    guide = f.read()

system_prompt = f"""You are LuLu's Cleveland Guest Assistant. You help Airbnb guests staying in Ohio City, Cleveland get personalized local recommendations based on their interests and situation.

You have been given LuLu's personal guide to the neighborhood below. Use ONLY this guide to make recommendations — do not invent places or add recommendations not in the guide. 

When responding:
- Be warm, friendly and conversational — like a knowledgeable local friend
- Ask about their interests and transportation if they haven't told you
- Give specific, tailored recommendations based on what they tell you
- Include helpful tips (like "make a reservation" or "patio is great in warm weather")
- Keep responses concise — 3 to 5 recommendations at a time is better than a big list
- If they ask about something not in the guide, say you're not sure and suggest they check Google

Here is LuLu's guide:

{guide}"""

conversation_history = []

print("""
👋 Welcome to LuLu's Cleveland Guest Guide!

I'm your personal neighborhood assistant, powered by LuLu's own local knowledge 
of Ohio City and Cleveland. Think of me as having LuLu on speed dial!

Here are some ways to get the most out of me:

  🍺  "We love craft beer and great food — what do you recommend?"
  👨‍👩‍👧  "We have two kids and want a fun afternoon — any ideas?"
  🚗  "We have a car and want to explore beyond the neighborhood"
  ☔  "It's raining — what's good to do inside?"
  🌅  "What's the best way to spend a Sunday morning?"
  🍣  "We want the most special dinner possible"
  🎨  "We love art and culture — where should we go?"
  🏛️  "What are the best museums in Cleveland worth the drive?"
  🎵  "We want to catch some live music — what's around?"
  🎭  "Are there any theaters or performances worth seeing?"

The more you tell me about your group, interests, and whether you have a car,
the better I can tailor recommendations just for you.

Type 'quit' at any time to exit.
""")

while True:
    user_input = input("You: ").strip()
    
    if user_input.lower() == 'quit':
        print("Enjoy your stay in Ohio City!")
        break
    
    if not user_input:
        continue
    
    conversation_history.append({
        "role": "user",
        "content": user_input
    })
    
    response = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=1024,
        system=system_prompt,
        messages=conversation_history
    )
    
    assistant_message = response.content[0].text
    
    conversation_history.append({
        "role": "assistant", 
        "content": assistant_message
    })
    
    print(f"\nLuLu's Assistant: {assistant_message}\n")
