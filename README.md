# Data Centric Development Milestone Project

[Demo Link](https://ms3-recipes.herokuapp.com/ "Demo Link")

## La variété alimentaire

This web was required for a chef to show a list of recipes available on its menu. The main idea is to present up on the main page with individual cards of each one with links to a more detailed description of them.

There were categorized by type:
* Vegan
* American
* Indian
* Pasta
* Pizza
* Vegetarian
* Fish

The target audience is a general public who is interested in cooking some kind of fashion recipes.

## UX

The site  "La variété alimentaire"  was structured with :


* Home page: This page  shows all the existing recipes separated by  cards.
Each card has a limited description of the recipe however: Name of the recipe, flavour, cooking time and a link to full details of the recipe ("Recipe details"). The main focus was to show the recipes with a picture and just a few elements for the user to rapidly identify the one which is looking for. Photo and "Recipe details" are linked both to the same recipe details page. "Home" is set  on the navigation bar so it is accessible through all the pages involved on this site.Also, clicking on the logo " La variété alimentaire" redirects to the "Home" page too.

* Add a Recipe: This option on the Navigation bar launches a page with a form to add a new recipe on the database. Submit button will add the record into the database. 

		Recipe Category: This is a drop down box select menu.
		Name
		Fancy Description: it pretends to be a place to bring more details  of the recipe, probably a paragraph to describe the flavours, etc
		Serves for
		Difficulty
		Core of the recipe: This pretends to be a place to set a few words of it, Main ingredients, etc.
		Method of cooking
		List of Ingredients: This is the place to set all the ingredients separate by a comma each one of them. By doing  this way, the list will be presented as an unordered list.




* Recipe details: The card shows limited information of each recipe. Clicking on "Recipe details" will trigger a second page with a more expanded photo, a few lines of text describing the recipe and flavours, the list of ingredients ( an unordered list) and cooking method. 

* Delete and Edit buttons: Once clicking on "Recipe details" the user will find the full details of the recipe. At the bottom of the page there are two buttons: Delete and Edit. Delete will simply remove the recipe from the database. Edit button will trigger another page where each field of the recipe is able of edited.

* Edit a Recipe: This page allows the user to edit all the fields of the recipe. There is also a drop down box for Recipe Category. The user should select one of the options there.  At the bottom of the page , a "CONFIRM CHANGES '' button will update the recipe on the database.

## Technologies Used:

		Python3 on backedn
		Flask framework
		Jinja
		NoSQL 
		HTML
		CSS
		Bootstrap
		Materialize
		Google Fonts
		Javascript
		JQuery
		Balsamiq Wireframes

## Features

The main feature of this website is the option to Create, Read, Update and Delete (CRUD) records on a non relational database. The solution is able to run on a mobile environment with a side-bar menu on the left. 


## Deployment

This site was designed using Python on the backend and Flask web-framework for presenting it on a web environment. We are also using Jinja templating language to write logic using HTML templates. The site runs queries and updates on a NoSQL database hosted in MongoDB.
The backend is hosted in gitpod and githup while the application is on heroku.
The Database is hosted on MongoDB.
Requirements file includes the following packages:
	click==7.1.2
	dnspython==2.0.0
	Flask==1.1.2
	Flask-PyMongo==2.3.0
	itsdangerous==1.1.0
	pymongo==3.11.0
	Werkzeug==1.0.1



## Potential and future features

The web site would need the option of registration on a site giving different permissions or roles to users. This could be potentially only owners to delete recipes and different roles for addition or edition.
Also, it should include a search option to filter out by types of recipes. 

## Testing

Access to the database has been tested intensively as the same as updating, editing or deleting options.

## External links

Information related to recipes are from Jamie Oliver chef:

https://www.jamieoliver.com/


Photos have no relation at all with the recipes and are all free of charge. They have been linked all from shutterstock 

https://www.shutterstock.com/




--------



