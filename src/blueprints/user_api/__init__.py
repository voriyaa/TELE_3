# blueprints/user_api/__init__.py
from flask import Blueprint, request
from flask_apispec import use_kwargs, marshal_with
from flask_jwt_extended import decode_token
from src.schemas.schemas import UserSchema, TariffSchema, AuthSchema
from src.Authorization.Authorization import Authorization as Auth
from src.User.HandleUser import HandleUser

user = Blueprint('user', __name__, url_prefix='/user_api')


@user.route('/check_token', methods=['POST'])
def protected():
    token = request.json.get('token')
    decoded_token = decode_token(token)  # Декодируем токен
    jwt_identity = decoded_token.get('sub')  # Получаем идентификатор пользователя из токена
    jwt_role = decoded_token.get('role')  # Получаем роль пользователя из токена
    data = {'username': jwt_identity, 'role': jwt_role}
    return data




