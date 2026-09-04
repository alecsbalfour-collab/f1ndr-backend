import json
import uuid
import os
from datetime import datetime


BASE = os.path.dirname(os.path.abspath(__file__))


def load_json(path):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except:
        return {}


def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)


class Trinn:
    def __init__(self):
        # Load config
        self.settings = load_json(f"{BASE}/config/trinn_settings.json")
        self.limits = load_json(f"{BASE}/config/trinn_limits.json")
        self.routes = load_json(f"{BASE}/config/trinn_routes.json")
        self.modes = load_json(f"{BASE}/config/trinn_modes.json")
        self.env = load_json(f"{BASE}/config/trinn_env.json")

        # Load data
        self.character = load_json(f"{BASE}/data/trinn_character.json")
        self.memory = load_json(f"{BASE}/data/trinn_memory.json")
        self.state = load_json(f"{BASE}/data/trinn_state.json")
        self.history = load_json(f"{BASE}/data/trinn_history.json")
        self.flags = load_json(f"{BASE}/data/trinn_flags.json")

        # Load DB
        self.db = load_json(f"{BASE}/db/trinn.db.json")
        self.db_memory = load_json(f"{BASE}/db/trinn_memory.db.json")
        self.db_sessions = load_json(f"{BASE}/db/trinn_sessions.db.json")
        self.db_logs = load_json(f"{BASE}/db/trinn_logs.db.json")
        self.db_users = load_json(f"{BASE}/db/trinn_users.db.json")
        self.db_cache = load_json(f"{BASE}/db/trinn_cache.db.json")
        self.db_index = load_json(f"{BASE}/db/trinn_index.db.json")
        self.db_store = load_json(f"{BASE}/db/trinn_store.db.json")

        # Runtime
        self.session_id = str(uuid.uuid4())
        self.state["session_id"] = self.session_id
        self.save_state()

    # -----------------------------
    # Persistence Helpers
    # -----------------------------

    def save_state(self):
        save_json(f"{BASE}/data/trinn_state.json", self.state)

    def save_history(self):
        save_json(f"{BASE}/data/trinn_history.json", self.history)

    def save_memory(self):
        save_json(f"{BASE}/data/trinn_memory.json", self.memory)

    def save_db(self):
        save_json(f"{BASE}/db/trinn.db.json", self.db)
        save_json(f"{BASE}/db/trinn_memory.db.json", self.db_memory)
        save_json(f"{BASE}/db/trinn_sessions.db.json", self.db_sessions)
        save_json(f"{BASE}/db/trinn_logs.db.json", self.db_logs)
        save_json(f"{BASE}/db/trinn_users.db.json", self.db_users)
        save_json(f"{BASE}/db/trinn_cache.db.json", self.db_cache)
        save_json(f"{BASE}/db/trinn_index.db.json", self.db_index)
        save_json(f"{BASE}/db/trinn_store.db.json", self.db_store)

    # -----------------------------
    # Core Runtime
    # -----------------------------

    def think(self, prompt: str):
        """Marks Trinn as thinking."""
        self.state["thinking"] = True
        self.state["last_prompt"] = prompt
        self.save_state()

    def respond(self, text: str):
        """Stores response and updates history."""
        self.state["thinking"] = False
        self.state["last_response"] = text

        self.history["history"].append({
            "prompt": self.state["last_prompt"],
            "response": text,
            "timestamp": datetime.utcnow().isoformat()
        })

        self.save_state()
        self.save_history()
        return text

    # -----------------------------
    # Memory System
    # -----------------------------

    def remember(self, key: str, value):
        """Writes long-term memory."""
        self.db_memory["facts"].append({
            "key": key,
            "value": value,
            "timestamp": datetime.utcnow().isoformat()
        })
        self.save_db()

    def recall(self, key: str):
        """Retrieves memory by key."""
        for item in self.db_memory.get("facts", []):
            if item["key"] == key:
                return item["value"]
        return None

    # -----------------------------
    # Session Management
    # -----------------------------

    def start_session(self):
        self.db_sessions["active"][self.session_id] = {
            "started": datetime.utcnow().isoformat(),
            "history": []
        }
        self.save_db()

    def end_session(self):
        session = self.db_sessions["active"].pop(self.session_id, None)
        if session:
            session["ended"] = datetime.utcnow().isoformat()
            self.db_sessions["history"].append(session)
            self.save_db()

    # -----------------------------
    # Logging
    # -----------------------------

    def log(self, event: str):
        self.db_logs["events"].append({
            "event": event,
            "timestamp": datetime.utcnow().isoformat()
        })
        self.save_db()

    # -----------------------------
    # Main Interaction
    # -----------------------------

    def handle(self, prompt: str):
        """Main entry point for Trinn."""
        self.think(prompt)

        # Basic example response logic
        response = f"Trinn received: {prompt}"

        return self.respond(response)
