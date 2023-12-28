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
    red = '\033[91m'
    green = '\033[92m'
    yellow = '\033[93m'
    blue = '\033[94m'
    end = '\033[0m'
if colour=="green":
    print(TextColors.green + "amazing! we have the same colour choice" + TextColors.END)
else:    
    print(TextColors.blue + "i like",colour,"but my favourite coulor is blue, like the sky." + TextColors.END)