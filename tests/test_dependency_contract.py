import tomllib
import unittest
from pathlib import Path


class TestDependencyContract(unittest.TestCase):
    def test_mcp_sdk_stays_on_certified_v1_release(self) -> None:
        pyproject_path = Path(__file__).parents[1] / "pyproject.toml"
        pyproject = tomllib.loads(pyproject_path.read_text())

        self.assertIn(
            "mcp[cli]==1.28.1",
            pyproject["project"]["dependencies"],
        )
