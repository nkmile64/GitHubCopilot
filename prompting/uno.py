from pathlib import Path

# __file__ is the path of the current script.
# i.e. __file__ = "C:/Dev/GitHubCopilot/prompting/process.py"
# Path(__file__) creates a Path object from the string path.
# The parent property returns the parent directory of the path.It removes the last segment of the path, which is the filename "process.py", and returns the directory "C:/Dev/GitHubCopilot/prompting".

script_dir = Path(__file__).parent
# The slash operator concatenates path segments in a cross platform way.
# So if,
# script_dir = "C:/Dev/GitHubCopilot/prompting"
# the result is "C:/Dev/GitHubCopilot/prompting/talks.json"
json_path = script_dir / "talks.json"
