import warnings
import leewise.http


def application(environ, start_response):

    warnings.warn("The WSGI application entrypoint moved from "
                  "leewise.service.wsgi_server.application to leewise.http.root "
                  "in 15.3.",
                  DeprecationWarning, stacklevel=1)
    return leewise.http.root(environ, start_response)
