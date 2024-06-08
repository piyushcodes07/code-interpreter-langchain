from langchain_experimental.tools import PythonREPLTool
from langchain import hub
from langchain_openai import ChatOpenAI
from langchain.agents import create_react_agent
from dotenv import load_dotenv
from langchain.agents import AgentExecutor

load_dotenv()


def main():

    instructions = """
    always use the tool even if you know the answer.
    You must always use python code to answer.
    You are a agent that can write code. only answer 
    the question with writing code even if you know the answer.
    if you dont know the answer respond "i dont know the answer".
    """
    base_prompt = hub.pull("langchain-ai/react-agent-template")
    prompt = base_prompt.partial(instructions=instructions)
    print(prompt)

    tools = [PythonREPLTool()]
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    agent = create_react_agent(llm=llm, tools=tools, prompt=prompt)

    agent_executor = AgentExecutor(agent=agent,tools=tools,verbose=True)
    agent_executor.invoke(input={
        "input":"shutdown this pc in 2 minutes"
    })


if __name__ == "__main__":
    main()
