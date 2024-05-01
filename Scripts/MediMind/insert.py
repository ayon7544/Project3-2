import os
import django

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MediMind.settings')
django.setup()

# Import the Disease model
from application.models import Disease

# Define the data for diseases
diseases_data = [
    {
        'name': 'Fungal infection',
        'description': 'Fungal infection is a common condition caused by various types of fungi.',
        'avoid_foods_and_drinks': 'Avoid sugary foods and drinks as they can promote fungal growth.',
        'examination_preparation': 'No specific preparation is required for diagnosis. A sample may be taken for examination.'
    },
    {
        'name': 'Allergy',
        'description': 'Allergy is an overreaction of the immune system to substances that are usually harmless.',
        'avoid_foods_and_drinks': 'Avoid foods that trigger allergic reactions. Consult with a healthcare provider for specific advice.',
        'examination_preparation': 'No specific preparation is required for diagnosis. Allergy tests may be performed as advised by a doctor.'
    },
    {
        'name': 'GERD (Gastroesophageal Reflux Disease)',
        'description': 'GERD is a digestive disorder that affects the lower esophageal sphincter (LES), the ring of muscle between the esophagus and stomach.',
        'avoid_foods_and_drinks': 'Avoid acidic, spicy, and fatty foods. Limit caffeine and alcohol intake.',
        'examination_preparation': 'No specific preparation is required for diagnosis. Endoscopy or other tests may be performed as advised by a doctor.'
    },
    {
        'name': 'Chronic cholestasis',
        'description': 'Chronic cholestasis is a condition where bile flow from the liver slows or stops, causing a buildup of bile in the liver.',
        'avoid_foods_and_drinks': 'Avoid fatty and fried foods. Limit alcohol intake.',
        'examination_preparation': 'No specific preparation is required for diagnosis. Liver function tests or imaging studies may be performed.'
    },
    {
        'name': 'Drug Reaction',
        'description': 'Drug reaction, also known as adverse drug reaction (ADR), is an unintended harmful reaction to a medication.',
        'avoid_foods_and_drinks': 'There are no specific foods or drinks to avoid, but it is important to avoid the triggering medication.',
        'examination_preparation': 'No specific preparation is required for diagnosis. Medical history and symptoms are evaluated.'
    },
    {
        'name': 'Peptic ulcer disease',
        'description': 'Peptic ulcer disease is a condition where painful sores or ulcers develop on the inner lining of the stomach or the upper part of the small intestine.',
        'avoid_foods_and_drinks': 'Avoid spicy foods, alcohol, and caffeine. Limit intake of acidic foods.',
        'examination_preparation': 'No specific preparation is required for diagnosis. Endoscopy or other tests may be performed.'
    },
    {
        'name': 'AIDS',
        'description': 'AIDS (Acquired Immunodeficiency Syndrome) is a chronic, potentially life-threatening condition caused by the human immunodeficiency virus (HIV).',
        'avoid_foods_and_drinks': 'There are no specific foods or drinks to avoid, but a balanced diet is important for overall health.',
        'examination_preparation': 'No specific preparation is required for diagnosis. HIV tests may be performed.'
    },
    {
        'name': 'Diabetes',
        'description': 'Diabetes is a chronic condition characterized by high levels of sugar (glucose) in the blood.',
        'avoid_foods_and_drinks': 'Avoid sugary foods and drinks. Limit carbohydrate intake.',
        'examination_preparation': 'No specific preparation is required for diagnosis. Blood tests may be performed to measure glucose levels.'
    },
    {
        'name': 'Gastroenteritis',
        'description': 'Gastroenteritis is inflammation of the stomach and intestines, typically resulting from bacterial or viral infection.',
        'avoid_foods_and_drinks': 'Avoid dairy products, fatty foods, spicy foods, and caffeine. Drink plenty of fluids.',
        'examination_preparation': 'No specific preparation is required for diagnosis. Medical history and symptoms are evaluated.'
    },
    {
        'name': 'Bronchial Asthma',
        'description': 'Bronchial asthma is a chronic condition characterized by inflammation and narrowing of the airways, causing difficulty breathing.',
        'avoid_foods_and_drinks': 'Avoid foods that trigger asthma symptoms, such as sulfites, preservatives, and certain food additives.',
        'examination_preparation': 'No specific preparation is required for diagnosis. Lung function tests may be performed.'
    },
    {
        'name': 'Hypertension',
        'description': 'Hypertension, or high blood pressure, is a common condition where the force of blood against the artery walls is consistently too high.',
        'avoid_foods_and_drinks': 'Limit salt intake. Avoid high-sodium foods, processed foods, and alcohol.',
        'examination_preparation': 'No specific preparation is required for diagnosis. Blood pressure measurements are taken.'
    },
    {
        'name': 'Migraine',
        'description': 'Migraine is a neurological condition characterized by recurrent, severe headaches often accompanied by other symptoms such as nausea, vomiting, and sensitivity to light and sound.',
        'avoid_foods_and_drinks': 'Avoid trigger foods such as aged cheese, chocolate, and caffeine. Stay hydrated.',
        'examination_preparation': 'No specific preparation is required for diagnosis. Medical history and symptoms are evaluated.'
    },
    {
        'name': 'Cervical spondylosis',
        'description': 'Cervical spondylosis is a common age-related condition that affects the joints and discs in the cervical spine (neck).',
        'avoid_foods_and_drinks': 'There are no specific foods or drinks to avoid, but maintaining a healthy weight can help reduce symptoms.',
        'examination_preparation': 'No specific preparation is required for diagnosis. Imaging tests such as X-rays or MRI may be performed.'
    },
    {
        'name': 'Paralysis (brain hemorrhage)',
        'description': 'Paralysis due to brain hemorrhage occurs when bleeding in the brain damages brain tissue and disrupts signals between the brain and muscles.',
        'avoid_foods_and_drinks': 'There are no specific foods or drinks to avoid, but a balanced diet is important for overall health.',
        'examination_preparation': 'No specific preparation is required for diagnosis. Medical history, imaging tests, and neurological examinations are performed.'
    },
    {
        'name': 'Jaundice',
        'description': 'Jaundice is a condition where the skin and whites of the eyes become yellow due to high levels of bilirubin in the blood.',
        'avoid_foods_and_drinks': 'Avoid fatty and fried foods. Drink plenty of fluids to stay hydrated.',
        'examination_preparation': 'No specific preparation is required for diagnosis. Blood tests and imaging studies may be performed.'
    },
    {
        'name': 'Malaria',
        'description': 'Malaria is a serious and sometimes fatal disease caused by Plasmodium parasites that are transmitted through the bite of infected female Anopheles mosquitoes.',
        'avoid_foods_and_drinks': 'There are no specific foods or drinks to avoid, but staying hydrated is important.',
        'examination_preparation': 'No specific preparation is required for diagnosis. Blood tests are performed to detect the presence of the malaria parasite.'
    },
    {
        'name': 'Chicken pox',
        'description': 'Chickenpox is a highly contagious viral infection characterized by an itchy rash and red spots or blisters all over the body.',
        'avoid_foods_and_drinks': 'There are no specific foods or drinks to avoid, but staying hydrated and eating nutritious foods can help support recovery.',
        'examination_preparation': 'No specific preparation is required for diagnosis. Chickenpox is typically diagnosed based on symptoms and clinical examination.'
    },
    {
        'name': 'Dengue',
        'description': 'Dengue fever is a mosquito-borne viral infection characterized by flu-like symptoms and, in severe cases, potentially life-threatening complications such as dengue hemorrhagic fever and dengue shock syndrome.',
        'avoid_foods_and_drinks': 'There are no specific foods or drinks to avoid, but staying hydrated is important.',
        'examination_preparation': 'No specific preparation is required for diagnosis. Blood tests are performed to detect the dengue virus.'
    },
    {
        'name': 'Typhoid',
        'description': 'Typhoid fever is a bacterial infection caused by Salmonella typhi bacteria, typically transmitted through contaminated food and water.',
        'avoid_foods_and_drinks': 'Avoid raw or undercooked foods, as well as foods and drinks from questionable sources. Drink only safe, bottled or boiled water.',
        'examination_preparation': 'No specific preparation is required for diagnosis. Blood, stool, or urine tests may be performed to detect the bacteria.'
    },
    {
        'name': 'Hepatitis A',
        'description': 'Hepatitis A is a highly contagious liver infection caused by the hepatitis A virus (HAV), typically transmitted through contaminated food or water or close contact with an infected person.',
        'avoid_foods_and_drinks': 'Avoid raw or undercooked shellfish, as well as foods and drinks from questionable sources. Drink only safe, bottled or boiled water.',
        'examination_preparation': 'No specific preparation is required for diagnosis. Blood tests are performed to detect antibodies to the hepatitis A virus.'
    },
    {
        'name': 'Hepatitis B',
        'description': 'Hepatitis B is a viral infection that attacks the liver and can cause both acute and chronic disease. It is transmitted through contact with the blood or other body fluids of an infected person.',
        'avoid_foods_and_drinks': 'There are no specific foods or drinks to avoid, but a balanced diet is important for overall health.',
        'examination_preparation': 'No specific preparation is required for diagnosis. Blood tests are performed to detect hepatitis B virus antigens and antibodies.'
    },
    {
        'name': 'Hepatitis C',
        'description': 'Hepatitis C is a viral infection that causes liver inflammation, sometimes leading to serious liver damage. The hepatitis C virus (HCV) is transmitted through contact with infected blood.',
        'avoid_foods_and_drinks': 'There are no specific foods or drinks to avoid, but a balanced diet is important for overall health.',
        'examination_preparation': 'No specific preparation is required for diagnosis. Blood tests are performed to detect hepatitis C virus antibodies.'
    },
    {
        'name': 'Hepatitis D',
        'description': 'Hepatitis D, also known as delta hepatitis, is a liver infection caused by the hepatitis D virus (HDV), which is transmitted through contact with infected blood.',
        'avoid_foods_and_drinks': 'There are no specific foods or drinks to avoid, but a balanced diet is important for overall health.',
        'examination_preparation': 'No specific preparation is required for diagnosis. Blood tests are performed to detect hepatitis D virus antibodies.'
    },
    {
        'name': 'Hepatitis E',
        'description': 'Hepatitis E is a liver disease caused by the hepatitis E virus (HEV), which is transmitted mainly through contaminated water.',
        'avoid_foods_and_drinks': 'Avoid raw or undercooked shellfish, as well as foods and drinks from questionable sources. Drink only safe, bottled or boiled water.',
        'examination_preparation': 'No specific preparation is required for diagnosis. Blood tests are performed to detect hepatitis E virus antibodies.'
    },
    {
        'name': 'Alcoholic hepatitis',
        'description': 'Alcoholic hepatitis is liver inflammation caused by drinking too much alcohol over time. It is a serious condition that can lead to liver damage and liver failure.',
        'avoid_foods_and_drinks': 'Avoid alcohol completely. Follow a healthy diet low in saturated fats and refined sugars.',
        'examination_preparation': 'No specific preparation is required for diagnosis. Blood tests, imaging studies, or liver biopsy may be performed.'
    },
    {
        'name': 'Tuberculosis',
        'description': 'Tuberculosis (TB) is a potentially serious infectious disease caused by the bacterium Mycobacterium tuberculosis. It primarily affects the lungs but can also affect other parts of the body.',
        'avoid_foods_and_drinks': 'Eat a healthy, balanced diet to support overall health and immunity.',
        'examination_preparation': 'No specific preparation is required for diagnosis. Tests such as a TB skin test, blood test, or imaging studies may be performed.'
    },
    {
        'name': 'Common Cold',
        'description': 'The common cold is a viral infection of the upper respiratory tract, causing symptoms such as coughing, sneezing, sore throat, and runny or stuffy nose.',
        'avoid_foods_and_drinks': 'Stay hydrated with water, herbal teas, and clear broths. Avoid alcohol and caffeinated drinks.',
        'examination_preparation': 'No specific preparation is required for diagnosis. Symptoms are evaluated clinically.'
    },
    {
        'name': 'Pneumonia',
        'description': 'Pneumonia is an infection that inflames the air sacs in one or both lungs, causing cough, fever, chills, and difficulty breathing.',
        'avoid_foods_and_drinks': 'Stay hydrated with water, herbal teas, and clear broths. Avoid alcohol and caffeinated drinks.',
        'examination_preparation': 'No specific preparation is required for diagnosis. Chest X-ray, blood tests, or sputum tests may be performed.'
    },
    {
        'name': 'Dimorphic hemorrhoids (piles)',
        'description': 'Hemorrhoids, also known as piles, are swollen veins in the lower rectum and anus. They can develop internally or externally and may cause discomfort, bleeding, or itching.',
        'avoid_foods_and_drinks': 'Eat a high-fiber diet to prevent constipation. Avoid straining during bowel movements.',
        'examination_preparation': 'No specific preparation is required for diagnosis. Physical examination or other tests may be performed.'
    },
    {
        'name': 'Heart attack',
        'description': 'A heart attack, also known as a myocardial infarction, occurs when blood flow to a part of the heart is blocked for a long enough time that part of the heart muscle is damaged or dies.',
        'avoid_foods_and_drinks': 'Eat a heart-healthy diet low in saturated fats, trans fats, cholesterol, and sodium. Avoid processed foods and excess salt.',
        'examination_preparation': 'No specific preparation is required for diagnosis. Blood tests, electrocardiogram (ECG), or imaging studies may be performed.'
    },
    {
        'name': 'Varicose veins',
        'description': 'Varicose veins are enlarged, swollen, and twisted veins, usually appearing blue or dark purple, that often occur on the legs and feet. They may cause aching pain and discomfort.',
        'avoid_foods_and_drinks': 'Eat a healthy, balanced diet to maintain a healthy weight. Avoid prolonged standing or sitting.',
        'examination_preparation': 'No specific preparation is required for diagnosis. Physical examination or imaging tests may be performed.'
    },
    {
        'name': 'Hypothyroidism',
        'description': 'Hypothyroidism is a condition in which the thyroid gland does not produce enough thyroid hormone, leading to symptoms such as fatigue, weight gain, and cold intolerance.',
        'avoid_foods_and_drinks': 'There are no specific foods or drinks to avoid, but a balanced diet is important for overall health.',
        'examination_preparation': 'No specific preparation is required for diagnosis. Blood tests to measure thyroid hormone levels may be performed.'
    },
    {
        'name': 'Hyperthyroidism',
        'description': 'Hyperthyroidism is a condition in which the thyroid gland produces too much thyroid hormone, leading to symptoms such as weight loss, rapid heartbeat, and heat intolerance.',
        'avoid_foods_and_drinks': 'Limit caffeine intake. Avoid stimulants such as energy drinks and certain medications.',
        'examination_preparation': 'No specific preparation is required for diagnosis. Blood tests to measure thyroid hormone levels may be performed.'
    },
    {
        'name': 'Hypoglycemia',
        'description': 'Hypoglycemia, also known as low blood sugar, occurs when blood sugar (glucose) levels fall below normal levels, leading to symptoms such as shakiness, sweating, and confusion.',
        'avoid_foods_and_drinks': 'Eat small, frequent meals containing complex carbohydrates and protein. Avoid sugary foods and drinks that can cause rapid blood sugar spikes.',
        'examination_preparation': 'No specific preparation is required for diagnosis. Blood tests to measure blood sugar levels may be performed.'
    },
    {
        'name': 'Osteoarthritis',
        'description': 'Osteoarthritis is a degenerative joint disease characterized by the breakdown of joint cartilage and underlying bone, leading to pain, stiffness, and decreased range of motion.',
        'avoid_foods_and_drinks': 'Maintain a healthy weight to reduce stress on the joints. Eat a balanced diet rich in fruits, vegetables, whole grains, and lean protein.',
        'examination_preparation': 'No specific preparation is required for diagnosis. Physical examination, imaging tests, or joint fluid analysis may be performed.'
    },
    {
        'name': 'Arthritis',
        'description': 'Arthritis is inflammation of one or more joints, causing pain, stiffness, and swelling. There are more than 100 different types of arthritis.',
        'avoid_foods_and_drinks': 'There are no specific foods or drinks to avoid, but maintaining a healthy weight and eating a balanced diet can help reduce symptoms.',
        'examination_preparation': 'No specific preparation is required for diagnosis. Physical examination, imaging tests, or blood tests may be performed.'
    },
    {
        'name': '(Vertigo) Paroxysmal Positional Vertigo',
        'description': 'Paroxysmal positional vertigo (BPPV) is a disorder of the inner ear characterized by brief episodes of dizziness and spinning sensations triggered by changes in head position.',
        'avoid_foods_and_drinks': 'There are no specific foods or drinks to avoid, but certain triggers such as caffeine or alcohol may exacerbate symptoms in some individuals.',
        'examination_preparation': 'No specific preparation is required for diagnosis. Physical examination or diagnostic maneuvers such as the Dix-Hallpike test may be performed.'
    },
    {
        'name': 'Acne',
        'description': 'Acne is a common skin condition that occurs when hair follicles become clogged with oil and dead skin cells, leading to pimples, blackheads, and whiteheads.',
        'avoid_foods_and_drinks': 'There is no strong evidence linking specific foods to acne, but some individuals may find that certain foods, such as dairy or high-glycemic index foods, exacerbate their acne.',
        'examination_preparation': 'No specific preparation is required for diagnosis. Acne is typically diagnosed based on physical examination and medical history.'
    },
    {
        'name': 'Urinary tract infection',
        'description': 'A urinary tract infection (UTI) is an infection involving the kidneys, ureters, bladder, or urethra. UTIs are usually caused by bacteria and may cause pain, burning with urination, and frequent urination.',
        'avoid_foods_and_drinks': 'Drink plenty of water to flush out bacteria. Avoid irritating foods and drinks such as caffeine, alcohol, and spicy foods.',
        'examination_preparation': 'No specific preparation is required for diagnosis. Urine tests are performed to detect the presence of bacteria or white blood cells.'
    },
    {
        'name': 'Psoriasis',
        'description': 'Psoriasis is a chronic autoimmune condition characterized by patches of thick, red skin covered with silvery scales. It is not contagious.',
        'avoid_foods_and_drinks': 'There are no specific foods or drinks to avoid, but some individuals may find that certain foods, such as alcohol or processed foods, trigger flare-ups.',
        'examination_preparation': 'No specific preparation is required for diagnosis. Psoriasis is typically diagnosed based on physical examination and medical history.'
    },
    {
        'name': 'Impetigo',
        'description': 'Impetigo is a highly contagious skin infection caused by bacteria.',
        'avoid_foods_and_drinks': 'There are no specific foods or drinks to avoid for impetigo treatment.',
        'examination_preparation': 'No specific preparation is required for diagnosis. A sample may be taken from the infected area for examination.'
    }
]


# Insert diseases into the database
for data in diseases_data:
    disease = Disease.objects.create(
        name=data['name'],
        description=data['description'],
        avoid_foods_and_drinks=data['avoid_foods_and_drinks'],
        examination_preparation=data['examination_preparation']
    )
    print(f"{disease.name} inserted into the database.") 