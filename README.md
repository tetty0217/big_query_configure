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

## 2. create service key for GCP project
https://cloud.google.com/bigquery/docs/reference/libraries?hl=ja

## 3. global variable setting command insert shell
```
export GOOGLE_APPLICATION_CREDENTIALS="/Users/your_host/.../your_google_credential.json"
```

## 4. 