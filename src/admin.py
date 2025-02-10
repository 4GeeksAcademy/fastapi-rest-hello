import os
from fastapi_admin.app import app as admin_app
from fastapi_admin.providers.login import UsernamePasswordProvider
from fastapi_admin.template import templates
from fastapi_admin.widgets import inputs, displays
from fastapi_admin.resources import Model
from .models import User

async def setup_admin(app):
    await admin_app.configure(
        templates=templates,
        providers=[
            UsernamePasswordProvider(
                admin_model=User,
                login_field="username",
                password_field="password",
            )
        ],
        admin_secret=os.environ.get('FASTAPI_ADMIN_SECRET', 'sample_secret'),
    )
    
    # Add your models here, for example this is how we add the User model to the admin
    admin_app.register_model(
        Model(
            label="User",
            model=User,
            page_display=displays.PageDisplay(
                fields=[
                    displays.Field(name="id"),
                    displays.Field(name="username"),
                    displays.Field(name="email"),
                ]
            ),
            page_form=inputs.PageForm(
                fields=[
                    inputs.Input(name="username"),
                    inputs.Input(name="email"),
                ]
            ),
        )
    )

    # You can duplicate that block to add new models
    # admin_app.register_model(
    #     Model(
    #         label="YourModelName",
    #         model=YourModelName,
    #         page_display=displays.PageDisplay(
    #             fields=[
    #                 displays.Field(name="id"),
    #                 displays.Field(name="field1"),
    #                 displays.Field(name="field2"),
    #             ]
    #         ),
    #         page_form=inputs.PageForm(
    #             fields=[
    #                 inputs.Input(name="field1"),
    #                 inputs.Input(name="field2"),
    #             ]
    #         ),
    #     )
    # )

    app.mount("/admin", admin_app)