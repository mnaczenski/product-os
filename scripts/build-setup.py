#!/usr/bin/env python3
"""Regenerates plugins/product-os/commands/workspace-setup.md from plugins/product-os/templates/.
Run after changing any template, then commit."""
import pathlib
P = pathlib.Path(__file__).resolve().parent.parent / "plugins" / "product-os"
T = P / "templates"
steps = [
 "Also create signals/<current year>/, signals/.raw/, work/.raw/ and inbox/processed/ (with a .gitkeep each).",
 "Create .gitignore (or append if it exists) with these lines: sources/*, !sources/README.md, inbox/*, !inbox/README.md, signals/.raw/, work/.raw/",
 "Then suggest: put existing documents into sources/ and run /bootstrap to build the evidence base, then /strategy to build the strategy with the user. Without documents, run /strategy directly and fill the top of CLAUDE.md manually.",
 "After the foundation: /sources to configure signal and work sources, edit tasks/routines.yml, then /today each morning.",
]
files = sorted((str(f.relative_to(T)), f.read_text()) for f in T.rglob("*") if f.is_file() and f.suffix in (".md", ".yml", ".yaml", ".json"))
out = ["---", "description: Scaffolds a product-os workspace (folders and templates) into the current repository.", "---",
       "Set up this repository as a product-os workspace.", "",
       "1. For each file below: if it already exists, skip it and report it. Otherwise create it with exactly the given content."]
out += [f"{i+2}. {s}" for i, s in enumerate(steps)]
out += [f"{len(steps)+2}. Do not commit. The user decides.", ""]
for rel, content in files:
    lang = "yaml" if rel.endswith((".yml", ".yaml")) else ("json" if rel.endswith(".json") else "markdown")
    out += [f"### File: {rel}", f"````{lang}", content.rstrip("\n"), "````", ""]
(P / "commands" / "workspace-setup.md").write_text("\n".join(out))
print(f"workspace-setup.md regenerated with {len(files)} templates")
