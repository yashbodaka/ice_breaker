from typing import List, Dict, Any
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

class summary(BaseModel):
    summary: str = Field(description="summary")
    faxxx: List[str] = Field(description="interesting facts about them")
    casual_icebreakers: List[str] = Field(description="light-hearted and informal conversation starters")
    formal_icebreakers: List[str] = Field(description="professional and respectful conversation starters")
    funny_icebreakers: List[str] = Field(description="humorous or witty conversation starters")

    def to_dict(self) -> Dict[str, Any]:
        return {
            "summary": self.summary,
            "faxxx": self.faxxx,
            "casual_icebreakers": self.casual_icebreakers,
            "formal_icebreakers": self.formal_icebreakers,
            "funny_icebreakers": self.funny_icebreakers,
        }

summary_parser = PydanticOutputParser(pydantic_object=summary)
