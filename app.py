import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo 
from bson.objectid import ObjectId

if os.path.exists("env.py"):
    import env


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'task_manager'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    return render_template('recipes.html', recipes=mongo.db.recipes.find())

#Function Select option into Recipe categories

@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipe.html', categories=mongo.db.recipes_categories.find())

#Function insert to add the dictionary into mongoDb.

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))


@app.route('/recipe/<recipe_id>')
# Take the ObjectID and display the information for the recipe
def recipe(recipe_id):
    the_recipe = mongo.db.Recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template('recipe_one.html', recipe=the_recipe,
                           title=the_recipe['recipe_name'])


if __name__=='__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
