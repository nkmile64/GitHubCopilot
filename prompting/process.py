# Description: The file processes talks.json

import json
from pathlib import Path


def filter_talks_by_tag(tag: str, talks: list) -> list:
    """Filter talks by tag using a list comprehension."""
    return [talk for talk in talks if tag in talk.get("tags", [])]


def prettyprint_talks(talks: list) -> None:
    """Pretty print talks."""
    for talk in talks:
        print(f"{talk['name']} - tags: {talk['tags']}")


# Read the json file
# __file__ is the path of the current script.
# i.e. __file__ = "C:/Dev/GitHubCopilot/prompting/process.py"
# Path(__file__) creates a Path object from the string path.
# The parent property returns the parent directory of the path.It removes the last
# # segment of the path, which is the filename "process.py", and returns
# the directory "C:/Dev/GitHubCopilot/prompting".
script_dir = Path(__file__).parent
# The slash operator concatenates path segments in a cross platform way.
# So if,
# script_dir = "C:/Dev/GitHubCopilot/prompting"
# the result is "C:/Dev/GitHubCopilot/prompting/talks.json"
json_path = script_dir / "talks.json"

with open(json_path, "r", encoding="utf-8") as f:
    talks: list = json.load(f)


python_talks = filter_talks_by_tag("history", talks)
prettyprint_talks(python_talks)
