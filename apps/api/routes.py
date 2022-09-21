import json

from flask import request
from flask_restx import Api, Resource
from werkzeug.datastructures import MultiDict


from apps.api import blueprint
from apps.authentication.decorators import token_required

from apps.api.forms import *
from apps.models    import *

api = Api(blueprint)



