from fastapi.middleware.cors import CORSMiddleware


def get_cors_middleware(app, settings):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_allow_origins,
        allow_methods=settings.cors_allow_methods,
        allow_headers=settings.cors_allow_headers,
        allow_credentials=False,
    )
