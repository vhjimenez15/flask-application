from flask import Blueprint, jsonify, request
from app import app, db
from app.elements.models import ElementsToProcess
from app.elements.schemas import ElementsToProcessSchema

elementBp = Blueprint('element', __name__)


@elementBp.route("/element/list/<id>", methods=['GET'])
def list_one_elements_to_process(id):
    elements_to_process = ElementsToProcess.query.get(id)
    schema = ElementsToProcessSchema()
    return jsonify(
        {
            'message': 'Successful',
            'data': schema.dump(elements_to_process)
        }
    )

@elementBp.route("/element/list", methods=['GET'])
def list_elements_to_process():
    elements_to_process = ElementsToProcess.query.all()
    schema = ElementsToProcessSchema(many=True)
    return jsonify(
        {
            'message': 'Successful',
            'data': schema.dump(elements_to_process)
        }
    )

@elementBp.route("/element/create", methods=['POST'])
def create_elements_to_process():
    data = request.json
    name = data.get('name')
    status = data.get('status')
    retries = data.get('retries')
    if not name or not status:
        return jsonify({'message': f'name or status is required'}), 400
    new_element = ElementsToProcess(name, status, retries)
    db.session.add(new_element)
    db.session.commit()
    return jsonify({'message': 'Successful'})

@elementBp.route("/element/update/<id>", methods=['PUT'])
def update_elements_to_process(id):
    data = request.json
    elements_to_process = ElementsToProcess.query.get(id)
    if not elements_to_process:
        return jsonify({'message': f'Id {id} not found'}), 400
    name = data.get('name')
    if name:
        elements_to_process.name = name
    status = data.get('status')
    if status:
        elements_to_process.status = status
    retries = data.get('retries')
    if retries:
        elements_to_process.retries = retries
    idBulk = data.get('idBulk')
    if idBulk:
        elements_to_process.idBulk = idBulk
    elements_to_process.name = data.get('name')
    db.session.commit()
    return jsonify({'message': 'Successful'})

@elementBp.route("/element/delete/<id>", methods=['DELETE'])
def delete_elements_to_process(id):
    elements_to_process = ElementsToProcess.query.get(id)
    if not elements_to_process:
        return jsonify({'message': f'Id {id} not found'}), 400
    db.session.delete(elements_to_process)
    db.session.commit()
    return jsonify({'message': 'Successful'})