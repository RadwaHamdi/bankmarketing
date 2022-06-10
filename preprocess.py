def getJob(job):
    job_list=['job_admin.', 'job_blue-collar',
       'job_entrepreneur', 'job_housemaid', 'job_management', 'job_retired',
       'job_self-employed', 'job_services', 'job_student', 'job_technician',
       'job_unemployed', 'job_unknown']
    l=[1 if job==l  else 0  for l in job_list]
    return l

def getMarital(marital):
    marital_list=['marital_divorced', 'marital_married','marital_single', 'marital_unknown']
    l=[1 if marital==l  else 0  for l in marital_list]
    return l

def getEducation(education):
    education_list=[ 'education_basic.4y','education_basic.6y', 'education_basic.9y', 'education_high.school',
       'education_illiterate', 'education_professional.course','education_university.degree', 'education_unknown']
    l=[1 if education==l  else 0  for l in education_list]
    return l

def getcredit(credit):
    credit_list=['default_no','default_unknown', 'default_yes']
    l=[1 if credit==l  else 0  for l in credit_list]
    return l

def getHousing(housing):
    housing_list=['housing_no', 'housing_unknown','housing_yes']
    l=[1 if housing==l  else 0  for l in housing_list]
    return l

def getLoan(loan):
    loan_list=['loan_no', 'loan_unknown', 'loan_yes']
    l=[1 if loan==l  else 0  for l in loan_list]
    return l

def getContact(contact):
    contact_list=['contact_cellular', 'contact_telephone']
    l=[1 if contact==l  else 0  for l in contact_list]
    return l

def getSeason(season):
    season_list=['season_Autumn','season_Spring', 'season_Summer', 'season_Winter']
    l=[1 if season==l  else 0  for l in season_list]
    return l

def getPoutcome(outcome):
    outcome_list=['poutcome_failure','poutcome_nonexistent', 'poutcome_success']
    l=[1 if outcome==l  else 0  for l in outcome_list]
    return l

def preprocess_data(data) :
    
    return [data.get('age'),data.get('campaign'),data.get('pdays'),data.get('previous'),data.get('cons_price_idx'),
     data.get('cons_conf_idx'),data.get('euribor3m')]+ getJob(data.get('job'))+getMarital(data.get('marital'))+getEducation(data.get('education'))+getcredit(data.get('credit'))+getHousing(data.get('housing'))+getLoan(data.get('loan'))+getContact(data.get('contact'))+getSeason(data.get('season'))+getPoutcome(data.get('outcome'))
 