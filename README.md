# neuro-san-mcp-examples
This repository contains simple examples of MCP servers in various languages and connecting them with neuro-san.

All the example MCP servers are configured to serve at the `http://127.0.0.1:8000/mcp` URL and have the same tools (mostly). A sample neuro-san project is created in the `neuro-san-server` directory which is configured to use the MCP server being served at the above URL. It also contains a agent network which connects to the MCP server. A sample agent network call script is provided which is preconfigured with a call to invoke the BMI calculation tool of the MCP server.

> Please read the [full MCP Guide for Neuro-SAN](https://github.com/cognizant-ai-lab/neuro-san-studio/blob/main/docs/user_guide.md#mcp-servers) for more info.

Steps:

1. Start any **one** of the servers in the language you are interested in. (given below)
2. Test the connectivity to neuro-san via running 

```py
python neuro-san-server/run_basic_mcp_agent.py
```

# MCP Servers

You can verify whether your MCP server is running using

```bash
npx -y @modelcontextprotocol/inspector --cli http://127.0.0.1:8000/mcp --method tools/list
```

It should give you the list of tools like so:

```json
{
  "tools": [
    {
      "name": "getGreeting",
      "description": "Get a personalized greeting",
      "inputSchema": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name to greet"
          }
        },
        "required": [
          "name"
        ],
        "additionalProperties": false
      }
    }
  ]
}
```

The list of available example MCP servers are given below:


## Python

Located in directory: `/python`
Start using `python start_mcp_server.py`

## Java

Located in dictory : `/java`
Start using: `mvn spring-boot:run`