from crewai import Crew,Process
from task import research_task,write_task
from agent import research,writer

## Forming the tech focused crew with some enhanced configuration
crew=Crew(
    agents=[research,writer],
    tasks=[research_task,write_task],
    process=Process.sequential,

)

## starting the task execution process wiht enhanced feedback

result=crew.kickoff(inputs={'topic':'AI in healthcare'})
print(result)