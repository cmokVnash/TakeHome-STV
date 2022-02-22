# TakeHome-STV


The Project uses default Django admin as admin portal with Basic and Session auths implemented

#Project Setup:
  python manage.py makemigrations
  python manage.py migrate
  
#Create super user
  python manage.py createsuperuser
 
#Run server:
  python manage.py runserver
  
###legend: postman fields are denoted using '{}' symbols

## api/login: (POST)
  <name> 
  <password>
## api/logout : (POST)
    
## api/signup : (POST)
  <name>
  <password> 
  <email> optional

### api/survey/create (POST)
    <name> (This is the title field that will showup)
      
### api/survey-list (GET)
    fetches all the surveys
      
### api/survey/{pk} (GET)
    fetches particular survey
    

### api/survey/{survey_id}/questions/{question_id} (GET)
### pi/survey/{pk}/questions
      retrieves question with pk
### api/survey/{survey pk}/question-create (POST)
      creates question of the survey pk
      
### api/survey/questions-create/{pk}/answer  (POST)
      creates answer for the question with pk
      
      


      
     
