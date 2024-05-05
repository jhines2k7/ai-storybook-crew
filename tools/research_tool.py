from gpt_researcher import GPTResearcher
from langchain.tools import tool

import asyncio

class ResearchTool():
    @tool("Perform research for crew members when needed.")
    def perform_research(query):
        """Useful for conducting research when given a query and returns a report"""
        report_type = "research_report"

        print("Performing research on the query at hand...")

        async def _async_research():
            researcher = GPTResearcher(query, report_type)
            await researcher.conduct_research()
            report = await researcher.write_report()
            return report

        # Create a new event loop
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        # Run the coroutine using the event loop
        return loop.run_until_complete(_async_research())