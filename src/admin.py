from sqladmin import ModelView
from .models import User


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.username, User.email]


def register_admin_views(admin):
    admin.add_view(UserAdmin)