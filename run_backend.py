import os
import sys
import time
import traceback

print(">>> RUNNING FILE:", __file__)

BACKEND_ROOT = os.path.dirname(os.path.abspath(__file__))
if BACKEND_ROOT not in sys.path:
    sys.path.insert(0, BACKEND_ROOT)

from module import f1ndr_backend


def main():
    print(">>> MAIN() ENTERED <<<")
    print("Starting F1NDR backend...")

    backend = f1ndr_backend

    try:
        print(">>> RUNNING INGEST <<<")
        backend["pipelines"]["ingest"].run({"status": "backend_started"})
        print("F1NDR backend initialized.")
    except Exception:
        print("\n🔥 REAL ERROR BELOW 🔥\n")
        traceback.print_exc()
        print("\n🔥 END ERROR 🔥\n")
        return

    print("Backend entering persistent loop...")

    while True:
        print(">>> tick thing <<<")
        time.sleep(5)


if __name__ == "__main__":
    print(">>> __main__ EXECUTED <<<")
    main()
