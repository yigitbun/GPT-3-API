import openai
openai.api_key = ""

# Set the engine and temperature
engine = "davinci"
temperature = 0.7

# Start a conversation loop
while True:
    # Get user input
    user_input = input("You: ")

    # Exit the loop if user types "exit"
    if user_input.lower() == "exit":
        break

    # Generate a response
    prompt = f"You: {user_input}\nChatbot:"
    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        max_tokens=60,
        temperature=temperature
    )

    # Print the response
    message = response.choices[0].text.strip()
    print(f"Chatbot: {message}")
