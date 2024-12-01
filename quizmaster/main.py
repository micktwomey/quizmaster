import asyncio
import asyncio.exceptions
from pathlib import Path
import signal

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
    srv = server.create_server(host=host, port=port, quiz=quiz)
    loop = asyncio.get_event_loop()

    # Try to exit a little more gracefully when run from watchfiles. Quietens
    # down one exception but there's still a asyncio.exceptions.CancelledError
    # from the lifespan loop. It's not important, but really bugs me :D. See
    # https://github.com/encode/uvicorn/issues/2173
    def signal_handler() -> None:
        srv.should_exit = True
    loop.add_signal_handler(signal.SIGINT, signal_handler)
    loop.add_signal_handler(signal.SIGTERM, signal_handler)

    asyncio.run(srv.serve())


if __name__ == "__main__":
    typer.run(app)
