import os
import pprint

os.environ['AGENT_MANIFEST_FILE'] = os.path.join(os.path.dirname(__file__), 'registries', 'manifest.hocon')

from neuro_san.client.agent_session_factory import DirectAgentSessionFactory

def invoke_agent(agent_name: str, user_text: str, sly_data=None):
    """
    Invoke a neuro-san agent and return its response.
    
    Args:
        agent_name: Name of the agent to invoke (without .hocon extension)
        user_text: The message to send to the agent
        sly_data: Optional additional data to pass to the agent
    
    Returns:
        The final message from the agent containing the response
    """
    # Create the factory and session
    factory = DirectAgentSessionFactory()
    session = factory.create_session(
        agent_name=agent_name,
        use_direct=True,
        metadata={},
    )

    # Prepare the request
    request_payload = {
        "user_message": {
            "text": user_text,
        },
        "sly_data": sly_data,
    }

    # Stream the response and collect messages
    stream = session.streaming_chat(request_payload)
    msg = []
    for chat_msg in stream:
        msg.append(chat_msg)
        if chat_msg.get("done") is True:
            break
    
    # Return the last message (which contains the complete response)
    return msg[-1]

# Invoke the agent with a simple message
response = invoke_agent('basic_mcp_agent', 'Get me the BMI. Height is 1.75m and weight is 70kg.')

# pprint.pprint(response)
# Print just the text response
print(response['response']['text'])