# Core Objective Functions

The Core Objective Functions (COF) are:

1. Reduce Suffering
2. Increase Prosperity
3. Increase Understanding

## Procedure

1. Generate training datasets
   - Format is `prompt` followed by `completion`
   - The `prompt` should be a context, scenario, or situation
   - The `completion` should be a solution or set of possible solutions (how to reduce suffering, increase prosperity, or increase understanding)
2. Finetune GPT-3 models with custom datasets

Previous work focused on several components:

1. Context
2. Proposed action
3. Evaluation
4. Explanation

Maybe I need to go back to that model... Given any context, generate some possible actions. Then, given a context and action, evaluate whether it will help and explain why or why not. Ugh, this is tedious. 
