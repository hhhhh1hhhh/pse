#게시글 posting 모델#
from pydantic import BaseModel


class CreatePosting(BaseModel):
    name: str
    id: str
    date: str
    contents: str
    title: str

    #collection = postings#