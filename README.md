<h3> Live Demo:</h3>http://rupnarayan163.pythonanywhere.com

Admin login:</br>
username: root </br>
password: root </br>

# Jobportal using Django
<h3>Some of the functionality of this project are as follows:</h3>
    1. User management ( Register, SignIN, SignOut, Update) and Login with Google account</br>
    2. View Job according to category, type, company, location, etc</br>
    3. CV upload</br>
    3. Apply for Job</br>
    4. Create Online Resume</br>
    5. View Applied Jobs</br>
    6. Admin Panel for Users under groups ( Company, Admin )</br>
    7. Job Creation</br>
    8. Group creation and User assignment</br>
    9. View Job Applicant</br>
    10. Select Applicant for Interview</br>
    11. Hire Applicant</br>
    12. Filter Applicant list according to Company, Name, Selected, etc</br>
    13. Download CSV file for Filtered Applicant List</br>
    14. RestAPI Build for users, jobs, job applications and so on.

# Database:
-Postgresql

# Procedure:
1. Clone the project with Http , or download the project.</br>
2. Open command promt and change the directory to jobportal.</br>
3. Create a virtual environment in the command promt using " mkvvirtualenv name " where name can be of your choice.</br>
4. Run Command " pip install -r requirements.txt " to install required packages.</br>
5. Go to Postgre Admin and create a database  "jobportal" and User login "job_portal" with password "root".</br>
6. Run "python manage.py runserver" in the command promt.</br>
7. Run "python manage.py creategroups" command to create default group</br>
8. To access Admin Panel login as Admin group or Company group.</br>
