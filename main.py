import yaml
from pathlib import Path

def define_env(env):

    def load_tips(theme=None):

        folder = Path(f"data/{theme}") if theme else Path("data")

        if not folder.exists():
            return []

        all_tips = []

        for file in sorted(folder.rglob("*.yml")):

            data = yaml.safe_load(file.read_text(encoding="utf-8"))

            if data:
                all_tips.append(data)

        return all_tips

    def get_themes():
            folder = Path("data")

            if not folder.exists():
                return []

            return sorted(
                directory.name
                for directory in folder.iterdir()
                if directory.is_dir()
            )

    env.variables["tips"] = load_tips
    env.variables["themes"] = get_themes
