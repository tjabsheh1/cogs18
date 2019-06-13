from functions import disease_from_counts, probability_of_diagnosis

def test_disease_from_counts():
    counts = [(27, 'Bipolar_Disorder'), (12, "Depression"), (5, "GAD")]
    symptom_count, disease = disease_from_counts(counts)
    assert(symptom_count == 27)
    assert(disease == 'Bipolar_Disorder')
    
def test_probability_diagnosis():
    probability=probability_of_diagnosis(30,60)
    assert(probability==50.0)
    
    
