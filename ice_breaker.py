from typing import Tuple
from dotenv import load_dotenv
import os
from langchain.prompts.prompt import PromptTemplate
from langchain_community.chat_models import ChatOpenAI
from third_parties.linkedin import scrape_linkedin_profile
from output_parsers import summary, summary_parser
from agents.linkedin_lookup_agent import lookup as linked_lookup_agent


def ice_break_with(name: str) -> Tuple[summary, str]:
    linkedin_username = linked_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile(
        linkedin_profile_url=linkedin_username
    )

    summary_template = """
Given the LinkedIN information: {information}    

Based only on the provided data, do the following:
1. Write a short professional summary of the person.
2. Mention two interesting facts about them.
3. Suggest:
   - Two **casual** icebreaker questions (fun and easy to say in an informal setting).
   - Two **formal** icebreaker questions (professional and respectful).
   - Two **funny** or lighthearted icebreaker questions (playful but not inappropriate).

Make sure to stick strictly to the provided information and do not make assumptions.

{format_instructions}
  
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
        partial_variables={"format_instructions": summary_parser.get_format_instructions()}
    )

    llm = ChatOpenAI(
        temperature=0,
        model_name="gpt-4o-mini",
        api_key=os.getenv("OPENAI_API_KEY"),
        base_url=os.getenv("OPENAI_API_BAS"),
        default_headers={
            "HTTP-Referer": "http://localhost",
            "X-Title": "linkedin-summary"
        }
    )

    chain = summary_prompt_template | llm | summary_parser
    res: summary = chain.invoke(input={"information": linkedin_data})

    return res, linkedin_data.get('photoUrl')


if __name__ == "__main__":
    load_dotenv()

    print("Hello LangChain")

    res, pic_url = ice_break_with(name="williamhgates")

    print("Summary for this guys is          :", res.summary)
    print("Facts about this guy is           :", res.faxxx)
    print("Profile picture URL               :", pic_url)

    print("hey")
