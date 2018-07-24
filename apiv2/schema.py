
"""Validation functions and schemas for input fields"""
from marshmallow import Schema, fields, validate, ValidationError
import re


def validate_name(data):
    """validate name method"""
    name_re = re.fullmatch(re.compile(r"^\w+$"),data)
    if not name_re:
        raise ValidationError("Name contains visible characters only")
    elif len(data) <= 2:
        raise ValidationError("Name is too short")

def validate_password(password):
    """validate password method"""
    if len(password) < 6:
        raise ValidationError("Enter a password more than 6 characters")
    elif not re.search(r'[a-z]+',password):
        raise ValidationError("Have atleast one small letter")
    elif not re.search (r'[A-Z]+',password):
        raise ValidationError("Have atleast one capital letter")
    elif not re.search(r'\W+',password):
        raise ValidationError("Have atleast one special character like #,!")
    else:
        password_re = re.fullmatch(re.compile(r"^\S+$"),password)
        if not password_re:
            raise ValidationError('No spaces in password')

class UserSchema(Schema):
    """user input schema """
    fname = fields.Str(validate=validate_name, required=True)
    lname = fields.Str(validate=validate_name, required=True)
    email = fields.Str(validate=validate_name, required=True)
    password = fields.Str(validate=validate_password, required=True) 
    cpass = fields.Str(validate=validate_password, required=True)
Userschema = UserSchema()

class RideSchema(Schema):
    "ride input schema"
    start_loc = fields.Str(validate=validate_name, required=True)
    end_loc = fields.Str(validate=validate_name, required=True)
    departure_time = fields.Str(validate=validate_name, required=True)
    date = fields.Str(validate=validate_name, required=True)
    route = fields.Str(validate=validate_name, required=True)
    cost = fields.Str(validate=validate_name, required=True)
rideschema = RideSchema()

class RequestSchema(Schema):
    "ride input schema"
    pickup_loc = fields.Str(validate=validate_name, required=True)
requestschema = RequestSchema()

class ResponseSchema(Schema):
    "response input schema"
    respo = fields.Str(validate=validate_name, required=True)
responsechema = ResponseSchema()