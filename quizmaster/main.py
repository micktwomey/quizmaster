import asyncio
from pathlib import Path

import rich
import typer
import yaml

from quizmaster import questions
from quizmaster import server

app = typer.Typer()


def parse_file(filename: Path) -> questions.Quiz:
    with filename.open("r") as fp:
        raw = yaml.safe_load(fp)
    return questions.Quiz.model_validate(raw)


@app.command()
def parse(input: Path):
    quiz = parse_file(input)
    rich.print(quiz)


@app.command()
def serve(input: Path, host: str = "127.0.0.1", port: int = 5000):
    quiz = parse_file(input)
    asyncio.run(server.start(host=host, port=port, quiz=quiz))


if __name__ == "__main__":
    typer.run(app)
