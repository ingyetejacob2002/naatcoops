from flask import Blueprint

member = Blueprint(
    'member',
    __name__,
    url_prefix='/member'
)