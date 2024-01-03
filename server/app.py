
from flask import Flask, request,make_response,jsonify
from flask_cors import CORS
from flask_migrate import Migrate
from models import db,Movie

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)
migrate = Migrate(app,db)
db.init_app(app)

@app.route('/movies',methods=['GET'])
def movies():
    if request.method =='GET':
        movies = Movie.query.all()
        # rec_dict = [movie.to_dict() for movie in movies]
        # response = make_response(
        #     jsonify(rec_dict), 200)
        return make_response(jsonify([movie.to_dict() for movie in movies]),200)


    
    return make_response(jsonify({{
                        "text": "Method not allowed."
                      }}), 200)




if __name__ =="__main__":
    app.run(port=5555)