import random

default_responses = [
    "I'm sorry, I don't understand that. Can you please rephrase?",
    "Can you clarify that for me?",
    "I'm not sure I understand. Could you say that in a different way?",
    "I don't have an answer for that. Can you ask something else?",
    "That's interesting! Tell me more."
]

# create two types of default responses 
# positive and negative to seperate responses
def solve_math(expression):
    try:
        result = sp.sympify(expression)
        return f"The result is: {result}"
    except Exception as e:
        return f"Sorry, I couldn't solve the expression. {str(e)}"

def AbrarTechBot_response(user_input):
    user_input = user_input.lower()  
    
   
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm here to help you!"
    elif "name" in user_input:
        return "I'm your friendly chatbot, AbrarTechBot."
    elif "thank you" in user_input or "thanks" in user_input:
        return "You're welcome! If you have any other questions, feel free to ask."
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"

    
    elif "founder" in user_input or "creator" in user_input:
        return "My creator is Abrar Ahamed, pursuing their 1st year B.Tech in Artificial Intelligence and Data Science at Dhaanish Ahmed College of Engineering."

    
    elif "capital of india" in user_input:
        return "The capital of India is New Delhi."
    elif "largest state in india" in user_input:
        return "The largest state in India by area is Rajasthan."
    elif "smallest state in india" in user_input:
        return "The smallest state in India by area is Goa."
    elif "national animal of india" in user_input:
        return "The national animal of India is the Bengal tiger."
    elif "national bird of india" in user_input:
        return "The national bird of India is the Indian peacock."
    elif "national flower of india" in user_input:
        return "The national flower of India is the lotus."
    elif "first prime minister of india" in user_input:
        return "The first Prime Minister of India was Jawaharlal Nehru."
    elif "father of the nation in india" in user_input:
        return "Mahatma Gandhi is known as the Father of the Nation in India."
    
    
    elif "capital of usa" in user_input:
        return "The capital of the United States is Washington, D.C."
    elif "largest country in the world" in user_input:
        return "The largest country in the world by area is Russia."
    elif "smallest country in the world" in user_input:
        return "The smallest country in the world by area is Vatican City."
    elif "tallest mountain in the world" in user_input:
        return "The tallest mountain in the world is Mount Everest."
    elif "deepest ocean in the world" in user_input:
        return "The deepest ocean in the world is the Pacific Ocean."
    elif "fastest land animal" in user_input:
        return "The fastest land animal is the cheetah."
    elif "largest desert in the world" in user_input:
        return "The largest desert in the world is the Sahara Desert."
    elif "longest river in the world" in user_input:
        return "The longest river in the world is the Nile River."
    elif "largest ocean in the world" in user_input:
        return "The largest ocean in the world is the Pacific Ocean."
    elif "most populated country in the world" in user_input:
        return "The most populated country in the world is China."

    
    elif "what is the time" in user_input:
        return "I don't have access to real-time data, but you can check the time on your device."
    elif "what is the date" in user_input:
        return "I don't have access to real-time data, but you can check the date on your device."
    elif "how to make coffee" in user_input:
        return "To make coffee, you need coffee grounds, water, and a coffee maker. Brew the coffee according to your coffee maker's instructions."
    elif "how to cook rice" in user_input:
        return "To cook rice, rinse the rice under cold water, then combine 1 cup of rice with 2 cups of water in a pot. Bring to a boil, then reduce heat to low, cover, and simmer for 18-20 minutes."
    elif "how to tie a tie" in user_input:
        return "To tie a tie, start with the wide end on your right and the small end on your left. Cross the wide end over the small end, then bring it up through the loop around your neck. Pass it down through the knot in front, tighten the knot, and adjust."
    elif "how to boil an egg" in user_input:
        return "To boil an egg, place the egg in a pot of water and bring it to a boil. Once boiling, reduce the heat and let it simmer for 9-12 minutes depending on the desired level of doneness."
    elif "how to lose weight" in user_input:
        return "To lose weight, maintain a balanced diet, exercise regularly, stay hydrated, and get enough sleep. It's best to consult with a healthcare provider for personalized advice."

    
    elif "tell me a fun fact" in user_input:
        return random.choice([
            "Did you know? Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still edible.",
            "Did you know? The shortest war in history was between Britain and Zanzibar on August 27, 1896. Zanzibar surrendered after 38 minutes.",
            "Did you know? A day on Venus is longer than a year on Venus. It takes Venus about 243 Earth days to rotate once, but only about 225 Earth days to orbit the Sun.",
            "Did you know? Bananas are berries, but strawberries aren't."
        ])

    
    elif "solve" in user_input or "calculate" in user_input:
        expression = user_input.replace("solve", "").replace("calculate", "").strip()
        return solve_math(expression)

    
    elif "chemical symbol for water" in user_input:
        return "The chemical symbol for water is H2O."
    elif "atomic number of carbon" in user_input:
        return "The atomic number of carbon is 6."
    elif "formula for sodium chloride" in user_input:
        return "The chemical formula for sodium chloride is NaCl."
    
    
    elif "speed of light" in user_input:
        return "The speed of light in a vacuum is approximately 299,792,458 meters per second."
    elif "newton's first law" in user_input:
        return "Newton's first law states that an object in motion will stay in motion, and an object at rest will stay at rest unless acted upon by an external force."
    elif "gravity on earth" in user_input:
        return "The acceleration due to gravity on Earth is approximately 9.8 meters per second squared."
    
    
    elif "first president of the united states" in user_input:
        return "The first President of the United States was George Washington."
    elif "world war ii start" in user_input:
        return "World War II started in 1939."
    elif "fall of the berlin wall" in user_input:
        return "The Berlin Wall fell on November 9, 1989."
    
   
    elif "synonym for happy" in user_input:
        return "A synonym for happy is joyful."
    elif "antonym for big" in user_input:
        return "An antonym for big is small."
    elif "plural of mouse" in user_input:
        return "The plural of mouse is mice."
    
    
    else:
        return random.choice(default_responses)

def main():
    print("AbrarTechBot: Hello! Type 'bye' to exit the chat.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ["bye", "goodbye"]:
            print("AbrarTechBot: Goodbye! Have a great day!")
            break
        
        response = AbrarTechBot_response(user_input)
        print("AbrarTechBot:", response)

if __name__ == "_main_":
    main()
