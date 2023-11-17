# Commands used
# Week 1:

## Connect Theia to your github account

git config --global user.email "<yourgithub@email.com>"

git config --global user.name "name"

git add .

git commit -m"Adding temporary changes to Github"

git push

## Clone repository

git clone <your_repo_name>

## Run the Django app on development server

cd ibm-CloudAppDevelopment_Capstone/server

python3 -m pip install -U -r requirements.txt

python3 manage.py makemigrations

python3 manage.py migrate

python3 manage.py runserver

# Week 2: 
## Environment setup

python3 -m pip install -U -r requirements.txt

## Create a supper user for your app
python3 manage.py createsuperuser

username: admin
email: admin@ibm.com'
password: password123!

python3 manage.py runserver

## Add user login/logout and signup menu items

# Week 3: Implement IBM Cloud Function Endpoints
## 1. Load data into the database

* Navigate to the resources page - <https://cloud.ibm.com/resources>.

* Click on the Cloudant service. If you don’t have one already, create one here - <https://cloud.ibm.com/catalog/services/cloudant>.

* To create an API Key, Manage -> Access IAM -> APIKeys -> Create+ -> Copy and Paste the API key somewhere safe.

* To create a database, in Cloudant service -> Create + -> navigation bar -> Resource List -> Databases -> Cloudant->view full detail -> Copy and paste the external endpoint preferred url

npm install -g couchimport

export IAM_API_KEY="I_AM_API_KEY"

export COUCH_URL="EXTERNAL ENDPOINT PREFERRED URL"

cd ibm-CloudAppDevelopment_Capstone/cloudant/data

cat ./dealerships.json | couchimport --type "json" --jsonpath "dealerships.*" --database dealerships

cat ./reviews.json | couchimport --type "json" --jsonpath "reviews.*" --database reviews

## 2. Create the action in IBM Cloud
1. Navigate to the resources page - <https://cloud.ibm.com/resources>.

2. Go to Functions -> Actions

3. Create an Action named get-dealership by choosing language as node.js

4. Select the package as dealership-package

5. Method used will be GET METHOD

6. Parameters for this action will be None since this will retrieve all the dealership details from the DB

* Update the code for the action

* Get the endpoint URL's

* Get specific state Endpoint: /api/dealership?state=""
 In browser, copy and paste getAllDealership url link, ?st=State

 Get all dealership endpoint: <https://us-south.functions.appdomain.cloud/api/v1/web/cebe1001-00af-4035-b9fc-dce1468a7b18/dealership-package/get-State>

 Get specific state dealership endpoint: <https://us-south.functions.appdomain.cloud/api/v1/web/cebe1001-00af-4035-b9fc-dce1468a7b18/dealership-package/get-State?st=CA>


