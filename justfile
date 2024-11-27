slides := "example_quiz.yaml"

develop: uv-sync
  watchfiles "quizmaster serve {{slides}}" .

serve: uv-sync
  quizmaster serve {{slides}}

lint: uv-sync
  ruff check
  ruff format --check

fix: uv-sync
  ruff check --fix
  ruff format

uv-sync:
  uv sync
