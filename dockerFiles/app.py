import flask
from flask import jsonify #request
from jsonschema import validate, ValidationError
  
app = flask.Flask(__name__)
students = None

schema = {
    'type': 'object',
    'properties': {
        'name': {'type': 'string'},
        'id': {'type': 'string'},
        'grade': {'type': 'number'}
    },
    'required': ['name', 'id', 'grade']
}

def initData():
    global students
    students = [
        {"name" : "Juan Camilo", "id" : "1144209010", "grade" : 5},
        {"name" : "Ervin Harold", "id" : "1144186226", "grade" : 3},
        {"name" : "Cristian Jimenez", "id" : "113782845", "grade" : 2.6},
        {"name" : "Alejandro Ararat", "id" : "3382963", "grade" : 3}
    ]
initData()

@app.route('/getStudents', methods=['GET'])
def getListStudents():
    if flask.request.method == 'GET':
        global students
        return jsonify(students)
    else:
         return "Error: incorrect method", 400


@app.route('/addNewStudent', methods=['POST'])
def addStudents(): 
    if flask.request.method == 'POST':
        ## validamos que la data de entrada sea un jso
        if flask.request.is_json:
            ## obtenemos la data del nuevo estudiante
            newStudent = flask.request.get_json()
            ## validamos si la data ingresada tiene la estructura de json {name, id, grade}
            try:
                validate(instance=newStudent, schema=schema)
            except ValidationError as e:
                return jsonify({"error": "Invalid JSON schema"}), 400
            ## se agrega el nuevo estudiante de ser exitosa la validación
            global students
            students.append(newStudent)
            return jsonify(students), 201
        else:
            return jsonify({"error": "Invalid JSON format"}), 400
    else:
        return "Error: incorrect method", 405


if __name__ == '__main__':
    app.run(host='0.0.0.0')
