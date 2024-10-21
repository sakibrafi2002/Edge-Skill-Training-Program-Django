## Install SQLite in Linux

```
sudo apt install sqlitebrowser
```

## Open SQLite from Linux

```
sqlitebrowser
```
## activate django shell
```
python3 manage.py shell
```
<!-- class 7 -->

# Model
## After making any model or changes
```
python3 manage.py makemigrations
```
or
```
py manage.py makemigrations
```
### Changes are ready to make impact on db. Now,
```
python3 manage.py migrate
```
or
```
py manage.py migrate
```

### suppose you are adding a new field in an existing model
***remember to add (null = true, blank true)***  , this will prevent the conflict.
### Then make migrations and then migrate

## If you are facing problem and want to migrate all newly
### ***Step 1:*** delte all ".py" file in migrations folder except the "__init__" file
### ***Step 2:*** Drop the DB: locate the database file and run
```
rm db.sqlite3
```
### ***Step 3:***
### Now make necessary changes to your model then migrate the changes now,
```
python3 manage.py makemigrations
```
### Changes are ready to make impact on db. Now,
```
python3 manage.py migrate
```
 
