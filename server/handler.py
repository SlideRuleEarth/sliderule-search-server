"""Lambda entrypoint. Mangum wraps the ASGI app for the Lambda runtime."""

from mangum import Mangum

from server.app import app

lambda_handler = Mangum(app, lifespan="off")
