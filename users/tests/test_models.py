from users.tests.factories import CustomUserFactory

class TestCompany:
    """Test suite for the company model."""

    def test_dunder_string(self):
        """Ensure the dunder string method returns the appropriate value."""

        user = CustomUserFactory()
        assert str(user) == f"{user.username}"