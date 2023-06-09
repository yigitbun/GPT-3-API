import openai

# Set up the OpenAI API client
openai.api_key = ""

# Define a function to generate responses
def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0.5,
    )

    return response.choices[0].text.strip()

# Define a function to handle user input and generate responses
def chat():
    print("Welcome to the chatbot! Type 'quit' to exit.")
    while True:
        # Get user input
        user_input = input("You: ")

        # Check if user wants to quit
        if user_input.lower() == "quit":
            print("Chatbot: Goodbye!")
            break

        # Generate a response using the OpenAI API
        response = generate_response(user_input)

        # Print the response
        print("Chatbot:", response)

# Call the chat function to start the chatbot
chat()
