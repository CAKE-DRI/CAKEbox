import yaml
from pathlib import Path


def define_env(env):

    tips_path = Path("data/tips")

    tips = {}

    for file in tips_path.glob("*.yml"):

        with open(file, "r") as f:
            tips[file.stem] = yaml.safe_load(f)

    env.variables["tips"] = tips
