import os

port = os.getenv("PORT", "8080")
bind = f"0.0.0.0:{port}"
workers = 1
threads = 8
timeout = 0
worker_class = "gthread" 