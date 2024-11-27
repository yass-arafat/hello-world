import unittest
import subprocess

class TestIntegration(unittest.TestCase):
    def test_hello_world_integration(self):
        # Run the hello.py script and capture its output
        result = subprocess.run(
            ["python", "app.py"],
            capture_output=True,
            text=True
        )
        # Check the output and exit code
        self.assertEqual(result.returncode, 0)  # Ensure the script exits successfully
        self.assertEqual(result.stdout.strip(), "Hello, World!")  # Check the printed output

if __name__ == "__main__":
    unittest.main()