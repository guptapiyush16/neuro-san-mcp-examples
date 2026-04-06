# Java MCP Weather Server

A Spring Boot-based [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) server that exposes tools for AI agents to consume.

## What it does

This server implements a stateless HTTP MCP server using Spring AI. It exposes three tools:

| Tool | Description |
|------|-------------|
| `getTemperature` | Fetches current temperature (°C) for a given latitude/longitude using the [Open-Meteo API](https://open-meteo.com/) |
| `calculateBmi` | Calculates BMI given weight (kg) and height (m) |
| `getGreeting` | Returns a personalized greeting for a given name |

The MCP endpoint is available at `POST /mcp`.

## Requirements

- Java 21+
- Maven (or use the included `mvnw` wrapper)

## How to start

```bash
cd java
mvn spring-boot:run
```

The server starts on **port 8000** by default.

To verify it is running:

```bash
curl http://localhost:8000/actuator/health
```

## Configuration

Key properties in [src/main/resources/application.properties](src/main/resources/application.properties):

| Property | Value | Description |
|----------|-------|-------------|
| `server.port` | `8000` | HTTP port |
| `spring.ai.mcp.server.protocol` | `STATELESS` | Stateless HTTP transport |
| `spring.ai.mcp.server.stateless.mcp-endpoint` | `/mcp` | MCP endpoint path |

## Using with neuro-san

Point your neuro-san agent network at this server by configuring an MCP connection to `http://localhost:8000/mcp`.
