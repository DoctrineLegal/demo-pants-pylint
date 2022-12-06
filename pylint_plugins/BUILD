python_requirement(
    requirements=[
        # Pylint checkers needs
        "astroid",
        "pylint>=2.13.0,<2.15",
    ],
    resolve="pylint-plugins",
)

python_sources(
    name="pylint-plugins-sources",
    sources=["**/*.py", "!**/test_*.py"],
    resolve="pylint-plugins",
)