import asyncio
import asyncio.exceptions
from pathlib import Path

import rich
import typer

from quizmaster import serialization, server

app = typer.Typer()


@app.command()
def parse(input: Path) -> None:
    quiz = serialization.parse_file(input)
    rich.print(quiz)


@app.command()
def serve(input: Path, host: str = "127.0.0.1", port: int = 5000) -> None:
    quiz = serialization.parse_file(input)
    asyncio.run(server.start(host=host, port=port, quiz=quiz))


if __name__ == "__main__":
    typer.run(app)
