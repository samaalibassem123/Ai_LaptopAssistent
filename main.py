from langchain.agents import create_agent
# Import configuration 
from config import AGENT_CONFIG



# Create the agent
agent = create_agent(**AGENT_CONFIG)


#Run

while True:
    user_text = str(input("Ask Bob : "))
    if(user_text=="exit"):
        print("GoodBye !")
        break
    
    try:
        response = agent.invoke({
            "messages":[
                ("user", user_text )
            ]
        },
         {"configurable": {"thread_id": "1"}}
         )
        print('\n')
        print("Bob Response : ", response["structured_response"].response)
        print('\n')
    except Exception as e:
        print(e)
    



