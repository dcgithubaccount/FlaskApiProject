from flask import request
from flask_restful import Resource
from Model import db, Contacts, ContactsSchema

contact_schema = ContactsSchema()
contacts_schema = ContactsSchema(many=True)


def data_and_error(json_data):
    errors = None
    try:
        data = contact_schema.load(json_data)
    except Exception as e:
        errors = e
    return data, errors


class ContactResource(Resource):
    def get(self):
        if not request.data:
            contacts = Contacts.query.all()
            contacts = contacts_schema.dump(contacts)
            return {'status': 'success', 'data': contacts}, 200
        else:
            json_data = request.get_json(force=True)
            # print(json_data)
            data, errors = data_and_error(json_data=json_data)
            if data.get('username') is not None:
                contact = Contacts.query.filter_by(username=data['username']).first()
                contact = contact_schema.dump(contact)
            elif data.get('email') is not None:
                contact = Contacts.query.filter_by(email=data['email']).first()
                contact = contact_schema.dump(contact)
            else:
                contact = Contacts.query.all()
                contact = contacts_schema.dump(contact)
            return {'status': 'success', 'data': contact}, 200

    def post(self):
        json_data = request.get_json(force=True)
        print(json_data)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = data_and_error(json_data=json_data)
        print(data['email'])
        if errors:
            return errors, 422
        contact = Contacts.query.filter_by(username=data['username']).first()
        if contact:
            return {'message': 'Contact already exists'}, 400
        contact = Contacts(
            username=data['username'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email']
        )

        db.session.add(contact)
        db.session.commit()

        result = contact_schema.dump(contact)

        return {"status": 'success', 'data': result}, 201

    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = data_and_error(json_data=json_data)
        if errors:
            return errors, 422
        contact = Contacts.query.filter_by(id=data['id']).first()
        # print(contact.email_two)
        # print(contact.email_three)
        if not contact:
            return {'message': 'Contact does not exist'}, 400
        contact.username = data.get('username', contact.username)
        contact.first_name = data.get('first_name', contact.first_name)
        contact.last_name = data.get('last_name', contact.last_name)
        contact.email = data.get('email', contact.email)
        contact.email_two = data.get('email_two', contact.email_two)
        contact.email_three = data.get('email_three', contact.email_three)
        db.session.commit()

        result = contact_schema.dump(contact)

        return {"status": 'success', 'data': result}, 204

    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = data_and_error(json_data=json_data)
        if errors:
            return errors, 422
        contact = Contacts.query.filter_by(id=data['id']).delete()
        db.session.commit()

        result = contact_schema.dump(contact)

        return {"status": 'success', 'data': result}, 204
