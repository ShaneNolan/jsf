import json
from pathlib import Path

from jsonschema import validate
from typer.testing import CliRunner

from jsf.cli import app

runner = CliRunner()


def test_app(TestData):
    file = Path("tmp.json")
    try:
        result = runner.invoke(app, ["--schema", TestData / "custom.json", "--instance", "tmp.json"])
        assert result.exit_code == 0
        assert file.exists()
        with open(file, "r") as f:
            instance = json.load(f)
        with open(TestData / "custom.json", "r") as f:
            schema = json.load(f)
        validate(instance, schema)
    finally:
        file.unlink()


def test_app_with_key(TestData):
    file = Path("tmp.json")
    try:
        result = runner.invoke(app, ["--schema", TestData / "custom_specification.json", "--instance", "tmp.json", "--key", "Example"])
        assert result.exit_code == 0
        assert file.exists()
        with open(file, "r") as f:
            instance = json.load(f)
        with open(TestData / "custom_specification.json", "r") as f:
            schema = json.load(f)
        validate(instance, schema)
    finally:
        file.unlink()
