project := "quizmaster"
slides := "example_quiz.yaml"

develop:
  watchfiles "quizmaster serve {{slides}}" .

serve:
  quizmaster serve {{slides}}

lint:
  ruff check
  ruff format --check
  mypy --strict {{project}}

fix:
  ruff check --fix
  ruff format

uv-sync:
  uv sync
