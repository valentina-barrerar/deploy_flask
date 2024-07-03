#Conexión con MySQL
from flask_app.config.mysqlconnection import connectToMySQL

#Importar flash: Encargado de mostrar mensajes
from flask import flash

class Post:
    def __init__(self, data):
        self.id = data["id"]
        self.content = data["content"]
        self.created_at = data["created_at"]
        self.updated_at = data ["updated_at"]
        self.user_id = data["user_id"]

        self.user_name = data ["user_name"]

    @classmethod
    def save(cls, form): #método para guardar publicación
        #form = content + user
        query = "INSERT INTO posts (content, user_id) VALUES(%(content)s, %(user_id)s)"
        return connectToMySQL("foro_publicaciones").query_db(query, form)
    
    @staticmethod #validaciones siempre con método estático
    def validate_post(form):
        #form = content + user
        is_valid = True

        if len(form["content"]) < 1:
            flash("Post content is required.", "post")
            is_valid = False
        
        return is_valid
    
    @classmethod
    def get_all(cls): #Ante un SELECT recibimos un resultado = result
        query = "SELECT posts.*, users.first_name AS user_name FROM posts JOIN users ON posts.user_id = users.id ORDER BY created_at DESC;"
        results = connectToMySQL("foro_publicaciones").query_db(query)
        #result = lista de diccionarios
        posts = []
        for post in results:
            #post = {"id":1, "content":"Hola...", "user_name": "Elena"}
            posts.append(cls(post)) #Genera objeto de publicación y lo agrega a la lista de posts []
        return posts
    
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM posts WHERE id = %(id)s"
        connectToMySQL("foro_publicaciones").query_db(query, data)
        #No necesita devolver nada por eso no hay return
