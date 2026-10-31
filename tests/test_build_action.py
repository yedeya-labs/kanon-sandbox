"""The build hook must refuse a build with no release or no output directory (#21).

Under `set -e`, bash ignores a failure in any command of an `&&` list but the last, so a guard
written as `test -n A && test -n B` lets an empty A through. Each case runs the hook's script the
way the runner does, with its inputs in the step's env, and checks it fails and writes nothing.
"""

import os
import pathlib
import subprocess
import tempfile
import unittest

import yaml

ACTION = pathlib.Path(__file__).resolve().parent.parent / ".github/actions/build/action.yml"


def run_build(release, output):
    (step,) = yaml.safe_load(ACTION.read_text())["runs"]["steps"]
    return subprocess.run(
        ["bash", "-e", "-c", step["run"]],
        env={"PATH": os.environ["PATH"], "RELEASE": release, "OUTPUT": output},
        capture_output=True,
        text=True,
    )


class BuildActionGuard(unittest.TestCase):
    def test_a_missing_release_or_output_fails_the_build(self):
        for release, output in (("", "out"), ("v1", ""), ("", "")):
            with self.subTest(release=release, output=output), tempfile.TemporaryDirectory() as tmp:
                out = os.path.join(tmp, output) if output else ""
                result = run_build(release, out)
                self.assertNotEqual(result.returncode, 0, result.stdout)
                self.assertIn("::error::", result.stdout)
                self.assertFalse(os.path.exists(os.path.join(tmp, "out", "dist", "hello.txt")))

    def test_a_release_and_output_build_hello_txt(self):
        with tempfile.TemporaryDirectory() as tmp:
            run_build("v1", tmp).check_returncode()
            self.assertEqual(pathlib.Path(tmp, "dist", "hello.txt").read_text(), "v1\n")


if __name__ == "__main__":
    unittest.main()
