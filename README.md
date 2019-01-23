# big_query_configure
## 1. python setting on local
```
pyenv install 2.7.13
pyenv local 2.7.13
python --version
> 2.7.13

pip install virtualenv
virtualenv env
. env/bin/activate
pip install -r requirements.txt
```

## 2. copy bigquery setting file
> cp gbq_setting.py.sample gbq_setting.py

## 3. create service key for GCP project
https://cloud.google.com/bigquery/docs/reference/libraries?hl=en

## 4. global variable setting command insert shell
```
export GOOGLE_APPLICATION_CREDENTIALS="/Users/your_host/.../your_google_credential.json"
```

## 5. fix gbq_setting.py
### fix point
1. your_gcp_project_name
2. your_project_dataset_id

## 6. test
run this command at project directory.
> python get_select.py

## 7. main bigquery jobs
1. create table
    > python create_table.py
    
2. get table column and row
    > python get_table.py
    
3. example data insert to table
    > python insert_data.py
    
