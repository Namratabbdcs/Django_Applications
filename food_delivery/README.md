# FoodApp

#### Virtual Environment

##### Install virtualenv
    sudo apt-get install python3-pip
    pip3 install virtualenv

##### Basic Usage
    virtualenv -p python3 vir

##### To begin using the virtual environment, it needs to be activated:
    source vir/bin/activate

##### Installation requires
    pip3 install kwikapi[django]
    pip3 install mysqlclient

##### Install MySQL database if it is not available
    sudo apt-get update
    sudo apt-get install mysql-server

##### Create mysql database if not exists:

    sudo mysqladmin -u <DB-USER> -p create <ARBITRARY-DB-NAME>

##### Clone the repository
    git clone "https://github.com/Namratabbdcs/Django_Applications.git"


##### Update Django settings
###### Goto the database directory by running following command:
    cd namrata/food_delivery/food_delivery

###### Update settings.py with database details: Following lines need to be updated
    DATABASES['default']['NAME']
    DATABASES['default']['USER']
    DATABASES['default']['PASSWORD']

###### We need to create log file and add the logfile path in the settings:
    LOG_FILE_PATH = <LOG-FILE-PATH>

#### Apply migrations
    cd ..
    python3 manage.py makemigrations
    python3 manage.py migrate

#### Run the server:
    python3 manage.py runserver 0:8000
#### Open in browser:
    "http://127.0.0.1:8000/api/v1/<fn_name>"

# Panel - Login through website

    - If we want to login through django panel, we need to create a superuser first.
        - python manage.py createsuperuser

#### 1.Admin(admin will be the superuser)

- Request: http://127.0.0.1:8000/admin/
    - Username: admin
    - password: password

    - Note: After login using the superuser we can create other users also and give them the permissions based on the needs.

#### 2. Delivery boy

- Request: http://127.0.0.1:8000/login
    - Username: delivery_boy
    - password: password

# API Functions - We can use the below API's to perform the task

#### 1. add_order

- Request: We can add the order in database using this API.
    -Ref:
        
        - http://127.0.0.1:8000/api/v1/add_order?order_no=1a&title=noodles&status=free&priority=medium&task=declined

#### 1. get_details

- Request:
    - Ref:
        - http://127.0.0.1:8000/api/v1/get_details
        - http://127.0.0.1:8000/api/v1/get_details?task=declined

#### 2. delete_order

- Request: We can delete the order based on the order no.
    - Ref:
        - http://127.0.0.1:8000/api/v1/get_details?order_no=1

#### 3. update_order

- Request:We can update any record based on the orer_no.
    - Ref:
        - http://127.0.0.1:8000/api/v1/get_details?order_no=1&task=new
        - http://127.0.0.1:8000/api/v1/update_order?order_no=2&task=declined&status=free
