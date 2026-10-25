"""The reusable workflow must print the caller's ref as data, never run it as shell (#15).

The runner substitutes a `${{ }}` expression into a `run:` script's TEXT before bash parses it,
and a git branch name may hold `$(...)` or backticks. So each step's script is rendered here the
way the runner renders it, for a ref that carries a command substitution, and run under bash.
"""

import os
import pathlib
import re
import subprocess
import tempfile
import unittest

import yaml

WORKFLOW = pathlib.Path(__file__).resolve().parent.parent / ".github/workflows/reusable.yml"

EXPR = re.compile(r"\$\{\{\s*([^}]*?)\s*\}\}")


def render(text, context):
    """Substitute every `${{ name }}` as the runner does: into the text, unescaped."""
    return EXPR.sub(lambda m: context[m.group(1)], text)


def run_step(step, context, cwd):
    env = {k: render(str(v), context) for k, v in (step.get("env") or {}).items()}
    return subprocess.run(
        ["bash", "-e", "-c", render(step["run"], context)],
        cwd=cwd,
        env={"PATH": os.environ["PATH"], **env},
        capture_output=True,
        text=True,
        check=True,
    )


class ReusableWorkflowRef(unittest.TestCase):
    def test_a_ref_with_a_command_substitution_is_printed_not_run(self):
        steps = yaml.safe_load(WORKFLOW.read_text())["jobs"]["hello"]["steps"]
        for branch in ("x$(touch${IFS}pwned)", "x`touch${IFS}pwned`"):
            ref = f"attacker/repo/.github/workflows/caller.yml@refs/heads/{branch}"
            with self.subTest(branch=branch), tempfile.TemporaryDirectory() as cwd:
                out = "".join(
                    run_step(s, {"github.workflow_ref": ref}, cwd).stdout for s in steps if "run" in s
                )
                self.assertFalse(os.path.exists(os.path.join(cwd, "pwned")), "the ref ran as a command")
                self.assertIn(ref, out)


if __name__ == "__main__":
    unittest.main()
