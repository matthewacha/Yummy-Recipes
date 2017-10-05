from flask import url_for, redirect, flash, render_template, request
from flask_login import current_user, login_required

from app.recipe import forms
from forms import Categoryform, Recipeform
from . import recipe

class Recipes(object):
    def __init__(self, recipe_name, recipe_description):
        self.recipe_name = recipe_name
        self.recipe_description = recipe_description

class Categories(object):
    def __init__(self, category_name, category_description):
        self.category_name = category_name
        self.category_description = category_description
        
all_categories = []
all_recipes = []


@recipe.route('/dashboard',methods=['GET','POST'])
def list_categories():
    list_categories = all_categories
    return render_template('category_dashboard.html', \
	                        list_categories=list_categories, title='Categories') 
 
@recipe.route('/dashboard/add',methods=['GET','POST']) 
def add_category(): 
    add_category = True
    form = Categoryform()

    if request.method == 'POST':       
        try:
            cname = form.category_name.data
            description = form.category_description.data
            new_category = Categories(cname, description)
            all_categories.append(new_category)
            flash('Successfully added category')
            return redirect(url_for('recipe.list_categories'))
            #flash('Wrong email or password')	
        except :
            flash('error')
            print form.errors
    return render_template('add_category.html', action="Add",
                           add_category=add_category, form=form,
                           title="Add Category")
						   

@recipe.route('/dashboard/edit/<string:category_name>', methods=['GET','POST'])
def edit_category(category_name):
    add_category=False	
    form = Categoryform(obj=category)
    if request.method == 'POST':
        all_categories
        name=form.category_name.data
        description=form.category_description.data
        User.add_category(name, description)
        flash('Successfully edited')
        return redirect(url_for('recipe.list_categories'))

    return render_template('dashboard/add.html', action="Edit",
                           add_item=add_item, form=form,
                           category=category, title="Edit category")
						   
@recipe.route('/dashboard/delete/<string:category_name>',methods=['GET', 'POST'])
def delete_category(category_name):
    for category in all_categories:
        if category.category_name == category_name:
            all_categories.remove(category)
            flash('Deleted category')
            return redirect(url_for('recipe.list_categories'))
    return render_template(title="Deleted Item")
 
"""Crud for recipes"""
@recipe.route('/recipe',methods=['GET','POST'])
def list_recipes():
    list_recipes = all_recipes
    return render_template('recipe_dashboard.html',
                           list_recipes = list_recipes, title='Recipes') 
 
@recipe.route('/recipe/add',methods=['GET','POST']) 
def add_recipe(): 
    add_recipe = True
    form = Recipeform()
    if request.method == 'POST':
        try:
            lname = form.recipe_name.data
            description = form.recipe_description.data
            new_recipe = Recipes(lname, description)
            all_recipes.append(new_recipe)
            flash('Successfully added item')
            return redirect(url_for('recipe.list_recipes'))	
        except:
            flash('Error')
            print form.errors
    return render_template('add_recipe.html', action="Add",
                           add_recipe=add_recipe, form = form,
                           title="Add Recipe")
	
@recipe.route('/recipe/edit/<string:recipe_name>', methods=['GET','POST'])
def edit_recipe(recipe_name):
    add_recipe = False
    form = Recipeform()
    if request.method == 'POST':
        rname = form.recipe_name.data
        description = form.recipe_description.data
        for recipe in all_recipes:
            if recipe.recipe_name == recipe_name:
                recipe.recipe_name = rname
                recipe.recipe_description = description
                flash('Successfully edited')
                return redirect(url_for('recipe.list_recipes'))
            flash('no')
    return render_template('add_recipe.html', action="Edit",
                           add_recipe = add_recipe, form=form, title="Edit Recipe")
						   
@recipe.route('/recipe/delete/<string:recipe_name>', methods=['GET', 'POST'])
def delete_recipe(recipe_name):
    for recipe in all_recipes:
        if recipe.recipe_name == recipe_name:
            all_recipes.remove(recipe)
            flash('Deleted category')
            return redirect(url_for('recipe.list_recipes'))
    return render_template('recipe_dashboard.html', title="Deleted Item")
