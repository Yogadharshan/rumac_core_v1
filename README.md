# rumac-core

rumac-core is a research-oriented codebase that studies intelligence as a system property, not a model feature.

the agent learns from interaction with environments, not from datasets.
it predicts, acts, observes outcomes, updates beliefs, and gradually builds abstractions such as regions and objects.


the focus is on **structure**, not scale.

---

## core ideas

the system is built around a simple loop:

predict  
act  
observe  
update  

everything else emerges from this.

the agent:
- interacts with explicit environments
- predicts outcomes before acting
- updates beliefs from prediction errors
- plans under uncertainty
- transfers learned structure across worlds

---

## what this repo contains

- multiple environments with different dynamics
- a learning agent that is environment-agnostic
- explicit world models (actions, regions, objects)
- experience logging and metrics
- rule induction from interaction data
- confidence-aware planning

no pretrained models are used.
no large datasets are involved.

---

## what this repo is not

- not agi
- not a finished system
- not optimized for performance
- not built for production

this is a research notebook expressed in code.

---

## why this exists

most ai systems focus on:
- language polish
- scale
- benchmarks

this work focuses on:
- causality
- adaptation
- transfer
- abstraction

the goal is to understand what *must* exist before general intelligence is even possible.

---

## how to run

```bash
python main.py
```

## the environment can be switched via:

```bash
ENV_NAME = "world"   # or "world2"
```

## license
mit
