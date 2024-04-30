from flask import Flask, request, jsonify
from models import db, Project

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@project-db/project_db'
db.init_app(app)

@app.route('/projects', methods=['POST'])
def create_project():
    data = request.get_json()
    project = Project(name=data['name'], description=data['description'])
    db.session.add(project)
    db.session.commit()
    return jsonify(project.to_dict()), 201

@app.route('/projects', methods=['GET'])
def get_projects():
    projects = Project.query.all()
    return jsonify([project.to_dict() for project in projects]), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)