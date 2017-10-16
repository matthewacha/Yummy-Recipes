from flask import url_for, redirect, flash, render_template, request,session
from app.recipe import forms
from app.user.views import all_users
from functools import wraps
from forms import Categoryform, Recipeform
from . import recipe
from app.user import views


all_recipes = []
def login_required(fx):
    @wraps(fx)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return fx(*args, **kwargs)
        else:
            flash('You need to be logged in')
            return redirect(url_for('user.login'))
    return wrap
 
"""Crud for recipes"""
@recipe.route('/recipe',methods=['GET','POST'])
@login_required
def list_recipes():
    for user in all_users:
        if user['email']==session['current_user']:
            list_recipes = user['recipes']
            return render_template('recipe_dashboard.html',
                           list_recipes = list_recipes, title='Recipes') 
 
@recipe.route('/recipe/add',methods=['GET','POST'])
@login_required
def add_recipe():
    add_recipe = True
    form = Recipeform()
    if request.method == 'POST':
        try:
            lname = form.recipe_name.data
            description = form.recipe_description.data
            new_recipe = {'recipe_name':lname, 'description':description}
            for user in all_users:
                if user['email'] == session['current_user']:
                    user['recipes'].append(new_recipe)
                    count=len(user['recipes'])
                    flash(count)
                    flash('Successfully added item')
                    return redirect(url_for('recipe.list_recipes'))
        except:
            flash('Error')
    return render_template('add_recipe.html', action="Add",
                           add_recipe=add_recipe, form = form,
                           title="Add Recipe")
	
@recipe.route('/recipe/edit/<string:recipe_name>', methods=['GET','POST'])
@login_required
def edit_recipe(recipe_name):
    add_recipe = False
    form = Recipeform()
    if request.method == 'POST':
        rname = form.recipe_name.data
        description = form.recipe_description.data
        for user in all_users:
            if user['email'] == session['current_user']:
                for recipe in user['recipes']:
                    if recipe['recipe_name']==recipe_name:
                        recipe['recipe_name']=rname
                        recipe['recipe_description']=description
                        count=len(user['recipes'])
                        flash(count)
                        flash('Successfully edited')
                        return redirect(url_for('recipe.list_recipes'))
    return render_template('add_recipe.html', action="Edit",
                                       add_recipe = add_recipe, form=form, title="Edit Recipe")
						   
@recipe.route('/recipe/delete/<string:recipe_name>', methods=['GET', 'POST'])
@login_required
def delete_recipe(recipe_name):
    if request.method == 'POST':
        for user in all_users:
                if user['email'] == session['current_user']:
                    for recipe in user['recipes']:
                        if recipe['recipe_name']==recipe_name:
                            user['recipes'].remove(recipe)
                            flash('Successfully deleted')
                            return redirect(url_for('recipe.list_recipes'))
    return redirect(url_for('recipe.list_recipes'))
