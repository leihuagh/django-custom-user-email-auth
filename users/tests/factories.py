from factory import DjangoModelFactory, post_generation
import factory
from django.contrib.auth import get_user_model
CustomUser = get_user_model()
from typing import Sequence, Any


class CustomUserFactory(DjangoModelFactory):
    """Custom User factory for testing purposes."""

    email = factory.Faker("email")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    life_motto = factory.Faker("sentence")

    class Meta:
        model = CustomUser
        django_get_or_create = ["email"]

    @post_generation
    def password(self, create: bool, extracted: Sequence[Any], **kwargs) -> None:
        """Post generation hook to set the user's password."""

        password = factory.Faker(
            "password",
            length=42,
            special_chars=True,
            digits=True,
            upper_case=True,
            lower_case=True,
        ).generate(extra_kwargs={})

        self.set_password(password)
        self.password_plain_text = password