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
