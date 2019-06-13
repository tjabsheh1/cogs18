
# coding: utf-8

# #         Cogs 18 Final Project Description
# 
# For this project I created a chatbot where a user answers questions based on symptoms and the chatbot will take the inputs and diagnose the user with the specific condition based on mental health disorders. This chatbot will also give treatments, and explainations of the disease as well as connecting with a live video chat doctor. This chatbot will also connect the user with another user on the app to that has the same condition and also can play games with each other. 

# In[1]:


from my_module.functions import disease_from_counts, probability_of_diagnosis, diagnose_condition


# In[2]:


"""functions from Assignment 3"""


import string
import random
import nltk
        
def is_question(input_string):
    
    """check if the user input is a string"""
    
    if '?' in input_string:
        output = True
        
    else:
        output = False
        
    return output 


def remove_punctuation(input_string):
    
    """remove any punctuation in the user input"""
    
    out_string = ""
    
    for item in input_string:
        
        if item not in string.punctuation: 
            out_string = out_string + item
            
    return out_string


def prepare_text(input_string):
    
    """makes input lower case, remove any puncuation, and then splits into word"""
    
    temp_string = input_string.lower()
    temp_string = remove_punctuation(temp_string) 
    out_list = temp_string.split()
    
    return out_list


def respond_echo(input_string,number_of_echoes,spacer):
    
    """ function that will return a string that has been repeated a specified number of times, with a given separator. """
    
    if input_string is not None:
        echo_output = (input_string + spacer)*number_of_echoes
        
    else:
        echo_output = None
        
    return echo_output  


def selector(input_list,check_list,return_list):
    
    """This function that will select an output for the chatbot, based on the input it got. """
    
    output = None
    
    for element in input_list:
        
        if element in check_list:
            output = random.choice(return_list)
            break
            
    return output


def string_concatenator(string1,string2,separator):
    
    """concatenates two strings, combining them with a specified separator. """
    
    output = string1 + separator + string2
    
    return output


def list_to_string(input_list,separator):
    
    """turns a list of strings back into one single concatenated string."""
    
    output = input_list[0]
    
    for item in input_list[1:]:
        output = string_concatenator(output,item,separator)  
        
    return output 


def end_chat(input_list):
    
    """ends the chat with our chatbot."""
    
    if 'quit' in input_list:
        return True
    
    else:
        return False



def is_in_list(list_one, list_two):
    """Check if any element of list_one is in list_two."""
    
    for element in list_one:
        if element in list_two:
            return True
    return False

def find_in_list(list_one, list_two):
    """Find and return an element from list_one that is in list_two, or None otherwise."""
    
    for element in list_one:
        if element in list_two:
            return element
    return None


# This cell defines a collection of input and output things our chatbot can say and respond to

GREETINGS_IN = ['hello', 'hi', 'hey', 'hola', 'welcome', 'bonjour', 'greetings']
GREETINGS_OUT = ["Hello, it's nice to talk to you!", 'Nice to meet you!',  "Hey - Let's chat!"]

COMP_IN = ['python', 'code', 'computer', 'algorithm', ]
COMP_OUT = ["Python is what I'm made of.",             "Did you know I'm made of code!?",             "Computers are so magical",             "Do you think I'll pass the Turing test?"]

PEOPLE_IN = ['turing', 'hopper', 'neumann', 'lovelace']
PEOPLE_OUT = ['was awesome!', 'did so many important things!', 'is someone you should look up :).']
PEOPLE_NAMES = {'turing': 'Alan', 'hopper': 'Grace', 'neumann': 'John von', 'lovelace': 'Ada'}

JOKES_IN = ['funny', 'hilarious', 'ha', 'haha', 'hahaha', 'lol']
JOKES_OUT = ['ha', 'haha', 'lol'] 

NONO_IN = ['matlab', 'java', 'C++']
NONO_OUT = ["I'm sorry, I don't want to talk about"]

UNKNOWN = ['Good.', 'Okay', 'Huh?', 'Yeah!', 'Thanks!']

QUESTION = "I'm too shy to answer questions. What do you want to talk about?"




def have_a_chat():
    """Main function to run our chatbot."""
    
    chat = True
    while chat:

        # Get a message from the user
        msg = input('INPUT :\t')
        out_msg = None

        # Check if the input is a question
        question = is_question(msg)

        # Prepare the input message
        msg = prepare_text(msg)

        # Check for an end msg 
        if end_chat(msg):
            out_msg = 'Bye!'
            chat = False

        # Check for a selection of topics that we have defined to respond to
        #   Here, we will check for a series of topics that we have designed to answer to
        if not out_msg:

            # Initialize to collect a list of possible outputs
            outs = []

            # Check if the input looks like a greeting, add a greeting output if so
            outs.append(selector(msg, GREETINGS_IN, GREETINGS_OUT))

            # Check if the input looks like a computer thing, add a computer output if so
            outs.append(selector(msg, COMP_IN, COMP_OUT))

            # Check if the input mentions a person that is specified, add a person output if so
            if is_in_list(msg, PEOPLE_IN):
                name = find_in_list(msg, PEOPLE_IN)
                outs.append(list_to_string([PEOPLE_NAMES[name], name.capitalize(),
                                            selector(msg, PEOPLE_IN, PEOPLE_OUT)], ' '))

            # Check if the input looks like a joke, add a repeat joke output if so
            outs.append(respond_echo(selector(msg, JOKES_IN, JOKES_OUT), 3, ''))

            # Check if the input has some words we don't want to talk about, say that, if so
            if is_in_list(msg, NONO_IN):
                outs.append(list_to_string([selector(msg, NONO_IN, NONO_OUT), find_in_list(msg, NONO_IN)], ' '))

            # IF YOU WANTED TO ADD MORE TOPICS TO RESPOND TO, YOU COULD ADD THEM IN HERE

            # We could have selected multiple outputs from the topic search above (if multiple return possible outputs)
            #   We also might have appended None in some cases, meaning we don't have a reply
            #   To deal with this, we are going to randomly select an output from the set of outputs that are not None
            options = list(filter(None, outs))
            if options:
                out_msg = random.choice(options)

        # If we don't have an output yet, but the input was a question, return msg related to it being a question
        if not out_msg and question:
            out_msg = QUESTION

        # Catch-all to say something if msg not caught & processed so far
        if not out_msg:
            out_msg = random.choice(UNKNOWN)

        print('OUTPUT:', out_msg)
        
        


#User selects symptoms from checklist



GAD_symptoms=["Persistent worrying or anxiety about a number of areas that are out of proportion to the impact of the events",
"Overthinking plans and solutions to all possible worst-case outcomes",
"Perceiving situations and events as threatening, even when they aren't",
"Difficulty handling uncertainty",
"Indecisiveness and fear of making the wrong decision",
"Inability to set aside or let go of a worry",
"Inability to relax, feeling restless, and feeling keyed up or on edge", 
"Difficulty concentrating, or the feeling that your mind goes blank"]



Depression_symptoms=["Feelings of sadness, tearfulness, emptiness or hopelessness",
"Angry outbursts, irritability or frustration, even over small matters",
"Loss of interest or pleasure in most or all normal activities, such as sex, hobbies or sports",
"Sleep disturbances, including insomnia or sleeping too much",
"Tiredness and lack of energy, so even small tasks take extra effort",
"Reduced appetite and weight loss or increased cravings for food and weight gain",
"Anxiety, agitation or restlessness",
"Slowed thinking, speaking or body movements",
"Feelings of worthlessness or guilt, fixating on past failures or self-blame",
"Trouble thinking, concentrating, making decisions and remembering things",
"Frequent or recurrent thoughts of death, suicidal thoughts, suicide attempts or suicide",
"Unexplained physical problems, such as back pain or headaches"]


Bipolar_Disorder_symptoms=["increased talkativeness",
"increased self-esteem or grandiosity",
"decreased need for sleep",
"increase in goal-direct activity, energy level, or irritability",
"racing thoughts",
"poor attention",
"increased risk-taking (spending money, risky sexual behaviors, etc.)"]

#Based on number symptoms user picks we will diagnose them with a Condition with percentage/likelihood

sypmtoms_by_disease = {'GAD':GAD_symptoms, 'Despression':Depression_symptoms, 'Bipolar_Disorder':Bipolar_Disorder_symptoms}
all_symptoms_count = len(GAD_symptoms) + len(Depression_symptoms) + len(Bipolar_Disorder_symptoms)



""""
a function that takes counts of symptoms inputed from user based on a yes or no question.
Parameters
----------
for loop : looks for symptoms in list and adds a count and uses tuple to sort

Returns
-------
found : Highest count of symptoms will display disease


"""



#Based on yes no question per symptom  and adds counter to get percentage of disease

def Diagnose_Condition():
    Counter_GAD=0
    Counter_Depression=0
    Counter_Bipolar_Disorder=0
    for symptom in GAD_symptoms:
        print(symptom)
        reply=input("Do you have this Symptom? Y/N ").strip()
        if reply.lower()=="y":
            Counter_GAD+=1
    
    for symptom in Depression_symptoms:
        print(symptom)
        reply=input("Do you have this Symptom? Y/N ").strip()
        if reply.lower()=="y":
            Counter_Depression+=1
            
            
    for symptom in Bipolar_Disorder_symptoms:
        print(symptom)
        reply=input("Do you have this Symptom? Y/N ").strip()
        if reply.lower()=="y":
            Counter_Bipolar_Disorder+=1
                             
    
    #Counts and sorts using tuple
    counts = [(Counter_Bipolar_Disorder, 'Bipolar_Disorder'), (Counter_Depression, "Depression"), (Counter_GAD, "GAD")]
    counts.sort()
    symptom_count, disease = disease_from_counts(counts)
    print()
    print('--- Diagnosis ---')
    print('The most likely disease given your symptoms is', disease)
    
    # probability of disease
    
    probability = probability_of_diagnosis(symptom_count, all_symptoms_count)
    
  
    print(f'The probability of you having {disease} is: {probability:.2f}%')
    
    return disease





                      

#Create a class of atributes for the 3 Mental Condiitions to display information about condition



"""a class used to get specific information from each condition

Attributes
----------
Condition name : string
the name of the condition.
explaination : string
explaination of the disorder.
treatment : string
Medications and treatment to cure the disease

        """





class Mental_Condition():
    def __init__(self, Condition_name, Explaination, treatment):
        self.Condition_name = Condition_name
        self.Explaination = Explaination
        self.treatment = treatment



Depression=Mental_Condition("Depression", 
                            """Depression is a mood disorder that causes a persistent feeling of sadness and loss of interest. 
                            Also called major depressive disorder or clinical depression, it affects how you feel, 
                            think and behave and can lead to a variety of emotional and physical problems. 
                            You may have trouble doing normal day-to-day activities, and sometimes you may feel as 
                            if life isn't worth living.""", 
                            """Medications and psychotherapy are effective for most people with depression. 
                            Your primary care doctor or psychiatrist can prescribe medications to relieve symptoms. 
                            However, many people with depression also benefit from seeing a psychiatrist, psychologist 
                            or other mental health professional.""")

GAD=Mental_Condition("GAD", "characterized by persistent and excessive worry about a number of different things. People with GAD may anticipate disaster and may be overly concerned about money, health, family, work, or other issues. Individuals with GAD find it difficult to control their worry. They may worry more than seems warranted about actual events or may expect the worst even when there is no apparent reason for concern.", "A number of types of treatment can help with GAD. Supportive and interpersonal therapy can help. Cognitive behavioral treatment (CBT) has been more researched and specifically targets thoughts, physical symptoms and behaviors including the over-preparation, planning and avoidance that characterizes GAD. Mindfulness based approaches and Acceptance Commitment Therapy have also been investigated with positive outcome. All therapies (sometimes in different ways) help people change their relationship to their symptoms. They help people to understand the nature of anxiety itself, to be less afraid of the presence of anxiety, and to help people make choices independent of the presence of anxiety. The adult CBT treatments for GAD have been modified for children and teens and show positive outcomes.")

Bipolar_Disorder=Mental_Condition("Bipolar Disorder", "is a complex disorder that likely stems from a combination of genetic and non-genetic factors. The mood episodes associated with it involve clinical depression or mania (extreme elation and high energy) with periods of normal mood and energy in between episodes. The severity of mood episodes can range from very mild to extreme, and they can happen gradually or suddenly within a timeframe of days to weeks. When discrete mood episodes happen four or more times per year, the process is called rapid cycling. Rapid cycling should not be confused with very frequent moment-to-moment changes in mood, which can sometimes occur in people with bipolar disorder or other conditions such as borderline personality disorder. Along with manic or depressive episodes, patients with bipolar disorder may have disturbances in thinking. They may also have distortions of perception and impairment in social functioning.", "Treatment for bipolar disorder may include the use of mood stabilizers such as lithium. Certain anticonvulsants, antipsychotics, and benzodiazepines may also be used to stabilize mood. Sometimes antidepressants are given in combination with mood stabilizers to boost the depressed mood, although antidepressants are often not as effective as some mood stabilizers or certain atypical antipsychotics for treating depression in bipolar disorder.")


Conditions=["GAD", "Depression", "Bipolar Disorder"]
Criteria= ["Condition", "Explaination", "Treatment",]

# store the mental condition classes
mental_condtions = {}
mental_condtions['Depression'] = Depression
mental_condtions['GAD']=GAD
mental_condtions['Bipolar_Disorder']=Bipolar_Disorder

disease = Diagnose_Condition()

# get mental condition class for given disease
mental_condition = mental_condtions[disease]

treatment = mental_condition.treatment
print('Thank you')
print()
reply=input("Would you like to see the treatment for this disease?Y/N")
if reply.lower()=="y":
    print(treatment)
    print()
    

explaination=mental_condition.Explaination
reply=input("Would you like to see the explaination for this disease?Y/N")
if reply.lower()=="y":
    print(explaination)









#Give options on what to do once you know all the information about condition


#1. Video Chat with live psychiatrist

"""
a function that connects with doctor
Parameters
----------
while: connection

Returns
-------
found : connected

"""



def connect_dr():
    connected=False
    while not connected:
        print("One moment, we are connecting you with a pyschiatrist")
        break
    connected=False
    while connected:
            print("Connected")
        




#2. Connect with someone who has same condition


"""
 a function that matches user with similiar user based on condition
Parameters
----------
loop : looks for matches in dictionary

Returns
-------
found : Match


"""




def connect_match(user_disease):
    user_keys={ "GAD": ["Kyle", "Roger", "Jessica"]}
    if user_disease in user_keys:
        print("You have MATCHES!")
        reply=input("Do you want to connect with MATCHES? Y/N")
        if reply.lower()=="y":
            print("Message Match")
            print()    
    
        connected=False
        while not connected:
            print("One moment, we are connected you with a match")
            break
            
        connected=False
        while connected:
            print("Start Chatting")
    else:
        print("Sorry you do not have any matches")
    
 #play game with Match   

"""
a function that plays game with match
Parameters
----------
while: challenges match

Returns
-------
found : challenge accepted

"""




def play_game():
    reply=input("Do you want to play a game with your new friend? Y/N")
    if reply.lower()=="y":
        print("Cool!!")
        print()  
        
        reply=input("Send challenge? Y/N")
        if reply.lower()=="y":
            print("Challenge sent!")
            print()   
            
            connected=False
            while not connected:
                print("Challenge Pending")
                break
        
        connected=True
        while connected:
            print("Challenge Accepted")
            


# In[ ]:




