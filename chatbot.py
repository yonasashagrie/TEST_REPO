import openai

openai.api_key = "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"

def ask_chatgpt(question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Adjust model as needed
        prompt=question,
        max_tokens=150,  # Adjust response length as needed
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()


print("Hi! my name is yobot and i am here to help you through your university journey :")
print("i'm going to ask you a few questions so i can get to know you a little better.")
name=str(input("what is your name?"))
print("hi",name)
age=int(input("how old are you?"))
if age<18:
    print("Wow! you're starting university at a young age! you must be really talented.")
if age==18:
    print("it's perfect age to join university by 18, i also join at 18.")
if age>18:
    print("that's fantastic! it's never too late to learn and grow.")        
faculty=str(input("what faculty do you belong to?"))
print("the",faculty,"is really great.how exciting!") 
majors=str(input("what is your majors?"))
print("Ah",majors,". A friend of mine studied that.")
print("i think those are all the question i needed to ask...")   
print("oh wait! i have one more.")
colour=str(input("what's your favourite colour?"))
colour=colour.lower()
class TextColors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'
if colour=="green":
    print(TextColors.GREEN + "amazing! we have the same colour choice" + TextColors.END)
else:    
    print(TextColors.BLUE + "i like",colour,"but my favourite coulor is blue, like the sky." + TextColors.END)
print("thanks for telling me more about your self! it's so lovely to meet you",name)
print("the",faculty,"faculity is lucy to have you!")
print("you can ask me whatever questions you need answers to and i'll do my best to answer them.")
print("when you're done asking questions, you can just say 'bye'.")
questions = ["how can i pay my tuition fees after registration","how can i access my class schedule online","can i change my class schedule after the registration period","what is a course catalog, and how can it help me during registration","how can i find out if a course has prerequisites","what is the difference between full-time and part-time enrollment","can i register for courses outside my major","how do i declare a major or minor","what is a waitlist, and how does it work","can i register for independent study or research projects"]
answers = ["Payment methods vary, but universities often provide online portals for fee payment. Check with the bursar's office for details on payment options.","Log in to the university's student portal or registration system to access and view your class schedule.","Yes, you can usually make changes during the add/drop period. Check the academic calendar for specific deadlines","The course catalog is a comprehensive list of available courses. Use it to explore course descriptions, prerequisites, and plan your schedule.","Check the course catalog or university website for prerequisites information. It's important to meet these requirements before registering.","Full-time enrollment usually requires taking a certain number of credits per semester, while part-time enrollment is a lower credit load. Check your university's definition for full-time status.","Yes, many programs allow you to take elective courses outside your major. Consult with your advisor to ensure they align with your academic goals.","To declare a major or minor, schedule a meeting with your academic advisor. They will guide you through the process.","A waitlist is a list of students waiting for an open spot in a full class. If a spot opens, the student at the top of the list is usually notified.","Yes, if your program allows it. Coordinate with a faculty advisor to plan and register for independent study or research courses." ]
question=str(input("do you have a question to ask me?"))
question=question.lower()
question=question.strip()
question=question.strip("?")
if (question in questions):
    question_no=questions.index(question)
    print(answers[question_no]) 
elif(question=="bye"):
    print("nice to meet you ,have a nice day")
else:
    try:
        answer = ask_chatgpt(question)
        print(answer)  # Or send the answer to the user
    except Exception as e:
            print("Sorry, there was an issue. Please try again later.")
            print(f"Error details: {str(e)}")
# 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
    
#import pyautogui
    #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