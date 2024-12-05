set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

# Create a superuser (pass required variables)
python manage.py shell << EOF
from django.contrib.auth.models import User
if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser(
        username=os.environ.get("DJANGO_SUPERUSER_USERNAME", "itvet"),
        email=os.environ.get("DJANGO_SUPERUSER_EMAIL", "itvet2023@gmail.com"),
        password=os.environ.get("DJANGO_SUPERUSER_PASSWORD", "Admin@123"),
    )
EOF