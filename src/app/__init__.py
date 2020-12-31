from ._app import create_app, read_run_configuration

__all__ = ['app', 'run_configuration']

# app = create_app()
run_configuration = read_run_configuration()
