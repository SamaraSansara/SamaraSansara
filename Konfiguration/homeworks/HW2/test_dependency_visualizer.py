import unittest
from unittest.mock import patch, MagicMock
from dependency_visualizer import get_commit_data, generate_mermaid_graph, save_mermaid_graph, load_config

class TestDependencyVisualizer(unittest.TestCase):
    def setUp(self):
        """Настройка окружения для тестов."""
        self.sample_commits = [
            {
                "id": "a1b2c3d",
                "parents": ["x1y2z3"],
                "author": "Author Name",
                "date": "2024-12-01 12:00:00 +0000",
                "message": "Initial commit",
            },
            {
                "id": "x1y2z3",
                "parents": [],
                "author": "Author Name",
                "date": "2024-11-30 11:00:00 +0000",
                "message": "Setup project structure",
            },
        ]

    def test_generate_mermaid_graph(self):
        """Проверка правильности генерации Mermaid-графа."""
        graph = generate_mermaid_graph(self.sample_commits)
        self.assertIn("graph TD", graph)
        self.assertIn("a1b2c3d[", graph)
        self.assertIn("x1y2z3 --> a1b2c3d", graph)

    def test_load_config(self):
        """Проверка чтения конфигурации из XML."""
        mock_config = """
        <config>
            <mermaidPath>/path/to/mermaid</mermaidPath>
            <repoPath>/path/to/repo</repoPath>
            <outputPath>output.png</outputPath>
        </config>
        """
        with patch("builtins.open", unittest.mock.mock_open(read_data=mock_config)):
            config = load_config("mock_config.xml")
            self.assertEqual(config["mermaid_path"], "/path/to/mermaid")
            self.assertEqual(config["repo_path"], "/path/to/repo")
            self.assertEqual(config["output_path"], "output.png")

    @patch("subprocess.run")
    def test_save_mermaid_graph(self, mock_subprocess):
        """Проверка сохранения Mermaid-графа в PNG."""
        mermaid_code = "graph TD\nA --> B"
        mermaid_cli = "/path/to/mermaid-cli"
        output_path = "output.png"

        save_mermaid_graph(mermaid_code, mermaid_cli, output_path)
        mock_subprocess.assert_called_once_with(
            [mermaid_cli, "-i", unittest.mock.ANY, "-o", output_path],
            check=True
        )

if __name__ == "__main__":
    unittest.main()
