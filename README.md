# THPWD08 - Filtering and Searching the Mineral Catalog

This is the eighth project to team tree house's Python Web Tech Degree.

## Goal
- Refine 'Mineral Catalog' project by adding an ability to search information and filter it to match user preferences.

## Deliverables / Objectives
1. Allow filtering by the first letter of the mineral name.
    - Add links for each letter of the alphabet. This should be added to the layout template so that it appears on every page. When a letter is clicked, a list of minerals that start with that letter should be displayed in the list view. The letter of the alphabet currently being displayed should be bolded. In the details view, no letter should be bolded. On the homepage, select ‘A’ by default.

2. Allow text search.
    - Add a search box and button. The search box and button should be implemented as a form. When the search button is clicked, the site will search for minerals whose name contains the search text. The names of the minerals that match the search will be displayed in the list view. Add the search form to the layout template so that searching can be performed from any page in the site.

3. Allow filtering by group.
    - Add the ability to filter the list of minerals by adding links to these groups on the left side of the layout template. Clicking a group name, displays a list of all of the minerals in the database that are in that group. The group name being displayed should be bolded. In the details view, no group name should be bolded.
        * Silicates
        * Oxides
        * Sulfates
        * Sulfides
        * Carbonates
        * Halides
        * Sulfosalts
        * Phosphates
        * Borates
        * Organic Minerals
        * Arsenates
        * Native Elements
        * Other

4. Optimize database queries
    - Use the django-debug-toolbar to check that queries to the database take no longer than 10ms to complete.

5. Unit test the app.
    - Write unit tests to test that each view is displaying the correct information.
    - Write unit tests to test that the models, classes, and other functions behave as expected.

6. Make the templates match the style used in the example files.
    - Look at the example HTML files and global.css to determine the styles used in the pages.

## Steps to running testing program
1. Once in project root folder of virtual environment (`step 3` under Steps to Running/Exiting the Program), type `coverage run --source='.' manage.py website` to setup info about the % of code covered
2. In project root folder, type `python manage.py test` to run the testing program
3. In project root folder, type `coverage report` to see the result

## Steps to accessing admin panel
1. Once the server is running, type `http://127.0.0.1:8000/admin` in a web browser
2. Log into the panel with account registered in `step 5` below

## Steps to Running/Exiting the Program
1. Install pipenv by typing `pip install pipenv` or `pip3 install pipenv` for python3 users
2. In project root folder, install dependencies by typing `pipenv install`
3. In project root folder, enter virtual environment by typing `pipenv shell`
4. In `mineral_catalog` of project root folder, run `python manage.py migrate` or `python3 manage.py migrate` for python3 users.
5. In `mineral_catalog` of project root folder, run `python manage.py createsuperuser` or `python3 manage.py createsuperuser` to create an admin
6. In `mineral_catalog` of project root folder, run `python manage.py loaddata minerals.json` or `python3 manage.py loaddata minerals.json` to pre-populate data
7. In `mineral_catalog` of project root folder, run by typing `python manage.py runserver` or `python3 manage.py runserver` for python3 users.
8. Open chrome and enter given url (i.e. `http://127.0.0.1:8000/`)
9. Once done, exit django by pressing `Ctrl`+`C` and virtual environment by typing `exit`

## FAQ
1. Q: How would a user know which version of python is installed as default?
    - A: Python version can be found by typing `python --version` in terminal. If X in `X.*.*` is 2, then python 2 is installed as default, and if it's 3, then python 3 is being used as default.