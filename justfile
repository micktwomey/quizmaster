project := "quizmaster"
quiz := "example_quiz.yaml"

default: serve

summary quiz=quiz:
  quizmaster summary {{quiz}}

develop quiz=quiz:
  watchfiles "quizmaster serve {{quiz}}" .

serve quiz=quiz:
  quizmaster serve {{quiz}}

lint:
  ruff check
  ruff format --check
  mypy --strict {{project}}

fix:
  ruff check --fix
  ruff format

uv-sync:
  uv sync
