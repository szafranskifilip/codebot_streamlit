from typing import Tuple, List
from enum import Enum

from langchain_openai import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings


class OpenaiConstants(Enum):
    GPT_35_TURBO = "gpt-3.5-turbo"

    def __str__(self) -> str:
        return self.value


def get_openai() -> Tuple[ChatOpenAI, OpenAIEmbeddings]:

    llm = ChatOpenAI(model_name=str(OpenaiConstants.GPT_35_TURBO))
    embeddings = OpenAIEmbeddings()

    return llm, embeddings
