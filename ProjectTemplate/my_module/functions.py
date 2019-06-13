 """
   a function that takes the count of yes or no from symptoms and gives the probability of the disease
    Parameters
    ----------
    sort : counts and sorts
    
    Returns
    -------
    found : probability
       The conditon that the probability is likely. 
       
    """


#disease get sorted and gets probability
    
def disease_from_counts(counts):
    counts.sort()
    symptom_count, disease = counts[-1]
    return symptom_count, disease

def probability_of_diagnosis(symptom_count, all_symptoms_count):
    probability = (symptom_count / all_symptoms_count) * 100
    return probability



     """
    a function that takes counts of symptoms inputed from user based on a yes or no question.
    Parameters
    ----------
    for loop : looks for symptoms in list and adds a count and uses tuple to sort
    
    Returns
    -------
    found : Highest count of symptoms will display disease
      
       
    """
    
#Based on yes no question per symptom  and adds counter to get percentage of disease

    
def diagnose_condition(GAD_symptoms,Depression_symptoms, Bipolar_Disorder_symptoms):
    counter_GAD=0
    Counter_Depression=0
    Counter_Bipolar_Disorder=0
    for symptom in GAD_symptoms:
        print(symptom)
        reply=input("Do you have this Symptom? Y/N ").strip()
        if reply.lower()=="y":
            counter_GAD+=1
    
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
                     
    counts = [(Counter_Bipolar_Disorder, 'Bipolar_Disorder'), (Counter_Depression, "Depression"), (counter_GAD, "GAD")]
    counts.sort()
    symptom_count, disease = disease_from_counts(counts)
    print()
    print('--- Diagnosis ---')
    print('The most likely disease given your symptoms is', disease)
    
    # probability of disease
    
    probability = probability_of_diagnosis(symptom_count, all_symptoms_count)
    
  
    print(f'The probability of you having {disease} is: {probability:.2f}%')
    
    return disease



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



#send game challenge to match
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

