from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()
db = SQLAlchemy()


class Contacts(db.Model):
    __tablename__ = 'Contacts'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    creation_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)

    def __init__(self, username, first_name, last_name):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name


class Email(Contacts):
    email = db.Column(db.String(100), nullable=False, unique=True)
    email_two = db.Column(db.String(100), nullable=True)
    email_three = db.Column(db.String(100), nullable=True)


class ContactsSchema(ma.Schema):
    id = fields.Integer()
    username = fields.String(required=False)
    first_name = fields.String(required=False)
    last_name = fields.String(required=False)
    creation_date = fields.DateTime()
    email = fields.String(required=False)
    email_two = fields.String(required=False)
    email_three = fields.String(required=False)

