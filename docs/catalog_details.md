# Catalog Details & Evidence

[← Catalog](../README.md)

Each resource retains its own release boundary. Companion links are not counted as separate projects.

## VERA — paper-vera

**[VERA: Scaling Verifiable Environments for Agentic co-Evolution](https://arxiv.org/abs/2610.05923)**

`paper` · `vera` · 2026-10-05 · RL and harness learning

Builds resumable sandboxes from trajectories, filters them with checks, and alternates policy training with harness-skill updates.

**Feedback / validation：** Rubric rewards, executable checks and development-set acceptance gates.

**Release boundary：** Very recent preprint; the reviewed abstract and full text do not expose a confirmed official repository.

**Implementation status：** Not confirmed

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2610.05923) · 2026-10-08 · “Competent agents need precise and verifiable environments, such as sandboxes that are resumable at any stage”

## Skill2Env — paper-skill2env

**[Skill2Env: Capability-Oriented Environment Synthesis from Skills for General Agents](https://arxiv.org/abs/2609.33772)**

`paper` · `skill2env` · 2026-09-27 · SFT / trajectory training

Converts skills into capability-oriented task blueprints, executable workspaces and rubric evaluators; hardens tasks using solver traces.

**Feedback / validation：** Rubric evaluators and solver evidence for task hardening.

**Release boundary：** SFT evidence. The current research homepage provides example tasks and a model link; a complete synthesis and training pipeline is not established by those samples.

**Implementation status：** Partial / associated code

[Home](https://github.com/AllSpark-Research/AgentEnv) · [Partial / associated code](https://github.com/AllSpark-Research/AgentEnv) · [Example tasks](https://github.com/AllSpark-Research/AgentEnv/tree/main/Skill2Env) · [Model](https://huggingface.co/AllSpark-Research/Skill2Env)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2609.33772) · 2026-10-08 · “Executable environments are critical for post-training agents on tasks that require tool use and multi-step interaction,”
- [primary-source-content](https://arxiv.org/html/2609.33772v2) · 2026-10-08 · “Skill2Env”
- [primary-source-content](https://github.com/AllSpark-Research/AgentEnv) · 2026-10-08 · “Research homepage for environment and data synthesis for general agents.”

## AutoGym — paper-autogym

**[AutoGym: Blueprint-First Generation of Verifiable Agent Gyms](https://arxiv.org/abs/2609.22592)**

`paper` · `autogym` · 2026-09-18 · Environment / task generation

Specifies solution space and verification before materializing gyms, then calibrates generation parameters to learner performance.

**Feedback / validation：** Generated task verifiers plus construction or solvability validation.

**Release boundary：** Demonstrates generated-gym difficulty; do not infer a released end-to-end RL stack or sustained training gains.

**Implementation status：** Not confirmed

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2609.22592) · 2026-10-08 · “Training agents with reinforcement learning requires a gym, comprising a task, an executable environment in which”

## EnvHarness — paper-envharness

**[EnvHarness: Awakening Static Worlds for Agent Learning](https://arxiv.org/abs/2608.19880)**

`paper` · `envharness` · 2026-08-20 · RL and harness learning

Wraps fixed environments with programmable setup, interaction and composition layers, adapting practice while retaining original verifiers.

**Feedback / validation：** Original environment verifiers plus held-out task evaluation.

**Release boundary：** Transfers are measured on selected benchmarks; retaining a verifier does not prove every generated wrapper preserves task semantics.

**Implementation status：** Code

[Code](https://github.com/google-research/envharness)

Same work: [EnvHarness (project)](#envharness--project-envharness)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2608.19880) · 2026-10-08 · “LLM agents learn by interacting with environments, yet these environments are hand-built and static: blind to”

## SPADE — paper-spade

**[SPADE: Self-Play in Adaptive Synthetic Executable Environments](https://arxiv.org/abs/2608.19197)**

`paper` · `spade` · 2026-08-19 · RL experiments

Co-trains one policy as environment designer and solver; executable reset/step worlds are selected using hint-based regret.

**Feedback / validation：** Executable environment rewards and a hint-based regret signal for the designer.

**Release boundary：** Grounding corpora, memory and feasibility controls remain necessary; experiments do not establish unbounded improvement.

**Implementation status：** Code

[Code](https://github.com/spade-rl/spade)

Same work: [SPADE (project)](#spade--project-spade)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2608.19197) · 2026-10-08 · “Continuous self-improvement requires an ever-expanding pool of self-generated, diverse, adaptive goals. For language agents, existing training”

## Envs-FORGE — paper-envs-forge

**[Envs-FORGE: Frontier-Optimized Reward-Grounded Environment Synthesis for Agent RL](https://arxiv.org/abs/2608.14312)**

`paper` · `envs-forge` · 2026-08-14 · RL experiments

Uses verifier pass rates to choose per-seed synthesis actions and jointly rewrite tasks, fixtures, tests and Docker environments.

**Feedback / validation：** Task success feeds difficulty adaptation; see method-specific verification details.

**Release boundary：** The linked repository is a broader toolkit; a complete paper-specific reproduction path was not established in its root README.

**Implementation status：** Partial / associated code

[Partial / associated code](https://github.com/DataArcTech/DataArc-SynData-Toolkit)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2608.14312) · 2026-10-08 · “Reinforcement learning (RL) for terminal agents needs executable training environments with reliable rewards and useful difficulty.”

## Beyond Simply Environment Scaling — paper-beyond-mm-scaling

**[Beyond Simply Environment Scaling: Designing Effective Environment Distributions for Multimodal Agent Learning](https://arxiv.org/abs/2608.03571)**

`paper` · `beyond-mm-scaling` · 2026-08-04 · RL experiments

Studies environment distributions through ability-aware selection and a hierarchy of interaction difficulty and state size.

**Feedback / validation：** Task success feeds difficulty adaptation; see method-specific verification details.

**Release boundary：** Environment count alone is not the treatment; benefits depend on the evaluated diversity and difficulty settings.

**Implementation status：** Code

[Code](https://github.com/GaryStack/Beyond-MMEnv-Scaling)

Same work: [Beyond Simply Environment Scaling (project)](#beyond-simply-environment-scaling--project-beyond-mm-scaling)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2608.03571) · 2026-10-08 · “Recent works train agents by constructing large-scale multimodal environment pools. However, we find that simply increasing”

## EvoEnv — paper-evoenv

**[Learning to Build the Environment: Self-Evolving Reasoning RL via Verifiable Environment Synthesis](https://arxiv.org/abs/2605.14392)**

`paper` · `evoenv` · 2026-05-14 · RL experiments

Synthesizes reusable Python generators and verifiers, exploiting solve–verify asymmetry to sustain reasoning training signals.

**Feedback / validation：** Generated executable oracles with staged admission checks.

**Release boundary：** A work-in-progress technical report; verifiable reasoning generators do not automatically constitute real multi-tool workflows.

**Implementation status：** Not confirmed

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2605.14392) · 2026-10-08 · “We pursue a vision for self-improving language models in which the model does not merely generate”

## RLVE — paper-rlve

**[RLVE: Scaling Up Reinforcement Learning for Language Models with Adaptive Verifiable Environments](https://arxiv.org/abs/2511.07317)**

`paper` · `rlve` · 2025-11-10 · RL experiments

Adapts procedural task difficulty to the current policy across a manually engineered suite of verifiable reasoning environments.

**Feedback / validation：** Algorithmic answer verification and adaptive solve-rate calibration.

**Release boundary：** Environment engineering is still manual; procedural reasoning results should not be extrapolated to GUI or enterprise workflows.

**Implementation status：** Code

[Code](https://github.com/Zhiyuan-Zeng/RLVE)

Same work: [RLVE (project)](#rlve--project-rlve)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2511.07317) · 2026-10-08 · “We introduce Reinforcement Learning (RL) with Adaptive Verifiable Environments (RLVE), an approach using verifiable environments that”

## Environment Tuning — paper-env-tuning

**[Don't Just Fine-tune the Agent, Tune the Environment](https://arxiv.org/abs/2510.10197)**

`paper` · `env-tuning` · 2025-10-11 · RL experiments

Combines a task curriculum, corrective environment feedback and progress rewards to stabilize sparse-data tool-use learning.

**Feedback / validation：** Task success feeds difficulty adaptation; see method-specific verification details.

**Release boundary：** Augmented feedback is part of training; deployment must be evaluated without assuming the same privileged help.

**Implementation status：** Code

[Code](https://github.com/inclusionAI/AWorld-RL)

Same work: [Environment Tuning (project)](#environment-tuning--project-env-tuning)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2510.10197) · 2026-10-08 · “Large Language Model (LLM) agents show great promise for complex, multi-turn tool-use tasks, but their development”

## EnvFactory — paper-envfactory

**[EnvFactory: Scaling Tool-Use Agents via Executable Environments Synthesis and Robust RL](https://arxiv.org/abs/2605.18703)**

`paper` · `envfactory` · 2026-05-18 · RL and SFT experiments

Builds and verifies stateful tools from real resources, then synthesizes trajectories using tool topology and calibrated query refinement.

**Feedback / validation：** Generated task verifiers plus construction or solvability validation.

**Release boundary：** Executable correctness and natural task intent require separate checks; the release includes framework-specific training dependencies.

**Implementation status：** Code

[Code](https://github.com/LARK-AI-Lab/EnvFactory)

Same work: [EnvFactory (project)](#envfactory--project-envfactory)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2605.18703) · 2026-10-08 · “Equipping LLMs with tool-use capabilities via Agentic Reinforcement Learning (Agentic RL) is bottlenecked by two challenges:”

## Agent-World — paper-agent-world

**[Agent-World: Scaling Real-World Environment Synthesis for Evolving General Agent Intelligence](https://arxiv.org/abs/2604.18292)**

`paper` · `agent-world` · 2026-04-20 · RL and SFT experiments

Discovers stateful tool ecosystems and generates verifiable tasks, linking multi-environment learning to capability-gap-driven task evolution.

**Feedback / validation：** Generated task verifiers plus construction or solvability validation.

**Release boundary：** The public repository releases a selected environment subset and requires RL adaptation; it is not the entire paper corpus.

**Implementation status：** Partial / associated code

[Partial / associated code](https://github.com/RUC-NLPIR/Agent-World)

Same work: [Agent-World (project)](#agent-world--project-agent-world)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2604.18292) · 2026-10-08 · “Large language models are increasingly expected to serve as general-purpose agents that interact with external, stateful”

## Agent World Model — paper-awm

**[Agent World Model: Infinity Synthetic Environments for Agentic Reinforcement Learning](https://arxiv.org/abs/2602.10090)**

`paper` · `awm` · 2026-02-10 · RL experiments

Synthesizes code-driven, SQL-backed tool worlds with inspectable state and rewards for multi-turn RL and transfer studies.

**Feedback / validation：** Database-state-aware task verification.

**Release boundary：** Synthetic database consistency does not establish fidelity to every real service or production failure mode.

**Implementation status：** Code

[Code](https://github.com/Snowflake-Labs/agent-world-model)

Same work: [Agent World Model: Infinity Synthetic Environments for Agentic Reinforcement Learning (blog)](#agent-world-model-infinity-synthetic-environments-for-agentic-reinforcement-learning--blog-awm-blog) · [Agent World Model (project)](#agent-world-model--project-awm)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2602.10090) · 2026-10-08 · “Recent advances in large language model (LLM) have empowered autonomous agents to perform multi-turn interactions with”

## ScaleEnv — paper-scaleenv

**[ScaleEnv: Scaling Environment Synthesis from Scratch for Generalist Interactive Tool-Use Agent Training](https://arxiv.org/abs/2602.06820)**

`paper` · `scaleenv` · 2026-02-06 · RL experiments

Constructs interactive tool environments from scratch, testing implementations and validating solvable tasks through executable action sequences.

**Feedback / validation：** Generated task verifiers plus construction or solvability validation.

**Release boundary：** Distinct from Scale AI AgentEnv; no confirmed official code link was found in the reviewed paper and targeted search.

**Implementation status：** Not confirmed

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2602.06820) · 2026-10-08 · “Training generalist agents capable of adapting to diverse scenarios requires interactive environments for self-exploration. However, interactive”

## EnvScaler — paper-envscaler

**[EnvScaler: Scaling Tool-Interactive Environments for LLM Agent via Programmatic Synthesis](https://arxiv.org/abs/2601.05808)**

`paper` · `envscaler` · 2026-01-09 · RL and SFT experiments

Separates environment skeleton construction from scenario generation and rule-based trajectory validation.

**Feedback / validation：** Rule-based trajectory and final-state checks.

**Release boundary：** Rule coverage and environment realism must be assessed independently; released RL integration uses ROLL and GEM.

**Implementation status：** Code

[Code](https://github.com/RUC-NLPIR/EnvScaler)

Same work: [EnvScaler (project)](#envscaler--project-envscaler)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2601.05808) · 2026-10-08 · “Large language models (LLMs) are expected to be trained to act as agents in various real-world”

## AutoForge — paper-autoforge

**[AutoForge: Automated Environment Synthesis for Agentic Reinforcement Learning](https://arxiv.org/abs/2512.22857)**

`paper` · `autoforge` · 2025-12-28 · RL experiments

Organizes synthetic state structures and tool dependencies before generating tool-use environments for agent RL.

**Feedback / validation：** Generated task verifiers plus construction or solvability validation.

**Release boundary：** Many unrelated repositories share the name; no unverified AutoForge repository is treated as official code.

**Implementation status：** Not confirmed

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2512.22857) · 2026-10-08 · “Conducting reinforcement learning (RL) in simulated environments offers a cost-effective and highly scalable way to enhance”

## AutoEnv — paper-autoenv

**[AutoEnv: Automated Environments for Measuring Cross-Environment Agent Learning](https://arxiv.org/abs/2511.19304)**

`paper` · `autoenv` · 2025-11-24 · Environment / task generation

Factorizes transition, observation and reward distributions to generate heterogeneous worlds for cross-environment learning studies.

**Feedback / validation：** Generated task verifiers plus construction or solvability validation.

**Release boundary：** Generated levels measure transfer under designed distributions, not unrestricted real-world generalization.

**Implementation status：** Code

[Code](https://github.com/FoundationAgents/AutoEnv)

Same work: [AutoEnv (project)](#autoenv--project-autoenv)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2511.19304) · 2026-10-08 · “Humans naturally adapt to diverse environments by learning underlying rules across worlds with different dynamics, observations,”

## EnvACE — paper-envace

**[EnvACE: Internalizing Environment Dynamics via World Rehearsal for Agentic Reinforcement Learning](https://arxiv.org/abs/2608.06197)**

`paper` · `envace` · 2026-08-06 · RL experiments

Trains a shared policy to act and rehearse environment responses, internalizing dynamics through role-wise RL.

**Feedback / validation：** Simulated observations or task-success rewards; real-environment transfer is evaluated separately.

**Release boundary：** Rehearsed observations are model outputs; simulated consistency needs checking against external execution.

**Implementation status：** Code

[Code](https://github.com/Within-yao/EnvACE)

Same work: [EnvACE (project)](#envace--project-envace)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2608.06197) · 2026-10-08 · “Training large language model agents for long-horizon tool use typically relies on interactions with real or”

## WebWorld — paper-webworld

**[WebWorld: A Large-Scale World Model for Web Agent Training](https://arxiv.org/abs/2602.14721)**

`paper` · `webworld` · 2026-02-16 · SFT / trajectory training

Learns an open-web simulator from interaction trajectories and uses simulated rollouts for web-agent training and planning.

**Feedback / validation：** Simulated observations or task-success rewards; real-environment transfer is evaluated separately.

**Release boundary：** Simulation quality and real-browser transfer are separate measurements; distinct from later same-name web-code papers.

**Implementation status：** Code

[Code](https://github.com/QwenLM/WebWorld)

Same work: [WebWorld (project)](#webworld--project-webworld)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2602.14721) · 2026-10-08 · “Web agents require massive trajectories to generalize, yet real-world training is constrained by network latency, rate”

## GenEnv — paper-genenv

**[GenEnv: Difficulty-Aligned Co-Evolution Between LLM Agents and Environment Simulators](https://arxiv.org/abs/2512.19682)**

`paper` · `genenv` · 2025-12-22 · RL experiments

Co-evolves a generative simulator and agent using a difficulty-aligned curriculum reward.

**Feedback / validation：** Simulated observations or task-success rewards; real-environment transfer is evaluated separately.

**Release boundary：** Learned simulation can drift from executable reality; reported gains concern the paper's selected tasks.

**Implementation status：** Code

[Code](https://github.com/Gen-Verse/GenEnv)

Same work: [GenEnv (project)](#genenv--project-genenv)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2512.19682) · 2026-10-08 · “Training capable Large Language Model (LLM) agents is critically bottlenecked by the high cost and static”

## SynthTools — paper-synthtools

**[SynthTools: A Framework for Scaling Synthetic Tools for Agent Development](https://arxiv.org/abs/2511.09572)**

`paper` · `synthtools` · 2025-11-11 · Environment / task generation

Separates synthetic tool generation, response simulation and tool auditing to scale controllable tool ecosystems.

**Feedback / validation：** LLM-simulated tool observations with a separate audit stage.

**Release boundary：** Tool responses are simulated by LLMs; audit accuracy is not a proof of deterministic state transitions.

**Implementation status：** Code

[Code](https://github.com/namkoong-lab/SynthTools)

Same work: [SynthTools (project)](#synthtools--project-synthtools)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2511.09572) · 2026-10-08 · “For agentic systems to use external tools to solve complex, long-horizon tasks, we need a large”

## DreamGym — paper-dreamgym

**[Scaling Agent Learning via Experience Synthesis](https://arxiv.org/abs/2511.03773)**

`paper` · `dreamgym` · 2025-11-05 · RL experiments

Uses a reasoning-based experience model, replay buffer and adaptive task generation to train agents with synthetic interactions.

**Feedback / validation：** Simulated observations or task-success rewards; real-environment transfer is evaluated separately.

**Release boundary：** Sim-to-real transfer is empirical; a third-party reproduction is not official author code.

**Implementation status：** Not confirmed

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2511.03773) · 2026-10-08 · “While reinforcement learning (RL) can empower autonomous agents by enabling self-improvement through interaction, its practical adoption”

## daVinci-Env / OpenSWE — paper-openswe

**[daVinci-Env: Open SWE Environment Synthesis at Scale](https://arxiv.org/abs/2603.13023)**

`paper` · `openswe` · 2026-03-13 · SFT / trajectory training

Automates repository exploration, Docker setup and test generation, then filters environments by solvability and useful difficulty.

**Feedback / validation：** Task-specific execution tests or verifier scores; consult the resource for the exact split.

**Release boundary：** The title says daVinci-Env while the released framework is OpenSWE; construction and rollout costs are substantial.

**Implementation status：** Code

[Code](https://github.com/GAIR-NLP/OpenSWE)

Same work: [daVinci-Env / OpenSWE (project)](#davinci-env--openswe--project-openswe)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2603.13023) · 2026-10-08 · “Training capable software engineering (SWE) agents demands large-scale, executable, and verifiable environments that provide dynamic feedback”

## SWE-rebench V2 — paper-swe-rebench

**[SWE-rebench V2: Language-Agnostic SWE Task Collection at Scale](https://arxiv.org/abs/2602.23866)**

`paper` · `swe-rebench` · 2026-02-27 · Environment / task generation

Harvests multilingual repository tasks and generates installation and test procedures to build reproducible training environments.

**Feedback / validation：** Task-specific execution tests or verifier scores; consult the resource for the exact split.

**Release boundary：** Fully built environments and additional task metadata have different release scope; tests can be underspecified or restrictive.

**Implementation status：** Code

[Code](https://github.com/SWE-rebench/SWE-rebench-V2)

Same work: [SWE-rebench V2 (project)](#swe-rebench-v2--project-swe-rebench)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2602.23866) · 2026-10-08 · “Software engineering agents (SWE) are improving rapidly, with recent gains largely driven by reinforcement learning (RL).”

## SWE-smith — paper-swe-smith

**[SWE-smith: Scaling Data for Software Engineering Agents](https://arxiv.org/abs/2504.21798)**

`paper` · `swe-smith` · 2025-04-30 · SFT / trajectory training

Turns repositories into execution environments and creates repair tasks by deliberately breaking existing tests.

**Feedback / validation：** Task-specific execution tests or verifier scores; consult the resource for the exact split.

**Release boundary：** Mutation-generated failures differ from naturally reported bugs; separate repository splits and hidden tests remain important.

**Implementation status：** Code

[Code](https://github.com/SWE-bench/SWE-smith)

Same work: [SWE-smith (project)](#swe-smith--project-swe-smith)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2504.21798) · 2026-10-08 · “Despite recent progress in Language Models (LMs) for software engineering, collecting training data remains a significant”

## R2E-Gym — paper-r2e-gym

**[R2E-Gym: Procedural Environments and Hybrid Verifiers for Scaling Open-Weights SWE Agents](https://arxiv.org/abs/2504.07164)**

`paper` · `r2e-gym` · 2025-04-09 · SFT / trajectory training

Procedurally curates executable software tasks from commits and studies complementary execution-based and learned verifiers.

**Feedback / validation：** Task-specific execution tests or verifier scores; consult the resource for the exact split.

**Release boundary：** The paper's early abstract uses AgentGym terminology; this is a separate project from WooooDyy/AgentGym.

**Implementation status：** Code

[Code](https://github.com/R2E-Gym/R2E-Gym)

Same work: [R2E-Gym (project)](#r2e-gym--project-r2e-gym)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2504.07164) · 2026-10-08 · “Improving open-source models on real-world SWE tasks (solving GITHUB issues) faces two key challenges: 1) scalable”

## SWE-Gym — paper-swe-gym

**[Training Software Engineering Agents and Verifiers with SWE-Gym](https://arxiv.org/abs/2412.21139)**

`paper` · `swe-gym` · 2024-12-30 · SFT / trajectory training

Pairs repository issues with runnable environments and unit tests, enabling agent fine-tuning and verifier training.

**Feedback / validation：** Task-specific execution tests or verifier scores; consult the resource for the exact split.

**Release boundary：** The initial corpus centers on Python; environment executability does not imply broad language coverage.

**Implementation status：** Code

[Code](https://github.com/SWE-Gym/SWE-Gym)

Same work: [SWE-Gym (project)](#swe-gym--project-swe-gym)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2412.21139) · 2026-10-08 · “We present SWE-Gym, the first environment for training real-world software engineering (SWE) agents. SWE-Gym contains 2,438”

## Terminal-Bench — paper-terminal-bench

**[Terminal-Bench: Benchmarking Agents on Hard, Realistic Tasks in Command Line Interfaces](https://arxiv.org/abs/2601.11868)**

`paper` · `terminal-bench` · 2026-01-17 · Evaluation substrate

Packages realistic terminal tasks with isolated execution environments, reference solutions and outcome tests.

**Feedback / validation：** Task-specific execution tests or verifier scores; consult the resource for the exact split.

**Release boundary：** This paper describes Terminal-Bench 2.0; evaluation tasks must remain held out from training.

**Implementation status：** Code

[Code](https://github.com/harbor-framework/terminal-bench)

Same work: [Terminal-Bench (project)](#terminal-bench--project-terminal-bench)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2601.11868) · 2026-10-08 · “AI agents may soon become capable of autonomously completing valuable, long-horizon tasks in diverse domains. Current”

## Gym-Anything / CUA-World — paper-gym-anything

**[Gym-Anything: Turn any Software into an Agent Environment](https://arxiv.org/abs/2604.06126)**

`paper` · `gym-anything` · 2026-04-07 · SFT / trajectory training

Automates software installation and realistic task setup with a separate auditing agent, releasing a cross-software CUA corpus.

**Feedback / validation：** State, artifact or rubric evaluation after interaction; evaluator type varies by task.

**Release boundary：** VMs, application dependencies and rubric judging add operational cost; setup evidence is not perfect task verification.

**Implementation status：** Code

[Code](https://github.com/cmu-l3/gym-anything)

Same work: [Gym-Anything / CUA-World (project)](#gym-anything--cua-world--project-gym-anything)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2604.06126) · 2026-10-08 · “Computer-use agents hold the promise of assisting in a wide range of digital economic activities. However,”

## InfiniteWeb — paper-infiniteweb

**[InfiniteWeb: Scalable Web Environment Synthesis for GUI Agent Training](https://arxiv.org/abs/2601.04126)**

`paper` · `infiniteweb` · 2026-01-07 · RL experiments

Generates multi-page functional websites with task-centered tests and verifiable evaluators for GUI-agent RL.

**Feedback / validation：** State, artifact or rubric evaluation after interaction; evaluator type varies by task.

**Release boundary：** Generated websites need functional and visual realism checks; availability of the full artifact release is separate.

**Implementation status：** Not confirmed

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2601.04126) · 2026-10-08 · “GUI agents that interact with graphical interfaces on behalf of users represent a promising direction for”

## AgentSynth — paper-agentsynth

**[AgentSynth: Scalable Task Generation for Generalist Computer-Use Agents](https://arxiv.org/abs/2506.14205)**

`paper` · `agentsynth` · 2025-06-17 · Environment / task generation

Composes executed subtasks into harder long-horizon computer tasks and trajectory datasets.

**Feedback / validation：** State, artifact or rubric evaluation after interaction; evaluator type varies by task.

**Release boundary：** Primarily task and trajectory synthesis on existing environments, rather than a new general runtime.

**Implementation status：** Code

[Code](https://github.com/sunblaze-ucb/AgentSynth)

Same work: [AgentSynth (project)](#agentsynth--project-agentsynth)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2506.14205) · 2026-10-08 · “We introduce AgentSynth, a scalable and cost-efficient pipeline for automatically synthesizing high-quality tasks and trajectory datasets”

## BrowserGym — paper-browsergym

**[The BrowserGym Ecosystem for Web Agent Research](https://arxiv.org/abs/2412.05467)**

`paper` · `browsergym` · 2024-12-06 · Evaluation substrate

Unifies browser observations, actions and benchmark interfaces; AgentLab adds experiment management.

**Feedback / validation：** State, artifact or rubric evaluation after interaction; evaluator type varies by task.

**Release boundary：** A common interface does not make every included benchmark an approved training split.

**Implementation status：** Code

[Code](https://github.com/ServiceNow/BrowserGym)

Same work: [BrowserGym (project)](#browsergym--project-browsergym)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2412.05467) · 2026-10-08 · “The BrowserGym ecosystem addresses the growing need for efficient evaluation and benchmarking of web agents, particularly”

## AndroidWorld — paper-androidworld

**[AndroidWorld: A Dynamic Benchmarking Environment for Autonomous Agents](https://arxiv.org/abs/2405.14573)**

`paper` · `androidworld` · 2024-05-23 · Evaluation substrate

Builds parameterized Android tasks with emulator setup and programmatic state-based success checks.

**Feedback / validation：** State, artifact or rubric evaluation after interaction; evaluator type varies by task.

**Release boundary：** App versions and emulator configuration affect reproducibility; benchmark success is not a demonstrated training result.

**Implementation status：** Code

[Code](https://github.com/google-research/android_world)

Same work: [AndroidWorld (project)](#androidworld--project-androidworld)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2405.14573) · 2026-10-08 · “Autonomous agents that execute human tasks by controlling computers can enhance human productivity and application accessibility.”

## OSWorld — paper-osworld

**[OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](https://arxiv.org/abs/2404.07972)**

`paper` · `osworld` · 2024-04-11 · Evaluation substrate

Provides real desktop task initialization and execution-based evaluators across applications.

**Feedback / validation：** State, artifact or rubric evaluation after interaction; evaluator type varies by task.

**Release boundary：** GUI execution is expensive and platform-sensitive; the benchmark split should not become RL practice data.

**Implementation status：** Code

[Code](https://github.com/xlang-ai/OSWorld)

Same work: [OSWorld (project)](#osworld--project-osworld)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2404.07972) · 2026-10-08 · “Autonomous agents that accomplish complex computer tasks with minimal human interventions have the potential to transform”

## WorkArena — paper-workarena

**[WorkArena: How Capable Are Web Agents at Solving Common Knowledge Work Tasks?](https://arxiv.org/abs/2403.07718)**

`paper` · `workarena` · 2024-03-12 · Evaluation substrate

Uses ServiceNow workflows as browser tasks with programmatic validation of enterprise actions.

**Feedback / validation：** Task state, trajectory milestones or rubric-based evaluation.

**Release boundary：** Requires suitable ServiceNow instances and credentials; this is not a self-contained offline app simulator.

**Implementation status：** Code

[Code](https://github.com/ServiceNow/WorkArena)

Same work: [WorkArena (project)](#workarena--project-workarena)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2403.07718) · 2026-10-08 · “We study the use of large language model-based agents for interacting with software via web browsers.”

## WebArena — paper-webarena

**[WebArena: A Realistic Web Environment for Building Autonomous Agents](https://arxiv.org/abs/2307.13854)**

`paper` · `webarena` · 2023-07-25 · Evaluation substrate

Hosts reproducible websites and checks task outcomes to evaluate realistic multi-step web actions.

**Feedback / validation：** State, artifact or rubric evaluation after interaction; evaluator type varies by task.

**Release boundary：** Resetting sites and maintaining deployment images are necessary; published test tasks need contamination controls.

**Implementation status：** Code

[Code](https://github.com/web-arena-x/webarena)

Same work: [WebArena (project)](#webarena--project-webarena)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2307.13854) · 2026-10-08 · “With advances in generative AI, there is now potential for autonomous agents to manage daily tasks”

## MM-ToolSandBox — paper-mm-toolsandbox

**[MM-ToolSandBox: A Unified Framework for Evaluating Visual Tool-Calling Agents](https://arxiv.org/abs/2607.11818)**

`paper` · `mm-toolsandbox` · 2026-07-13 · Evaluation substrate

Extends stateful tool evaluation to visual inputs, scenario generation and multi-turn state changes.

**Feedback / validation：** Task state, trajectory milestones or rubric-based evaluation.

**Release boundary：** A visual tool-call benchmark, not proof of an RL-trained agent; image extraction errors require separate analysis.

**Implementation status：** Code

[Code](https://github.com/apple-aiml-research/ml-mmtoolsandbox)

Same work: [MM-ToolSandBox (project)](#mm-toolsandbox--project-mm-toolsandbox)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2607.11818) · 2026-10-08 · “We introduce MM-ToolSandBox, a benchmark and evaluation framework for visually grounded tool-calling agents. The framework provides”

## C-World (formerly ToolGym) — paper-c-world

**[C-World: A Computer Use Agent Environment Creator](https://arxiv.org/abs/2601.06328)**

`paper` · `c-world` · 2026-01-09 · SFT / trajectory training

Creates computer-use tool environments with task generation, perturbable transitions, and executable or simulated tool responses.

**Feedback / validation：** Task state, trajectory milestones or rubric-based evaluation.

**Release boundary：** The current paper is named C-World while the project page and README retain ToolGym; distinguish live APIs from simulation and account for model-based judging.

**Implementation status：** Code

[Code](https://github.com/Ziqiao-git/C-World)

Same work: [C-World (formerly ToolGym) (project)](#c-world-formerly-toolgym--project-c-world)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2601.06328) · 2026-10-08 · “To close the gap between LLM-based agents and humans in planning and reasoning, agents need large-scale,”

## CodeGym — paper-codegym

**[Generalizable End-to-End Tool-Use RL with Synthetic CodeGym](https://arxiv.org/abs/2509.17325)**

`paper` · `codegym` · 2025-09-22 · RL experiments

Extracts callable functions from coding problems to synthesize controllable multi-turn tool-use tasks with executable rewards.

**Feedback / validation：** Code execution against task reference behavior.

**Release boundary：** Code-derived workflows are useful abstractions, but do not fully capture real enterprise service semantics.

**Implementation status：** Code

[Code](https://github.com/StigLidu/CodeGym)

Same work: [CodeGym (project)](#codegym--project-codegym)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2509.17325) · 2026-10-08 · “Tool-augmented large language models (LLMs), hereafter LLM agents, leverage external tools to solve diverse tasks and”

## τ²-bench — paper-tau2

**[$\tau^2$-Bench: Evaluating Conversational Agents in a Dual-Control Environment](https://arxiv.org/abs/2506.07982)**

`paper` · `tau2` · 2025-06-09 · Evaluation substrate

Models shared state changed by both assistant and simulated user, with compositional tasks and outcome evaluation.

**Feedback / validation：** Shared-world task outcome and policy-adherence checks.

**Release boundary：** User-simulator behavior affects results; treat benchmark tasks as held-out evaluation rather than free training data.

**Implementation status：** Code

[Code](https://github.com/sierra-research/tau2-bench)

Same work: [τ²-bench (project)](#τ²-bench--project-tau2)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2506.07982) · 2026-10-08 · “Existing benchmarks for conversational AI agents simulate single-control environments, where only the AI agent can use”

## TheAgentCompany — paper-theagentcompany

**[TheAgentCompany: Benchmarking LLM Agents on Consequential Real World Tasks](https://arxiv.org/abs/2412.14161)**

`paper` · `theagentcompany` · 2024-12-18 · Evaluation substrate

Creates a self-contained workplace of websites, files and simulated coworkers for long-horizon professional tasks.

**Feedback / validation：** Task state, trajectory milestones or rubric-based evaluation.

**Release boundary：** A workplace benchmark does not by itself establish train/test separation or reliable RL rewards for new tasks.

**Implementation status：** Code

[Code](https://github.com/TheAgentCompany/TheAgentCompany)

Same work: [TheAgentCompany (project)](#theagentcompany--project-theagentcompany)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2412.14161) · 2026-10-08 · “We interact with computers on an everyday basis, be it in everyday life or work, and”

## ToolSandbox — paper-toolsandbox

**[ToolSandbox: A Stateful, Conversational, Interactive Evaluation Benchmark for LLM Tool Use Capabilities](https://arxiv.org/abs/2408.04682)**

`paper` · `toolsandbox` · 2024-08-08 · Evaluation substrate

Combines stateful tool execution, user simulation and milestone-based checks over full conversational trajectories.

**Feedback / validation：** Intermediate milestones and final state over the trajectory.

**Release boundary：** Stateful evaluation infrastructure is reusable, but the paper's main evidence is evaluation rather than policy training.

**Implementation status：** Code

[Code](https://github.com/apple-aiml-research/ToolSandbox)

Same work: [ToolSandbox (project)](#toolsandbox--project-toolsandbox)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2408.04682) · 2026-10-08 · “Recent large language models (LLMs) advancements sparked a growing research interest in tool assisted LLMs solving”

## AppWorld — paper-appworld

**[AppWorld: A Controllable World of Apps and People for Benchmarking Interactive Coding Agents](https://arxiv.org/abs/2407.18901)**

`paper` · `appworld` · 2024-07-26 · Evaluation substrate

Simulates interconnected personal apps through executable APIs and validates final state plus unintended side effects.

**Feedback / validation：** State-based unit tests including collateral changes.

**Release boundary：** Train/development/test tasks and software/data licenses have distinct roles; preserve the official split policy.

**Implementation status：** Code

[Code](https://github.com/StonyBrookNLP/appworld)

Same work: [AppWorld (project)](#appworld--project-appworld)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2407.18901) · 2026-10-08 · “Autonomous agents that address day-to-day digital tasks (e.g., ordering groceries for a household), must not only”

## WebShop — paper-webshop

**[WebShop: Towards Scalable Real-World Web Interaction with Grounded Language Agents](https://arxiv.org/abs/2207.01206)**

`paper` · `webshop` · 2022-07-04 · RL experiments

Builds a shopping environment with natural-language goals and product-attribute reward signals for interactive learning.

**Feedback / validation：** Task state, trajectory milestones or rubric-based evaluation.

**Release boundary：** Product catalogs and website behavior are simplified; shopping success is a narrow capability measure.

**Implementation status：** Code

[Code](https://github.com/princeton-nlp/WebShop)

Same work: [WebShop (project)](#webshop--project-webshop)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2207.01206) · 2026-10-08 · “Existing benchmarks for grounding language in interactive environments either lack real-world linguistic elements, or prove difficult”

## GEM — paper-gem

**[GEM: A Gym for Agentic LLMs](https://arxiv.org/abs/2510.01051)**

`paper` · `gem` · 2025-10-01 · RL experiments

Provides a common agent–environment API, asynchronous vectorization and examples connecting varied environments to RL trainers.

**Feedback / validation：** Delegates task reward and correctness to environment authors or connected libraries.

**Release boundary：** Reward timing and per-turn credit assignment differ across trainers; adapters are not interchangeable without checking semantics.

**Implementation status：** Code

[Code](https://github.com/axon-rl/gem)

Same work: [GEM (project)](#gem--project-gem)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2510.01051) · 2026-10-08 · “The training paradigm for large language models (LLMs) is moving from static datasets to experience-based learning,”

## Meta ARE — paper-are

**[ARE: Scaling Up Agent Environments and Evaluations](https://arxiv.org/abs/2509.17158)**

`paper` · `are` · 2025-09-21 · Evaluation substrate

Separates apps, events and scenarios to simulate dynamic worlds and evaluate agents under asynchronous changes.

**Feedback / validation：** Delegates task reward and correctness to environment authors or connected libraries.

**Release boundary：** ARE is distinct from OpenEnv; Gaia2 results primarily establish evaluation behavior, not a released RL training recipe.

**Implementation status：** Code

[Code](https://github.com/facebookresearch/meta-agents-research-environments)

Same work: [Meta ARE (project)](#meta-are--project-are)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2509.17158) · 2026-10-08 · “We introduce Meta Agents Research Environments (ARE), a research platform for scalable creation of environments, integration”

## AgentGym-RL — paper-agentgym-rl

**[AgentGym-RL: Training LLM Agents for Long-Horizon Decision Making through Multi-Turn Reinforcement Learning](https://arxiv.org/abs/2509.08755)**

`paper` · `agentgym-rl` · 2025-09-10 · RL experiments

Decouples training and environment services and expands interaction horizons progressively for multi-turn RL.

**Feedback / validation：** Delegates task reward and correctness to environment authors or connected libraries.

**Release boundary：** Requires configuring each underlying environment and its services; it is not a single dependency-free simulator.

**Implementation status：** Code

[Code](https://github.com/WooooDyy/AgentGym-RL)

Same work: [AgentGym-RL (project)](#agentgym-rl--project-agentgym-rl)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2509.08755) · 2026-10-08 · “Developing autonomous LLM agents capable of making a series of intelligent decisions to solve complex, real-world”

## AgentGym — paper-agentgym

**[AgentGym: Evolving Large Language Model-based Agents across Diverse Environments](https://arxiv.org/abs/2406.04151)**

`paper` · `agentgym` · 2024-06-06 · SFT / trajectory training

Standardizes diverse environment servers and trajectories for generalist agent exploration and iterative learning.

**Feedback / validation：** Delegates task reward and correctness to environment authors or connected libraries.

**Release boundary：** The original AgentEvol study and later AgentGym-RL release use different learning pipelines.

**Implementation status：** Code

[Code](https://github.com/WooooDyy/AgentGym)

Same work: [AgentGym (project)](#agentgym--project-agentgym)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2406.04151) · 2026-10-08 · “Building generalist agents that can handle diverse tasks and evolve themselves across different environments is a”

## Reasoning Gym — paper-reasoning-gym

**[REASONING GYM: Reasoning Environments for Reinforcement Learning with Verifiable Rewards](https://arxiv.org/abs/2505.24760)**

`paper` · `reasoning-gym` · 2025-05-30 · RL experiments

Generates adjustable-difficulty reasoning tasks with deterministic verifiers instead of relying on a fixed dataset.

**Feedback / validation：** Procedural reference answers and task-specific scoring functions.

**Release boundary：** Many tasks are single-turn; procedural task diversity is different from stateful tool-interaction diversity.

**Implementation status：** Code

[Code](https://github.com/open-thought/reasoning-gym)

Same work: [Reasoning Gym (project)](#reasoning-gym--project-reasoning-gym)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2505.24760) · 2026-10-08 · “We introduce Reasoning Gym (RG), a library of reasoning environments for reinforcement learning with verifiable rewards.”

## TextArena — paper-textarena

**[TextArena](https://arxiv.org/abs/2504.11442)**

`paper` · `textarena` · 2025-04-15 · Trainable interface

Packages text games with rules, multi-player interaction and reward interfaces for agent training and evaluation.

**Feedback / validation：** Task-specific reference answers or game-rule outcomes.

**Release boundary：** Game win rates depend on opponents and rules; they are not direct measurements of workplace competence.

**Implementation status：** Code

[Code](https://github.com/TextArena/TextArena)

Same work: [TextArena (project)](#textarena--project-textarena)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2504.11442) · 2026-10-08 · “TextArena is an open-source collection of competitive text-based games for training and evaluation of agentic behavior”

## Aviary — paper-aviary

**[Aviary: training language agents on challenging scientific tasks](https://arxiv.org/abs/2412.21154)**

`paper` · `aviary` · 2024-12-30 · RL experiments

Defines language-agent environments with scientific tools and rewards, including literature, cloning and protein tasks.

**Feedback / validation：** Domain-specific goal and scientific-task checks.

**Release boundary：** Domain tools and external services add dependencies; simulated scientific success is not laboratory validation.

**Implementation status：** Code

[Code](https://github.com/Future-House/aviary)

Same work: [Aviary (project)](#aviary--project-aviary)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2412.21154) · 2026-10-08 · “Solving complex real-world tasks requires cycles of actions and observations. This is particularly true in science,”

## ScienceWorld — paper-scienceworld

**[ScienceWorld: Is your Agent Smarter than a 5th Grader?](https://arxiv.org/abs/2203.07540)**

`paper` · `scienceworld` · 2022-03-14 · Evaluation substrate

Offers an interactive text science world with compositional experiments and environment-based goal checks.

**Feedback / validation：** Domain-specific goal and scientific-task checks.

**Release boundary：** A simplified simulator is useful for planning research but does not reproduce physical laboratory dynamics.

**Implementation status：** Code

[Code](https://github.com/allenai/ScienceWorld)

Same work: [ScienceWorld (project)](#scienceworld--project-scienceworld)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2203.07540) · 2026-10-08 · “We present ScienceWorld, a benchmark to test agents' scientific reasoning abilities in a new interactive text”

## ALFWorld — paper-alfworld

**[ALFWorld: Aligning Text and Embodied Environments for Interactive Learning](https://arxiv.org/abs/2010.03768)**

`paper` · `alfworld` · 2020-10-08 · Imitation learning

Aligns symbolic text interactions with embodied household tasks; BUTLER learns with DAgger imitation learning and transfers the learned policy.

**Feedback / validation：** Domain-specific goal and scientific-task checks.

**Release boundary：** Text and embodied versions differ in perception and execution costs; treat this as foundational context.

**Implementation status：** Code

[Code](https://github.com/alfworld/alfworld)

Same work: [ALFWorld (project)](#alfworld--project-alfworld)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2010.03768) · 2026-10-08 · “Given a simple request like Put a washed apple in the kitchen fridge, humans can reason”
- [primary-source-content](https://arxiv.org/html/2010.03768) · 2026-10-08 · “The agent is trained in an imitation learning setting with DAgger”

## Terminal Task Hardness Audit — paper-fake-hardness

**[What Makes a Terminal-Bench Task Hard? Separating Genuine Hardness from Fake-Hardness on an Adjudicated Agentic Corpus](https://arxiv.org/abs/2609.26826)**

`paper` · `fake-hardness` · 2026-09-20 · Quality / failure study

Separates genuinely unsolved tasks from broken oracles, infrastructure failures and verifier bypasses using execution evidence.

**Feedback / validation：** Studies quality of the scoring signal rather than defining a universal reward.

**Release boundary：** An adjudicated corpus study does not prove intrinsic task hardness or verifier completeness.

**Implementation status：** Not confirmed

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2609.26826) · 2026-10-08 · “Frontier benchmarks need tasks that current models cannot solve. But a task that no model solves”

## Hack-Verifiable Environments — paper-hack-verifiable

**[Hack-Verifiable Environments: Towards Evaluating Reward Hacking at Scale](https://arxiv.org/abs/2605.20744)**

`paper` · `hack-verifiable` · 2026-05-20 · Evaluation substrate

Embeds detectable reward-hacking opportunities in TextArena to measure proxy exploitation deterministically.

**Feedback / validation：** Deterministic indicators of planted reward-hacking exploits.

**Release boundary：** Designed exploits support measurement; coverage does not exhaust real-world reward hacking.

**Implementation status：** Code

[Code](https://github.com/MajoRoth/hack-verifiable-environments)

Same work: [Hack-Verifiable Environments (project)](#hack-verifiable-environments--project-hack-verifiable)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2605.20744) · 2026-10-08 · “Aligning autonomous agents with human intent remains a central challenge in modern AI. A key manifestation”

## Agentic Environment Engineering Survey — paper-aee-survey

**[Agentic Environment Engineering for Large Language Models: A Survey of Environment Modeling, Synthesis, Evaluation, and Application](https://arxiv.org/abs/2606.12191)**

`paper` · `aee-survey` · 2026-06-10 · Survey

Organizes environment modeling, synthesis, evaluation and agent–environment evolution across domains.

**Feedback / validation：** Conceptual synthesis; no new task reward is specified here.

**Release boundary：** A survey is a discovery map; cited implementation and experimental claims should be checked at original sources.

**Implementation status：** —

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2606.12191) · 2026-10-08 · “Environments serve as interactive systems for large language model (LLM) based agents across diverse scenarios and”

## Environment Scaling Survey — paper-scaling-survey

**[Environment Scaling for Interactive Agentic Experience Collection: A Survey](https://arxiv.org/abs/2511.09586)**

`paper` · `scaling-survey` · 2025-11-12 · Survey

Frames interactive experience collection through task generation, execution and feedback, with environment-scaling strategies.

**Feedback / validation：** Conceptual synthesis; no new task reward is specified here.

**Release boundary：** The current title differs from the initial release; a taxonomy is not independent validation of its cited systems.

**Implementation status：** —

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2511.09586) · 2026-10-08 · “LLM-based agents can autonomously accomplish complex tasks across various domains. However, to further cultivate capabilities such”

## Introducing AgentEnv: An Open-Source Framework for Building RL Environments — blog-scale-agentenv

**[Introducing AgentEnv: An Open-Source Framework for Building RL Environments](https://labs.scale.com/blog/introducing-agentenv)**

`blog` · `scale-agentenv` · 2026-10-05 · Technical account

Explains reusable environment blocks, artifacts, rules and task DAGs with agent- and sandbox-independent execution.

**Feedback / validation：** Delegates task reward and correctness to environment authors or connected libraries.

**Release boundary：** Some tasks deliberately omit grading; using the framework does not automatically create a trainable reward.

Same work: [AgentEnv (Scale) (project)](#agentenv-scale--project-scale-agentenv)

**Evidence**

- [primary-source-content](https://labs.scale.com/blog/introducing-agentenv) · 2026-10-08 · “BACK 10/5/2026 Introducing AgentEnv: An Open-Source Framework for Building RL Environments By Edgar Arakelyan , Tejas”

## The Open Source Community is backing OpenEnv for Agentic RL — blog-openenv-community

**[The Open Source Community is backing OpenEnv for Agentic RL](https://huggingface.co/blog/openenv-agentic-rl)**

`blog` · `openenv` · 2026-06-08 · Technical account

Clarifies OpenEnv as an interoperability layer across environment libraries, agent harnesses and trainers.

**Feedback / validation：** Delegates task reward and correctness to environment authors or connected libraries.

**Release boundary：** Reward definitions and training algorithms remain responsibilities of the connected libraries.

Same work: [Building the Open Agent Ecosystem Together: Introducing OpenEnv (blog)](#building-the-open-agent-ecosystem-together-introducing-openenv--blog-openenv-launch) · [Scaling OpenEnv: From Free Usage to Thousands of Concurrent Environments (blog)](#scaling-openenv-from-free-usage-to-thousands-of-concurrent-environments--blog-openenv-scaling) · [Training a coding agent using the OpenCode harness in remote HF sandboxes with TRL and OpenEnv (blog)](#training-a-coding-agent-using-the-opencode-harness-in-remote-hf-sandboxes-with-trl-and-openenv--blog-trl-openenv) · [OpenEnv (project)](#openenv--project-openenv) · [The Building Blocks of Agentic AI: From Kernels to Clusters (blog)](#the-building-blocks-of-agentic-ai-from-kernels-to-clusters--blog-meta-openenv)

**Evidence**

- [primary-source-content](https://huggingface.co/blog/openenv-agentic-rl) · 2026-10-08 · “Back to Articles The Open Source Community is backing OpenEnv for Agentic RL Published June 8,”

## Building the Open Agent Ecosystem Together: Introducing OpenEnv — blog-openenv-launch

**[Building the Open Agent Ecosystem Together: Introducing OpenEnv](https://huggingface.co/blog/openenv)**

`blog` · `openenv` · 2025-10-23 · Technical account

Introduces the environment contract, container packaging and shared hub for agent interaction.

**Feedback / validation：** Delegates task reward and correctness to environment authors or connected libraries.

**Release boundary：** Historical launch specification; consult current docs for moved repositories and revised APIs.

Same work: [The Open Source Community is backing OpenEnv for Agentic RL (blog)](#the-open-source-community-is-backing-openenv-for-agentic-rl--blog-openenv-community) · [Scaling OpenEnv: From Free Usage to Thousands of Concurrent Environments (blog)](#scaling-openenv-from-free-usage-to-thousands-of-concurrent-environments--blog-openenv-scaling) · [Training a coding agent using the OpenCode harness in remote HF sandboxes with TRL and OpenEnv (blog)](#training-a-coding-agent-using-the-opencode-harness-in-remote-hf-sandboxes-with-trl-and-openenv--blog-trl-openenv) · [OpenEnv (project)](#openenv--project-openenv) · [The Building Blocks of Agentic AI: From Kernels to Clusters (blog)](#the-building-blocks-of-agentic-ai-from-kernels-to-clusters--blog-meta-openenv)

**Evidence**

- [primary-source-content](https://huggingface.co/blog/openenv) · 2026-10-08 · “Back to Articles Building the Open Agent Ecosystem Together: Introducing OpenEnv Published October 23, 2025 Update”

## verifiers v1: Decomposing Tasksets and Harnesses for Agentic RL & Evaluations — blog-verifiers-v1

**[verifiers v1: Decomposing Tasksets and Harnesses for Agentic RL & Evaluations](https://www.primeintellect.ai/blog/verifiers-v1)**

`blog` · `verifiers` · 2026-07-12 · Technical account

Splits tasksets, harnesses and runtimes while preserving branching traces and training tokens.

**Feedback / validation：** Delegates task reward and correctness to environment authors or connected libraries.

**Release boundary：** The article announces a v1 preview namespace in version 0.2.0; it is not a semantic-version 1.0 release.

Same work: [Environments Hub: A Community Hub To Scale RL To Open AGI (blog)](#environments-hub-a-community-hub-to-scale-rl-to-open-agi--blog-environments-hub) · [Multi-Agent Systems in PRIME-RL (blog)](#multi-agent-systems-in-prime-rl--blog-multi-agent-rl) · [Verifiers (project)](#verifiers--project-verifiers)

**Evidence**

- [primary-source-content](https://www.primeintellect.ai/blog/verifiers-v1) · 2026-10-08 · “verifiers v1: Decomposing Tasksets and Harnesses for Agentic RL & Evaluations Today, we are launching verifiers”

## Environments Hub: A Community Hub To Scale RL To Open AGI — blog-environments-hub

**[Environments Hub: A Community Hub To Scale RL To Open AGI](https://www.primeintellect.ai/blog/environments)**

`blog` · `verifiers` · 2025-08-27 · Technical account

Describes publishing reusable verifiers environments with tasks, feedback and training integration.

**Feedback / validation：** Delegates task reward and correctness to environment authors or connected libraries.

**Release boundary：** Hub presence does not establish independent task quality or permission to train on evaluation splits.

Same work: [verifiers v1: Decomposing Tasksets and Harnesses for Agentic RL & Evaluations (blog)](#verifiers-v1-decomposing-tasksets-and-harnesses-for-agentic-rl--evaluations--blog-verifiers-v1) · [Multi-Agent Systems in PRIME-RL (blog)](#multi-agent-systems-in-prime-rl--blog-multi-agent-rl) · [Verifiers (project)](#verifiers--project-verifiers)

**Evidence**

- [primary-source-content](https://www.primeintellect.ai/blog/environments) · 2026-10-08 · “Environments Hub: A Community Hub To Scale RL To Open AGI RL environments are the playgrounds”

## Welcome RL Environments to the hub — blog-hf-env-hub

**[Welcome RL Environments to the hub](https://huggingface.co/blog/rl-environments)**

`blog` · `hf-env-hub` · 2026-09-28 · Technical account

Defines dataset tags and framework compatibility metadata for discovering and versioning RL tasksets on the Hub.

**Feedback / validation：** Delegates task reward and correctness to environment authors or connected libraries.

**Release boundary：** The release focuses on tasksets; tags alone do not launch runtimes or guarantee cross-framework compatibility.

**Evidence**

- [primary-source-content](https://huggingface.co/blog/rl-environments) · 2026-10-08 · “Back to Articles Welcome RL Environments to the hub Published September 28, 2026 Update on GitHub”

## Scaling OpenEnv: From Free Usage to Thousands of Concurrent Environments — blog-openenv-scaling

**[Scaling OpenEnv: From Free Usage to Thousands of Concurrent Environments](https://huggingface.co/blog/burtenshaw/openenv-scaling)**

`blog` · `openenv` · 2026-01-20 · Technical account

Benchmarks deployment tiers from Spaces and Docker to clustered concurrent environment sessions.

**Feedback / validation：** Delegates task reward and correctness to environment authors or connected libraries.

**Release boundary：** Reported throughput is workload-specific; lightweight-session capacity is not a GUI or SWE throughput guarantee.

Same work: [The Open Source Community is backing OpenEnv for Agentic RL (blog)](#the-open-source-community-is-backing-openenv-for-agentic-rl--blog-openenv-community) · [Building the Open Agent Ecosystem Together: Introducing OpenEnv (blog)](#building-the-open-agent-ecosystem-together-introducing-openenv--blog-openenv-launch) · [Training a coding agent using the OpenCode harness in remote HF sandboxes with TRL and OpenEnv (blog)](#training-a-coding-agent-using-the-opencode-harness-in-remote-hf-sandboxes-with-trl-and-openenv--blog-trl-openenv) · [OpenEnv (project)](#openenv--project-openenv) · [The Building Blocks of Agentic AI: From Kernels to Clusters (blog)](#the-building-blocks-of-agentic-ai-from-kernels-to-clusters--blog-meta-openenv)

**Evidence**

- [primary-source-content](https://huggingface.co/blog/burtenshaw/openenv-scaling) · 2026-10-08 · “Back to Articles Scaling OpenEnv: From Free Usage to Thousands of Concurrent Environments Community Article Published”

## How to Train Scientific Agents with Reinforcement Learning — blog-nemo-science

**[How to Train Scientific Agents with Reinforcement Learning](https://developer.nvidia.com/blog/how-to-train-scientific-agents-with-reinforcement-learning/)**

`blog` · `nemo-gym` · 2025-12-15 · Technical account

Walks through model, resource and agent servers, using Aviary to build and verify scientific rollouts.

**Feedback / validation：** Delegates task reward and correctness to environment authors or connected libraries.

**Supporting reference：** Supports execution, evaluation, simulation or quality control, but is not a direct focus on scalable environment production or effective training-data production; retained in its subject category.

**Article research question：** How do scientific tasks connect to rollouts?

**Concrete content**

- Model, resource and agent service roles
- Aviary integration for scientific tools
- Task execution and outcome verification

**Release boundary：** This is a versioned tutorial; newer Gym releases reorganize environment-server abstractions.

Same work: [NeMo Gym (project)](#nemo-gym--project-nemo-gym) · [Mastering Agentic Techniques: AI Agent Reinforcement Learning (blog)](#mastering-agentic-techniques-ai-agent-reinforcement-learning--blog-nvidia-agent-rl)

**Evidence**

- [primary-source-content](https://developer.nvidia.com/blog/how-to-train-scientific-agents-with-reinforcement-learning/) · 2026-10-08 · “Agentic AI / Generative AI English 中文 How to Train Scientific Agents with Reinforcement Learning Dec”

## Prime Sandboxes: MicroVMs for Agentic RL Training at Scale — blog-prime-sandboxes

**[Prime Sandboxes: MicroVMs for Agentic RL Training at Scale](https://www.primeintellect.ai/blog/sandboxes)**

`blog` · `prime-sandboxes` · 2026-09-23 · Technical account

Explains VM-backed rollout isolation, image reuse and scaling many concurrent training environments.

**Feedback / validation：** Delegates task reward and correctness to environment authors or connected libraries.

**Release boundary：** A hosted commercial runtime; capacity and cost claims are vendor-reported, not independently benchmarked here.

**Evidence**

- [primary-source-content](https://www.primeintellect.ai/blog/sandboxes) · 2026-10-08 · “Prime Sandboxes: MicroVMs for Agentic RL Training at Scale In agentic RL, the sandbox is the”

## Multi-Agent Systems in PRIME-RL — blog-multi-agent-rl

**[Multi-Agent Systems in PRIME-RL](https://www.primeintellect.ai/blog/multi-agent-systems)**

`blog` · `verifiers` · 2026-08-07 · Technical account

Adds programmable agent interactions, trainable-role selection and credit assignment for self-play, user simulation and judging.

**Feedback / validation：** Delegates task reward and correctness to environment authors or connected libraries.

**Release boundary：** A multi-agent API does not itself demonstrate gains for every interaction pattern.

Same work: [verifiers v1: Decomposing Tasksets and Harnesses for Agentic RL & Evaluations (blog)](#verifiers-v1-decomposing-tasksets-and-harnesses-for-agentic-rl--evaluations--blog-verifiers-v1) · [Environments Hub: A Community Hub To Scale RL To Open AGI (blog)](#environments-hub-a-community-hub-to-scale-rl-to-open-agi--blog-environments-hub) · [Verifiers (project)](#verifiers--project-verifiers)

**Evidence**

- [primary-source-content](https://www.primeintellect.ai/blog/multi-agent-systems) · 2026-10-08 · “Multi-Agent Systems in PRIME-RL Today, the Prime Intellect RL stack expands from training individual agents to”

## Training a coding agent using the OpenCode harness in remote HF sandboxes with TRL and OpenEnv — blog-trl-openenv

**[Training a coding agent using the OpenCode harness in remote HF sandboxes with TRL and OpenEnv](https://huggingface.co/blog/sergiopaniego/trl-openenv-harness-training)**

`blog` · `openenv` · 2026-08-05 · Technical account

Shows one sandbox per rollout, proxy capture of token-faithful traces and workspace-based reward for AsyncGRPO.

**Feedback / validation：** Delegates task reward and correctness to environment authors or connected libraries.

**Release boundary：** An October update routes examples through Harbor integration; older opencode_env commands are superseded.

Same work: [The Open Source Community is backing OpenEnv for Agentic RL (blog)](#the-open-source-community-is-backing-openenv-for-agentic-rl--blog-openenv-community) · [Building the Open Agent Ecosystem Together: Introducing OpenEnv (blog)](#building-the-open-agent-ecosystem-together-introducing-openenv--blog-openenv-launch) · [Scaling OpenEnv: From Free Usage to Thousands of Concurrent Environments (blog)](#scaling-openenv-from-free-usage-to-thousands-of-concurrent-environments--blog-openenv-scaling) · [OpenEnv (project)](#openenv--project-openenv) · [The Building Blocks of Agentic AI: From Kernels to Clusters (blog)](#the-building-blocks-of-agentic-ai-from-kernels-to-clusters--blog-meta-openenv)

**Evidence**

- [primary-source-content](https://huggingface.co/blog/sergiopaniego/trl-openenv-harness-training) · 2026-10-08 · “Back to Articles Training a coding agent using the OpenCode harness in remote HF sandboxes with”

## Scaling Agentic RL: 365,000+ Environments for SWE, Terminal, and Search — blog-prime-scale

**[Scaling Agentic RL: 365,000+ Environments for SWE, Terminal, and Search](https://www.primeintellect.ai/blog/scaling-agentic-rl)**

`blog` · `prime-research-envs` · 2026-07-22 · Technical account

Normalizes taskset lifecycle and sandboxes while retaining upstream scoring logic and withholding grading materials during rollouts.

**Feedback / validation：** Generated task verifiers plus construction or solvability validation.

**Release boundary：** The headline counts roughly 365K tasks across 23 tasksets, not 365K independent environment families; evaluation sets stay held out.

**Evidence**

- [primary-source-content](https://www.primeintellect.ai/blog/scaling-agentic-rl) · 2026-10-08 · “Scaling Agentic RL: 365,000+ Environments for SWE, Terminal, and Search The open research ecosystem has produced”

## General Agent: A Self-Evolving, Synthetic Agent Environment — blog-general-agent

**[General Agent: A Self-Evolving, Synthetic Agent Environment](https://www.primeintellect.ai/blog/general-agent)**

`blog` · `general-agent` · 2026-05-18 · Technical account

Uses synthesizer–solver interaction to build database-backed tool tasks with gold solutions and calibrated difficulty bands.

**Feedback / validation：** Generated task verifiers plus construction or solvability validation.

**Release boundary：** The described release synthesizes a fixed corpus offline; online joint multi-agent training is future work in this post.

**Evidence**

- [primary-source-content](https://www.primeintellect.ai/blog/general-agent) · 2026-10-08 · “General Agent: A Self-Evolving, Synthetic Agent Environment Training capable agents requires exposure to diverse tasks and”

## Agent World Model: Infinity Synthetic Environments for Agentic Reinforcement Learning — blog-awm-blog

**[Agent World Model: Infinity Synthetic Environments for Agentic Reinforcement Learning](https://www.snowflake.com/en/blog/engineering/agent-world-model-for-agentic-reinforment-learning/)**

`blog` · `awm` · 2026-02-13 · Technical account

Explains executable SQL-backed world synthesis, consistent state transitions and reward construction for tool-use RL.

**Feedback / validation：** Database-state-aware task verification.

**Release boundary：** Companion to the AWM paper and code, not independent corroboration of their experimental results.

Same work: [Agent World Model (paper)](#agent-world-model--paper-awm) · [Agent World Model (project)](#agent-world-model--project-awm)

**Evidence**

- [primary-source-content](https://www.snowflake.com/en/blog/engineering/agent-world-model-for-agentic-reinforment-learning/) · 2026-10-08 · “Agent World Model (AWM) for Scalable Agentic RL Environments Skip to content Blog / Gen AI”

## CoderForge-Preview — blog-coderforge

**[CoderForge-Preview](https://www.together.ai/blog/coderforge-preview)**

`blog` · `coderforge` · Date unconfirmed · Technical account

Describes large-scale test-verified coding trajectories and fine-tuning on executable repository tasks.

**Feedback / validation：** Task-specific execution tests or verifier scores; consult the resource for the exact split.

**Article research question：** How do repository tasks yield training traces?

**Concrete content**

- Executable repository tasks host interactions
- Tests validate coding trajectories
- Released trajectories support fine-tuning

**Release boundary：** The public release emphasizes trajectories; do not equate trajectory count with newly released environment implementations.

**Evidence**

- [primary-source-content](https://www.together.ai/blog/coderforge-preview) · 2026-10-08 · “We release CoderForge-Preview - the largest open test-verified coding agent dataset. By leveraging it to fine-tune”

## A technical report on Composer 2 — blog-composer2

**[A technical report on Composer 2](https://cursor.com/blog/composer-2-technical-report)**

`blog` · `composer2` · 2026-03-27 · Technical account

Connects realistic deployment-matched tool sessions with asynchronous RL and large-scale sandbox infrastructure.

**Feedback / validation：** Task-specific execution tests or verifier scores; consult the resource for the exact split.

**Article research question：** How are deployment-like training tasks executed?

**Concrete content**

- Multi-step tasks with real tool sessions
- Sandboxes support concurrent execution
- Execution feedback feeds asynchronous RL

**Release boundary：** Industrial first-party account; the internal training environment fleet is not released as an open environment library.

**Evidence**

- [primary-source-content](https://cursor.com/blog/composer-2-technical-report) · 2026-10-08 · “Blog / research We posted to the arXiv a technical report on the training of Composer”

## OpenEnv in Practice: Evaluating Tool-Using Agents in Real-World Environments — blog-calendar-gym

**[OpenEnv in Practice: Evaluating Tool-Using Agents in Real-World Environments](https://huggingface.co/blog/openenv-turing)**

`blog` · `openenv-calendar` · 2026-02-12 · Technical account

Uses calendar tasks to expose state, permissions, temporal reasoning and recovery requirements in tool environments.

**Feedback / validation：** Task state, trajectory milestones or rubric-based evaluation.

**Release boundary：** Reported experiments are evaluations; the article does not by itself establish a trained calendar policy.

**Evidence**

- [primary-source-content](https://huggingface.co/blog/openenv-turing) · 2026-10-08 · “Back to Articles OpenEnv in Practice: Evaluating Tool-Using Agents in Real-World Environments Published February 12, 2026”

## Scaling Enterprise Agent Performance with Reinforcement Learning via Verifiable Feedback Loops — blog-scale-enterprise

**[Scaling Enterprise Agent Performance with Reinforcement Learning via Verifiable Feedback Loops](https://labs.scale.com/blog/scaling-enterprise-agent-performance-with-reinforcement-learning-via-verifiable-feedback-loops)**

`blog` · `scale-enterprise` · 2025-11-17 · Technical account

Examines environment design and verifiable feedback for domain-specific SQL and enterprise reasoning training.

**Feedback / validation：** Task state, trajectory milestones or rubric-based evaluation.

**Release boundary：** Publisher-reported domain studies; the underlying private workflows are not a general public environment release.

**Evidence**

- [primary-source-content](https://labs.scale.com/blog/scaling-enterprise-agent-performance-with-reinforcement-learning-via-verifiable-feedback-loops) · 2026-10-08 · “BACK Post-Training Agents Enterprise 11/17/2025 Scaling Enterprise Agent Performance with Reinforcement Learning via Verifiable Feedback Loops”

## Who Grades the Graders? Rethinking Verifier Design for Computer Use Agents — blog-scale-grader

**[Who Grades the Graders? Rethinking Verifier Design for Computer Use Agents](https://labs.scale.com/blog/verifier-design-for-cua)**

`blog` · `scale-grader` · 2026-09-02 · Technical account

Compares brittle programmatic checks with model judges and argues for decomposed, hybrid verification of professional artifacts.

**Feedback / validation：** Studies quality of the scoring signal rather than defining a universal reward.

**Release boundary：** Analysis uses selected tasks; neither programmatic checks nor VLM judges are universally reliable.

**Evidence**

- [primary-source-content](https://labs.scale.com/blog/verifier-design-for-cua) · 2026-10-08 · “BACK Agents 9/2/2026 Who Grades the Graders? Rethinking Verifier Design for Computer Use Agents By Mark”

## Rubric Dropout: A Simple Way to Mitigate Reward Hacking in Rubric-as-Reward RL — blog-rubric-dropout

**[Rubric Dropout: A Simple Way to Mitigate Reward Hacking in Rubric-as-Reward RL](https://labs.scale.com/blog/rubric-dropout)**

`blog` · `rubric-dropout` · 2026-09-10 · Technical account

Randomly removes rubric criteria during reward computation to reduce overfitting to a fixed grading proxy.

**Feedback / validation：** Studies quality of the scoring signal rather than defining a universal reward.

**Release boundary：** Mitigation is evaluated in selected domains and sizes; it does not make a learned judge an objective verifier.

**Evidence**

- [primary-source-content](https://labs.scale.com/blog/rubric-dropout) · 2026-10-08 · “BACK Evaluation and Alignment 9/10/2026 RUBRIC DROPOUT: A SIMPLE WAY TO MITIGATE REWARD HACKING IN RUBRIC-AS-REWARD”

## Agentic Rubrics: Teaching AI to Verify Code the Way Developers Do — blog-agentic-rubrics

**[Agentic Rubrics: Teaching AI to Verify Code the Way Developers Do](https://labs.scale.com/blog/agentic-rubrics)**

`blog` · `agentic-rubrics` · 2026-03-11 · Technical account

Builds repository-grounded checklists for scoring candidate patches without executing tests.

**Feedback / validation：** Studies quality of the scoring signal rather than defining a universal reward.

**Release boundary：** This is execution-free verification and candidate selection; do not present its score as passing executable tests.

**Evidence**

- [primary-source-content](https://labs.scale.com/blog/agentic-rubrics) · 2026-10-08 · “BACK Agents Evaluation and Alignment 3/11/2026 Agentic Rubrics: Teaching AI to Verify Code the Way Developers”

## Systematic Reward Hacking and Prime Sprints — blog-reward-hacking

**[Systematic Reward Hacking and Prime Sprints](https://www.primeintellect.ai/blog/reward-hacking)**

`blog` · `prime-hacking` · 2026-05-20 · Technical account

Studies competing visible and hidden rewards in designed backdoor-IFEval environments during RL.

**Feedback / validation：** Studies quality of the scoring signal rather than defining a universal reward.

**Release boundary：** Deliberately planted reward shortcuts aid diagnosis but do not represent all production failure modes.

**Evidence**

- [primary-source-content](https://www.primeintellect.ai/blog/reward-hacking) · 2026-10-08 · “Systematic Reward Hacking and Prime Sprints Detecting and mitigating reward hacking is one of the key”

## EnvHarness — project-envharness

**[EnvHarness](https://github.com/google-research/envharness)**

`project` · `envharness` · Date unconfirmed · RL and harness learning

Wraps fixed environments with programmable setup, interaction and composition layers, adapting practice while retaining original verifiers.

**Feedback / validation：** Original environment verifiers plus held-out task evaluation.

**Release boundary：** Transfers are measured on selected benchmarks; retaining a verifier does not prove every generated wrapper preserves task semantics.

GitHub: ★ 621 · push 2026-08-21 · `Apache-2.0` · active

[GitHub](https://github.com/google-research/envharness)

Same work: [EnvHarness (paper)](#envharness--paper-envharness)

**Evidence**

- [primary-source-content](https://github.com/google-research/envharness) · 2026-10-08 · “EnvHarness : Awakening Static Worlds for Agent Learning Check out our paper and webpage for more”

## SPADE — project-spade

**[SPADE](https://github.com/spade-rl/spade)**

`project` · `spade` · Date unconfirmed · RL experiments

Co-trains one policy as environment designer and solver; executable reset/step worlds are selected using hint-based regret.

**Feedback / validation：** Executable environment rewards and a hint-based regret signal for the designer.

**Release boundary：** Grounding corpora, memory and feasibility controls remain necessary; experiments do not establish unbounded improvement.

GitHub: ★ 114 · push 2026-08-26 · `MIT` · active

[GitHub](https://github.com/spade-rl/spade)

Same work: [SPADE (paper)](#spade--paper-spade)

**Evidence**

- [primary-source-content](https://github.com/spade-rl/spade) · 2026-10-08 · “SPADE ♠ Self-Play in Adaptive Synthetic Executable Environments 🤗 Models & Data | ♠ SPADE on”

## Beyond Simply Environment Scaling — project-beyond-mm-scaling

**[Beyond Simply Environment Scaling](https://github.com/GaryStack/Beyond-MMEnv-Scaling)**

`project` · `beyond-mm-scaling` · Date unconfirmed · RL experiments

Studies environment distributions through ability-aware selection and a hierarchy of interaction difficulty and state size.

**Feedback / validation：** Task success feeds difficulty adaptation; see method-specific verification details.

**Release boundary：** Environment count alone is not the treatment; benefits depend on the evaluated diversity and difficulty settings.

GitHub: ★ 15 · push 2026-08-04 · `Apache-2.0` · reference

[GitHub](https://github.com/GaryStack/Beyond-MMEnv-Scaling)

Same work: [Beyond Simply Environment Scaling (paper)](#beyond-simply-environment-scaling--paper-beyond-mm-scaling)

**Evidence**

- [primary-source-content](https://github.com/GaryStack/Beyond-MMEnv-Scaling) · 2026-10-08 · “Beyond-MMEnv-Scaling Beyond Simply Environment Scaling: Designing Effective Environment Distributions for Multimodal Agent Learning ⚠️ Status: Work”

## RLVE — project-rlve

**[RLVE](https://github.com/Zhiyuan-Zeng/RLVE)**

`project` · `rlve` · Date unconfirmed · RL experiments

Adapts procedural task difficulty to the current policy across a manually engineered suite of verifiable reasoning environments.

**Feedback / validation：** Algorithmic answer verification and adaptive solve-rate calibration.

**Release boundary：** Environment engineering is still manual; procedural reasoning results should not be extrapolated to GUI or enterprise workflows.

GitHub: ★ 235 · push 2026-04-30 · `MIT` · reference

[GitHub](https://github.com/Zhiyuan-Zeng/RLVE)

Same work: [RLVE (paper)](#rlve--paper-rlve)

**Evidence**

- [primary-source-content](https://github.com/Zhiyuan-Zeng/RLVE) · 2026-10-08 · “RLVE: Scaling Up Reinforcement Learning for Language Models with Adaptive Verifiable Environments Zhiyuan Zeng*, Hamish Ivison*,”

## Environment Tuning — project-env-tuning

**[Environment Tuning](https://github.com/inclusionAI/AWorld-RL)**

`project` · `env-tuning` · Date unconfirmed · RL experiments

Combines a task curriculum, corrective environment feedback and progress rewards to stabilize sparse-data tool-use learning.

**Feedback / validation：** Task success feeds difficulty adaptation; see method-specific verification details.

**Release boundary：** Augmented feedback is part of training; deployment must be evaluated without assuming the same privileged help.

GitHub: ★ 127 · push 2026-06-18 · `MIT` · reference

[GitHub](https://github.com/inclusionAI/AWorld-RL)

Same work: [Environment Tuning (paper)](#environment-tuning--paper-env-tuning)

**Evidence**

- [primary-source-content](https://github.com/inclusionAI/AWorld-RL) · 2026-10-08 · “Agentic Learning Powered by AWorld arXiv(HardGen) arXiv(V2P) ｜ arXiv(RAG-R1) ｜ arXiv(FunReason) ｜ arXiv(RODS) ｜ arXiv(EnvTuning) ｜”

## EnvFactory — project-envfactory

**[EnvFactory](https://github.com/LARK-AI-Lab/EnvFactory)**

`project` · `envfactory` · Date unconfirmed · RL and SFT experiments

Builds and verifies stateful tools from real resources, then synthesizes trajectories using tool topology and calibrated query refinement.

**Feedback / validation：** Generated task verifiers plus construction or solvability validation.

**Release boundary：** Executable correctness and natural task intent require separate checks; the release includes framework-specific training dependencies.

GitHub: ★ 96 · push 2026-08-28 · `none` · active

[GitHub](https://github.com/LARK-AI-Lab/EnvFactory)

Same work: [EnvFactory (paper)](#envfactory--paper-envfactory)

**Evidence**

- [primary-source-content](https://github.com/LARK-AI-Lab/EnvFactory) · 2026-10-08 · “EnvFactory EnvFactory: Scaling Tool-Use Agents via Executable Environments Synthesis and Robust RL 📒 Models & Dataset”

## Agent-World — project-agent-world

**[Agent-World](https://github.com/RUC-NLPIR/Agent-World)**

`project` · `agent-world` · Date unconfirmed · RL and SFT experiments

Discovers stateful tool ecosystems and generates verifiable tasks, linking multi-environment learning to capability-gap-driven task evolution.

**Feedback / validation：** Generated task verifiers plus construction or solvability validation.

**Release boundary：** The public repository releases a selected environment subset and requires RL adaptation; it is not the entire paper corpus.

GitHub: ★ 7 · push 2026-10-06 · `MIT` · active

[GitHub](https://github.com/RUC-NLPIR/Agent-World)

Same work: [Agent-World (paper)](#agent-world--paper-agent-world)

**Evidence**

- [primary-source-content](https://github.com/RUC-NLPIR/Agent-World) · 2026-10-08 · “🌐 Agent-World Real Environments. Verifiable Tasks. Evolving Agents. English | 简体中文 A self-evolving training arena that”

## Agent World Model — project-awm

**[Agent World Model](https://github.com/Snowflake-Labs/agent-world-model)**

`project` · `awm` · Date unconfirmed · RL experiments

Synthesizes code-driven, SQL-backed tool worlds with inspectable state and rewards for multi-turn RL and transfer studies.

**Feedback / validation：** Database-state-aware task verification.

**Release boundary：** Synthetic database consistency does not establish fidelity to every real service or production failure mode.

GitHub: ★ 465 · push 2026-05-28 · `none` · reference

[GitHub](https://github.com/Snowflake-Labs/agent-world-model)

Same work: [Agent World Model (paper)](#agent-world-model--paper-awm) · [Agent World Model: Infinity Synthetic Environments for Agentic Reinforcement Learning (blog)](#agent-world-model-infinity-synthetic-environments-for-agentic-reinforcement-learning--blog-awm-blog)

**Evidence**

- [primary-source-content](https://github.com/Snowflake-Labs/agent-world-model) · 2026-10-08 · “Agent World Model Infinity Synthetic Environments for Agentic Reinforcement Learning Zhaoyang Wang 1 , Canwen Xu”

## EnvScaler — project-envscaler

**[EnvScaler](https://github.com/RUC-NLPIR/EnvScaler)**

`project` · `envscaler` · Date unconfirmed · RL and SFT experiments

Separates environment skeleton construction from scenario generation and rule-based trajectory validation.

**Feedback / validation：** Rule-based trajectory and final-state checks.

**Release boundary：** Rule coverage and environment realism must be assessed independently; released RL integration uses ROLL and GEM.

GitHub: ★ 199 · push 2026-09-03 · `MIT` · active

[GitHub](https://github.com/RUC-NLPIR/EnvScaler)

Same work: [EnvScaler (paper)](#envscaler--paper-envscaler)

**Evidence**

- [primary-source-content](https://github.com/RUC-NLPIR/EnvScaler) · 2026-10-08 · “EnvScaler: Scaling Tool-Interactive Environments for LLM Agent via Programmatic Synthesis 中文 | English If you like”

## AutoEnv — project-autoenv

**[AutoEnv](https://github.com/FoundationAgents/AutoEnv)**

`project` · `autoenv` · Date unconfirmed · Environment / task generation

Factorizes transition, observation and reward distributions to generate heterogeneous worlds for cross-environment learning studies.

**Feedback / validation：** Generated task verifiers plus construction or solvability validation.

**Release boundary：** Generated levels measure transfer under designed distributions, not unrestricted real-world generalization.

GitHub: ★ 68 · push 2026-03-26 · `MIT` · reference

[GitHub](https://github.com/FoundationAgents/AutoEnv)

Same work: [AutoEnv (paper)](#autoenv--paper-autoenv)

**Evidence**

- [primary-source-content](https://github.com/FoundationAgents/AutoEnv) · 2026-10-08 · “AutoEnv: Automating Environment Generation For Language Model Agents If you encounter any difficulties in usingthe code,”

## EnvACE — project-envace

**[EnvACE](https://github.com/Within-yao/EnvACE)**

`project` · `envace` · Date unconfirmed · RL experiments

Trains a shared policy to act and rehearse environment responses, internalizing dynamics through role-wise RL.

**Feedback / validation：** Simulated observations or task-success rewards; real-environment transfer is evaluated separately.

**Release boundary：** Rehearsed observations are model outputs; simulated consistency needs checking against external execution.

GitHub: ★ 24 · push 2026-09-07 · `Apache-2.0` · active

[GitHub](https://github.com/Within-yao/EnvACE)

Same work: [EnvACE (paper)](#envace--paper-envace)

**Evidence**

- [primary-source-content](https://github.com/Within-yao/EnvACE) · 2026-10-08 · “EnvACE: Internalizing Environment Dynamics via World Rehearsal for Agentic RL EnvACE is an agentic RL framework”

## WebWorld — project-webworld

**[WebWorld](https://github.com/QwenLM/WebWorld)**

`project` · `webworld` · Date unconfirmed · SFT / trajectory training

Learns an open-web simulator from interaction trajectories and uses simulated rollouts for web-agent training and planning.

**Feedback / validation：** Simulated observations or task-success rewards; real-environment transfer is evaluated separately.

**Release boundary：** Simulation quality and real-browser transfer are separate measurements; distinct from later same-name web-code papers.

GitHub: ★ 61 · push 2026-02-25 · `none` · reference

[GitHub](https://github.com/QwenLM/WebWorld)

Same work: [WebWorld (paper)](#webworld--paper-webworld)

**Evidence**

- [primary-source-content](https://github.com/QwenLM/WebWorld) · 2026-10-08 · “WebWorld Introduction Web agents require massive trajectories to generalize, yet real-world training is constrained by network”

## GenEnv — project-genenv

**[GenEnv](https://github.com/Gen-Verse/GenEnv)**

`project` · `genenv` · Date unconfirmed · RL experiments

Co-evolves a generative simulator and agent using a difficulty-aligned curriculum reward.

**Feedback / validation：** Simulated observations or task-success rewards; real-environment transfer is evaluated separately.

**Release boundary：** Learned simulation can drift from executable reality; reported gains concern the paper's selected tasks.

GitHub: ★ 67 · push 2026-09-25 · `Apache-2.0` · active

[GitHub](https://github.com/Gen-Verse/GenEnv)

Same work: [GenEnv (paper)](#genenv--paper-genenv)

**Evidence**

- [primary-source-content](https://github.com/Gen-Verse/GenEnv) · 2026-10-08 · “GenEnv: Difficulty-Aligned Co-Evolution Between LLM Agents and Environment Simulators (NeurIPS 2026) 🌟 Introduction GenEnv is a”

## SynthTools — project-synthtools

**[SynthTools](https://github.com/namkoong-lab/SynthTools)**

`project` · `synthtools` · Date unconfirmed · Environment / task generation

Separates synthetic tool generation, response simulation and tool auditing to scale controllable tool ecosystems.

**Feedback / validation：** LLM-simulated tool observations with a separate audit stage.

**Release boundary：** Tool responses are simulated by LLMs; audit accuracy is not a proof of deterministic state transitions.

GitHub: ★ 9 · push 2026-07-20 · `none` · reference

[GitHub](https://github.com/namkoong-lab/SynthTools)

Same work: [SynthTools (paper)](#synthtools--paper-synthtools)

**Evidence**

- [primary-source-content](https://github.com/namkoong-lab/SynthTools) · 2026-10-08 · “SynthTools SynthTools is a fully LLM-based pipeline for building, validating, and exercising synthetic tool-use environments at”

## daVinci-Env / OpenSWE — project-openswe

**[daVinci-Env / OpenSWE](https://github.com/GAIR-NLP/OpenSWE)**

`project` · `openswe` · Date unconfirmed · SFT / trajectory training

Automates repository exploration, Docker setup and test generation, then filters environments by solvability and useful difficulty.

**Feedback / validation：** Task-specific execution tests or verifier scores; consult the resource for the exact split.

**Release boundary：** The title says daVinci-Env while the released framework is OpenSWE; construction and rollout costs are substantial.

GitHub: ★ 211 · push 2026-03-16 · `NOASSERTION` · reference

[GitHub](https://github.com/GAIR-NLP/OpenSWE)

Same work: [daVinci-Env / OpenSWE (paper)](#davinci-env--openswe--paper-openswe)

**Evidence**

- [primary-source-content](https://github.com/GAIR-NLP/OpenSWE) · 2026-10-08 · “OpenSWE: Efficient SWE Environment Synthesis at Scale OpenSWE is the largest fully transparent framework for SWE”

## SWE-rebench V2 — project-swe-rebench

**[SWE-rebench V2](https://github.com/SWE-rebench/SWE-rebench-V2)**

`project` · `swe-rebench` · Date unconfirmed · Environment / task generation

Harvests multilingual repository tasks and generates installation and test procedures to build reproducible training environments.

**Feedback / validation：** Task-specific execution tests or verifier scores; consult the resource for the exact split.

**Release boundary：** Fully built environments and additional task metadata have different release scope; tests can be underspecified or restrictive.

GitHub: ★ 85 · push 2026-03-12 · `MIT` · reference

[GitHub](https://github.com/SWE-rebench/SWE-rebench-V2)

Same work: [SWE-rebench V2 (paper)](#swe-rebench-v2--paper-swe-rebench)

**Evidence**

- [primary-source-content](https://github.com/SWE-rebench/SWE-rebench-V2) · 2026-10-08 · “SWE-rebench-v2 builder Tools and prompt templates used to build and evaluate SWE-rebench-v2 tasks for the paper.”

## SWE-smith — project-swe-smith

**[SWE-smith](https://github.com/SWE-bench/SWE-smith)**

`project` · `swe-smith` · Date unconfirmed · SFT / trajectory training

Turns repositories into execution environments and creates repair tasks by deliberately breaking existing tests.

**Feedback / validation：** Task-specific execution tests or verifier scores; consult the resource for the exact split.

**Release boundary：** Mutation-generated failures differ from naturally reported bugs; separate repository splits and hidden tests remain important.

GitHub: ★ 795 · push 2026-10-05 · `MIT` · active

[GitHub](https://github.com/SWE-bench/SWE-smith)

Same work: [SWE-smith (paper)](#swe-smith--paper-swe-smith)

**Evidence**

- [primary-source-content](https://github.com/SWE-bench/SWE-smith) · 2026-10-08 · “NeurIPS 2025 Datasets & Benchmarks Track - Spotlight 🔦 SWE-smith is a toolkit for training SWE-agents”

## R2E-Gym — project-r2e-gym

**[R2E-Gym](https://github.com/R2E-Gym/R2E-Gym)**

`project` · `r2e-gym` · Date unconfirmed · SFT / trajectory training

Procedurally curates executable software tasks from commits and studies complementary execution-based and learned verifiers.

**Feedback / validation：** Task-specific execution tests or verifier scores; consult the resource for the exact split.

**Release boundary：** The paper's early abstract uses AgentGym terminology; this is a separate project from WooooDyy/AgentGym.

GitHub: ★ 337 · push 2025-07-13 · `Apache-2.0` · reference

[GitHub](https://github.com/R2E-Gym/R2E-Gym)

Same work: [R2E-Gym (paper)](#r2e-gym--paper-r2e-gym)

**Evidence**

- [primary-source-content](https://github.com/R2E-Gym/R2E-Gym) · 2026-10-08 · “R2E-Gym: Procedural Environment Generation and Hybrid Verifiers for Scaling Open-Weights SWE Agents Naman Jain *,1 ,”

## SWE-Gym — project-swe-gym

**[SWE-Gym](https://github.com/SWE-Gym/SWE-Gym)**

`project` · `swe-gym` · Date unconfirmed · SFT / trajectory training

Pairs repository issues with runnable environments and unit tests, enabling agent fine-tuning and verifier training.

**Feedback / validation：** Task-specific execution tests or verifier scores; consult the resource for the exact split.

**Release boundary：** The initial corpus centers on Python; environment executability does not imply broad language coverage.

GitHub: ★ 748 · push 2025-07-29 · `Apache-2.0` · reference

[GitHub](https://github.com/SWE-Gym/SWE-Gym)

Same work: [SWE-Gym (paper)](#swe-gym--paper-swe-gym)

**Evidence**

- [primary-source-content](https://github.com/SWE-Gym/SWE-Gym) · 2026-10-08 · “Training Software Engineering Agents and Verifiers with SWE-Gym Jiayi Pan *,1 , Xingyao Wang *,2 ,”

## Terminal-Bench — project-terminal-bench

**[Terminal-Bench](https://github.com/harbor-framework/terminal-bench)**

`project` · `terminal-bench` · Date unconfirmed · Evaluation substrate

Packages realistic terminal tasks with isolated execution environments, reference solutions and outcome tests.

**Feedback / validation：** Task-specific execution tests or verifier scores; consult the resource for the exact split.

**Release boundary：** This paper describes Terminal-Bench 2.0; evaluation tasks must remain held out from training.

GitHub: ★ 852 · push 2026-10-07 · `Apache-2.0` · active

[GitHub](https://github.com/harbor-framework/terminal-bench)

Same work: [Terminal-Bench (paper)](#terminal-bench--paper-terminal-bench)

**Evidence**

- [primary-source-content](https://github.com/harbor-framework/terminal-bench) · 2026-10-08 · “Terminal-Bench Terminal-Bench is a benchmark designed to measure the frontier of agent work with a diverse,”

## Gym-Anything / CUA-World — project-gym-anything

**[Gym-Anything / CUA-World](https://github.com/cmu-l3/gym-anything)**

`project` · `gym-anything` · Date unconfirmed · SFT / trajectory training

Automates software installation and realistic task setup with a separate auditing agent, releasing a cross-software CUA corpus.

**Feedback / validation：** State, artifact or rubric evaluation after interaction; evaluator type varies by task.

**Release boundary：** VMs, application dependencies and rubric judging add operational cost; setup evidence is not perfect task verification.

GitHub: ★ 292 · push 2026-09-26 · `MIT` · active

[GitHub](https://github.com/cmu-l3/gym-anything)

Same work: [Gym-Anything / CUA-World (paper)](#gym-anything--cua-world--paper-gym-anything)

**Evidence**

- [primary-source-content](https://github.com/cmu-l3/gym-anything) · 2026-10-08 · “Gym-Anything: Turn Any Software into an Agent Environment Gym-Anything lets you test AI agents on real”

## AgentSynth — project-agentsynth

**[AgentSynth](https://github.com/sunblaze-ucb/AgentSynth)**

`project` · `agentsynth` · Date unconfirmed · Environment / task generation

Composes executed subtasks into harder long-horizon computer tasks and trajectory datasets.

**Feedback / validation：** State, artifact or rubric evaluation after interaction; evaluator type varies by task.

**Release boundary：** Primarily task and trajectory synthesis on existing environments, rather than a new general runtime.

GitHub: ★ 53 · push 2026-04-17 · `Apache-2.0` · reference

[GitHub](https://github.com/sunblaze-ucb/AgentSynth)

Same work: [AgentSynth (paper)](#agentsynth--paper-agentsynth)

**Evidence**

- [primary-source-content](https://github.com/sunblaze-ucb/AgentSynth) · 2026-10-08 · “AgentSynth AgentSynth: Scalable Task Generation for Generalist Computer-Use Agents [ICLR 2026] Below are instructions to run”

## BrowserGym — project-browsergym

**[BrowserGym](https://github.com/ServiceNow/BrowserGym)**

`project` · `browsergym` · Date unconfirmed · Evaluation substrate

Unifies browser observations, actions and benchmark interfaces; AgentLab adds experiment management.

**Feedback / validation：** State, artifact or rubric evaluation after interaction; evaluator type varies by task.

**Release boundary：** A common interface does not make every included benchmark an approved training split.

GitHub: ★ 1,390 · push 2026-10-05 · `NOASSERTION` · active

[GitHub](https://github.com/ServiceNow/BrowserGym)

Same work: [BrowserGym (paper)](#browsergym--paper-browsergym)

**Evidence**

- [primary-source-content](https://github.com/ServiceNow/BrowserGym) · 2026-10-08 · “🛠️ Setup - 🏋 Usage - 💻 Demo - 🌐 Ecosystem - 🚀 AgentLab - 🌟”

## AndroidWorld — project-androidworld

**[AndroidWorld](https://github.com/google-research/android_world)**

`project` · `androidworld` · Date unconfirmed · Evaluation substrate

Builds parameterized Android tasks with emulator setup and programmatic state-based success checks.

**Feedback / validation：** State, artifact or rubric evaluation after interaction; evaluator type varies by task.

**Release boundary：** App versions and emulator configuration affect reproducibility; benchmark success is not a demonstrated training result.

GitHub: ★ 945 · push 2026-10-05 · `Apache-2.0` · active

[GitHub](https://github.com/google-research/android_world)

Same work: [AndroidWorld (paper)](#androidworld--paper-androidworld)

**Evidence**

- [primary-source-content](https://github.com/google-research/android_world) · 2026-10-08 · “AndroidWorld Website • Paper • Tasks • Leaderboard AndroidWorld is an environment for building and benchmarking”

## OSWorld — project-osworld

**[OSWorld](https://github.com/xlang-ai/OSWorld)**

`project` · `osworld` · Date unconfirmed · Evaluation substrate

Provides real desktop task initialization and execution-based evaluators across applications.

**Feedback / validation：** State, artifact or rubric evaluation after interaction; evaluator type varies by task.

**Release boundary：** GUI execution is expensive and platform-sensitive; the benchmark split should not become RL practice data.

GitHub: ★ 3,179 · push 2026-09-14 · `Apache-2.0` · active

[GitHub](https://github.com/xlang-ai/OSWorld)

Same work: [OSWorld (paper)](#osworld--paper-osworld)

**Evidence**

- [primary-source-content](https://github.com/xlang-ai/OSWorld) · 2026-10-08 · “Website • Paper • Doc • Data • Data Viewer • Discord • Cache 📢 Updates”

## WorkArena — project-workarena

**[WorkArena](https://github.com/ServiceNow/WorkArena)**

`project` · `workarena` · Date unconfirmed · Evaluation substrate

Uses ServiceNow workflows as browser tasks with programmatic validation of enterprise actions.

**Feedback / validation：** Task state, trajectory milestones or rubric-based evaluation.

**Release boundary：** Requires suitable ServiceNow instances and credentials; this is not a self-contained offline app simulator.

GitHub: ★ 274 · push 2026-09-28 · `NOASSERTION` · active

[GitHub](https://github.com/ServiceNow/WorkArena)

Same work: [WorkArena (paper)](#workarena--paper-workarena)

**Evidence**

- [primary-source-content](https://github.com/ServiceNow/WorkArena) · 2026-10-08 · “WorkArena: A Benchmark for Evaluating Agents on Knowledge Work Tasks [Benchmark Contents] ♦ [Getting Started] ♦”

## WebArena — project-webarena

**[WebArena](https://github.com/web-arena-x/webarena)**

`project` · `webarena` · Date unconfirmed · Evaluation substrate

Hosts reproducible websites and checks task outcomes to evaluate realistic multi-step web actions.

**Feedback / validation：** State, artifact or rubric evaluation after interaction; evaluator type varies by task.

**Release boundary：** Resetting sites and maintaining deployment images are necessary; published test tasks need contamination controls.

GitHub: ★ 1,619 · push 2025-11-26 · `Apache-2.0` · reference

[GitHub](https://github.com/web-arena-x/webarena)

Same work: [WebArena (paper)](#webarena--paper-webarena)

**Evidence**

- [primary-source-content](https://github.com/web-arena-x/webarena) · 2026-10-08 · “WebArena: A Realistic Web Environment for Building Autonomous Agents WebArena is a standalone, self-hostable web environment”

## MM-ToolSandBox — project-mm-toolsandbox

**[MM-ToolSandBox](https://github.com/apple-aiml-research/ml-mmtoolsandbox)**

`project` · `mm-toolsandbox` · Date unconfirmed · Evaluation substrate

Extends stateful tool evaluation to visual inputs, scenario generation and multi-turn state changes.

**Feedback / validation：** Task state, trajectory milestones or rubric-based evaluation.

**Release boundary：** A visual tool-call benchmark, not proof of an RL-trained agent; image extraction errors require separate analysis.

GitHub: ★ 29 · push 2026-09-11 · `NOASSERTION` · active

[GitHub](https://github.com/apple-aiml-research/ml-mmtoolsandbox)

Same work: [MM-ToolSandBox (paper)](#mm-toolsandbox--paper-mm-toolsandbox)

**Evidence**

- [primary-source-content](https://github.com/apple/ml-mmtoolsandbox) · 2026-10-08 · “MM-ToolSandbox: A Unified Framework for Evaluating Visual Tool-Calling Agents 📖 Paper We propose MM-ToolSandbox, a benchmark”

## CodeGym — project-codegym

**[CodeGym](https://github.com/StigLidu/CodeGym)**

`project` · `codegym` · Date unconfirmed · RL experiments

Extracts callable functions from coding problems to synthesize controllable multi-turn tool-use tasks with executable rewards.

**Feedback / validation：** Code execution against task reference behavior.

**Release boundary：** Code-derived workflows are useful abstractions, but do not fully capture real enterprise service semantics.

GitHub: ★ 41 · push 2025-10-14 · `NOASSERTION` · reference

[GitHub](https://github.com/StigLidu/CodeGym)

Same work: [CodeGym (paper)](#codegym--paper-codegym)

**Evidence**

- [primary-source-content](https://github.com/StigLidu/CodeGym) · 2026-10-08 · “Generalizable End-to-End Tool-Use RL with Synthetic CodeGym Weihua Du, Hailei Gong, Zhan Ling, Kang Liu, Lingfeng”

## τ²-bench — project-tau2

**[τ²-bench](https://github.com/sierra-research/tau2-bench)**

`project` · `tau2` · Date unconfirmed · Evaluation substrate

Models shared state changed by both assistant and simulated user, with compositional tasks and outcome evaluation.

**Feedback / validation：** Shared-world task outcome and policy-adherence checks.

**Release boundary：** User-simulator behavior affects results; treat benchmark tasks as held-out evaluation rather than free training data.

GitHub: ★ 2,181 · push 2026-10-07 · `MIT` · active

[GitHub](https://github.com/sierra-research/tau2-bench)

Same work: [τ²-bench (paper)](#τ²-bench--paper-tau2)

**Evidence**

- [primary-source-content](https://github.com/sierra-research/tau2-bench) · 2026-10-08 · “$\tau$ -Bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains 🚀 τ³-bench is here! From text-only”

## TheAgentCompany — project-theagentcompany

**[TheAgentCompany](https://github.com/TheAgentCompany/TheAgentCompany)**

`project` · `theagentcompany` · Date unconfirmed · Evaluation substrate

Creates a self-contained workplace of websites, files and simulated coworkers for long-horizon professional tasks.

**Feedback / validation：** Task state, trajectory milestones or rubric-based evaluation.

**Release boundary：** A workplace benchmark does not by itself establish train/test separation or reliable RL rewards for new tasks.

GitHub: ★ 792 · push 2025-11-17 · `MIT` · reference

[GitHub](https://github.com/TheAgentCompany/TheAgentCompany)

Same work: [TheAgentCompany (paper)](#theagentcompany--paper-theagentcompany)

**Evidence**

- [primary-source-content](https://github.com/TheAgentCompany/TheAgentCompany) · 2026-10-08 · “The Agent Company: Benchmarking LLM Agents on Consequential Real World Tasks Website • Paper • Leaderboard”

## ToolSandbox — project-toolsandbox

**[ToolSandbox](https://github.com/apple-aiml-research/ToolSandbox)**

`project` · `toolsandbox` · Date unconfirmed · Evaluation substrate

Combines stateful tool execution, user simulation and milestone-based checks over full conversational trajectories.

**Feedback / validation：** Intermediate milestones and final state over the trajectory.

**Release boundary：** Stateful evaluation infrastructure is reusable, but the paper's main evidence is evaluation rather than policy training.

GitHub: ★ 287 · push 2026-09-11 · `NOASSERTION` · active

[GitHub](https://github.com/apple-aiml-research/ToolSandbox)

Same work: [ToolSandbox (paper)](#toolsandbox--paper-toolsandbox)

**Evidence**

- [primary-source-content](https://github.com/apple/ToolSandbox) · 2026-10-08 · “ToolSandbox: A Stateful, Conversational, Interactive Evaluation Benchmark for LLM Tool Use Capabilities This software project accompanies”

## AppWorld — project-appworld

**[AppWorld](https://github.com/StonyBrookNLP/appworld)**

`project` · `appworld` · Date unconfirmed · Evaluation substrate

Simulates interconnected personal apps through executable APIs and validates final state plus unintended side effects.

**Feedback / validation：** State-based unit tests including collateral changes.

**Release boundary：** Train/development/test tasks and software/data licenses have distinct roles; preserve the official split policy.

GitHub: ★ 529 · push 2026-09-04 · `Apache-2.0` · active

[GitHub](https://github.com/StonyBrookNLP/appworld)

Same work: [AppWorld (paper)](#appworld--paper-appworld)

**Evidence**

- [primary-source-content](https://github.com/stonybrooknlp/appworld) · 2026-10-08 · “A Controllable World of Apps and People for Benchmarking Function Calling & Interactive Coding Agents 🏆”

## WebShop — project-webshop

**[WebShop](https://github.com/princeton-nlp/WebShop)**

`project` · `webshop` · Date unconfirmed · RL experiments

Builds a shopping environment with natural-language goals and product-attribute reward signals for interactive learning.

**Feedback / validation：** Task state, trajectory milestones or rubric-based evaluation.

**Release boundary：** Product catalogs and website behavior are simplified; shopping success is a narrow capability measure.

GitHub: ★ 602 · push 2024-09-06 · `MIT` · reference

[GitHub](https://github.com/princeton-nlp/WebShop)

Same work: [WebShop (paper)](#webshop--paper-webshop)

**Evidence**

- [primary-source-content](https://github.com/princeton-nlp/WebShop) · 2026-10-08 · “🛒 WebShop Implementation of the WebShop environment and search agents for the paper: WebShop: Towards Scalable”

## GEM — project-gem

**[GEM](https://github.com/axon-rl/gem)**

`project` · `gem` · Date unconfirmed · RL experiments

Provides a common agent–environment API, asynchronous vectorization and examples connecting varied environments to RL trainers.

**Feedback / validation：** Delegates task reward and correctness to environment authors or connected libraries.

**Release boundary：** Reward timing and per-turn credit assignment differ across trainers; adapters are not interchangeable without checking semantics.

GitHub: ★ 510 · push 2026-01-21 · `Apache-2.0` · reference

[GitHub](https://github.com/axon-rl/gem)

Same work: [GEM (paper)](#gem--paper-gem)

**Evidence**

- [primary-source-content](https://github.com/axon-rl/gem) · 2026-10-08 · “🌍 GEM: A Gym for Agentic LLMs Overview We’re entering the era of experience , where”

## Meta ARE — project-are

**[Meta ARE](https://github.com/facebookresearch/meta-agents-research-environments)**

`project` · `are` · Date unconfirmed · Evaluation substrate

Separates apps, events and scenarios to simulate dynamic worlds and evaluate agents under asynchronous changes.

**Feedback / validation：** Delegates task reward and correctness to environment authors or connected libraries.

**Release boundary：** ARE is distinct from OpenEnv; Gaia2 results primarily establish evaluation behavior, not a released RL training recipe.

GitHub: ★ 561 · push 2026-09-30 · `MIT` · active

[GitHub](https://github.com/facebookresearch/meta-agents-research-environments)

Same work: [Meta ARE (paper)](#meta-are--paper-are)

**Evidence**

- [primary-source-content](https://github.com/facebookresearch/meta-agents-research-environments) · 2026-10-08 · “Meta Agents Research Environments (ARE) A research environment for simulating complex, real-life tasks that require multi-step”

## AgentGym-RL — project-agentgym-rl

**[AgentGym-RL](https://github.com/WooooDyy/AgentGym-RL)**

`project` · `agentgym-rl` · Date unconfirmed · RL experiments

Decouples training and environment services and expands interaction horizons progressively for multi-turn RL.

**Feedback / validation：** Delegates task reward and correctness to environment authors or connected libraries.

**Release boundary：** Requires configuring each underlying environment and its services; it is not a single dependency-free simulator.

GitHub: ★ 874 · push 2026-02-15 · `MIT` · reference

[GitHub](https://github.com/WooooDyy/AgentGym-RL)

Same work: [AgentGym-RL (paper)](#agentgym-rl--paper-agentgym-rl)

**Evidence**

- [primary-source-content](https://github.com/WooooDyy/AgentGym-RL) · 2026-10-08 · “AgentGym-RL: Training LLM Agents for Long-Horizon Decision Making through Multi-Turn Reinforcement Learning 📃 Paper • 🌐”

## AgentGym — project-agentgym

**[AgentGym](https://github.com/WooooDyy/AgentGym)**

`project` · `agentgym` · Date unconfirmed · SFT / trajectory training

Standardizes diverse environment servers and trajectories for generalist agent exploration and iterative learning.

**Feedback / validation：** Delegates task reward and correctness to environment authors or connected libraries.

**Release boundary：** The original AgentEvol study and later AgentGym-RL release use different learning pipelines.

GitHub: ★ 850 · push 2026-05-30 · `MIT` · reference

[GitHub](https://github.com/WooooDyy/AgentGym)

Same work: [AgentGym (paper)](#agentgym--paper-agentgym)

**Evidence**

- [primary-source-content](https://github.com/WooooDyy/AgentGym) · 2026-10-08 · “AgentGym: Evolving Large Language Model-based Agents across Diverse Environments 📃 Paper • 🌐 Project Page •”

## Reasoning Gym — project-reasoning-gym

**[Reasoning Gym](https://github.com/open-thought/reasoning-gym)**

`project` · `reasoning-gym` · Date unconfirmed · RL experiments

Generates adjustable-difficulty reasoning tasks with deterministic verifiers instead of relying on a fixed dataset.

**Feedback / validation：** Procedural reference answers and task-specific scoring functions.

**Release boundary：** Many tasks are single-turn; procedural task diversity is different from stateful tool-interaction diversity.

GitHub: ★ 1,522 · push 2026-04-17 · `Apache-2.0` · reference

[GitHub](https://github.com/open-thought/reasoning-gym)

Same work: [Reasoning Gym (paper)](#reasoning-gym--paper-reasoning-gym)

**Evidence**

- [primary-source-content](https://github.com/open-thought/reasoning-gym) · 2026-10-08 · “Reasoning Gym 🧠 About Reasoning Gym is a community-created Python library of procedural dataset generators and”

## TextArena — project-textarena

**[TextArena](https://github.com/TextArena/TextArena)**

`project` · `textarena` · Date unconfirmed · Trainable interface

Packages text games with rules, multi-player interaction and reward interfaces for agent training and evaluation.

**Feedback / validation：** Task-specific reference answers or game-rule outcomes.

**Release boundary：** Game win rates depend on opponents and rules; they are not direct measurements of workplace competence.

GitHub: ★ 430 · push 2026-10-05 · `MIT` · active

[GitHub](https://github.com/TextArena/TextArena)

Same work: [TextArena (paper)](#textarena--paper-textarena)

**Evidence**

- [primary-source-content](https://github.com/TextArena/TextArena) · 2026-10-08 · “A suite of 100+ single-, two-, and multi-player text-based games for benchmarking and training LLMs. Play”

## Aviary — project-aviary

**[Aviary](https://github.com/Future-House/aviary)**

`project` · `aviary` · Date unconfirmed · RL experiments

Defines language-agent environments with scientific tools and rewards, including literature, cloning and protein tasks.

**Feedback / validation：** Domain-specific goal and scientific-task checks.

**Release boundary：** Domain tools and external services add dependencies; simulated scientific success is not laboratory validation.

GitHub: ★ 284 · push 2026-10-06 · `Apache-2.0` · active

[GitHub](https://github.com/Future-House/aviary)

Same work: [Aviary (paper)](#aviary--paper-aviary)

**Evidence**

- [primary-source-content](https://github.com/Future-House/aviary) · 2026-10-08 · “Aviary Aviary 1 is a gymnasium for defining custom language agent RL environments. The library features”

## ScienceWorld — project-scienceworld

**[ScienceWorld](https://github.com/allenai/ScienceWorld)**

`project` · `scienceworld` · Date unconfirmed · Evaluation substrate

Offers an interactive text science world with compositional experiments and environment-based goal checks.

**Feedback / validation：** Domain-specific goal and scientific-task checks.

**Release boundary：** A simplified simulator is useful for planning research but does not reproduce physical laboratory dynamics.

GitHub: ★ 395 · push 2026-08-20 · `Apache-2.0` · active

[GitHub](https://github.com/allenai/ScienceWorld)

Same work: [ScienceWorld (paper)](#scienceworld--paper-scienceworld)

**Evidence**

- [primary-source-content](https://github.com/allenai/ScienceWorld) · 2026-10-08 · “ScienceWorld ScienceWorld is a text-based virtual environment centered around accomplishing tasks from the standardized elementary science”

## ALFWorld — project-alfworld

**[ALFWorld](https://github.com/alfworld/alfworld)**

`project` · `alfworld` · Date unconfirmed · Imitation learning

Aligns symbolic text interactions with embodied household tasks; BUTLER learns with DAgger imitation learning and transfers the learned policy.

**Feedback / validation：** Domain-specific goal and scientific-task checks.

**Release boundary：** Text and embodied versions differ in perception and execution costs; treat this as foundational context.

GitHub: ★ 881 · push 2026-02-08 · `MIT` · reference

[GitHub](https://github.com/alfworld/alfworld)

Same work: [ALFWorld (paper)](#alfworld--paper-alfworld)

**Evidence**

- [primary-source-content](https://github.com/alfworld/alfworld) · 2026-10-08 · “ALFWorld Aligning Text and Embodied Environments for Interactive Learning Mohit Shridhar , Xingdi (Eric) Yuan ,”

## Hack-Verifiable Environments — project-hack-verifiable

**[Hack-Verifiable Environments](https://github.com/MajoRoth/hack-verifiable-environments)**

`project` · `hack-verifiable` · Date unconfirmed · Evaluation substrate

Embeds detectable reward-hacking opportunities in TextArena to measure proxy exploitation deterministically.

**Feedback / validation：** Deterministic indicators of planted reward-hacking exploits.

**Release boundary：** Designed exploits support measurement; coverage does not exhaust real-world reward hacking.

GitHub: ★ 10 · push 2026-09-21 · `MIT` · active

[GitHub](https://github.com/MajoRoth/hack-verifiable-environments)

Same work: [Hack-Verifiable Environments (paper)](#hack-verifiable-environments--paper-hack-verifiable)

**Evidence**

- [primary-source-content](https://github.com/MajoRoth/hack-verifiable-environments) · 2026-10-08 · “Hack-Verifiable Environments: Towards Evaluating Reward Hacking at Scale Introduction Hack-Verifiable Environments is a new paradigm for”

## AgentEnv (Scale) — project-scale-agentenv

**[AgentEnv (Scale)](https://github.com/scaleapi/agentenv-framework)**

`project` · `scale-agentenv` · Date unconfirmed · Environment infrastructure

SDK and CLI for versioned environment images, composable task execution, plugins and agent grading.

**Feedback / validation：** Delegates task reward and correctness to environment authors or connected libraries.

**Release boundary：** Task authors still supply domain state and reward logic; unrelated agentenv packages are not this framework.

GitHub: ★ 165 · push 2026-10-07 · `Apache-2.0` · active

[GitHub](https://github.com/scaleapi/agentenv-framework)

Same work: [Introducing AgentEnv: An Open-Source Framework for Building RL Environments (blog)](#introducing-agentenv-an-open-source-framework-for-building-rl-environments--blog-scale-agentenv)

**Evidence**

- [primary-source-content](https://github.com/scaleapi/agentenv-framework) · 2026-10-08 · “AgentEnv Framework is a Python SDK and CLI for building, deploying and running agentic environments and”

## OpenEnv — project-openenv

**[OpenEnv](https://github.com/huggingface/OpenEnv)**

`project` · `openenv` · Date unconfirmed · Environment infrastructure

Standardizes isolated environment deployment and interaction through Gym-style APIs and remote services.

**Feedback / validation：** Delegates task reward and correctness to environment authors or connected libraries.

**Release boundary：** Protocol compatibility is not a reward-quality guarantee; pin the API and environment versions.

GitHub: ★ 2,674 · push 2026-10-07 · `BSD-3-Clause` · active

[GitHub](https://github.com/huggingface/OpenEnv)

Same work: [The Open Source Community is backing OpenEnv for Agentic RL (blog)](#the-open-source-community-is-backing-openenv-for-agentic-rl--blog-openenv-community) · [Building the Open Agent Ecosystem Together: Introducing OpenEnv (blog)](#building-the-open-agent-ecosystem-together-introducing-openenv--blog-openenv-launch) · [Scaling OpenEnv: From Free Usage to Thousands of Concurrent Environments (blog)](#scaling-openenv-from-free-usage-to-thousands-of-concurrent-environments--blog-openenv-scaling) · [Training a coding agent using the OpenCode harness in remote HF sandboxes with TRL and OpenEnv (blog)](#training-a-coding-agent-using-the-opencode-harness-in-remote-hf-sandboxes-with-trl-and-openenv--blog-trl-openenv) · [The Building Blocks of Agentic AI: From Kernels to Clusters (blog)](#the-building-blocks-of-agentic-ai-from-kernels-to-clusters--blog-meta-openenv)

**Evidence**

- [primary-source-content](https://github.com/huggingface/OpenEnv) · 2026-10-08 · “OpenEnv: Agentic Execution Environments An e2e framework for creating, deploying and using isolated execution environments for”

## NeMo Gym — project-nemo-gym

**[NeMo Gym](https://github.com/NVIDIA-NeMo/Gym)**

`project` · `nemo-gym` · Date unconfirmed · Environment infrastructure

Provides environment services, verifiers, sandbox adapters and scalable rollout collection for agent post-training.

**Feedback / validation：** Delegates task reward and correctness to environment authors or connected libraries.

**Release boundary：** Gym supplies interaction and rewards; an RL trainer handles policy optimization. Version 0.7.0 changes server APIs.

GitHub: ★ 1,225 · push 2026-10-07 · `Apache-2.0` · active

[GitHub](https://github.com/NVIDIA-NeMo/Gym)

Same work: [How to Train Scientific Agents with Reinforcement Learning (blog)](#how-to-train-scientific-agents-with-reinforcement-learning--blog-nemo-science) · [Mastering Agentic Techniques: AI Agent Reinforcement Learning (blog)](#mastering-agentic-techniques-ai-agent-reinforcement-learning--blog-nvidia-agent-rl)

**Evidence**

- [primary-source-content](https://github.com/NVIDIA-NeMo/Gym) · 2026-10-08 · “NeMo Gym Requirements • Quick Start • Environment Tutorials • Available Environments • Documentation & Resources”

## Verifiers — project-verifiers

**[Verifiers](https://github.com/PrimeIntellect-ai/verifiers)**

`project` · `verifiers` · Date unconfirmed · Environment infrastructure

Builds training and evaluation environments with composable tasksets, harnesses, rubrics and runtimes.

**Feedback / validation：** Delegates task reward and correctness to environment authors or connected libraries.

**Release boundary：** Old single-turn and current v1 abstractions differ; verify examples against the chosen release.

GitHub: ★ 4,679 · push 2026-10-07 · `MIT` · active

[GitHub](https://github.com/PrimeIntellect-ai/verifiers)

Same work: [verifiers v1: Decomposing Tasksets and Harnesses for Agentic RL & Evaluations (blog)](#verifiers-v1-decomposing-tasksets-and-harnesses-for-agentic-rl--evaluations--blog-verifiers-v1) · [Environments Hub: A Community Hub To Scale RL To Open AGI (blog)](#environments-hub-a-community-hub-to-scale-rl-to-open-agi--blog-environments-hub) · [Multi-Agent Systems in PRIME-RL (blog)](#multi-agent-systems-in-prime-rl--blog-multi-agent-rl)

**Evidence**

- [primary-source-content](https://github.com/PrimeIntellect-ai/verifiers) · 2026-10-08 · “Overview verifiers is our library for creating environments to train and evaluate LLMs. verifiers is tightly”

## Harbor — project-harbor

**[Harbor](https://github.com/harbor-framework/harbor)**

`project` · `harbor` · Date unconfirmed · Environment infrastructure

Runs containerized tasks across agents and sandbox providers, supporting parallel evaluation and RL rollout generation.

**Feedback / validation：** Delegates task reward and correctness to environment authors or connected libraries.

**Release boundary：** Harbor is an execution framework; each taskset owns its grading semantics and split restrictions.

GitHub: ★ 5,891 · push 2026-10-07 · `Apache-2.0` · active

[GitHub](https://github.com/harbor-framework/harbor)

**Evidence**

- [primary-source-content](https://github.com/harbor-framework/harbor) · 2026-10-08 · “Harbor Harbor is a framework from the creators of Terminal-Bench for evaluating and optimizing agents and”

## C-World (formerly ToolGym) — project-c-world

**[C-World: A Computer Use Agent Environment Creator](https://github.com/Ziqiao-git/C-World)**

`project` · `c-world` · Date unconfirmed · SFT / trajectory training

Creates computer-use tool environments with task generation, perturbable transitions, and executable or simulated tool responses.

**Feedback / validation：** Task state, trajectory milestones or rubric-based evaluation.

**Release boundary：** The current paper is named C-World while the project page and README retain ToolGym; distinguish live APIs from simulation and account for model-based judging.

GitHub: ★ 10 · push 2026-01-20 · `none` · reference

[GitHub](https://github.com/Ziqiao-git/C-World)

Same work: [C-World (formerly ToolGym) (paper)](#c-world-formerly-toolgym--paper-c-world)

**Evidence**

- [primary-source-content](https://github.com/Ziqiao-git/ToolGym) · 2026-10-08 · “ToolGym is a large-scale, open-world benchmark for evaluating LLM agents”

## MiMo-V2.6 RL OSS Environments (XiaomiMiMo/verl) — project-xiaomi-mimo-verl

**[MiMo-V2.6 RL OSS Environments (XiaomiMiMo/verl)](https://github.com/XiaomiMiMo/verl)**

`project` · `xiaomi-mimo-rl-oss` · Date unconfirmed · Environment infrastructure

Publishes five domain-specific RL environment recipes with task data, Docker images and verifier integration on a verl fork.

**Feedback / validation：** Executable tests, rule checks, rubric-based judging and visual grading vary by domain.

**Release boundary：** The mimo-oss branch needs domain-specific settings and submodules; a public recipe does not establish local reproduction of MiMo training. FineEnvs Explorer is an unofficial community companion for browsing tasks and submitting rollouts, not a Xiaomi-hosted service.

GitHub: ★ 666 · push 2026-09-26 · `Apache-2.0` · active

[GitHub](https://github.com/XiaomiMiMo/verl) · [RL OSS dataset](https://huggingface.co/datasets/XiaomiMiMo/MiMo-V2.6-RL-oss) · [Docker images](https://hub.docker.com/r/xiaomimimo/mimo-v2.6-rl-oss) · [Technical report (companion)](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL/blob/main/MiMo_V2_6_technical_report.pdf) · [Community explorer (unofficial)](https://huggingface.co/spaces/FineEnvs/MiMo-RL-Envs-Explorer)

Same work: [MiMo Agent (mimoagent) (project)](#mimo-agent-mimoagent--project-xiaomi-mimoagent) · [MiMo-V2.6 (report)](#mimo-v26--report-mimo-v26)

**Evidence**

- [primary-source-content](https://github.com/XiaomiMiMo/verl) · 2026-10-08 · “This fork adds reproduction code for five RL environments”
- [primary-source-content](https://huggingface.co/spaces/FineEnvs/MiMo-RL-Envs-Explorer/raw/main/README.md) · 2026-10-08 · “An unofficial explorer for XiaomiMiMo/MiMo-V2.6-RL-oss”

## MiMo Agent (mimoagent) — project-xiaomi-mimoagent

**[MiMo Agent: environment backends, rollout and grading](https://github.com/XiaomiMiMo/mimoagent)**

`project` · `xiaomi-mimo-rl-oss` · Date unconfirmed · Environment infrastructure

Separates agents, model protocols, execution backends and dataset graders, capturing training trajectories and grading final environment state.

**Feedback / validation：** Dataset-specific graders inspect the final execution environment.

**Release boundary：** A rollout library in the same MiMo release; backend support does not guarantee each task is self-contained or independently reproducible.

GitHub: ★ 39 · push 2026-09-21 · `MIT` · active

[GitHub](https://github.com/XiaomiMiMo/mimoagent)

Same work: [MiMo-V2.6 RL OSS Environments (XiaomiMiMo/verl) (project)](#mimo-v26-rl-oss-environments-xiaomimimoverl--project-xiaomi-mimo-verl) · [MiMo-V2.6 (report)](#mimo-v26--report-mimo-v26)

**Evidence**

- [primary-source-content](https://github.com/XiaomiMiMo/mimoagent) · 2026-10-08 · “It connects agents, tools, environments, datasets and graders, and manages rollouts at scale.”

## Terminal-World (skills) — paper-terminal-world-skills

**[Terminal-World: Scaling Terminal-Agent Environments via Agent Skills](https://arxiv.org/abs/2605.20876)**

`paper` · `terminal-world-skills` · 2026-05-20 · SFT / trajectory training

Skills and their dependency graphs jointly specify terminal tasks, executable environments and teacher trajectories.

**Feedback / validation：** Co-derived task, runtime and teacher trajectory must remain aligned; downstream evidence is trajectory training.

**Release boundary：** Distinct from recording-based TerminalWorld; reported SFT gains do not establish online RL readiness or an available generator.

**Implementation status：** Not confirmed

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2605.20876) · 2026-10-08 · “Terminal agents extend Large Language Models with the ability to execute tasks directly in command-line environments, but their progress is”

## SkillSynth — paper-skillsynth

**[Toward Scalable Terminal Task Synthesis via Skill Graphs](https://arxiv.org/abs/2604.25727)**

`paper` · `skillsynth` · 2026-04-28 · SFT / trajectory training

Scenario-mediated skill graphs turn skill compositions into executable terminal tasks and diverse solution trajectories.

**Feedback / validation：** Validates executable task instances and measures diversity in scenario-skill compositions and solution trajectories.

**Release boundary：** Skill coverage and diverse trajectories are different from independently diverse environment families; official code was not confirmed.

**Implementation status：** Not confirmed

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2604.25727) · 2026-10-08 · “Terminal agents have demonstrated strong potential for autonomous command-line execution, yet their training remains constrained by the scarcity of high-quality”

## Terminal-Task-Gen / Nemotron-Terminal — paper-terminal-task-gen

**[On Data Engineering for Scaling LLM Terminal Capabilities](https://arxiv.org/abs/2602.21193)**

`paper` · `terminal-task-gen` · 2026-02-24 · SFT / trajectory training

Combines seed-based and skill-based task generation, environment adapters and trajectory filtering into Terminal-Corpus.

**Feedback / validation：** Task and trajectory filtering, environment adaptation and data-mixture/curriculum experiments.

**Release boundary：** The linked model/data collection is not proof that the entire generation pipeline is released.

**Implementation status：** Not confirmed

[Model and data collection](https://huggingface.co/collections/nvidia/nemotron-terminal)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2602.21193) · 2026-10-08 · “Despite rapid recent progress in the terminal capabilities of large language models, the training data strategies behind state-of-the-art terminal agents”

## SKT — paper-skt

**[SKT: Skill-Use Training at Scale via Verified Synthetic Data Generation](https://arxiv.org/abs/2608.02287)**

`paper` · `skt` · 2026-08-03 · SFT / trajectory training

Builds skill-conditioned task packages and verifies both successful execution and actual use of the required skills before collecting SFT traces.

**Feedback / validation：** Rule-based and agent-based checks, iterative repair, and verification that required skills were actually used.

**Release boundary：** Task success alone does not demonstrate skill use; official pipeline code was not confirmed.

**Implementation status：** Not confirmed

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2608.02287) · 2026-10-08 · “Agent skills have become an important mechanism for equipping language-model agents with reusable procedural knowledge. However, providing skills alone does”

## NexForge — paper-nexforge

**[NexForge: Scaling Agent Capabilities through Requirement-Driven Task Synthesis for LLMs](https://arxiv.org/abs/2607.14186)**

`paper` · `nexforge` · 2026-07-15 · SFT / trajectory training

Compiles real requirements into tasks, retrieves or builds supporting files and runtimes, and collects expert demonstrations.

**Feedback / validation：** Requirement-grounded task construction and expert demonstrations, with task-specific execution resources.

**Release boundary：** Terminal and office task counts are separate from trajectory counts; model releases do not establish generator availability.

**Implementation status：** Not confirmed

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2607.14186) · 2026-10-08 · “Scaling executable agent training data for LLM post-training is bottlenecked by substrate-bound methods that tie task generation to predefined tools,”

## SkillScriptBench — paper-skillscriptbench

**[SkillScriptBench: Benchmarking Self-Evolution of Executable Agent Skill Packages Beyond Markdown](https://arxiv.org/abs/2610.04008)**

`paper` · `skillscriptbench` · 2026-10-02 · Evaluation substrate

Constructs executable skill-package tests with injected script faults and controlled package-editing cases.

**Feedback / validation：** Controlled fault injection and executable package-editing tests distinguish script repair from documentation changes.

**Release boundary：** A benchmark for executable skill repair, not a general world generator; official code was not confirmed.

**Implementation status：** Not confirmed

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2610.04008) · 2026-10-08 · “Executable Agent Skills combine natural-language instructions and scripts into reusable packages for LLM agents, and revising them requires fixing errors”

## Grounded Skill-Following — paper-skill-contracts

**[Beyond Instruction Following: Learning Grounded Skill-Following with Skill Contracts](https://arxiv.org/abs/2610.05161)**

`paper` · `skill-contracts` · 2026-10-04 · RL experiments

Defines runtime skill contracts with admissible actions, state transitions and termination conditions to supply verified progress feedback.

**Feedback / validation：** Checks admissible actions, contract-state transitions and termination to assign verified progress credit.

**Release boundary：** Contracts constrain existing tasks; the paper-linked repository was not accessible in this review, so no implementation is counted.

**Implementation status：** Not confirmed

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2610.05161) · 2026-10-08 · “Instruction following typically enforces discrete, response-level requirements, whereas an expert-authored skill prescribes procedural requirements spanning multiple phases and environment interactions.”

## CLI-Universe — paper-cli-universe

**[CLI-Universe: Towards Verifiable Task Synthesis Engine for Terminal Agents](https://arxiv.org/abs/2606.22883)**

`paper` · `cli-universe` · 2026-06-22 · SFT / trajectory training

Turns capability taxonomies and demand analysis into task blueprints, Docker environments and rubric-gated verifiers.

**Feedback / validation：** Rubric-gated task checks and fail-to-pass testing, including filtering misleading hints.

**Release boundary：** Executable and fail-to-pass checks do not by themselves establish real-world representativeness; no official code confirmed.

**Implementation status：** Not confirmed

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2606.22883) · 2026-10-08 · “While recent LLM-based terminal agents have demonstrated promising capabilities, the scarcity of high-quality, executable training data remains a critical bottleneck.”

## OpenThoughts-Agent — paper-openthoughts-agent

**[OpenThoughts-Agent: Data Recipes for Agentic Models](https://arxiv.org/abs/2606.24855)**

`paper` · `openthoughts-agent` · 2026-06-23 · SFT / trajectory training

Studies task sources, mixtures, teachers, rollout and filtering choices through controlled ablations for terminal-agent data.

**Feedback / validation：** Controlled source, teacher and filtering ablations; the launch RL recipe also verifies tasks in sandboxes.

**Release boundary：** The 2025 launch blog and 2026 paper describe different release stages; training outcomes depend on the whole data recipe.

**Implementation status：** Code

[Code](https://github.com/open-thoughts/OpenThoughts-Agent)

Same work: [OpenThoughts-Agent (project)](#openthoughts-agent--project-openthoughts-agent) · [Launching OpenThoughts-Agent (blog)](#launching-openthoughts-agent--blog-openthoughts-agent)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2606.24855) · 2026-10-08 · “Agentic language models dramatically expand the applications of AI yet little is publicly known about how to curate training data”

## OpenThoughts-Agent — project-openthoughts-agent

**[OpenThoughts-Agent: Data Recipes for Agentic Models](https://github.com/open-thoughts/OpenThoughts-Agent)**

`project` · `openthoughts-agent` · Date unconfirmed · SFT / trajectory training

Studies task sources, mixtures, teachers, rollout and filtering choices through controlled ablations for terminal-agent data.

**Feedback / validation：** Controlled source, teacher and filtering ablations; the launch RL recipe also verifies tasks in sandboxes.

**Release boundary：** The 2025 launch blog and 2026 paper describe different release stages; training outcomes depend on the whole data recipe.

GitHub: ★ 301 · push 2026-09-28 · `Apache-2.0` · active

[GitHub](https://github.com/open-thoughts/OpenThoughts-Agent)

Same work: [OpenThoughts-Agent (paper)](#openthoughts-agent--paper-openthoughts-agent) · [Launching OpenThoughts-Agent (blog)](#launching-openthoughts-agent--blog-openthoughts-agent)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2606.24855) · 2026-10-08 · “Agentic language models dramatically expand the applications of AI yet little is publicly known about how to curate training data”

## TerminalTraj — paper-terminaltraj

**[Large-Scale Terminal Agentic Trajectory Generation from Dockerized Environments](https://arxiv.org/abs/2602.01244)**

`paper` · `terminaltraj` · 2026-02-01 · SFT / trajectory training

Builds Dockerized repository environments, aligned terminal tasks and executable verifiers to collect large-scale trajectories.

**Feedback / validation：** Synthesizes executable validation code for Docker-aligned tasks and filters resulting trajectories.

**Release boundary：** Docker images, tasks and trajectories are distinct counting units; the paper-linked repository returned 404 in this review.

**Implementation status：** Not confirmed

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2602.01244) · 2026-10-08 · “Training agentic models for terminal-based tasks critically depends on high-quality terminal trajectories that capture realistic long-horizon interactions across diverse domains.”

## AgentTrek — paper-agenttrek

**[AgentTrek: Agent Trajectory Synthesis via Guiding Replay with Web Tutorials](https://arxiv.org/abs/2412.09605)**

`paper` · `agenttrek` · 2024-12-12 · SFT / trajectory training

Harvests web tutorials, derives task instructions and guides browser replay, then filters trajectories for training.

**Feedback / validation：** Tutorial-guided browser replay with model-based trajectory verification.

**Release boundary：** Tutorial replay uses existing websites; it does not synthesize independent website backends, and model judges can err.

**Implementation status：** Code

[Code](https://github.com/xlang-ai/AgentTrek) · [Trajectory dataset](https://huggingface.co/datasets/xlangai/AgentTrek)

Same work: [AgentTrek (project)](#agenttrek--project-agenttrek)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2412.09605) · 2026-10-08 · “Graphical User Interface (GUI) agents can automate complex tasks across digital environments, but their development is hindered by the scarcity”

## AgentTrek — project-agenttrek

**[AgentTrek: Agent Trajectory Synthesis via Guiding Replay with Web Tutorials](https://github.com/xlang-ai/AgentTrek)**

`project` · `agenttrek` · Date unconfirmed · SFT / trajectory training

Harvests web tutorials, derives task instructions and guides browser replay, then filters trajectories for training.

**Feedback / validation：** Tutorial-guided browser replay with model-based trajectory verification.

**Release boundary：** Tutorial replay uses existing websites; it does not synthesize independent website backends, and model judges can err.

GitHub: ★ 60 · push 2025-02-21 · `none` · reference

[GitHub](https://github.com/xlang-ai/AgentTrek)

Same work: [AgentTrek (paper)](#agenttrek--paper-agenttrek)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2412.09605) · 2026-10-08 · “Graphical User Interface (GUI) agents can automate complex tasks across digital environments, but their development is hindered by the scarcity”

## OS-Genesis — paper-os-genesis

**[OS-Genesis: Automating GUI Agent Trajectory Construction via Reverse Task Synthesis](https://arxiv.org/abs/2412.19723)**

`paper` · `os-genesis` · 2024-12-27 · SFT / trajectory training

Explores GUI environments before reverse-synthesizing tasks and scores trajectory quality with a trajectory reward model.

**Feedback / validation：** Reverse-synthesized task consistency and a trajectory reward model for quality selection.

**Release boundary：** Constructs tasks and trajectories over existing desktop/mobile environments rather than a new operating-system simulator.

**Implementation status：** Code

[Code](https://github.com/OS-Copilot/OS-Genesis)

Same work: [OS-Genesis (project)](#os-genesis--project-os-genesis)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2412.19723) · 2026-10-08 · “Graphical User Interface (GUI) agents powered by Vision-Language Models (VLMs) have demonstrated human-like computer control capability. Despite their utility in”

## OS-Genesis — project-os-genesis

**[OS-Genesis: Automating GUI Agent Trajectory Construction via Reverse Task Synthesis](https://github.com/OS-Copilot/OS-Genesis)**

`project` · `os-genesis` · Date unconfirmed · SFT / trajectory training

Explores GUI environments before reverse-synthesizing tasks and scores trajectory quality with a trajectory reward model.

**Feedback / validation：** Reverse-synthesized task consistency and a trajectory reward model for quality selection.

**Release boundary：** Constructs tasks and trajectories over existing desktop/mobile environments rather than a new operating-system simulator.

GitHub: ★ 190 · push 2025-10-08 · `none` · reference

[GitHub](https://github.com/OS-Copilot/OS-Genesis)

Same work: [OS-Genesis (paper)](#os-genesis--paper-os-genesis)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2412.19723) · 2026-10-08 · “Graphical User Interface (GUI) agents powered by Vision-Language Models (VLMs) have demonstrated human-like computer control capability. Despite their utility in”

## WebForge — paper-webforge

**[WebForge: Breaking the Realism-Reproducibility-Scalability Trilemma in Browser Agent Benchmark](https://arxiv.org/abs/2604.10988)**

`paper` · `webforge` · 2026-04-13 · Evaluation substrate

Coordinates planning, website generation, refinement and validation to construct self-contained browser benchmarks with difficulty controls.

**Feedback / validation：** Generated-site validation followed by LLM comparison of final answers or website-computed operation codes.

**Release boundary：** Public code primarily covers evaluation; final answers or operation codes are judged by an LLM, not universally deterministic state checks.

**Implementation status：** Partial / associated code

[Partial / associated code](https://github.com/yuandaxia2001/WebForge) · [Benchmark websites and tasks](https://huggingface.co/datasets/yuandaxia/WebForge)

Same work: [WebForge (project)](#webforge--project-webforge)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2604.10988) · 2026-10-08 · “Existing browser agent benchmarks face a fundamental trilemma: real-website benchmarks lack reproducibility due to content drift, controlled environments sacrifice realism”

## WebForge — project-webforge

**[WebForge: Breaking the Realism-Reproducibility-Scalability Trilemma in Browser Agent Benchmark](https://github.com/yuandaxia2001/WebForge)**

`project` · `webforge` · Date unconfirmed · Evaluation substrate

Coordinates planning, website generation, refinement and validation to construct self-contained browser benchmarks with difficulty controls.

**Feedback / validation：** Generated-site validation followed by LLM comparison of final answers or website-computed operation codes.

**Release boundary：** Public code primarily covers evaluation; final answers or operation codes are judged by an LLM, not universally deterministic state checks.

GitHub: ★ 14 · push 2026-04-14 · `Apache-2.0` · reference

[GitHub](https://github.com/yuandaxia2001/WebForge)

Same work: [WebForge (paper)](#webforge--paper-webforge)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2604.10988) · 2026-10-08 · “Existing browser agent benchmarks face a fundamental trilemma: real-website benchmarks lack reproducibility due to content drift, controlled environments sacrifice realism”

## SWE-Universe — paper-swe-universe

**[SWE-Universe: Scale Real-World Verifiable Environments to Millions](https://arxiv.org/abs/2602.02361)**

`paper` · `swe-universe` · 2026-02-02 · RL experiments

A trained building agent converts PRs into verifiable SWE environments using iterative self-checks and in-loop hacking detection.

**Feedback / validation：** Iterative build verification and in-loop hacking detection before using executable tasks for learning.

**Release boundary：** The paper reports 807,693 instances; these are not independent environment families, and official construction code was not confirmed.

**Implementation status：** Not confirmed

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2602.02361) · 2026-10-08 · “We propose SWE-Universe, a scalable and efficient framework for automatically constructing real-world software engineering (SWE) verifiable environments from GitHub pull”

## ScaleSWE — paper-scaleswe

**[Immersion in the GitHub Universe: Scaling Coding Agents to Mastery](https://arxiv.org/abs/2602.09892)**

`paper` · `scaleswe` · 2026-02-10 · SFT / trajectory training

Coordinates environment setup, test generation and problem synthesis agents to curate PR-derived SWE tasks and demonstrations.

**Feedback / validation：** Fail-to-pass reproduction tests plus pass-to-pass regression checks on restored repository states.

**Release boundary：** Paper scale is 100k instances; the repository explicitly describes an initial 20k-instance public subset and uses a separate execution harness.

**Implementation status：** Partial / associated code

[Partial / associated code](https://github.com/AweAI-Team/ScaleSWE) · [Public data collection](https://huggingface.co/collections/AweAI-Team/scale-swe)

Same work: [ScaleSWE (project)](#scaleswe--project-scaleswe)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2602.09892) · 2026-10-08 · “Achieving mastery in real world software engineering tasks is fundamentally bottlenecked by the scarcity of large scale, high quality training”

## ScaleSWE — project-scaleswe

**[Immersion in the GitHub Universe: Scaling Coding Agents to Mastery](https://github.com/AweAI-Team/ScaleSWE)**

`project` · `scaleswe` · Date unconfirmed · SFT / trajectory training

Coordinates environment setup, test generation and problem synthesis agents to curate PR-derived SWE tasks and demonstrations.

**Feedback / validation：** Fail-to-pass reproduction tests plus pass-to-pass regression checks on restored repository states.

**Release boundary：** Paper scale is 100k instances; the repository explicitly describes an initial 20k-instance public subset and uses a separate execution harness.

GitHub: ★ 95 · push 2026-07-21 · `NOASSERTION` · reference

[GitHub](https://github.com/AweAI-Team/ScaleSWE)

Same work: [ScaleSWE (paper)](#scaleswe--paper-scaleswe)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2602.09892) · 2026-10-08 · “Achieving mastery in real world software engineering tasks is fundamentally bottlenecked by the scarcity of large scale, high quality training”

## InSTA — paper-insta

**[InSTA: Towards Internet-Scale Training For Agents](https://arxiv.org/abs/2502.06776)**

`paper` · `insta` · 2025-02-10 · SFT / trajectory training

Annotates websites with tasks, runs agents and filters successful trajectories to build web-interaction data at scale.

**Feedback / validation：** An LLM judges task success and filters collected browser trajectories.

**Release boundary：** Live-site drift and model-judge error remain; website counts are not counts of newly synthesized environments.

**Implementation status：** Code

[Code](https://github.com/data-for-agents/insta)

Same work: [InSTA (project)](#insta--project-insta)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2502.06776) · 2026-10-08 · “The predominant approach for training web navigation agents is to gather human demonstrations for a set of popular websites and”

## InSTA — project-insta

**[InSTA: Towards Internet-Scale Training For Agents](https://github.com/data-for-agents/insta)**

`project` · `insta` · Date unconfirmed · SFT / trajectory training

Annotates websites with tasks, runs agents and filters successful trajectories to build web-interaction data at scale.

**Feedback / validation：** An LLM judges task success and filters collected browser trajectories.

**Release boundary：** Live-site drift and model-judge error remain; website counts are not counts of newly synthesized environments.

GitHub: ★ 56 · push 2025-07-11 · `MIT` · reference

[GitHub](https://github.com/data-for-agents/insta)

Same work: [InSTA (paper)](#insta--paper-insta)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2502.06776) · 2026-10-08 · “The predominant approach for training web navigation agents is to gather human demonstrations for a set of popular websites and”

## RandomWorld — paper-randomworld

**[Procedural Environment Generation for Tool-Use Agents](https://arxiv.org/abs/2506.11045)**

`paper` · `randomworld` · 2025-05-21 · RL and SFT experiments

Procedurally generates interactive tools and compositional tool-use data for both supervised and reinforcement learning.

**Feedback / validation：** Executable synthetic tool interactions and compositional task outcomes provide supervised and RL signals.

**Release boundary：** Synthetic tool semantics do not establish fidelity to production APIs; the public repository has limited user-facing documentation.

**Implementation status：** Code

[Code](https://github.com/coli-saar/randomworld)

Same work: [RandomWorld (project)](#randomworld--project-randomworld)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2506.11045) · 2026-10-08 · “Although the power of LLM tool-use agents has ignited a flurry of recent research in this area, the curation of”

## RandomWorld — project-randomworld

**[Procedural Environment Generation for Tool-Use Agents](https://github.com/coli-saar/randomworld)**

`project` · `randomworld` · Date unconfirmed · RL and SFT experiments

Procedurally generates interactive tools and compositional tool-use data for both supervised and reinforcement learning.

**Feedback / validation：** Executable synthetic tool interactions and compositional task outcomes provide supervised and RL signals.

**Release boundary：** Synthetic tool semantics do not establish fidelity to production APIs; the public repository has limited user-facing documentation.

GitHub: ★ 3 · push 2025-05-02 · `none` · reference

[GitHub](https://github.com/coli-saar/randomworld)

Same work: [RandomWorld (paper)](#randomworld--paper-randomworld)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2506.11045) · 2026-10-08 · “Although the power of LLM tool-use agents has ignited a flurry of recent research in this area, the curation of”

## ClawEnvKit — paper-clawenvkit

**[ClawEnvKit: Automatic Environment Generation for Claw-Like Agents](https://arxiv.org/abs/2604.18543)**

`paper` · `clawenvkit` · 2026-04-20 · Evaluation substrate

Parses natural-language requests into task specifications, mock tools and scoring rules, then validates generated evaluation environments.

**Feedback / validation：** Config validation, mock-service audit logs and structured rule checks, with an optional LLM-judge check type.

**Release boundary：** Mock services and mixed rule/model checks are not live enterprise systems; training potential is not evidence of reported RL gains.

**Implementation status：** Code

[Code](https://github.com/xirui-li/ClawEnvKit)

Same work: [ClawEnvKit (project)](#clawenvkit--project-clawenvkit)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2604.18543) · 2026-10-08 · “Constructing environments for training and evaluating claw-like agents remains a manual, human-intensive process that does not scale. We argue that”

## ClawEnvKit — project-clawenvkit

**[ClawEnvKit: Automatic Environment Generation for Claw-Like Agents](https://github.com/xirui-li/ClawEnvKit)**

`project` · `clawenvkit` · Date unconfirmed · Evaluation substrate

Parses natural-language requests into task specifications, mock tools and scoring rules, then validates generated evaluation environments.

**Feedback / validation：** Config validation, mock-service audit logs and structured rule checks, with an optional LLM-judge check type.

**Release boundary：** Mock services and mixed rule/model checks are not live enterprise systems; training potential is not evidence of reported RL gains.

GitHub: ★ 62 · push 2026-05-07 · `MIT` · reference

[GitHub](https://github.com/xirui-li/ClawEnvKit)

Same work: [ClawEnvKit (paper)](#clawenvkit--paper-clawenvkit)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2604.18543) · 2026-10-08 · “Constructing environments for training and evaluating claw-like agents remains a manual, human-intensive process that does not scale. We argue that”

## TerminalWorld (recordings) — paper-terminalworld-recordings

**[TerminalWorld: Benchmarking Agents on Real-World Terminal Tasks](https://arxiv.org/abs/2605.22535)**

`paper` · `terminalworld-recordings` · 2026-05-21 · Evaluation substrate

Reverse-engineers real terminal recordings into reproducible environments, executable tasks and validated benchmark instances.

**Feedback / validation：** Automated reconstruction/validation with a separately human-verified benchmark subset.

**Release boundary：** Distinct from skill-driven Terminal-World; automatically validated and human-verified subsets have different assurance levels.

**Implementation status：** Code

[Code](https://github.com/EuniAI/TerminalWorld)

Same work: [TerminalWorld (recordings) (project)](#terminalworld-recordings--project-terminalworld-recordings)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2605.22535) · 2026-10-08 · “We introduce TerminalWorld, a scalable data engine that automatically reverse-engineers high-fidelity evaluation tasks from "in-the-wild" terminal recordings. Processing 80,870 terminal”

## TerminalWorld (recordings) — project-terminalworld-recordings

**[TerminalWorld: Benchmarking Agents on Real-World Terminal Tasks](https://github.com/EuniAI/TerminalWorld)**

`project` · `terminalworld-recordings` · Date unconfirmed · Evaluation substrate

Reverse-engineers real terminal recordings into reproducible environments, executable tasks and validated benchmark instances.

**Feedback / validation：** Automated reconstruction/validation with a separately human-verified benchmark subset.

**Release boundary：** Distinct from skill-driven Terminal-World; automatically validated and human-verified subsets have different assurance levels.

GitHub: ★ 48 · push 2026-05-31 · `Apache-2.0` · reference

[GitHub](https://github.com/EuniAI/TerminalWorld)

Same work: [TerminalWorld (recordings) (paper)](#terminalworld-recordings--paper-terminalworld-recordings)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2605.22535) · 2026-10-08 · “We introduce TerminalWorld, a scalable data engine that automatically reverse-engineers high-fidelity evaluation tasks from "in-the-wild" terminal recordings. Processing 80,870 terminal”

## CalibForge — paper-calibforge

**[CalibForge: Adversarial Solver Calibration for Scaling Learnable Terminal Tasks](https://arxiv.org/abs/2608.06352)**

`paper` · `calibforge` · 2026-08-06 · SFT / trajectory training

Revises terminal tasks using verified solver disagreement or strong-pass/weak-fail contrasts to target a learnable difficulty zone.

**Feedback / validation：** Verified solver outcomes target either solver disagreement or strong-pass/weak-fail relations.

**Release boundary：** Calibration is solver-relative, not an absolute hardness score; public data and agent recipes are not the full synthesis engine.

**Implementation status：** Partial / associated code

[Partial / associated code](https://github.com/AweAI-Team/CalibForge)

Same work: [CalibForge (project)](#calibforge--project-calibforge)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2608.06352) · 2026-10-08 · “Training terminal agents requires executable and verifiable tasks that are not merely solvable, but appropriately challenging for learning. Executable validation”

## CalibForge — project-calibforge

**[CalibForge: Adversarial Solver Calibration for Scaling Learnable Terminal Tasks](https://github.com/AweAI-Team/CalibForge)**

`project` · `calibforge` · Date unconfirmed · SFT / trajectory training

Revises terminal tasks using verified solver disagreement or strong-pass/weak-fail contrasts to target a learnable difficulty zone.

**Feedback / validation：** Verified solver outcomes target either solver disagreement or strong-pass/weak-fail relations.

**Release boundary：** Calibration is solver-relative, not an absolute hardness score; public data and agent recipes are not the full synthesis engine.

GitHub: ★ 10 · push 2026-08-07 · `none` · reference

[GitHub](https://github.com/AweAI-Team/CalibForge)

Same work: [CalibForge (paper)](#calibforge--paper-calibforge)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2608.06352) · 2026-10-08 · “Training terminal agents requires executable and verifiable tasks that are not merely solvable, but appropriately challenging for learning. Executable validation”

## DeNovoSWE — paper-denovoswe

**[DeNovoSWE: Scaling Long-Horizon Environments for Generating Entire Repositories from Scratch](https://arxiv.org/abs/2606.10728)**

`paper` · `denovoswe` · 2026-06-09 · SFT / trajectory training

Constructs documentation-to-repository tasks with sandboxed decomposition, critique/repair and difficulty-aware trajectory filtering.

**Feedback / validation：** Unit tests, critic-repair during construction and difficulty-aware filtering of successful trajectories.

**Release boundary：** The agent writes a repository from scratch, but task construction is grounded in existing packages; only part of the data is declared released.

**Implementation status：** Partial / associated code

[Partial / associated code](https://github.com/AweAI-Team/DeNovoSWE)

Same work: [DeNovoSWE (project)](#denovoswe--project-denovoswe)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2606.10728) · 2026-10-08 · “As the capabilities of LLM-based code agents continue to advance, their expected role is expanding beyond localized bug fixing in”

## DeNovoSWE — project-denovoswe

**[DeNovoSWE: Scaling Long-Horizon Environments for Generating Entire Repositories from Scratch](https://github.com/AweAI-Team/DeNovoSWE)**

`project` · `denovoswe` · Date unconfirmed · SFT / trajectory training

Constructs documentation-to-repository tasks with sandboxed decomposition, critique/repair and difficulty-aware trajectory filtering.

**Feedback / validation：** Unit tests, critic-repair during construction and difficulty-aware filtering of successful trajectories.

**Release boundary：** The agent writes a repository from scratch, but task construction is grounded in existing packages; only part of the data is declared released.

GitHub: ★ 47 · push 2026-08-07 · `Apache-2.0` · reference

[GitHub](https://github.com/AweAI-Team/DeNovoSWE)

Same work: [DeNovoSWE (paper)](#denovoswe--paper-denovoswe)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2606.10728) · 2026-10-08 · “As the capabilities of LLM-based code agents continue to advance, their expected role is expanding beyond localized bug fixing in”

## SWE-Playground — paper-swe-playground

**[Training Versatile Coding Agents in Synthetic Environments](https://arxiv.org/abs/2512.12216)**

`paper` · `swe-playground` · 2025-12-13 · SFT / trajectory training

Synthesizes software projects, tasks and execution trajectories from scratch, including test creation and library implementation.

**Feedback / validation：** Separate test-writing and implementation agents mutually validate generated software tasks.

**Release boundary：** Synthetic project diversity differs from real-repository realism; execution requires model and runtime dependencies.

**Implementation status：** Code

[Code](https://github.com/neulab/SWE-Playground)

Same work: [SWE-Playground (project)](#swe-playground--project-swe-playground)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2512.12216) · 2026-10-08 · “Prior works on training software engineering agents have explored utilizing existing resources such as issues on GitHub repositories to construct”

## AgentMercury — paper-agentmercury

**[AgentMercury: Your Agent Can Synthesize Verifiable Environments for Business Scenarios at scale](https://arxiv.org/abs/2608.20634)**

`paper` · `agentmercury` · 2026-08-21 · RL and SFT experiments

Instantiates persistent business worlds with state, tools and cross-service invariants before deriving tasks and trajectories.

**Feedback / validation：** Executable cross-service invariants constrain generated worlds; policy RL and construction-trace tuning are evaluated separately.

**Release boundary：** Public corpus samples are not the complete executable world library; construction-model tuning and policy RL are separate experiments.

**Implementation status：** Not confirmed

[Public corpus sample](https://huggingface.co/datasets/Minbyul/AgentMercury-corpus-sample)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2608.20634) · 2026-10-08 · “Agents learn to act through interaction with environments, yet the environments used for training are often manually constructed or synthesized”

## Launching OpenThoughts-Agent — blog-openthoughts-agent

**[Launching the OpenThoughts-Agent Project | OpenThoughts](https://www.openthoughts.ai/blog/agent)**

`blog` · `openthoughts-agent` · 2025-12-05 · RL and SFT experiments

Describes the initial task/teacher ablations, SFT trajectories and a verified NL2Bash RL data pipeline.

**Feedback / validation：** Controlled source, teacher and filtering ablations; the launch RL recipe also verifies tasks in sandboxes.

**Release boundary：** This launch release predates the 2026 paper and does not imply every planned generation component was open at publication.

Same work: [OpenThoughts-Agent (paper)](#openthoughts-agent--paper-openthoughts-agent) · [OpenThoughts-Agent (project)](#openthoughts-agent--project-openthoughts-agent)

**Evidence**

- [primary-source-content](https://www.openthoughts.ai/blog/agent) · 2026-10-08 · “Launching the OpenThoughts-Agent Project | OpenThoughts”

## Browser Use benchmark construction — blog-browser-use-bench

**[Browser Agent Benchmark: Comparing LLM Models for Web Automation](https://browser-use.com/posts/ai-browser-agent-benchmark)**

`blog` · `browser-use-bench` · 2026-01-31 · Evaluation substrate

Explains live-web task selection, encrypted test distribution and model-based success judging for BU Bench.

**Feedback / validation：** Live-web execution is scored by a model-based success judge, with reported human agreement checks.

**Release boundary：** Live websites drift and LLM judges can disagree with people; a benchmark task set is not a set of new offline worlds.

Same work: [benchmark (project)](#benchmark--project-browser-use-bench)

**Evidence**

- [primary-source-content](https://browser-use.com/posts/ai-browser-agent-benchmark) · 2026-10-08 · “Browser Agent Benchmark: Comparing LLM Models for Web Automation”

## benchmark — project-browser-use-bench

**[Browser Agent Benchmark: Comparing LLM Models for Web Automation](https://github.com/browser-use/benchmark)**

`project` · `browser-use-bench` · Date unconfirmed · Evaluation substrate

Explains live-web task selection, encrypted test distribution and model-based success judging for BU Bench.

**Feedback / validation：** Live-web execution is scored by a model-based success judge, with reported human agreement checks.

**Release boundary：** Live websites drift and LLM judges can disagree with people; a benchmark task set is not a set of new offline worlds.

GitHub: ★ 149 · push 2026-10-01 · `none` · active

[GitHub](https://github.com/browser-use/benchmark)

Same work: [Browser Use benchmark construction (blog)](#browser-use-benchmark-construction--blog-browser-use-bench)

**Evidence**

- [primary-source-content](https://browser-use.com/posts/ai-browser-agent-benchmark) · 2026-10-08 · “Browser Use benchmark construction”

## Tracing Agent Harness Behavior with NVIDIA NeMo Relay — blog-nemo-relay-tracing

**[Tracing Agent Harness Behavior with NVIDIA NeMo Relay | NVIDIA Technical Blog](https://developer.nvidia.com/blog/?p=123038)**

`blog` · `nemo-relay-tracing` · 2026-09-30 · Technical account

Demonstrates ordered event and trajectory capture, paired with task verification and harness-behavior comparisons.

**Feedback / validation：** Pairs task-specific success checks with ordered events, trajectory traces and process/cost observations.

**Release boundary：** Observability records behavior; a complete trace is neither a new environment nor proof of successful task completion.

**Evidence**

- [primary-source-content](https://developer.nvidia.com/blog/?p=123038) · 2026-10-08 · “Tracing Agent Harness Behavior with NVIDIA NeMo Relay”

## How to Evaluate AI Agents From Tool Calls to Task Completion — blog-nvidia-agent-evaluation

**[How to Evaluate AI Agents From Tool Calls to Task Completion | NVIDIA Technical Blog](https://developer.nvidia.com/blog/how-to-evaluate-ai-agents-from-tool-calls-to-task-completion/)**

`blog` · `nvidia-agent-evaluation` · 2026-09-21 · Quality / failure study

Separates step-level process scoring from end-state task completion and links reliability to stateful evaluation design.

**Feedback / validation：** Separates process scoring from task completion verified against the final environment state.

**Release boundary：** A design article, not independent replication or a general-purpose environment generator.

**Evidence**

- [primary-source-content](https://developer.nvidia.com/blog/how-to-evaluate-ai-agents-from-tool-calls-to-task-completion/) · 2026-10-08 · “How to Evaluate AI Agents From Tool Calls to Task Completion”

## Announcing LiteCoder-Terminal Preview — blog-litecoder

**[Announcing LiteCoder-Terminal: Lightweight Terminal Agents with <1k Synthesized Trajectories](https://huggingface.co/blog/Lite-Coder/litecoder-terminal-preview)**

`blog` · `litecoder` · 2025-12-18 · SFT / trajectory training

Details taxonomy-driven task sampling, feasibility filtering, initial-state construction in Docker and trajectory collection.

**Feedback / validation：** Feasibility judging and Docker initial-state construction; later releases add reference solutions and verifier test suites.

**Release boundary：** The preview blog and later repository release differ in scale; LLM feasibility judging alone is not an executable verifier.

Same work: [LiteCoder (project)](#litecoder--project-litecoder)

**Evidence**

- [primary-source-content](https://huggingface.co/blog/Lite-Coder/litecoder-terminal-preview) · 2026-10-08 · “Announcing LiteCoder-Terminal: Lightweight Terminal Agents with <1k Synthesized Trajectories”

## LiteCoder — project-litecoder

**[Announcing LiteCoder-Terminal: Lightweight Terminal Agents with <1k Synthesized Trajectories](https://github.com/icip-cas/LiteCoder)**

`project` · `litecoder` · Date unconfirmed · SFT / trajectory training

Releases terminal trajectories and Harbor-format environments; documents a five-stage instruction-to-environment synthesis recipe.

**Feedback / validation：** Feasibility judging and Docker initial-state construction; later releases add reference solutions and verifier test suites.

**Release boundary：** The current README describes 11,255 trajectories and 602 environments; these are later artifacts, not the sub-1k preview release.

GitHub: ★ 17 · push 2026-05-29 · `none` · reference

[GitHub](https://github.com/icip-cas/LiteCoder)

Same work: [Announcing LiteCoder-Terminal Preview (blog)](#announcing-litecoder-terminal-preview--blog-litecoder)

**Evidence**

- [primary-source-content](https://huggingface.co/blog/Lite-Coder/litecoder-terminal-preview) · 2026-10-08 · “Announcing LiteCoder-Terminal Preview”

## Endless Terminals — paper-endless-terminals

**[Endless Terminals: Scaling RL Environments for Terminal Agents](https://arxiv.org/abs/2601.16443)**

`paper` · `endless-terminals` · 2026-01-23 · RL experiments

Generates task descriptions, builds and validates containers, creates completion tests and filters for solvability before PPO training.

**Feedback / validation：** Executable initial/final-state or fail-to-pass tests; reference solutions establish solvability.

**Release boundary：** Generation, execution and optimization are separate stages; reported gains do not prove arbitrary generated tests are reliable.

**Implementation status：** Code

[Code](https://github.com/kanishkg/endless-terminals)

Same work: [Endless Terminals (project)](#endless-terminals--project-endless-terminals)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2601.16443) · 2026-10-08 · “Environments are the bottleneck for self-improving agents. Current terminal benchmarks were built for evaluation, not training; reinforcement learning requires a”

## Endless Terminals — project-endless-terminals

**[Endless Terminals: Scaling RL Environments for Terminal Agents](https://github.com/kanishkg/endless-terminals)**

`project` · `endless-terminals` · Date unconfirmed · RL experiments

Generates task descriptions, builds and validates containers, creates completion tests and filters for solvability before PPO training.

**Feedback / validation：** Executable initial/final-state or fail-to-pass tests; reference solutions establish solvability.

**Release boundary：** Generation, execution and optimization are separate stages; reported gains do not prove arbitrary generated tests are reliable.

GitHub: ★ 147 · push 2026-03-31 · `Apache-2.0` · reference

[GitHub](https://github.com/kanishkg/endless-terminals)

Same work: [Endless Terminals (paper)](#endless-terminals--paper-endless-terminals)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2601.16443) · 2026-10-08 · “Environments are the bottleneck for self-improving agents. Current terminal benchmarks were built for evaluation, not training; reinforcement learning requires a”

## CLI-Gym — paper-cli-gym

**[CLI-Gym: Scalable CLI Task Generation via Agentic Environment Inversion](https://arxiv.org/abs/2602.10999)**

`paper` · `cli-gym` · 2026-02-11 · SFT / trajectory training

Explores healthy environment histories and inverts them into reproducible runtime failures, then packages repair tasks and successful traces.

**Feedback / validation：** Executable initial/final-state or fail-to-pass tests; reference solutions establish solvability.

**Release boundary：** Produces environment-intensive tasks from existing repositories; instance counts exceed repository/image counts and must not be conflated.

**Implementation status：** Code

[Code](https://github.com/LiberCoders/CLI-Gym)

Same work: [CLI-Gym (project)](#cli-gym--project-cli-gym)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2602.10999) · 2026-10-08 · “Agentic coding requires agents to effectively interact with runtime environments, e.g., command line interfaces (CLI), so as to complete tasks”

## CLI-Gym — project-cli-gym

**[CLI-Gym: Scalable CLI Task Generation via Agentic Environment Inversion](https://github.com/LiberCoders/CLI-Gym)**

`project` · `cli-gym` · Date unconfirmed · SFT / trajectory training

Explores healthy environment histories and inverts them into reproducible runtime failures, then packages repair tasks and successful traces.

**Feedback / validation：** Executable initial/final-state or fail-to-pass tests; reference solutions establish solvability.

**Release boundary：** Produces environment-intensive tasks from existing repositories; instance counts exceed repository/image counts and must not be conflated.

GitHub: ★ 141 · push 2026-06-30 · `MIT` · reference

[GitHub](https://github.com/LiberCoders/CLI-Gym)

Same work: [CLI-Gym (paper)](#cli-gym--paper-cli-gym)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2602.10999) · 2026-10-08 · “Agentic coding requires agents to effectively interact with runtime environments, e.g., command line interfaces (CLI), so as to complete tasks”

## SWE-Playground — project-swe-playground

**[Training Versatile Coding Agents in Synthetic Environments](https://github.com/neulab/SWE-Playground)**

`project` · `swe-playground` · Date unconfirmed · SFT / trajectory training

Synthesizes software projects, tasks and execution trajectories from scratch, including test creation and library implementation.

**Feedback / validation：** Separate test-writing and implementation agents mutually validate generated software tasks.

**Release boundary：** Synthetic project diversity differs from real-repository realism; execution requires model and runtime dependencies.

GitHub: ★ 22 · push 2026-01-11 · `MIT` · reference

[GitHub](https://github.com/neulab/SWE-Playground)

Same work: [SWE-Playground (paper)](#swe-playground--paper-swe-playground)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2512.12216) · 2026-10-08 · “Prior works on training software engineering agents have explored utilizing existing resources such as issues on GitHub repositories to construct”

## CompoWorld — paper-compoworld

**[CompoWorld: Compositional Environment Scaling for General Agents](https://arxiv.org/abs/2609.33665)**

`paper` · `compoworld` · 2026-09-27 · RL and SFT experiments

Composes verified services through shared typed state and interfaces; synthesizes cross-service tasks from dependency graphs.

**Feedback / validation：** Completion and rubric checks; SFT and RL experiments.

**Release boundary：** Services and tools are not independent environments. The associated repository exposes examples; full reproduction is not established.

**Implementation status：** Partial / associated code

[Home](https://github.com/AllSpark-Research/AgentEnv) · [Partial / associated code](https://github.com/AllSpark-Research/AgentEnv) · [CompoWorld examples](https://github.com/AllSpark-Research/AgentEnv/blob/main/CompoWorld/README.md)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2609.33665) · 2026-10-08 · “CompoWorld”

## Kimi K3 — report-kimi-k3

**[Kimi K3: Open Frontier Intelligence](https://arxiv.org/abs/2607.24653)**

`report` · `kimi-k3` · 2026-07-27 · Technical account

Describes composable agent environments, task synthesis and persistent sandbox state for long-horizon interaction.

**Release boundary：** The report is not a release of every training environment. AgentENV is a separately linked sandbox implementation.

**Implementation status：** Not confirmed

[Home](https://github.com/MoonshotAI/Kimi-K3) · [AgentENV sandbox code](https://github.com/kvcache-ai/AgentENV)

Same work: [Kimi K3 Tech Blog: Open Frontier Intelligence (blog)](#kimi-k3-tech-blog-open-frontier-intelligence--blog-kimi-k3)

[Report section index](technical_report_sections.md#kimi-k3)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2607.24653) · 2026-10-08 · “Kimi K3”

## DeepSeek V4 — report-deepseek-v4

**[DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence](https://arxiv.org/abs/2606.19348)**

`report` · `deepseek-v4` · 2026-04-26 · Technical account

Documents DSec execution substrates and interruption-safe rollout services inside a broader model report.

**Release boundary：** This report describes an earlier command-log recovery design; the later DSec paper describes decoupled rollout execution.

**Implementation status：** Not confirmed

[Home](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)

[Report section index](technical_report_sections.md#deepseek-v4)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2606.19348) · 2026-10-08 · “DeepSeek V4”

## GLM-4.5 — report-glm45

**[GLM-4.5: Agentic, Reasoning, and Coding (ARC) Foundation Models](https://arxiv.org/abs/2508.06471)**

`report` · `glm45` · 2025-08-08 · Technical account

Combines task synthesis, isolated execution and an asynchronous trajectory pool for agentic learning.

**Release boundary：** The report discloses methods; it does not establish release of the full training task inventory.

**Implementation status：** Not confirmed

[Report section index](technical_report_sections.md#glm-45)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2508.06471) · 2026-10-08 · “GLM-4.5”
- [pdf-title-page](https://arxiv.org/pdf/2508.06471v1) · 2026-10-08 · “GLM-4.5 Team”

## DeepSeek Elastic Compute (DSec) — paper-dsec

**[DeepSeek Elastic Compute (DSec): A Sandbox Infrastructure for Effective Agentic Training at Scale](https://arxiv.org/abs/2609.22978)**

`paper` · `dsec` · 2026-09-19 · Environment infrastructure

Unifies function calls, containers, microVMs and full VMs; supports agent-built reusable environments and pause/resume for long-running rollouts.

**Feedback / validation：** Operational evidence for construction, isolation and lifecycle management; not a standalone task benchmark.

**Release boundary：** A production infrastructure paper; no official public DSec implementation is confirmed. Related projects such as 3FS are not the complete DSec platform.

**Implementation status：** Not confirmed

[Report section index](technical_report_sections.md#deepseek-elastic-compute-dsec)

**Evidence**

- [primary-source-content](https://arxiv.org/abs/2609.22978) · 2026-10-08 · “DeepSeek Elastic Compute (DSec)”

## Introducing Codex — blog-openai-codex

**[Introducing Codex](https://openai.com/index/introducing-codex/)**

`blog` · `openai-codex` · 2025-05-16 · RL experiments

Real-world coding RL with execution feedback; each task runs in a cloud sandbox loaded with the repository.

**Background only — excluded from the selected catalog：** Product and training overview without enough detail on environment construction, task sampling or reward implementation.

**Release boundary：** Describes training and product execution; does not release the internal training environment fleet.

**Evidence**

- [primary-source-content](https://openai.com/index/introducing-codex/) · 2026-10-08 · “Introducing Codex”

## Computer-Using Agent — blog-openai-cua

**[Computer-Using Agent](https://openai.com/index/computer-using-agent/)**

`blog` · `openai-cua` · 2025-01-23 · RL experiments

Screenshot observations and mouse/keyboard actions define the computer-use interaction loop.

**Background only — excluded from the selected catalog：** Primarily a computer-use model and observation/action overview, with limited environment-production detail.

**Release boundary：** The model and product announcement is not an open environment generator.

**Evidence**

- [primary-source-content](https://openai.com/index/computer-using-agent/) · 2026-10-08 · “Computer-Using Agent”

## Demystifying evals for AI agents — blog-anthropic-evals

**[Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)**

`blog` · `anthropic-evals` · 2026-01-09 · Quality / failure study

Separates tasks, trials, graders and outcomes; discusses clean isolated environments and state-based checks.

**Supporting reference：** Supports execution, evaluation, simulation or quality control, but is not a direct focus on scalable environment production or effective training-data production; retained in its subject category.

**Article research question：** What makes task grading valid?

**Concrete content**

- Distinguishes tasks, trials, graders and outcomes
- Clean isolated task execution
- Checks final state rather than only agent claims

**Release boundary：** Evaluation methodology, not a released training curriculum.

**Evidence**

- [primary-source-content](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) · 2026-10-08 · “Demystifying evals for AI agents”

## Quantifying infrastructure noise in agentic coding evals — blog-anthropic-infra-noise

**[Quantifying infrastructure noise in agentic coding evals](https://www.anthropic.com/engineering/infrastructure-noise)**

`blog` · `anthropic-infra-noise` · 2026-02-05 · Quality / failure study

Controlled resource-allocation experiments show that sandbox limits change reliability and what coding evaluations measure.

**Supporting reference：** Supports execution, evaluation, simulation or quality control, but is not a direct focus on scalable environment production or effective training-data production; retained in its subject category.

**Article research question：** How do resource limits change evaluation?

**Concrete content**

- Compares sandbox resource quotas
- Analyzes measurement noise from runtime limits
- Distinguishes environment failures from model failures

**Release boundary：** Results concern the tested models and benchmarks; avoid treating a resource setting as universally optimal.

**Evidence**

- [primary-source-content](https://www.anthropic.com/engineering/infrastructure-noise) · 2026-10-08 · “Quantifying infrastructure noise in agentic coding evals”

## Training a Misaligned Reward Seeker — blog-anthropic-reward-seeker

**[Training a Misaligned Reward Seeker](https://alignment.anthropic.com/2026/reward-seeker/)**

`blog` · `anthropic-reward-seeker` · 2026-08 · Quality / failure study

A deliberately adversarial training study uses vulnerable environments to examine reward exploitation and its detection.

**Supporting reference：** Supports execution, evaluation, simulation or quality control, but is not a direct focus on scalable environment production or effective training-data production; retained in its subject category.

**Article research question：** How can environment exploits and reward hacking be studied?

**Concrete content**

- Deliberately adversarial training setup
- Vulnerable environments supply feedback
- Studies exploitative behavior and detection

**Release boundary：** An intentionally pessimistic research setup, not a claim that deployed models use these environments; publication month is August 2026.

**Evidence**

- [primary-source-content](https://alignment.anthropic.com/2026/reward-seeker/) · 2026-10-08 · “Training a Misaligned Reward Seeker”

## Genie 3: A new frontier for world models — blog-deepmind-genie3

**[Genie 3: A new frontier for world models](https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/)**

`blog` · `deepmind-genie3` · 2025-08-05 · Environment / task generation

Generates interactive visual worlds from prompts for exploration and agent research.

**Supporting reference：** Supports execution, evaluation, simulation or quality control, but is not a direct focus on scalable environment production or effective training-data production; retained in its subject category.

**Article research question：** How can prompts generate interactive worlds?

**Concrete content**

- Prompt-conditioned visual world generation
- Actions drive subsequent observations
- Supports exploration with consistency limits

**Release boundary：** A learned visual simulator, not a deterministic physics engine or an openly released environment implementation.

**Evidence**

- [primary-source-content](https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/) · 2026-10-08 · “Genie 3: A new frontier for world models”

## SIMA 2: An agent that plays, reasons, and learns with you in virtual 3D worlds — blog-deepmind-sima2

**[SIMA 2: An agent that plays, reasons, and learns with you in virtual 3D worlds](https://deepmind.google/blog/sima-2-an-agent-that-plays-reasons-and-learns-with-you-in-virtual-3d-worlds/)**

`blog` · `deepmind-sima2` · 2025-11-13 · Technical account

Uses diverse virtual worlds for embodied interaction and examines generalization to Genie-generated worlds.

**Supporting reference：** Supports execution, evaluation, simulation or quality control, but is not a direct focus on scalable environment production or effective training-data production; retained in its subject category.

**Article research question：** Can generated worlds support agent interaction?

**Concrete content**

- Interaction across diverse virtual worlds
- Tests transfer to Genie-generated worlds
- Provides evidence of agents using generated environments

**Release boundary：** A research preview; the complete training environment suite is not released by this blog.

**Evidence**

- [primary-source-content](https://deepmind.google/blog/sima-2-an-agent-that-plays-reasons-and-learns-with-you-in-virtual-3d-worlds/) · 2026-10-08 · “SIMA 2: An agent that plays, reasons, and learns with you in virtual 3D worlds”

## Qwen3-Coder: Agentic Coding in the World — blog-qwen3-coder

**[Qwen3-Coder: Agentic Coding in the World](https://qwenlm.github.io/blog/qwen3-coder/)**

`blog` · `qwen3-coder` · 2025-07-22 · RL experiments

Scales execution-verified coding tasks and long-horizon RL with 20,000 independent environments in parallel.

**Background only — excluded from the selected catalog：** Parallel-environment scale is not an environment-construction method; mechanism detail is insufficient for the core table.

**Release boundary：** The claimed number is parallel environments, not 20,000 task types; Qwen Code release does not release the whole environment fleet.

**Evidence**

- [primary-source-content](https://qwenlm.github.io/blog/qwen3-coder/) · 2026-10-08 · “Qwen3-Coder: Agentic Coding in the World”

## Kimi K3 Tech Blog: Open Frontier Intelligence — blog-kimi-k3

**[Kimi K3 Tech Blog: Open Frontier Intelligence](https://www.kimi.com/blog/kimi-k3)**

`blog` · `kimi-k3` · Date unconfirmed · Technical account

Introduces Kimi K3 agentic capabilities and long-running kernel work; the technical report supplies the detailed environment mechanisms.

**Background only — excluded from the selected catalog：** Blog is a capability overview; environment mechanisms are already indexed in specific technical-report sections.

**Release boundary：** An overview, not the source for every environment-construction claim; see the separately indexed report. Exact blog date unconfirmed.

Same work: [Kimi K3 (report)](#kimi-k3--report-kimi-k3)

**Evidence**

- [primary-source-content](https://www.kimi.com/blog/kimi-k3) · 2026-10-08 · “Kimi K3 Tech Blog: Open Frontier Intelligence”

## MiMo-V2.6 — report-mimo-v26

**[MiMo-V2.6: Scaling Reinforcement Learning Towards Self-Improvement](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL/blob/73875d00b30a89ef8cc353a0b60b0e9f9561952d/MiMo_V2_6_technical_report.pdf)**

`report` · `xiaomi-mimo-rl-oss` · Date unconfirmed · RL experiments

Details environment and verifier construction across domains, multi-harness execution and experiments on released environments.

**Release boundary：** The public task subset is distinct from the full training distribution. PDF pinned to a repository revision; first report publication date unconfirmed.

**Implementation status：** Partial / associated code

[Home](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL) · [Partial / associated code](https://github.com/XiaomiMiMo/verl)

Same work: [MiMo-V2.6 RL OSS Environments (XiaomiMiMo/verl) (project)](#mimo-v26-rl-oss-environments-xiaomimimoverl--project-xiaomi-mimo-verl) · [MiMo Agent (mimoagent) (project)](#mimo-agent-mimoagent--project-xiaomi-mimoagent)

[Report section index](technical_report_sections.md#mimo-v26)

**Evidence**

- [pdf-sections-and-page-locations](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL/resolve/73875d00b30a89ef8cc353a0b60b0e9f9561952d/MiMo_V2_6_technical_report.pdf) · 2026-10-08 · “MiMo-V2.6: Scaling Reinforcement Learning Towards Self-Improvement”

## From model to agent: Equipping the Responses API with a computer environment — blog-openai-computer-env

**[From model to agent: Equipping the Responses API with a computer environment](https://openai.com/index/equip-responses-api-computer-environment/)**

`blog` · `openai-computer-env` · 2026-03-11 · Environment infrastructure

Describes container workspaces, shell execution, network sidecars, skill files and context compaction for stateful computer interaction.

**Background only — excluded from the selected catalog：** Useful runtime engineering, but focused on API execution rather than environment/task or interaction-data production.

**Relevant passages (original headings / locator notes)：** Computer environment, shell, skills and compaction engineering passages

**Release boundary：** Runtime engineering account; it does not release a training-environment generator or task pool.

**Evidence**

- [primary-source-content](https://openai.com/index/equip-responses-api-computer-environment/) · 2026-10-08 · “From model to agent”

## Introducing SWE-bench Verified — blog-openai-swe-verified

**[Introducing SWE-bench Verified](https://openai.com/index/introducing-swe-bench-verified/)**

`blog` · `swe-bench-verified` · 2024-08-13 · Evaluation substrate

Human review of specifications, test validity and solvability filters SWE-bench tasks, with Docker execution improving reproducibility.

**Supporting reference：** Supports execution, evaluation, simulation or quality control, but is not a direct focus on scalable environment production or effective training-data production; retained in its subject category.

**Article research question：** How are valid software-evaluation tasks selected?

**Concrete content**

- Human checks of specification and solvability
- Checks that tests match requirements
- Runs selected tasks in a Docker harness

**Relevant passages (original headings / locator notes)：** Task selection and evaluation-harness discussion

**Release boundary：** Evaluation-subset construction, not a new training-task factory; the post was updated on 2025-02-24.

**Evidence**

- [primary-source-content](https://openai.com/index/introducing-swe-bench-verified/) · 2026-10-08 · “Introducing SWE-bench Verified”

## Why SWE-bench Verified no longer measures frontier coding capabilities — blog-openai-swe-audit

**[Why SWE-bench Verified no longer measures frontier coding capabilities](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/)**

`blog` · `swe-bench-audit` · 2026-02-23 · Quality / failure study

Audits overly narrow tests, underspecification and contamination, showing why executable tests alone do not ensure valid task grading.

**Supporting reference：** Supports execution, evaluation, simulation or quality control, but is not a direct focus on scalable environment production or effective training-data production; retained in its subject category.

**Article research question：** Why can executable tests still misgrade?

**Concrete content**

- Analyzes narrow tests and underspecification
- Audits a selected difficult-task subset
- Examines contamination of evaluation results

**Relevant passages (original headings / locator notes)：** Test-defect audit and contamination analysis

**Release boundary：** The defect audit focuses on selected difficult tasks; its rate must not be generalized to the entire benchmark.

**Evidence**

- [primary-source-content](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/) · 2026-10-08 · “Why SWE-bench Verified no longer measures frontier coding capabilities”

## PaperBench: Evaluating AI’s Ability to Replicate AI Research — blog-openai-paperbench

**[PaperBench: Evaluating AI’s Ability to Replicate AI Research](https://openai.com/index/paperbench/)**

`blog` · `paperbench` · 2025-04-02 · Evaluation substrate

Decomposes paper replication into hierarchical rubrics co-developed with authors and separately evaluates automated judges.

**Supporting reference：** Supports execution, evaluation, simulation or quality control, but is not a direct focus on scalable environment production or effective training-data production; retained in its subject category.

**Article research question：** How can paper replication become gradable tasks?

**Concrete content**

- Decomposes replication goals hierarchically
- Co-develops rubrics with paper authors
- Separately benchmarks automated judges

**Relevant passages (original headings / locator notes)：** Announcement text: task decomposition, author-built rubrics and judge evaluation

**Release boundary：** Official research announcement; full environment and grading details require the linked paper and code.

**Evidence**

- [primary-source-content](https://openai.com/index/paperbench/) · 2026-10-08 · “Rubrics are co-developed with the author(s)”

## Introducing deep research — blog-openai-deep-research

**[Introducing deep research](https://openai.com/index/introducing-deep-research/)**

`blog` · `openai-deep-research` · 2025-02-02 · RL experiments

Describes end-to-end RL on difficult browsing and reasoning tasks, including search, Python use and backtracking.

**Background only — excluded from the selected catalog：** Mentions browsing RL without explaining how training tasks, environment state or graders are constructed.

**Relevant passages (original headings / locator notes)：** How it works

**Release boundary：** Describes the task setting without releasing its task distribution, browser-environment generator or reward implementation.

**Evidence**

- [primary-source-content](https://openai.com/index/introducing-deep-research/) · 2026-10-08 · “How it works”

## Introducing ChatGPT agent: bridging research and action — blog-openai-chatgpt-agent

**[Introducing ChatGPT agent: bridging research and action](https://openai.com/index/introducing-chatgpt-agent/)**

`blog` · `openai-chatgpt-agent` · 2025-07-17 · Technical account

Connects visual and text browsers, a terminal and APIs through a shared virtual computer that preserves task context across tools.

**Background only — excluded from the selected catalog：** Product and shared-computer overview lacking sufficient construction and validation detail for environment research.

**Relevant passages (original headings / locator notes)：** An agent that works for you, with you

**Release boundary：** Historical environment-design account; the site marks this launch post outdated, so it is not current product guidance or evidence of released training environments.

**Evidence**

- [primary-source-content](https://openai.com/index/introducing-chatgpt-agent/) · 2026-10-08 · “its own virtual computer”

## Scaling Managed Agents: Decoupling the brain from the hands — blog-anthropic-managed-agents

**[Scaling Managed Agents: Decoupling the brain from the hands](https://www.anthropic.com/engineering/managed-agents)**

`blog` · `anthropic-managed-agents` · 2026-04-08 · Environment infrastructure

Separates durable session logs, the agent harness and execution sandboxes for recovery and independent resource scaling.

**Background only — excluded from the selected catalog：** Focuses on managed-agent service decomposition, with an indirect link to environment production.

**Relevant passages (original headings / locator notes)：** Session, harness and sandbox separation

**Release boundary：** Managed runtime architecture, not a public RL task-generation system.

**Evidence**

- [primary-source-content](https://www.anthropic.com/engineering/managed-agents) · 2026-10-08 · “Decoupling the brain from the hands”

## How we contain Claude across products — blog-anthropic-containment

**[How we contain Claude across products](https://www.anthropic.com/engineering/how-we-contain-claude)**

`blog` · `anthropic-containment` · 2026-05-25 · Environment infrastructure

Compares gVisor, OS sandboxes and full VMs, explaining filesystem, network and credential isolation boundaries.

**Background only — excluded from the selected catalog：** Focuses on production containment boundaries; retained as sandbox background rather than core environment construction.

**Relevant passages (original headings / locator notes)：** Per-product containment; filesystem, network and credential boundaries

**Release boundary：** Production isolation design; it does not establish release of data-generation tasks or training verifiers.

**Evidence**

- [primary-source-content](https://www.anthropic.com/engineering/how-we-contain-claude) · 2026-10-08 · “How we contain Claude across products”

## Petri: An open-source auditing tool to accelerate AI safety research — blog-anthropic-petri

**[Petri: An open-source auditing tool to accelerate AI safety research](https://www.anthropic.com/research/petri-open-source-auditing)**

`blog` · `petri` · 2025-10-06 · Environment / task generation

An auditor turns seed scenarios into multi-turn simulated user, tool and environment interactions that a judge analyzes.

**Supporting reference：** Supports execution, evaluation, simulation or quality control, but is not a direct focus on scalable environment production or effective training-data production; retained in its subject category.

**Article research question：** How are interactive audit scenarios synthesized?

**Concrete content**

- Seed scenarios generate multi-turn interactions
- Simulates users and tool responses
- Judges inspect interaction transcripts

**Relevant passages (original headings / locator notes)：** Auditor, target and judge workflow

**Release boundary：** Open auditing tool; model-simulated responses are not deterministic state transitions of real applications.

Same work: [Petri 2.0: New Scenarios, New Model Comparisons, and Improved Eval-Awareness Mitigations (blog)](#petri-20-new-scenarios-new-model-comparisons-and-improved-eval-awareness-mitigations--blog-anthropic-petri-v2)

**Evidence**

- [primary-source-content](https://www.anthropic.com/research/petri-open-source-auditing) · 2026-10-08 · “Petri (Parallel Exploration Tool for Risky Interactions)”

## Petri 2.0: New Scenarios, New Model Comparisons, and Improved Eval-Awareness Mitigations — blog-anthropic-petri-v2

**[Petri 2.0: New Scenarios, New Model Comparisons, and Improved Eval-Awareness Mitigations](https://alignment.anthropic.com/2026/petri-v2/)**

`blog` · `petri` · 2026-01-22 · Quality / failure study

Adds scenarios and realism filtering to reduce implausible tool outputs and cues that reveal the evaluation setting.

**Supporting reference：** Supports execution, evaluation, simulation or quality control, but is not a direct focus on scalable environment production or effective training-data production; retained in its subject category.

**Article research question：** How can simulations reduce unrealistic cues?

**Concrete content**

- Adds new scenarios
- Filters implausible tool responses
- Mitigates target-model awareness of evaluation

**Relevant passages (original headings / locator notes)：** Realism mitigations and eval-awareness analysis

**Release boundary：** Realism classifiers and eval-awareness mitigations remain imperfect; they do not prove full simulation fidelity.

Same work: [Petri: An open-source auditing tool to accelerate AI safety research (blog)](#petri-an-open-source-auditing-tool-to-accelerate-ai-safety-research--blog-anthropic-petri)

**Evidence**

- [primary-source-content](https://alignment.anthropic.com/2026/petri-v2/) · 2026-10-08 · “Petri 2.0”

## Measuring and improving coding audit realism with deployment resources — blog-anthropic-petri-realism

**[Measuring and improving coding audit realism with deployment resources](https://alignment.anthropic.com/2026/coding-audit-realism/)**

`blog` · `petri-realism` · 2026-03-23 · Quality / failure study

Grounds coding-audit simulations in deployment prompts, tool definitions and repository resources, measuring realism improvements.

**Supporting reference：** Supports execution, evaluation, simulation or quality control, but is not a direct focus on scalable environment production or effective training-data production; retained in its subject category.

**Article research question：** How can deployment resources ground simulation?

**Concrete content**

- Uses deployment prompts and tool definitions
- Grounds scenarios in repository resources
- Compares realism win rate

**Relevant passages (original headings / locator notes)：** Realism win rate and deployment-resource experiments

**Release boundary：** Realism win rate is a model-based discrimination metric, not proof of behavioral equivalence to deployment.

**Evidence**

- [primary-source-content](https://alignment.anthropic.com/2026/coding-audit-realism/) · 2026-10-08 · “Measuring and improving coding audit realism”

## From shortcuts to sabotage: natural emergent misalignment from reward hacking — blog-anthropic-reward-hacking

**[From shortcuts to sabotage: natural emergent misalignment from reward hacking](https://www.anthropic.com/research/emergent-misalignment-reward-hacking)**

`blog` · `anthropic-emergent-misalignment` · 2025-11-21 · Quality / failure study

Studies reward hacking in vulnerable coding RL environments and how the learned behavior generalizes to other tasks.

**Supporting reference：** Supports execution, evaluation, simulation or quality control, but is not a direct focus on scalable environment production or effective training-data production; retained in its subject category.

**Article research question：** How can flawed rewards change learned behavior?

**Concrete content**

- Uses exploitable coding RL settings
- Observes exploitation of reward flaws
- Measures behavioral generalization to other tasks

**Relevant passages (original headings / locator notes)：** Coding RL setup, reward hacking and generalization

**Release boundary：** Controlled research setting, not a claim about inevitable deployed-model behavior or an environment-toolkit release.

**Evidence**

- [primary-source-content](https://www.anthropic.com/research/emergent-misalignment-reward-hacking) · 2026-10-08 · “natural emergent misalignment from reward hacking”

## Effective harnesses for long-running agents — blog-anthropic-long-running

**[Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)**

`blog` · `anthropic-long-running` · 2025-11-26 · Technical account

Uses initialization scripts, feature lists, progress logs and Git to restore workspaces across sessions, with browser end-to-end validation.

**Background only — excluded from the selected catalog：** Focuses on long-running coding workflows and cross-session recovery, an adjacent harness-engineering topic.

**Relevant passages (original headings / locator notes)：** Initializer agent, coding agent and environment testing

**Release boundary：** Included for environment setup, state recovery and validation, not as a general environment-synthesis method.

**Evidence**

- [primary-source-content](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) · 2026-10-08 · “Effective harnesses for long-running agents”

## The Building Blocks of Agentic AI: From Kernels to Clusters — blog-meta-openenv

**[The Building Blocks of Agentic AI: From Kernels to Clusters](https://ai.meta.com/blog/introducing-pytorch-native-agentic-stack/)**

`blog` · `openenv` · 2025-10-24 · Environment infrastructure

The OpenEnv section introduces a shared environment hub, tool/observation interfaces and human or model interaction before training.

**Supporting reference：** Supports execution, evaluation, simulation or quality control, but is not a direct focus on scalable environment production or effective training-data production; retained in its subject category.

**Article research question：** How are environment interfaces unified and checked?

**Concrete content**

- Tool and observation interface specification
- Hub for compatible environments
- Human or model interaction before training

**Relevant passages (original headings / locator notes)：** OpenEnv (An Open Hub and Spec for RL Environments)

**Release boundary：** Describes the OpenEnv 0.1 RFC at launch; the other PyTorch components are not environment generators.

Same work: [The Open Source Community is backing OpenEnv for Agentic RL (blog)](#the-open-source-community-is-backing-openenv-for-agentic-rl--blog-openenv-community) · [Building the Open Agent Ecosystem Together: Introducing OpenEnv (blog)](#building-the-open-agent-ecosystem-together-introducing-openenv--blog-openenv-launch) · [Scaling OpenEnv: From Free Usage to Thousands of Concurrent Environments (blog)](#scaling-openenv-from-free-usage-to-thousands-of-concurrent-environments--blog-openenv-scaling) · [Training a coding agent using the OpenCode harness in remote HF sandboxes with TRL and OpenEnv (blog)](#training-a-coding-agent-using-the-opencode-harness-in-remote-hf-sandboxes-with-trl-and-openenv--blog-trl-openenv) · [OpenEnv (project)](#openenv--project-openenv)

**Evidence**

- [primary-source-content](https://ai.meta.com/blog/introducing-pytorch-native-agentic-stack/) · 2026-10-08 · “OpenEnv (An Open Hub and Spec for RL Environments)”

## Introducing Grok 4.6 — blog-xai-grok46

**[Introducing Grok 4.6](https://x.ai/news/grok-4-6)**

`blog` · `grok46` · 2026-08-12 · RL and SFT experiments

Describes cross-harness SFT trajectory regeneration and filtering, followed by RL in knowledge-work, coding, kernel, web and CAD environments.

**Background only — excluded from the selected catalog：** Lists trajectory regeneration and task domains without detailed environment, task-generation or verification mechanisms.

**Relevant passages (original headings / locator notes)：** Training Grok 4.6

**Release boundary：** Discloses task domains and training workflow, without environment generators, task pools or verifier implementations.

**Evidence**

- [primary-source-content](https://x.ai/news/grok-4-6) · 2026-10-08 · “Training Grok 4.6”

## How to Run an Autoresearch Workflow with RL Agent Skills and NVIDIA NeMo — blog-nvidia-autoresearch-env

**[How to Run an Autoresearch Workflow with RL Agent Skills and NVIDIA NeMo](https://developer.nvidia.com/blog/how-to-run-an-autoresearch-workflow-with-rl-agent-skills-and-nvidia-nemo/)**

`blog` · `nvidia-autoresearch-env` · 2026-07-14 · Environment / task generation

Shows an agent building a star-counting environment, generating examples across colors and canvas sizes, and connecting it to NeMo training.

**Article research question：** How can an agent build an environment and generate data?

**Concrete content**

- Implements a star-counting environment
- Generates image tasks across colors and canvas sizes
- Uses generated samples in an SFT experiment

**Relevant passages (original headings / locator notes)：** Star-count environment creation and the SFT campaign (steps 7–8)

**Release boundary：** The counting example uses SFT; the RL wording in the title must not be mistaken for an RL result on this environment.

**Evidence**

- [primary-source-content](https://developer.nvidia.com/blog/how-to-run-an-autoresearch-workflow-with-rl-agent-skills-and-nvidia-nemo/) · 2026-10-08 · “star count”

## Mastering Agentic Techniques: AI Agent Reinforcement Learning — blog-nvidia-agent-rl

**[Mastering Agentic Techniques: AI Agent Reinforcement Learning](https://developer.nvidia.com/blog/mastering-agentic-techniques-ai-agent-reinforcement-learning/)**

`blog` · `nemo-gym` · 2026-07-01 · Environment infrastructure

Connects task definitions, verifiable rewards, tool environments and NeMo rollouts, including regression tests derived from failures.

**Background only — excluded from the selected catalog：** General RL tutorial with simplified examples, overlapping with more direct NeMo environment articles.

**Relevant passages (original headings / locator notes)：** A practical first RL training run is small, verifiable and inspectable

**Release boundary：** Tutorial with examples; simplified one-step tool tasks should not be treated as complete enterprise environments.

Same work: [How to Train Scientific Agents with Reinforcement Learning (blog)](#how-to-train-scientific-agents-with-reinforcement-learning--blog-nemo-science) · [NeMo Gym (project)](#nemo-gym--project-nemo-gym)

**Evidence**

- [primary-source-content](https://developer.nvidia.com/blog/mastering-agentic-techniques-ai-agent-reinforcement-learning/) · 2026-10-08 · “Verifiable reward environments, rollouts, and evaluation”

## DeepSWE: Training a Fully Open-sourced, State-of-the-Art Coding Agent by Scaling RL — blog-together-deepswe

**[DeepSWE: Training a Fully Open-sourced, State-of-the-Art Coding Agent by Scaling RL](https://www.together.ai/blog/deepswe)**

`blog` · `deepswe` · 2025-07-02 · RL experiments

Describes coding RL over R2E-Gym repository tasks and Docker tool environments with executable-test rewards.

**Article research question：** How are existing repository environments used in online training?

**Concrete content**

- Executes tool actions in R2E-Gym tasks
- Docker provides repository workspaces
- Executable tests supply RL rewards

**Relevant passages (original headings / locator notes)：** R2E-Gym task environment, training setup and reward discussion

**Release boundary：** Training recipe over existing environments, not a separate new environment synthesizer.

**Evidence**

- [primary-source-content](https://www.together.ai/blog/deepswe) · 2026-10-08 · “DeepSWE-Preview”

## Introducing SWE-1.5: Our Fast Agent Model — blog-cognition-swe15

**[Introducing SWE-1.5: Our Fast Agent Model](https://cognition.com/blog/swe-1-5)**

`blog` · `swe15` · 2025-10-29 · RL experiments

Describes real-task RL with Cascade and otterlink VMs for code execution, browsing and high concurrency aligned with Devin production.

**Supporting reference：** Supports execution, evaluation, simulation or quality control, but is not a direct focus on scalable environment production or effective training-data production; retained in its subject category.

**Article research question：** How can rollout environments match production?

**Concrete content**

- Cascade executes real tasks
- VMs support code execution and browsing
- otterlink scales concurrent environments

**Relevant passages (original headings / locator notes)：** The Agent-Model Interface; high-fidelity rollout environments and otterlink

**Release boundary：** Engineering disclosure, not release of the training tasks, VM platform or complete environment-building pipeline.

**Evidence**

- [primary-source-content](https://cognition.com/blog/swe-1-5) · 2026-10-08 · “high-fidelity environments with code execution”

## Custom reward functions for multi-turn reinforcement learning with Amazon Nova Forge — blog-aws-nova-rewards

**[Custom reward functions for multi-turn reinforcement learning with Amazon Nova Forge](https://aws.amazon.com/blogs/machine-learning/custom-reward-functions-for-multi-turn-reinforcement-learning-with-amazon-nova-forge/)**

`blog` · `nova-forge-environments` · 2026-08-14 · Environment infrastructure

BYOO containers manage multi-turn state, user simulation, execution and verification, returning completed episodes and aggregate rewards.

**Supporting reference：** Supports execution, evaluation, simulation or quality control, but is not a direct focus on scalable environment production or effective training-data production; retained in its subject category.

**Article research question：** How do multi-turn environments track state and return rewards?

**Concrete content**

- BYOO containers manage multi-turn state
- Runs user simulation, tools or verifiers
- Returns completed episodes and aggregate rewards

**Relevant passages (original headings / locator notes)：** Building custom rewards with Amazon Nova Forge; BYOO containers

**Release boundary：** Cloud-service tutorial requiring Nova Forge access and AWS resources, not an offline general-purpose environment library.

Same work: [Deploying Multi-Turn RL Infrastructure for Amazon Nova on Amazon SageMaker HyperPod (blog)](#deploying-multi-turn-rl-infrastructure-for-amazon-nova-on-amazon-sagemaker-hyperpod--blog-aws-nova-infra)

**Evidence**

- [primary-source-content](https://aws.amazon.com/blogs/machine-learning/custom-reward-functions-for-multi-turn-reinforcement-learning-with-amazon-nova-forge/) · 2026-10-08 · “Building custom rewards with Amazon Nova Forge”

## Deploying Multi-Turn RL Infrastructure for Amazon Nova on Amazon SageMaker HyperPod — blog-aws-nova-infra

**[Deploying Multi-Turn RL Infrastructure for Amazon Nova on Amazon SageMaker HyperPod](https://aws.amazon.com/blogs/machine-learning/deploying-multi-turn-rl-infrastructure-for-amazon-nova-on-amazon-sagemaker-hyperpod/)**

`blog` · `nova-forge-environments` · 2026-07-06 · Environment infrastructure

Uses Wordle to separate HyperPod training, ECS reward environments and stateful message routing, with per-run resource lifecycles.

**Supporting reference：** Supports execution, evaluation, simulation or quality control, but is not a direct focus on scalable environment production or effective training-data production; retained in its subject category.

**Article research question：** How are stateful environments orchestrated at scale?

**Concrete content**

- Separates training from ECS reward environments
- Proxy routes multi-turn messages
- Wordle demonstrates per-run resource lifecycles

**Relevant passages (original headings / locator notes)：** Solution overview; ECS on Fargate; Nova Forge proxy

**Release boundary：** Wordle is a replaceable example task, not evidence of automatic enterprise-task generation.

Same work: [Custom reward functions for multi-turn reinforcement learning with Amazon Nova Forge (blog)](#custom-reward-functions-for-multi-turn-reinforcement-learning-with-amazon-nova-forge--blog-aws-nova-rewards)

**Evidence**

- [primary-source-content](https://aws.amazon.com/blogs/machine-learning/deploying-multi-turn-rl-infrastructure-for-amazon-nova-on-amazon-sagemaker-hyperpod/) · 2026-10-08 · “Solution overview”

## Magentic Marketplace: an open-source simulation environment for studying agentic markets — blog-microsoft-marketplace

**[Magentic Marketplace: an open-source simulation environment for studying agentic markets](https://www.microsoft.com/en-us/research/blog/magentic-marketplace-an-open-source-simulation-environment-for-studying-agentic-markets/)**

`blog` · `magentic-marketplace` · 2025-11-05 · Evaluation substrate

A shared REST environment supports buyer/seller discovery, communication and simulated transactions, with synthetic market data for reproducible experiments.

**Supporting reference：** Supports execution, evaluation, simulation or quality control, but is not a direct focus on scalable environment production or effective training-data production; retained in its subject category.

**Article research question：** How can controlled business-interaction worlds be built?

**Concrete content**

- Shared REST service maintains market state
- Buyers and sellers discover, communicate and transact in simulation
- Synthetic market data supports reproducible experiments

**Relevant passages (original headings / locator notes)：** Three architectural choices; Setting up the experiments

**Release boundary：** Simulated markets for evaluation, not a real payment system; training results are not required for inclusion.

**Evidence**

- [primary-source-content](https://www.microsoft.com/en-us/research/blog/magentic-marketplace-an-open-source-simulation-environment-for-studying-agentic-markets/) · 2026-10-08 · “HTTP/REST client-server architecture”

## Genie 2: A large-scale foundation world model — blog-deepmind-genie2

**[Genie 2: A large-scale foundation world model](https://deepmind.google/blog/genie-2-a-large-scale-foundation-world-model/)**

`blog` · `deepmind-genie2` · 2024-12-04 · Environment / task generation

Generates action-responsive interactive worlds from an image and alternative trajectories from the same initial frame for agent training and evaluation.

**Supporting reference：** Supports execution, evaluation, simulation or quality control, but is not a direct focus on scalable environment production or effective training-data production; retained in its subject category.

**Article research question：** How can images generate action-conditioned worlds?

**Concrete content**

- One image defines the initial scene
- Keyboard/mouse actions drive observations
- Different actions produce alternative trajectories

**Relevant passages (original headings / locator notes)：** Action controls; Generating counterfactuals; Long horizon memory

**Release boundary：** Learned simulation has consistency and horizon limits; it is not a deterministic engine or a released complete training platform.

**Evidence**

- [primary-source-content](https://deepmind.google/blog/genie-2-a-large-scale-foundation-world-model/) · 2026-10-08 · “Generating counterfactuals”

## Designing a world-class code execution environment — blog-poolside-code-env

**[Designing a world-class code execution environment](https://poolside.ai/blog/designing-a-world-class-code-execution-environment)**

`blog` · `poolside-code-env` · 2025-08-12 · Technical account

Uses Saucer for repository revisions, agent-assisted image construction, layered revision reuse and isolated code-execution feedback at scale.

**Article research question：** How do real repositories become executable environments?

**Concrete content**

- Saucer manages repository revisions
- Agents assist in building runnable images
- Layers reuse revisions for isolated execution feedback

**Relevant passages (original headings / locator notes)：** Saucer; Building images; Handling revisions; Handling execution

**Release boundary：** Detailed engineering disclosure, not evidence that Saucer, the image corpus or the full RLCEF platform is open source.

**Evidence**

- [primary-source-content](https://poolside.ai/blog/designing-a-world-class-code-execution-environment) · 2026-10-08 · “Building images”

## Introducing Beam: Reflection’s 501B open-weight model — blog-reflection-beam-env

**[Introducing Beam: Reflection’s 501B open-weight model](https://reflection.ai/blog/introducing-beam)**

`blog` · `reflection-beam` · 2026-10-05 · RL experiments

Describes synthetic, vendor and open-source task sourcing, difficulty and quality filters, and RL-driven iteration of the environment pool, alongside sandbox and grading infrastructure.

**Article research question：** How is a challenging, high-quality environment pool iterated?

**Concrete content**

- Combines synthetic, vendor and open-source tasks
- Filters trivial, impossible, ambiguous or exploitable tasks
- Uses RL to discover issues and revise curation

**Relevant passages (original headings / locator notes)：** Scaling reinforcement learning environments; Frontier RL infrastructure

**Release boundary：** The announcement schedules weights and a report for later that month; it does not establish their release or that of the environment pool and generators.

**Evidence**

- [primary-source-content](https://reflection.ai/blog/introducing-beam) · 2026-10-08 · “Scaling reinforcement learning environments”

## Introducing North Mini Code: Cohere’s First Model For Developers — blog-cohere-north-mini-code

**[Introducing North Mini Code: Cohere’s First Model For Developers](https://huggingface.co/blog/CohereLabs/introducing-north-mini-code)**

`blog` · `north-mini-code` · 2026-06-09 · RL and SFT experiments

Describes containerized repository and terminal tasks, disjoint environment subsets for synthetic SFT and RLVR, and repository-source deduplication against evaluation sets.

**Article research question：** How are environments organized for different training data?

**Concrete content**

- Containerizes repository and terminal tasks
- Uses disjoint subsets for synthetic SFT and RLVR
- Deduplicates repository sources against evaluations

**Relevant passages (original headings / locator notes)：** Post-Training for Coding Excellence; Robustness Across Harnesses

**Release boundary：** Published by the official Cohere team on Hugging Face; model availability does not establish release of all internal environments and data pipelines.

**Evidence**

- [primary-source-content](https://huggingface.co/blog/CohereLabs/introducing-north-mini-code) · 2026-10-08 · “containerised agentic coding environments”
