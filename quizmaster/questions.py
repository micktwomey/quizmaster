from typing import Optional

from pydantic import BaseModel, HttpUrl


class Source(BaseModel):
    url: HttpUrl
    title: Optional[str] = None
    description: Optional[str] = None


class Answer(BaseModel):
    answer: str
    image: Optional[str] = None


class Question(BaseModel):
    question: str
    image: Optional[str] = None


class SingleChoiceQuestion(BaseModel):
    question: str | Question
    answer: str | Answer
    sources: Optional[list[str | Source]] = None


class MultipleChoiceQuestion(BaseModel):
    question: str | Question
    choices: list[str | Answer]
    sources: Optional[list[str | Source]] = None


class Round(BaseModel):
    title: str
    sub_title: Optional[str] = None
    questions: list[MultipleChoiceQuestion | SingleChoiceQuestion]


class Quiz(BaseModel):
    title: str
    sub_title: Optional[str] = None
    rounds: list[Round]
