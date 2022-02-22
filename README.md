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

## api/login: 
  <name> 
  <password>
## api/logout :
    
## api/signup : 
  <name>
  <password> 
  <email> optional

### api/survey/create
    <name> (This is the title field that will showup)
      
### api/survey-list
    fetches all the surveys
### api/survey/{pk}
    fetches particular survey
    
### api/survey/create (POST):
  <name> (this is the heading of the survey field that will show up)
  
### api/survey-list (GET)
    fetches all the surveys
    
### api/survey/{pk}
    fetches a particular survey
### api/survey/{pk}/
    fetches a particular question
### api/survey/<pk>/question-create
    <question>
    <default_answer>
### api/survey/questions-create/{pk}/answer
    <answer>
    

      
     
