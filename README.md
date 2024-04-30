# FINAL_PROJ
FINAL_PROJ



1. To create sets: see generate_arrangements.py

2. To create a single passage of some kind (multi/single, disambiguate/ambiguous)
    uncomment the lines in the bottom of arrangements_generator/single_choice_generator.py, arrangements_generator/multi_choice_generator.py

3. Prompts can be found in `/prompts/prompts.json`:
    1. Prompts of type yes-no question are divided into 4 types. see json for futher clarification.
       Each prompt has: 
       1. it's prompt string (contating brackets {} to be formatted)
       2. mapping from (TRUE, FALSE, UNABLE_TO_DETERMINE) -> suitable output of the prompt at hand.

4. to enable initializing together.ai python client, enter environment variable TOGETHER_API_KEY

5. Drawing graph can be done using the arrangements generator's generate_passage routine with the *draw_graph* flag:
    `generator.generate_passage(graph, draw_graph=True)` . see image below for 


This will create:

![img.png](img.png)
