```prompt
I want each agent within my multi-agent setup to log their individual token usage during interactions. How can I implement this functionality to monitor and print each agent's token usage after every interaction? Additionally, where in the existing code should this feature be integrated for optimal tracking and minimal performance impact? Please provide guidance on which methods or modules would be most appropriate to modify or extend to capture token usage data effectively.
```

```response
## Tracking Token Usage for Individual Agents in CrewAI

While the sources don't explicitly outline how to print the token usage of each agent individually, they do provide insights into how token usage is tracked and accessed within the CrewAI framework. Based on this information, we can devise a potential implementation strategy.

### 1. Accessing Total Crew Usage: The Foundation

The `Crew` class in CrewAI offers a `usage_metrics` attribute, which stores a summary of token usage across all tasks and agents.  You can access this data after the crew's execution using:

```python
crew = Crew(agents=[agent1, agent2], tasks=[task1, task2])
crew.kickoff()
print(crew.usage_metrics)
```

This provides the total token usage for the entire crew but doesn't break it down per agent.

### 2. Agent-Level Token Tracking:  `_token_process`

The sources suggest that token usage is tracked at the agent level using the `_token_process` attribute. This attribute is an instance of the `TokenProcess` class, which contains methods for summing prompt tokens, completion tokens, and successful requests. You can find this in:

- [Source 2: `TokenProcess` Class Definition]
- [Source 2: `calculate_usage_metrics` Method]

### 3. Proposed Implementation Strategy

To achieve your goal of printing each agent's token usage, you'd need to:

**a) Access the `_token_process` Attribute:** After the crew's execution, iterate through the `agents` list in the `Crew` object and access the `_token_process` attribute of each agent.

**b) Call the `get_summary()` Method:** Invoke the `get_summary()` method on the `_token_process` object to retrieve a `UsageMetrics` object containing the agent's token usage summary.

**c) Print the Summary:** Print the relevant information from the `UsageMetrics` object, such as `total_tokens`, `prompt_tokens`, and `completion_tokens`.

### 4. Example Code Snippet

```python
crew = Crew(agents=[agent1, agent2], tasks=[task1, task2])
crew.kickoff()

for agent in crew.agents:
  token_summary = agent._token_process.get_summary()
  print(f"Agent: {agent.role}")
  print(f"  Total Tokens: {token_summary.total_tokens}")
  print(f"  Prompt Tokens: {token_summary.prompt_tokens}")
  print(f"  Completion Tokens: {token_summary.completion_tokens}")
```

### 5. Important Considerations

- **Private Attribute:** The `_token_process` attribute is prefixed with an underscore, indicating that it's intended for internal use within the class. Accessing it directly might be considered a violation of encapsulation principles.  

    - **Potential Solution:** You could consider contributing to the CrewAI project by proposing a public method or property that exposes this information in a controlled manner.

- **Framework Updates:** Keep in mind that software frameworks evolve. The specific implementation details might change in future versions of CrewAI.

### 6.  Additional Insights from Sources

- The `calculate_usage_metrics` method in the `Crew` class ([Source 2]) demonstrates how to aggregate token usage data from multiple agents. This might be useful for understanding how token usage is accumulated at the crew level.

- The `TokenCalcHandler` class ([Source 2]) is used as a callback to track token usage during agent execution. This highlights how CrewAI integrates token tracking into its execution pipeline.

By combining the insights from the sources and the proposed implementation strategy, you should be able to enhance the CrewAI framework to provide more granular visibility into agent-level token usage, allowing for better resource monitoring and optimization. 
```