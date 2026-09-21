import unittest
from pathlib import Path


class TestReClaimProject(unittest.TestCase):

    def setUp(self):
        self.root = Path(__file__).resolve().parent.parent
        self.client = self.root / "client"
        self.server = self.root / "server"

    def test_client_exists(self):
        self.assertTrue(
            self.client.exists(),
            "client directory is missing"
        )

    def test_client_package_json_exists(self):
        self.assertTrue(
            (self.client / "package.json").exists(),
            "client/package.json is missing"
        )

    def test_client_package_lock_exists(self):
        self.assertTrue(
            (self.client / "package-lock.json").exists(),
            "client/package-lock.json is missing"
        )

    def test_server_exists(self):
        self.assertTrue(
            self.server.exists(),
            "server directory is missing"
        )

    def test_server_package_json_exists(self):
        self.assertTrue(
            (self.server / "package.json").exists(),
            "server/package.json is missing"
        )

    def test_react_dependency_exists(self):
        package_json = (self.client / "package.json").read_text(
            encoding="utf-8"
        )

        self.assertIn(
            '"react"',
            package_json,
            "React dependency is missing"
        )

    def test_vite_build_script_exists(self):
        package_json = (self.client / "package.json").read_text(
            encoding="utf-8"
        )

        self.assertIn(
            '"build": "vite build"',
            package_json,
            "Vite build script is missing"
        )


if __name__ == "__main__":
    unittest.main()