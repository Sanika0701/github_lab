# github_lab
Additional Improvements and Exploration

Apart from the standard lab instructions (Steps 1–5), the following enhancements and debugging refinements were implemented to improve reliability, automation, and maintainability of the project.

🧩 1. Enhanced Project Structure and Git Hygiene

Created a comprehensive .gitignore file to exclude unnecessary files and folders such as virtual environments, __pycache__, .pytest_cache, .vscode, .env, and build artifacts.

Ensured the virtual environment (lab_01/) and temporary files are ignored to maintain a clean Git history and reduce repository size.

Configured Git locally with user credentials and branch alignment (default branch set to main).

🧮 2. Improved calculator.py Implementation

Extended the functionality beyond the professor’s template:

Added fun5(x, y) to compute the power of a number (x ** y).

Introduced type validation for all functions (fun1–fun5) using isinstance() to handle invalid input gracefully.

Added detailed docstrings following professional Python documentation standards (Args, Returns, Raises).

Improved fun4 to validate all inputs and handle summation of three numbers safely.

🧪 3. Expanded Testing Suite

Created unit tests using both pytest and unittest frameworks, each validating:

Correct mathematical operations (fun1–fun5).

Proper handling of invalid input (raising ValueError for non-numeric data).

Added parametrized tests in pytest for multiple input–output scenarios for fun5().

Included a sys.path.append() workaround in test files to ensure reliable imports in both local and CI environments.

⚙️ 4. Dependency Management

Updated requirements.txt to include only necessary dependencies:

pytest>=7.4,<9


(Excluded unittest, since it’s part of the Python standard library.)

Verified dependency installation through the virtual environment and GitHub Actions.

🚀 5. GitHub Actions (CI/CD) Improvements

Created two workflows under .github/workflows/:

pytest_action.yml

unittest_action.yml

Integrated modern, stable action versions:

actions/checkout@v4

actions/setup-python@v5

actions/upload-artifact@v4

Pinned Python version to 3.10.14 for full compatibility with Ubuntu 24.04 runners.

Defined explicit test paths (pytest test ... and python -m unittest discover -s test ...) to ensure test discovery succeeds in CI.

Added artifact upload for Pytest XML reports for better result tracking.

Enhanced readability with success/failure message echoes using emojis (✅, ❌).

🧭 6. Debugging and Continuous Integration Success

Fixed multiple setup and path-related issues:

ModuleNotFoundError: No module named 'src'

No tests collected (exit code 5)

Deprecated actions/upload-artifact@v2

Python version not found for Ubuntu 24.04

Verified both workflows run successfully and pass all tests (green checkmarks on Actions tab).

🏁 7. Current Branch Setup

Development and testing were performed in the featurea branch to isolate experimental changes from the main branch.

Both workflows are fully functional within this branch, and all tests pass successfully in GitHub Actions.

✅ Outcome

Both Pytest and Unittest workflows now execute automatically via GitHub Actions.

All test cases pass successfully.

The repository demonstrates best practices in environment management, testing, and CI/CD pipeline setup beyond the basic lab scope.