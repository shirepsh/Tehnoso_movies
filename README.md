
# Tehnoso's movies library
![Logo](static/movies.png)

### **tutorial:**

- This page shows all the existing movies in the company's list.

- full crud operation (get / post / delete / put) of the movies.

- any user can rate the movies.
Each rating affects the rating average of that movie (which is also displayed on the page)

- using the following technologies: python, fastAPI, json, HTML, css

### **project locator:**
https://github.com/shirepsh/Tehnoso_movies


### **guide line:**
- If you have not installed Python3, please do
- Please make sure you have 'pip' installed on your OS. 
If it is not installed, please refer to the link below and follow the steps: [Link to PyPa.io](https://pip.pypa.io/en/stable/cli/pip_install/)

1.if you use GitHub download the project from GitHub by the comment:
```bash
git clone
```
2. install virtualenv (if u dont have one)
```bash 
pip install virtualenv
```
3. open venv named venv
```bash
python -m virtualenv venv
```
4. get into the venv 
```bash
venv\Scripts\active
```
5. install all the right packages with the requirements file
```bash
pip install -r requirements.txt  
``` 
6. run the application by the comment:
```
uvicorn myapp:app --reload
```
7. once the code is active go to your browser and at the url write http://localhost:8000/ it will open the html page.

### **The structure of the project**
the project build from:

- **index.html** file - located inside the static folder, the FRONTEND of the project

- **Movies.json** file- Used as a DataBase

- **myapp.py file** - the BACKEND of the project 

- **requirements.txt** - All necessary installations

- **README.md file** - Project description and visibility to the user

