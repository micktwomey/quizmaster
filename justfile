slides := "example_quiz.yaml"

develop:
  watchfiles "quizmaster serve {{slides}}" .

serve:
  quizmaster serve {{slides}}
