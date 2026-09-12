import unittest
from pathlib import Path


class TestReClaimProject(unittest.TestCase):

    def setUp(self):
        self.root = Path(__file__).resolve().parent.parent

    def test_home_page_exists(self):
        self.assertTrue(
            (self.root / "index.html").exists(),
            "index.html is missing"
        )

    def test_login_page_exists(self):
        self.assertTrue(
            (self.root / "login.html").exists(),
            "login.html is missing"
        )

    def test_register_page_exists(self):
        self.assertTrue(
            (self.root / "register.html").exists(),
            "register.html is missing"
        )

    def test_found_items_page_exists(self):
        self.assertTrue(
            (self.root / "found-items.html").exists(),
            "found-items.html is missing"
        )

    def test_html_pages_have_html_tag(self):
        pages = [
            "index.html",
            "login.html",
            "register.html",
            "found-items.html"
        ]

        for page in pages:
            content = (self.root / page).read_text(
                encoding="utf-8"
            ).lower()

            self.assertIn(
                "<html",
                content,
                f"{page} does not contain an HTML tag"
            )

    def test_css_folder_exists(self):
        self.assertTrue(
            (self.root / "css").exists(),
            "CSS folder is missing"
        )

    def test_js_folder_exists(self):
        self.assertTrue(
            (self.root / "js").exists(),
            "JavaScript folder is missing"
        )


if __name__ == "__main__":
    unittest.main()