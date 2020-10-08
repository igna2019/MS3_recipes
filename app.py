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
    recip = mongo.db.recipes.find()
    return render_template('recipes.html', recipes=recip)

# Function Select option into Recipe categories

@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipe.html', categories=mongo.db.recipes_categories.find())

# Function insert to add the dictionary into mongoDb.

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))


@app.route('/recipe/<recipe_id>')
# Take the ObjectID and display the information for the recipe
def recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template('recipe.html', recipe=the_recipe)

# Take the ObjectID open edit recipe form

@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_categories = mongo.db.recipes_categories.find()
    return render_template('editrecipe.html', recipe=the_recipe, categories=all_categories)


@app.route('/update_recipe/<recipe_id>' , methods=['POST'])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update( {'_id': ObjectId(recipe_id)},
    {
        'recipe_name':request.form.get('recipe_name'),
        'recipe_cat':request.form.get('recipe_cat'),
        'cooks_in':request.form.get('cooks_in'),
        'flavour':request.form.get('flavour'),
        'dificulty':request.form.get('dificulty'),
        'ingredients':request.form.get('ingredients'),
        'recipe_tag':request.form.get('recipe_tag'),
        'method':request.form.get('method'),
        'url_image':request.form.get('url_image')
    })
    return redirect(url_for('get_recipes'))

# Take the ObjectID and delete recipe option

@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))


if __name__=='__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
