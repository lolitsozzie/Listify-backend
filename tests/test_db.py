import pytest


@pytest.mark.django_db
def test_db_connection():
    """Checks that the test suite can access the database"""
    from django.db import connection
    with connection.cursor() as cursor:
        cursor.execute('SELECT version()')
        assert cursor.fetchone()
