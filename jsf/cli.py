from pathlib import Path

import typer

from .parser import JSF

app = typer.Typer()


@app.command()
def main(
    schema: Path = typer.Option(
        ..., exists=True, file_okay=True, dir_okay=False, writable=False, readable=True, resolve_path=True,
    ),
    instance: Path = typer.Option(
        ..., exists=False, file_okay=True, dir_okay=False, writable=True, readable=False, resolve_path=True,
    ),
    key: str = typer.Option('', help='Key under Components->Schema->{Key}. CASE SENSITIVE.'),
):
    if key:
        JSF.from_json_with_key(schema, key).to_json(instance)
    else:
        JSF.from_json(schema).to_json(instance)

if __name__ == '__main__':
    main()