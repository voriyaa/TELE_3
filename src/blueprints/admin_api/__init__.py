# blueprints/admin_api/__init__.py
from flask import Blueprint, request, jsonify, make_response, render_template
from flask_apispec import use_kwargs, marshal_with
from src.Tools.DataBase import database
from flask_jwt_extended import JWTManager, jwt_required
from src.schemas.schemas import AdminSchema, TariffSchema, AuthSchema
from src.Authorization.Authorization import Authorization as Auth
from src.Admin.HandleAdmin import HandleAdmin

admin = Blueprint('api', __name__, url_prefix='/admin_api')


@admin.route('/login', methods=['POST'])
@marshal_with(AuthSchema)
@use_kwargs(AdminSchema(only=('username', 'password')))
def login(**kwargs):
    ans = Auth.admin_login(**kwargs)
    if not ans:
        return make_response(render_template('There is no such user'), 204)
    adm = HandleAdmin(**kwargs)
    token = HandleAdmin.get_token(adm)
    return {'access_token': token}


@admin.route('/register', methods=['POST'])
@marshal_with(AuthSchema)
@use_kwargs(AdminSchema)
def register(**kwargs):
    if HandleAdmin.is_addmin(**kwargs.get('username')):
        return make_response(render_template('There is already admin with this login'), 204)
    token = HandleAdmin.create_admin_account(**kwargs)
    return {'access_token': token}


@admin.route('/list_tariff', methods=['GET'])
@jwt_required
@marshal_with(TariffSchema(many=True))
def get_list_of_tariff():
    return HandleAdmin.get_list_of_tariffs()

@admin.route('/list_tariff/<int:tutorial_id>', methods='PUT')
@jwt_required
@use_kwargs(TariffSchema)
@marshal_with(TariffSchema)
def edit_tariff(tutorial_id, **kwargs):
    HandleAdmin.edit_tariff(tutorial_id, **kwargs)

@admin.route('/login/create_tariif', methods=['POST'])
@jwt_required
@use_kwargs(TariffSchema)
def create_tariif(**kwargs):
    HandleAdmin.create_new_tariff(**kwargs)
    return {'message': 'Successfully'}, 200