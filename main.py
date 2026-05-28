import yaml
from pathlib import Path

def define_env(env):

    def load_tips(theme):

        folder = Path(f"data/tips/{theme}")

        if not folder.exists():
            return []

        all_tips = []

        for file in sorted(folder.glob("*.yml")):

            data = yaml.safe_load(file.read_text(encoding="utf-8"))

            if data:
                all_tips.append(data)

        return all_tips

    env.variables["tips"] = load_tips