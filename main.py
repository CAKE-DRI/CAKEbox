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

    def get_keywords():
            folder = Path("data")

            if not folder.exists():
                return []

            all_keywords = set()

            for file in sorted(folder.rglob("*.yml")):
                data = yaml.safe_load(file.read_text(encoding="utf-8"))

                if not isinstance(data, dict):
                    continue

                keywords = data.get("keywords", [])

                if isinstance(keywords, str):
                    keywords = [keywords]

                if isinstance(keywords, list):
                    for keyword in keywords:
                        if isinstance(keyword, str) and keyword.strip():
                            all_keywords.add(keyword.strip())

            return sorted(all_keywords, key=str.casefold)

    env.variables["tips"] = load_tips
    env.variables["themes"] = get_themes
    env.variables["keywords"] = get_keywords
