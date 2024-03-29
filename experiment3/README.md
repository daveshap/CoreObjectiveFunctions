# Experiment 2 - COF as a Basic Cognitive Architecture

## Overview

Ongoing experiment to demonstrate Core Objective Functions in a cognitive architecture

## Proceedure

### Step 1 - Generate COF Ideas

The idea is to simplify the first step of the Core Objective Functions by simply generating lists of ideas to fit each COF. This initial step is unbound by the need to explicate, characterize, or describe the COF (which GPT-3 is capable of) because it's generally not necessary. 

### Step 2 - Integrate COF Ideas

Following the generation of COF ideas, they will be integrated with a subsequent prompt. This will be step 2 (integration). This should use information from all three COF in order to decide on an action. Obviously, this is merely generative, and does not rely on memory or recall. For the sake of simplicity, we will assume that recall has already happened by this point, and that all necessary information is present. This shows how all COF can be combined into a single action, or a set of possible actions, that should satisfy all three COF.

# Open Issues

## Clean up COF JSONL if it contains quotes

- If it contains quotes, then we should prepend the phrase with something like `'I would say "..."'`
- Or remove this alltogether. It shouldn't be recommending what to say verbatim. We can leave the rhetoric up to a future model
- Try finetuning with DAVINCI instead of CURIE. Curie may be the problem (it's not quite smart enough not to get stuck on repeat).

## Enhance the COF COMBINE prompt and function

- It doesn't quite understand the goal of condensing the functions down
- Test in playground.