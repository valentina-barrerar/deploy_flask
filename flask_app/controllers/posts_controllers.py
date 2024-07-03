from flask import Flask, render_template, redirect, request, session, flash
from flask_app import app

#Importamos los modelos desde la clase
from flask_app.models.post import Post

@app.route("/create_post", methods=["post"])
def create_post():
    #request.form = {content + user}
    if not Post.validate_post(request.form):
        return redirect("/dashboard")
    
    Post.save(request.form)
    return redirect("/dashboard")

@app.route("/delete_post/<int:id>")
def delete_post(id):
    #Función que borre un registro en base a su id
    dicc = {"id": id}
    Post.delete(dicc)
    return redirect("/dashboard")