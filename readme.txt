Execution Flow:

Install python.
Run the below commands in command prompt under the project directory.

1. py -m venv env 
This comamnd creates an environment, which should be specific to the project.
"env" folder is created after running the above command in the project directory. 
Different projects are expected to have separate environments.

2. env\Scripts\Activate
This command should be used to activate the environment that we created for this project. 
After this command we see (env) variable being prefixed in the command prompt.

*Installing the dependencies
3. pip isntall flask
4. pip install nltk
5. pip install pyspark
etc..

*Create the required files & import the libraries in the project directory.

*Create an app.py file, this is the main file which will contain all the requests.
*Setting app.py as the main file using the below command.
6. set FLASK_APP=app.py
Can configure the port for running the app on browser in app.py.

*Running the flask app. It results in some details with an "url", run this url in the browser to play with the requests. 
7. flask run

8. After every modification use [(env) cmd> Ctl+c] and run [(env) cmd>flask run] again. 
