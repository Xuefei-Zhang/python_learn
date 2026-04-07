from pathlib import Path


def test_project_scaffold_exists() -> None:
    assert Path("core").exists()
    assert Path("runtime").exists()
    assert Path("systems").exists()
    assert Path("tests").exists()
    assert Path("core/__init__.py").exists()
    assert Path("runtime/__init__.py").exists()
    assert Path("systems/__init__.py").exists()
    assert Path("tests/__init__.py").exists()
    assert Path("README.md").exists()
    assert Path(".gitignore").exists()
    assert Path("pyproject.toml").exists()


def test_learning_support_directories_exist() -> None:
    assert Path("missions").exists()
    assert Path("notes/interview").exists()
    assert Path("notes/complexity").exists()
    assert Path("benchmarks").exists()
    assert Path("playground").exists()
    assert Path("missions/phase-00-foundations.md").exists()
    assert Path("missions/phase-01-linear-structures.md").exists()
    assert Path("missions/phase-02-hash-and-cache.md").exists()
    assert Path("missions/phase-03-trees-heaps-priority.md").exists()
    assert Path("missions/phase-04-graphs-and-scheduling.md").exists()
    assert Path("missions/phase-05-runtime-mechanisms.md").exists()
    assert Path("missions/phase-06-integrated-project.md").exists()


def test_phase_00_manual_framework_exists() -> None:
    assert Path("core/foundation_utils.py").exists()
    assert Path("systems/mission_tracker.py").exists()
    assert Path("tests/core/test_foundation_utils.py").exists()
    assert Path("tests/systems/test_mission_tracker.py").exists()
    assert Path("notes/complexity/phase-00-foundations.md").exists()
