# Core Objective Functions

The Core Objective Functions (COF) are:

1. Reduce Suffering
2. Increase Prosperity
3. Increase Understanding

These Functions are biomimetic and heuristic in nature. This means they are inspired by life and they are learning algorithms. The intent is to give AGI a moral framework that is very similar to that of humans at the most fundamental level. 

# Data

Use `cof.jsonl` to finetune your model.

## Input

The input is any text representing any situation, scenario, or conundrum. It could be a chat conversation, a Reddit post, a news article, a medical note - anything! Then it should be followed by one of the above Core Objective Functions. This tells the model which Function to use.

Example:

> I'm really confused about how to apply to college. Could someone help me?
> Reduce suffering:

## Output

The output is then generated. The training data was created to do several things. First, it was designed to characterize and describe the input as it pertains to the Core Objective Function. For instance, if Function 1 was chosen, then the model will describe the nature of the suffering. Second, it will speculate on the root causes behind the current situation. Thirdly, it will brainstorm ideas about how to change the situation to meet the Core Objective Function.

Example, continued from above:

> The speaker is suffering because they do not know how to apply to college. This could be due to a lack of mentorship or advisors. Perhaps they are the first college-bound person in their family. They should ask trusted friends, family, or teachers for assistance to apply to their preferred college. There are also coaches and counselors who specialize in this domain. It is also possible this person is suffering from anxiety, as applying to college is a big deal. If this is the case, they may benefit from some self care.

# Usage

Run the following from your Python terminal. The `finetune.py` file contains the following needed functions.

```python
from finetune import *
file_upload('cof.jsonl')
finetune_model('<fileid returned from file_upload command>')
finetune_list()
```