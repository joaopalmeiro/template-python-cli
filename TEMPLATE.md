# Template Notes

- https://stackoverflow.com/questions/52781947/how-to-flush-interpreters-list-cache:
  - `Python: Clear Workspace Interpreter Setting` or
  - `Python Debugger: Clear Cache and Reload Window`
- https://packaging.python.org/en/latest/discussions/distribution-package-vs-import-package/#how-do-distribution-package-names-and-import-package-names-compare:
  - "hyphens `-` or underscores `_`"
- https://textual.textualize.io/how-to/package-with-hatch/
- https://click.palletsprojects.com/en/latest/changes/

## Commands

```bash
hatch new --cli --interactive hatch-cli-demo
```

```bash
hatch env prune && hatch env create
```

## Snippets

```toml
[project.scripts]
hatch-cli-demo = "hatch_cli_demo.cli:hatch_cli_demo"
```

### `ruff.toml` file

```toml
# https://docs.astral.sh/ruff/settings/#required-version
required-version = "0.3.0"
# https://docs.astral.sh/ruff/settings/#target-version
target-version = "py310"
# https://docs.astral.sh/ruff/settings/#output-format
output-format = "full"
# https://docs.astral.sh/ruff/settings/#preview
preview = false

[lint]
# All:
# https://docs.astral.sh/ruff/linter/#rule-selection
select = ["ALL"]
# https://docs.astral.sh/ruff/settings/#lint_fixable
fixable = ["ALL"]
# https://docs.astral.sh/ruff/settings/#lint_ignore
# https://docs.astral.sh/ruff/rules/#pydocstyle-d
# https://docs.astral.sh/ruff/formatter/#conflicting-lint-rules
ignore = ["D", "COM812", "ISC001"]

# Minimal:
# https://docs.astral.sh/ruff/settings/#lint_extend-select
# https://docs.astral.sh/ruff/rules/#isort-i
# extend-select = ["I"]

# https://docs.astral.sh/ruff/settings/#lint_isort_combine-as-imports
[lint.isort]
combine-as-imports = true
```
