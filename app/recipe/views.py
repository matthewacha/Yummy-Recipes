from flask import url_for, redirect, flash, render_template, request
from flask_login import current_user, login_required

from app.recipe import forms
from forms import Categoryform, Recipeform
from ..models import Category, Recipe
from . import recipe
from app import yummy, models

@recipe.route('/dashboard',methods=['GET','POST'])
#@login_required
def list_categories():
    if current_user:
        #listcat=Category.query.all()
        return render_template('category_dashboard.html',title='Categories') 
 
@recipe.route('/dashboard/add',methods=['GET','POST']) 
#@login_required 
def add_category(): 
    add_category = True
    form=Categoryform()
    if request.method=='POST':
        try:
            if form.validate():
                Iname=form.name.data
                Description=form.description.data	
                category = Category(Iname,Description)
                yummy.session.add(category)
                yummy.session.commit()
                flash('Successfully added item')
                return redirect(url_for('recipe.list_categories'))
            flash('Wrong email or password')	
        except:
            flash('Error')
     
    return render_template('add_category.html', action="Add",
                           add_category=add_category, form=form,
                           title="Add Category")
						   

@recipe.route('/dashboard/edit/<int:id>', methods=['GET','POST'])
@login_required
def edit_category(id):
    add_category=False	

    category = categories.query.get_or_404(id)
    form = Categoryform(obj=category)
    if form.validate():
        category.name=form.name.data
        category.description=form.description.data
        yummy.session.commit()
        flash('Successfully edited')
        return redirect(url_for('user.list_categories'))
  
    form.description.data = category.description
    form.name.data = category.name
 
    return render_template('dashboard/add.html', action="Edit",\
                            add_item=add_item, form=form,\
							category=category, title="Edit category")
						   
@recipe.route('/dashboard/delete/<int:id>',methods=['GET','POST'])
@login_required
def delete_category(id):
 category = Categories.query.get_or_404(id)
 yummy.session.delete(category)
 yummy.session.commit()
 flash('Deleted category')
 return redirect(url_for('recipe.list_category'))
 return render_template(title="Deleted Item")
 
 ##CRUD recipes
@recipe.route('/recipe',methods=['GET','POST'])
#@login_required
def list_recipes():
    #user=current_user()
    #list_recipes=Recipes.query.all()
    return render_template('recipe_dashboard.html',title='Recipes') 
 
@recipe.route('/recipe/add',methods=['GET','POST']) 
@login_required 
def add_recipe(): 
    add_category = True
    form=Recipeform()
    if request.method=='POST':
        try:
            if form.validate():
                Iname=form.name.data
                Description=form.description.data	
                recipe = Recipe(Iname,Description)
                yummy.session.add(category)
                yummy.session.commit()
                flash('Successfully added item')
                return redirect(url_for('recipe.list_categories'))
            flash('Wrong email or password')	
        except:
            flash('Error')
     
    return render_template('add_category.html', action="Add",
                           add_category=add_category, form=form,
                           title="Add Category")
						   

@recipe.route('/dashboard/edit/<int:id>', methods=['GET','POST'])
@login_required
def edit_recipe(id):
    add_category=False	

    category = categories.query.get_or_404(id)
    form = Categoryform(obj=category)
    if form.validate():
        category.name=form.name.data
        category.description=form.description.data
        yummy.session.commit()
        flash('Successfully edited')
        return redirect(url_for('user.list_categories'))
  
    form.description.data = category.description
    form.name.data = category.name
 
    return render_template('dashboard/add_recipe.html', action="Edit",\
                            add_item=add_item, form=form,\
							category=category, title="Edit category")
						   
@recipe.route('/dashboard/delete/<int:id>',methods=['GET','POST'])
@login_required
def delete_recipe(id):
 recipe = recipes.query.get_or_404(id)
 yummy.session.delete(category)
 yummy.session.commit()
 flash('Deleted category')
 return redirect(url_for('recipe.list_recipes'))
 return render_template(title="Deleted Item")