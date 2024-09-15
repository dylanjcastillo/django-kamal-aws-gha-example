import pytest
from django.contrib.auth import get_user_model


@pytest.mark.django_db
def test_create_user():
    User = get_user_model()
    user = User.objects.create_user(
        username="dcast", email="dcast@email.com", password="testpass123"
    )
    assert user.username == "dcast"
    assert user.email == "dcast@email.com"
    assert user.is_active
    assert not user.is_staff
    assert not user.is_superuser


@pytest.mark.django_db
def test_create_superuser():
    User = get_user_model()
    admin_user = User.objects.create_superuser(
        username="superadmin", email="superadmin@email.com", password="testpass123"
    )
    assert admin_user.username == "superadmin"
    assert admin_user.email == "superadmin@email.com"
    assert admin_user.is_active
    assert admin_user.is_staff
    assert admin_user.is_superuser
