
import yaml
from pathlib import Path

def define_env(env):

    @env.macro
    def tips(theme):

        folder = Path(f"data/tips/{theme}")

        all_tips = []

        if folder.exists():

            for file in sorted(folder.glob("*.yml")):

                tip = yaml.safe_load(
                    file.read_text(encoding="utf-8")
                )

                if tip:
                    all_tips.append(tip)

        return all_tips
