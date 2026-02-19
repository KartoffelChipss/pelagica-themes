import json
import os
import sys
import uuid

INDEX_FILE = "index.json"

ALLOWED_MODES = {"light", "dark"}

def fail(message):
    print(f"❌ {message}")
    sys.exit(1)

def load_json(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        fail(f"Invalid JSON in {path}: {e}")
    except FileNotFoundError:
        fail(f"File not found: {path}")

def validate_theme_schema(theme_path):
    theme_data = load_json(theme_path)

    required_fields = ["name", "author", "description", "version", "colors", "radius", "modes"]

    for field in required_fields:
        if field not in theme_data:
            fail(f"{theme_path} is missing required field '{field}'")

    # Validate modes
    if not isinstance(theme_data["modes"], list):
        fail(f"{theme_path} 'modes' must be an array")

    modes = set(theme_data["modes"])

    if not modes:
        fail(f"{theme_path} must define at least one mode")

    if not modes.issubset(ALLOWED_MODES):
        fail(f"{theme_path} contains invalid modes. Only 'light' and 'dark' allowed")

    # Validate colors structure
    if not isinstance(theme_data["colors"], dict):
        fail(f"{theme_path} 'colors' must be an object")

    color_modes = set(theme_data["colors"].keys())

    # colors must match declared modes exactly
    if not color_modes.issubset(ALLOWED_MODES):
        fail(f"{theme_path} 'colors' contains invalid mode keys")

    if color_modes != modes:
        fail(f"{theme_path} 'colors' keys must match declared 'modes'")

    # Each mode must be an object
    for mode, value in theme_data["colors"].items():
        if not isinstance(value, dict):
            fail(f"{theme_path} colors.{mode} must be an object")

def main():
    if not os.path.exists(INDEX_FILE):
        fail("index.json not found")

    data = load_json(INDEX_FILE)

    if "themes" not in data or not isinstance(data["themes"], list):
        fail("index.json must contain a 'themes' array")

    seen_ids = set()

    for i, theme in enumerate(data["themes"]):
        required_fields = ["id", "name", "author", "description", "version", "path", "previews"]

        for field in required_fields:
            if field not in theme:
                fail(f"Theme #{i} is missing required field '{field}'")

        # Validate UUIDv4
        try:
            uuid_obj = uuid.UUID(theme["id"])
        except ValueError:
            fail(f"Theme '{theme['name']}' has invalid UUID: {theme['id']}")

        if uuid_obj.version != 4:
            fail(f"Theme '{theme['name']}' UUID is not version 4: {theme['id']}")

        if str(uuid_obj) != theme["id"].lower():
            fail(f"Theme '{theme['name']}' UUID must be canonical lowercase")

        # Check uniqueness
        if theme["id"] in seen_ids:
            fail(f"Duplicate UUID found: {theme['id']}")
        seen_ids.add(theme["id"])

        # Validate theme file exists
        if not os.path.exists(theme["path"]):
            fail(f"Theme file not found: {theme['path']}")

        # Validate preview files exist
        if not isinstance(theme["previews"], list):
            fail(f"'previews' must be an array in theme '{theme['name']}'")

        for preview in theme["previews"]:
            if not os.path.exists(preview):
                fail(f"Preview file not found: {preview}")

        # Validate theme schema
        validate_theme_schema(theme["path"])

    print("✅ Registry validation passed.")

if __name__ == "__main__":
    main()
