# equipment_apirestreport

API service with database of network equipment 


#### Stack: 
Python 3, Django, MySQL, -VueJS

## How start project:

Clone a repository and go to command line:

```sh
git clone https://github.com/menyanet73/equipment_api.git
```

```sh
cd equipment_api
```

```sh
python -m venv env
```

```sh
. /env/bin/activate
```

```sh
cd backend/equipment
```

Install MySQL, create user and database with conf.settings options (user, password and database = equipment)

```sh
pip install -r requirements.txt
```

```sh
python manage.py migrate
```

```sh
python manage.py runserver
```
#ENDPOINTS:
GET:/api/equipment - get equipment list
GET:/api/equipment/{id} - get equipment item
POST:/api/equipment - create equipment item, request fields: {"equipment_type":int(id), "serial_number":string(serial_number validated for type mask)
PUT:/api/equipment/{id} - update equipment item fields
DELETE:/api/equipment/{id} - soft delete equipment item
GET:/api/equipment-type - get equipment type list 
POST:/api/user/create - signup form, create user, request fields: {"username":string(username), "password":string(password)}
POST:/api/user/login - signin form, create bearer token, request fields: {"username":string(username), "password":string(password)}



Done!

### Author
##### https://github.com/menyanet73
