from pipelines.module import pipelines


def build_f1ndr_backend():
    return {
        "pipelines": pipelines,
    }


f1ndr_backend = build_f1ndr_backend()
