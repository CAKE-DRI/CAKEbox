import yaml
from pathlib import Path

def define_env(env):

    def load_tips(theme):
        path = Path(f"data/tips/{theme}.yml")
        if not path.exists():
            return []
        return yaml.safe_load(path.read_text()) or []

    env.variables["tips"] = load_tips
