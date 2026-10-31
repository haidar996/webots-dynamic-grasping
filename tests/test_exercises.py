"""The exercise checker: blank templates are 'todo', reference solutions pass."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "exercises"))

import check   # noqa: E402


def test_templates_are_reported_as_not_started():
    assert {r["status"] for r in check.run()} == {"todo"}


def test_reference_solutions_pass():
    results = check.run(folder=ROOT / "tests" / "exercise_solutions")
    assert [r["status"] for r in results] == ["pass"] * 6, results


def test_wrong_answer_gets_a_hint(tmp_path):
    (tmp_path / "ex5_grip_force.py").write_text(
        "def min_grip_force(mass, mu):\n    return mass * 9.81 / mu\n"
        "def holds_while_lifting(f, m, mu, a):\n    return True\n")
    [r] = check.run([5], folder=tmp_path)
    assert r["status"] == "fail" and "two fingers" in r["message"]
