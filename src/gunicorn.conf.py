# Basic configuration
name = "webapp"
wsgi_app = "config.wsgi:application"

# Worker processes
workers = 3
worker_class = "sync"

# User and group
user = "django"
group = "django"

# Logging
loglevel = "error"

# Timeout
timeout = 120
bind = "0.0.0.0:8000"

# Environment variables
raw_env = [
    "DJANGO_SETTINGS_MODULE=config.settings",
]


# Hooks
def on_starting(server):
    server.log.info("Starting gunicorn server for data-viz-app")


def on_exit(server):
    server.log.info("Stopping gunicorn server for data-viz-app")
