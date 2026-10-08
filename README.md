# Awesome Agent Environments

Two research tracks: high-quality agent environments at scale, and effective training data synthesized from environments and content. Compare scale, quality, cost and SFT/RL learning outcomes across papers, blogs, reports and projects.

[English](README.md) | [中文](README_zh.md)

**138 work families · 93 papers · 4 model reports · 53 blogs · 68 GitHub projects**

Snapshot: **2026-10-08**. Covers environment construction, task synthesis, interaction data, training and evaluation. Report sections and companion links are not counted as independent resources.

12 adjacent background articles are kept separately and excluded from these counts.

## Two Research Tracks

| Theme | Question to answer |
| --- | --- |
| Track 1: Build high-quality environments at scale | How can content, skills, requirements and real software yield many executable, verifiable, diverse and appropriately difficult environments at low cost? |
| Track 2: Synthesize effective training data from environments and content | How can environments and content produce tasks and selected trajectories for SFT or RL, with gains tested on independent tasks? |

The focus is environment production and training-data production. Interfaces, sandboxes, static benchmarks, general simulation and safety audits are supporting references unless they directly explain production or quality mechanisms. Construction-only work can be relevant without establishing training gains.

Working hypothesis: content / skills / repositories → environment and task generation → quality checks → interaction sampling and filtering → SFT or RL → independent evaluation → revise generation. The final feedback step is a research proposal, not a demonstrated result of this catalog.

SFT uses selected demonstrations; online RL additionally needs sampleable task distributions, executable environments and reliable rewards. More generated artifacts do not by themselves establish better learning.

[研究主张、指标与实验设想 / Research focus](docs/research_focus_zh.md)

## Model Company Articles — By Environment Contribution

Only articles directly addressing environment production at scale or training-data production are featured here. Interfaces, general evaluation and runtime facilities remain supporting references in the subject catalog.

[Scope decisions and background articles](docs/north_american_company_blogs.md)

### Blog theme: Track 1: Build high-quality environments at scale

How can content, skills, requirements and real software yield many executable, verifiable, diverse and appropriately difficult environments at low cost?

| Article / publisher | Core question | Concrete content / outputs | Date | Boundary / source passages |
| --- | --- | --- | --- | --- |
| [Automating the Data Flywheel with Terminal Agents](https://microsoft.github.io/Orchard-Agentic/autoenvscaling/) · Microsoft Research | How can agents automatically generate and iterate environments? | Proposer agent reads solver failures, builds/runs/fixes new environments in sandbox; validation and difficulty calibration filters; single model can serve both proposer and solver roles for recursive self-improvement | 2026 (preprint) | Frontier proposers produce valid environments 25× more often with terminal access vs one-shot prompting; Qwen3.6-35B improved from 41.1 to 53.3 on Terminal-Bench 2.1 via self-play |
| [AutoBenchmark: Benchmark Creation & the Role of Humans](https://facebookresearch.github.io/RAM/blogs/autobench/) · Meta AI | How can auto-generated benchmarks reach meaningful difficulty? | Uses Muse-Spark-1.1 to create three research agent benchmarks (Graveyard/SilentTrain/Rebuttal Bench); compares no feedback, coarse-grained and fine-grained human feedback on difficulty | 2026-09 | Fine-grained human feedback reduced solver scores by 28-46.5 points; coarse feedback only 0.3-13.8 points; auto-generated benchmarks near saturated (>80%) without feedback |
| [Introducing Beam: Reflection’s 501B open-weight model](https://reflection.ai/blog/introducing-beam) · Reflection | How is a challenging, high-quality environment pool iterated? | Combines synthetic, vendor and open-source tasks; Filters trivial, impossible, ambiguous or exploitable tasks; Uses RL to discover issues and revise curation | 2026-10-05 | The announcement schedules weights and a report for later that month; it does not establish their release or that of the environment pool and generators. [Details](docs/catalog_details.md#introducing-beam-reflections-501b-open-weight-model--blog-reflection-beam-env) |
| [Designing a world-class code execution environment](https://poolside.ai/blog/designing-a-world-class-code-execution-environment) · Poolside | How do real repositories become executable environments? | Saucer manages repository revisions; Agents assist in building runnable images; Layers reuse revisions for isolated execution feedback | 2025-08-12 | Detailed engineering disclosure, not evidence that Saucer, the image corpus or the full RLCEF platform is open source. [Details](docs/catalog_details.md#designing-a-world-class-code-execution-environment--blog-poolside-code-env) |

### Blog theme: Track 2: Synthesize effective training data from environments and content

How can environments and content produce tasks and selected trajectories for SFT or RL, with gains tested on independent tasks?

| Article / publisher | Core question | Concrete content / outputs | Date | Boundary / source passages |
| --- | --- | --- | --- | --- |
| [Odyssey: Forging Language Agents with Synthesized Environments and Mixed RL](https://bigai-nlco.github.io/Odyssey/) · BIGAI | How to auto-generate verifiable environments from structured data for mixed RL? | Odyssey-Env mines structured data (Wikipedia etc.) to auto-generate 13K tasks (5K environments, 6 domains, 4 difficulty levels); Odyssey-RL uses Heuristic Credit Assignment to detect observable failures and localize negative gradients; trains across multiple environments simultaneously | 2026-09-24 | Qwen 4B/8B/14B: +4.5-11.4 on BFCL-v4, +9.2-13.4 on ACEBench; 14B achieves 42.7% on GAIA (+15.5); environment synthesis cost ~$11,440 ($0.88/task); models and environments promised for near-future release |
| [How to Run an Autoresearch Workflow with RL Agent Skills and NVIDIA NeMo](https://developer.nvidia.com/blog/how-to-run-an-autoresearch-workflow-with-rl-agent-skills-and-nvidia-nemo/) · NVIDIA | How can an agent build an environment and generate data? | Implements a star-counting environment; Generates image tasks across colors and canvas sizes; Uses generated samples in an SFT experiment | 2026-07-14 | The counting example uses SFT; the RL wording in the title must not be mistaken for an RL result on this environment. [Details](docs/catalog_details.md#how-to-run-an-autoresearch-workflow-with-rl-agent-skills-and-nvidia-nemo--blog-nvidia-autoresearch-env) |
| [Introducing North Mini Code: Cohere’s First Model For Developers](https://huggingface.co/blog/CohereLabs/introducing-north-mini-code) · Cohere Labs | How are environments organized for different training data? | Containerizes repository and terminal tasks; Uses disjoint subsets for synthetic SFT and RLVR; Deduplicates repository sources against evaluations | 2026-06-09 | Published by the official Cohere team on Hugging Face; model availability does not establish release of all internal environments and data pipelines. [Details](docs/catalog_details.md#introducing-north-mini-code-coheres-first-model-for-developers--blog-cohere-north-mini-code) |
| [A technical report on Composer 2](https://cursor.com/blog/composer-2-technical-report) · Cursor | How are deployment-like training tasks executed? | Multi-step tasks with real tool sessions; Sandboxes support concurrent execution; Execution feedback feeds asynchronous RL | 2026-03-27 | Industrial first-party account; the internal training environment fleet is not released as an open environment library. [Details](docs/catalog_details.md#a-technical-report-on-composer-2--blog-composer2) |
| [DeepSWE: Training a Fully Open-sourced, State-of-the-Art Coding Agent by Scaling RL](https://www.together.ai/blog/deepswe) · Together AI | How are existing repository environments used in online training? | Executes tool actions in R2E-Gym tasks; Docker provides repository workspaces; Executable tests supply RL rewards | 2025-07-02 | Training recipe over existing environments, not a separate new environment synthesizer. [Details](docs/catalog_details.md#deepswe-training-a-fully-open-sourced-state-of-the-art-coding-agent-by-scaling-rl--blog-together-deepswe) |
| [CoderForge-Preview](https://www.together.ai/blog/coderforge-preview) · Together AI | How do repository tasks yield training traces? | Executable repository tasks host interactions; Tests validate coding trajectories; Released trajectories support fine-tuning | Unconfirmed | The public release emphasizes trajectories; do not equate trajectory count with newly released environment implementations. [Details](docs/catalog_details.md#coderforge-preview--blog-coderforge) |

## Selected Research for the Two Tracks

### Papers: Track 1: Build high-quality environments at scale

| Work | Focus | Mechanism / output | Reported evidence | Limits / details |
| --- | --- | --- | --- | --- |
| [EnvCraft](https://arxiv.org/abs/2609.05576) | Topology-aware environment and trajectory synthesis | Environment synthesis engine builds sandbox-isolated workspaces; topology-aware data generation engine produces coherent task trajectories; synthesizes 139 interactive environments with ~20K complex tasks | RL experiments | Paper focuses on RL training for Claw-like agents; environment count and task count should be distinguished |
| [GraphForge](https://arxiv.org/abs/2609.38923) | Evidence-graph based workspace synthesis | Starts from occupation-grounded seeds, assembles real-file workspace for each seed and builds relation evidence graph; tasks and verification grounded in real files; generates 2,169 SFT trajectories | SFT / trajectory training | Qwen3.6 27B and 35B-A3B both improved; 27B GDPVal +65.7 Elo, Workspace-Bench-Lite +7.7 pts, SpreadsheetBench II +13.7 pts; 35B-A3B GDPVal +101.7 Elo |
| [Envs-FORGE](https://arxiv.org/abs/2608.14312) | Feedback-driven synthesis | Uses verifier pass rates to choose per-seed synthesis actions and jointly rewrite tasks, fixtures, tests and Docker environments. | RL experiments | The linked repository is a broader toolkit; a complete paper-specific reproduction path was not established in its root README. [Details](docs/catalog_details.md#envs-forge--paper-envs-forge) |
| [SWE-Universe](https://arxiv.org/abs/2602.02361) | Automated construction and in-loop quality checks | A trained building agent converts PRs into verifiable SWE environments using iterative self-checks and in-loop hacking detection. | RL experiments | The paper reports 807,693 instances; these are not independent environment families, and official construction code was not confirmed. [Details](docs/catalog_details.md#swe-universe--paper-swe-universe) |
| [daVinci-Env / OpenSWE](https://arxiv.org/abs/2603.13023) | Repository builds, solvability and useful difficulty | Automates repository exploration, Docker setup and test generation, then filters environments by solvability and useful difficulty. | SFT / trajectory training | The title says daVinci-Env while the released framework is OpenSWE; construction and rollout costs are substantial. [Details](docs/catalog_details.md#davinci-env--openswe--paper-openswe) |
| [Agent-World](https://arxiv.org/abs/2604.18292) | Stateful worlds and capability-gap-driven evolution | Discovers stateful tool ecosystems and generates verifiable tasks, linking multi-environment learning to capability-gap-driven task evolution. | RL and SFT experiments | The public repository releases a selected environment subset and requires RL adaptation; it is not the entire paper corpus. [Details](docs/catalog_details.md#agent-world--paper-agent-world) |
| [EnvScaler](https://arxiv.org/abs/2601.05808) | Environment skeletons, scenarios and rule-based verification | Separates environment skeleton construction from scenario generation and rule-based trajectory validation. | RL and SFT experiments | Rule coverage and environment realism must be assessed independently; released RL integration uses ROLL and GEM. [Details](docs/catalog_details.md#envscaler--paper-envscaler) |
| [CLI-Universe](https://arxiv.org/abs/2606.22883) | Requirements, executable environments and verifiers | Turns capability taxonomies and demand analysis into task blueprints, Docker environments and rubric-gated verifiers. | SFT / trajectory training | Executable and fail-to-pass checks do not by themselves establish real-world representativeness; no official code confirmed. [Details](docs/catalog_details.md#cli-universe--paper-cli-universe) |
| [CalibForge](https://arxiv.org/abs/2608.06352) | Calibration of learnable difficulty | Revises terminal tasks using verified solver disagreement or strong-pass/weak-fail contrasts to target a learnable difficulty zone. | SFT / trajectory training | Calibration is solver-relative, not an absolute hardness score; public data and agent recipes are not the full synthesis engine. [Details](docs/catalog_details.md#calibforge--paper-calibforge) |
| [Endless Terminals](https://arxiv.org/abs/2601.16443) | Automatic production of tasks, containers and tests | Generates task descriptions, builds and validates containers, creates completion tests and filters for solvability before PPO training. | RL experiments | Generation, execution and optimization are separate stages; reported gains do not prove arbitrary generated tests are reliable. [Details](docs/catalog_details.md#endless-terminals--paper-endless-terminals) |

### Papers: Track 2: Synthesize effective training data from environments and content

| Work | Focus | Mechanism / output | Reported evidence | Limits / details |
| --- | --- | --- | --- | --- |
| [TraceDance](https://arxiv.org/abs/2609.33295) | Building behavior benchmarks from real deployment traces | Extracts execution traces from real agent deployment records, automatically constructs 107 benchmarks with 4,125 instances; evaluates models without training | Evaluation benchmark | No model training; 9 frontier models averaged 26.7% pass rate on new evaluation; reveals behavioral weaknesses, not capability improvements; most tested models lack comparable parameter scales |
| [WorkForge](https://arxiv.org/abs/2610.04906) | Real-file workspace task synthesis | ~16.7K real-file workspace tasks covering 40 professional domains; used for RL training | RL experiments | Qwen3.5 35B-A3B-Base GDPVal 45.5→73.6, APEX 5.0→21.3; post-trained 27B also improved from 79.4→82.4, 25.7→29.9 |
| [Skill2Env](https://arxiv.org/abs/2609.33772) | Skills to environments and SFT trajectories | Converts skills into capability-oriented task blueprints, executable workspaces and rubric evaluators; hardens tasks using solver traces. | SFT / trajectory training | SFT evidence. The current research homepage provides example tasks and a model link; a complete synthesis and training pipeline is not established by those samples. [Details](docs/catalog_details.md#skill2env--paper-skill2env) |
| [Terminal-World (skills)](https://arxiv.org/abs/2605.20876) | Skill dependencies to tasks and teacher traces | Skills and their dependency graphs jointly specify terminal tasks, executable environments and teacher trajectories. | SFT / trajectory training | Distinct from recording-based TerminalWorld; reported SFT gains do not establish online RL readiness or an available generator. [Details](docs/catalog_details.md#terminal-world-skills--paper-terminal-world-skills) |
| [NexForge](https://arxiv.org/abs/2607.14186) | Real requirements to resources and demonstrations | Compiles real requirements into tasks, retrieves or builds supporting files and runtimes, and collects expert demonstrations. | SFT / trajectory training | Terminal and office task counts are separate from trajectory counts; model releases do not establish generator availability. [Details](docs/catalog_details.md#nexforge--paper-nexforge) |
| [OpenThoughts-Agent](https://arxiv.org/abs/2606.24855) | Controlled study of sources, teachers and filtering | Studies task sources, mixtures, teachers, rollout and filtering choices through controlled ablations for terminal-agent data. | SFT / trajectory training | The 2025 launch blog and 2026 paper describe different release stages; training outcomes depend on the whole data recipe. [Details](docs/catalog_details.md#openthoughts-agent--paper-openthoughts-agent) |
| [TerminalTraj](https://arxiv.org/abs/2602.01244) | Repositories to tasks, verifiers and trajectories | Builds Dockerized repository environments, aligned terminal tasks and executable verifiers to collect large-scale trajectories. | SFT / trajectory training | Docker images, tasks and trajectories are distinct counting units; the paper-linked repository returned 404 in this review. [Details](docs/catalog_details.md#terminaltraj--paper-terminaltraj) |
| [AgentTrek](https://arxiv.org/abs/2412.09605) | Tutorials to interaction replay and filtering | Harvests web tutorials, derives task instructions and guides browser replay, then filters trajectories for training. | SFT / trajectory training | Tutorial replay uses existing websites; it does not synthesize independent website backends, and model judges can err. [Details](docs/catalog_details.md#agenttrek--paper-agenttrek) |
| [OS-Genesis](https://arxiv.org/abs/2412.19723) | Exploration to reverse-generated tasks and data | Explores GUI environments before reverse-synthesizing tasks and scores trajectory quality with a trajectory reward model. | SFT / trajectory training | Constructs tasks and trajectories over existing desktop/mobile environments rather than a new operating-system simulator. [Details](docs/catalog_details.md#os-genesis--paper-os-genesis) |
| [RandomWorld](https://arxiv.org/abs/2506.11045) | Generated tools for both SFT and RL | Procedurally generates interactive tools and compositional tool-use data for both supervised and reinforcement learning. | RL and SFT experiments | Synthetic tool semantics do not establish fidelity to production APIs; the public repository has limited user-facing documentation. [Details](docs/catalog_details.md#randomworld--paper-randomworld) |
| [DreamGym](https://arxiv.org/abs/2511.03773) | Simulated experience and replay for RL | Uses a reasoning-based experience model, replay buffer and adaptive task generation to train agents with synthetic interactions. | RL experiments | Sim-to-real transfer is empirical; a third-party reproduction is not official author code. [Details](docs/catalog_details.md#dreamgym--paper-dreamgym) |
| [VERA](https://arxiv.org/abs/2610.05923) | Recoverable environments and policy/skill updates | Builds resumable sandboxes from trajectories, filters them with checks, and alternates policy training with harness-skill updates. | RL and harness learning | Very recent preprint; the reviewed abstract and full text do not expose a confirmed official repository. [Details](docs/catalog_details.md#vera--paper-vera) |

These are editorial selections from the existing catalog, not a performance ranking. SFT, RL and construction-only evidence are kept distinct; no experiments were reproduced here.

## Environment Sections in Technical Reports

Section locations are pinned to the versions below. PDF links open at the first relevant page; the section index explains each passage separately. Model weights or an agent client do not establish release of the training environments.

| Report / paper | Version | Relevant sections | Location | Content |
| --- | --- | --- | --- | --- |
| [Kimi K3](https://arxiv.org/abs/2607.24653) | arXiv v2 · 2026-08-07 | §4.2.1, §4.2.2, §4.2.3, §4.2.4, §4.2.5, §4.2.6, §4.2.7, §5.3.2 | [PDF pp. 14, 15, 16, 22](https://arxiv.org/pdf/2607.24653v2#page=14) · [Section index](docs/technical_report_sections.md#kimi-k3) | Describes composable agent environments, task synthesis and persistent sandbox state for long-horizon interaction. |
| [DeepSeek V4](https://arxiv.org/abs/2606.19348) | arXiv v1 · 2026-04-26 | §5.2.3, §5.2.5 | [PDF pp. 34, 35, 36](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro/resolve/89d501aed998d33fa4f4702102ec1bb2331e10f6/DeepSeek_V4.pdf#page=34) · [Section index](docs/technical_report_sections.md#deepseek-v4) | Documents DSec execution substrates and interruption-safe rollout services inside a broader model report. |
| [GLM-4.5](https://arxiv.org/abs/2508.06471) | arXiv v1 · 2025-08-08 | §3.3.1, §3.5 | [PDF pp. 10, 12, 13, 14](https://arxiv.org/pdf/2508.06471v1#page=10) · [Section index](docs/technical_report_sections.md#glm-45) | Combines task synthesis, isolated execution and an asynchronous trajectory pool for agentic learning. |
| [DeepSeek Elastic Compute (DSec)](https://arxiv.org/abs/2609.22978) | arXiv v1 · 2026-09-19 | §5.1, §6.1, §6.2, §6.3 | [PDF pp. 14, 15, 17, 18](https://arxiv.org/pdf/2609.22978v1#page=14) · [Section index](docs/technical_report_sections.md#deepseek-elastic-compute-dsec) | Unifies function calls, containers, microVMs and full VMs; supports agent-built reusable environments and pause/resume for long-running rollouts. |
| [MiMo-V2.6](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL/blob/73875d00b30a89ef8cc353a0b60b0e9f9561952d/MiMo_V2_6_technical_report.pdf) | HF revision 73875d0 · checked 2026-10-08 | §4.2.1, §4.2.2, §4.2.3, §4.2.4, §4.2.5, §4.2.6, §6.1, §6.2, §7.2 | [PDF pp. 9, 10, 11, 12, 13, 14, 15, 16, 26, 27, 28, 29, 34, 35, 36](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL/resolve/73875d00b30a89ef8cc353a0b60b0e9f9561952d/MiMo_V2_6_technical_report.pdf#page=9) · [Section index](docs/technical_report_sections.md#mimo-v26) | Details environment and verifier construction across domains, multi-harness execution and experiments on released environments. |

## Catalog

Major groups organize contributions; subcategories identify construction methods or infrastructure roles. Papers and repositories use separate tables. Stars are recorded snapshots, not a quality ranking. Full titles, feedback, release boundaries and evidence are in the linked details.

[覆盖审计 / Coverage](docs/coverage_audit.md) · [技能与需求合成](docs/skills_to_environments.md) · [中文综述](docs/research_landscape_zh.md) · [收录标准 / Policy](docs/curation_policy.md)

- [Environment & Task Construction](#environment--task-construction)
  - [Skills → Tasks & Environments](#skills--tasks--environments)
  - [Requirements → Executable Tasks](#requirements--executable-tasks)
  - [Repository-derived Construction](#repository-derived-construction)
  - [Web & GUI Environment / Task Synthesis](#web--gui-environment--task-synthesis)
  - [Structured Tools & Business Worlds](#structured-tools--business-worlds)
  - [Procedural Task Generators](#procedural-task-generators)
  - [Learned Interaction Simulators](#learned-interaction-simulators)
- [Interaction Data & Experience](#interaction-data--experience)
  - [Exploration, Replay & Reverse Synthesis](#exploration-replay--reverse-synthesis)
  - [Trajectory Curation & Data Recipes](#trajectory-curation--data-recipes)
  - [Trace Capture & Inspection](#trace-capture--inspection)
- [Environment Infrastructure](#environment-infrastructure)
  - [Interfaces, Adapters & Registries](#interfaces-adapters--registries)
  - [Sandboxes & Rollout Execution](#sandboxes--rollout-execution)
- [Domain Environments & Benchmarks](#domain-environments--benchmarks)
  - [Software, Terminal & Executable Skills](#software-terminal--executable-skills)
  - [Browser, Desktop & Mobile](#browser-desktop--mobile)
  - [Tools & Enterprise Workflows](#tools--enterprise-workflows)
  - [Games & Interactive Reasoning](#games--interactive-reasoning)
  - [Science & Embodied Environments](#science--embodied-environments)
- [Adaptation & Quality](#adaptation--quality)
  - [Curricula & Co-evolving Environments](#curricula--co-evolving-environments)
  - [Verifiers, Contracts & Failure Audits](#verifiers-contracts--failure-audits)
- [Surveys & Research Maps](#surveys--research-maps)
  - [Environment Scaling & Evolution Surveys](#environment-scaling--evolution-surveys)

## Environment & Task Construction

### Skills → Tasks & Environments

**Papers**

| Paper | Date | Resources | Environment / task contribution | Feedback / evidence | Release boundary |
| --- | --- | --- | --- | --- | --- |
| [Skill2Env](https://arxiv.org/abs/2609.33772) | 2026-09-27 | [Home](https://github.com/AllSpark-Research/AgentEnv) · [Partial / associated code](https://github.com/AllSpark-Research/AgentEnv) · [Example tasks](https://github.com/AllSpark-Research/AgentEnv/tree/main/Skill2Env) · [Model](https://huggingface.co/AllSpark-Research/Skill2Env) · [Details](docs/catalog_details.md#skill2env--paper-skill2env) | Converts skills into capability-oriented task blueprints, executable workspaces and rubric evaluators; hardens tasks using solver traces. | SFT / trajectory training: Rubric evaluators and solver evidence for task hardening. | SFT evidence. The current research homepage provides example tasks and a model link; a complete synthesis and training pipeline is not established by those samples. |
| [SKT](https://arxiv.org/abs/2608.02287) | 2026-08-03 | [Details](docs/catalog_details.md#skt--paper-skt) | Builds skill-conditioned task packages and verifies both successful execution and actual use of the required skills before collecting SFT traces. | SFT / trajectory training: Rule-based and agent-based checks, iterative repair, and verification that required skills were actually used. | Task success alone does not demonstrate skill use; official pipeline code was not confirmed. |
| [Terminal-World (skills)](https://arxiv.org/abs/2605.20876) | 2026-05-20 | [Details](docs/catalog_details.md#terminal-world-skills--paper-terminal-world-skills) | Skills and their dependency graphs jointly specify terminal tasks, executable environments and teacher trajectories. | SFT / trajectory training: Co-derived task, runtime and teacher trajectory must remain aligned; downstream evidence is trajectory training. | Distinct from recording-based TerminalWorld; reported SFT gains do not establish online RL readiness or an available generator. |
| [SkillSynth](https://arxiv.org/abs/2604.25727) | 2026-04-28 | [Details](docs/catalog_details.md#skillsynth--paper-skillsynth) | Scenario-mediated skill graphs turn skill compositions into executable terminal tasks and diverse solution trajectories. | SFT / trajectory training: Validates executable task instances and measures diversity in scenario-skill compositions and solution trajectories. | Skill coverage and diverse trajectories are different from independently diverse environment families; official code was not confirmed. |
| [Terminal-Task-Gen / Nemotron-Terminal](https://arxiv.org/abs/2602.21193) | 2026-02-24 | [Model and data collection](https://huggingface.co/collections/nvidia/nemotron-terminal) · [Details](docs/catalog_details.md#terminal-task-gen--nemotron-terminal--paper-terminal-task-gen) | Combines seed-based and skill-based task generation, environment adapters and trajectory filtering into Terminal-Corpus. | SFT / trajectory training: Task and trajectory filtering, environment adaptation and data-mixture/curriculum experiments. | The linked model/data collection is not proof that the entire generation pipeline is released. |

### Requirements → Executable Tasks

**Papers**

| Paper | Date | Resources | Environment / task contribution | Feedback / evidence | Release boundary |
| --- | --- | --- | --- | --- | --- |
| [AutoGym](https://arxiv.org/abs/2609.22592) | 2026-09-18 | [Details](docs/catalog_details.md#autogym--paper-autogym) | Specifies solution space and verification before materializing gyms, then calibrates generation parameters to learner performance. | Environment / task generation: Generated task verifiers plus construction or solvability validation. | Demonstrates generated-gym difficulty; do not infer a released end-to-end RL stack or sustained training gains. |
| [NexForge](https://arxiv.org/abs/2607.14186) | 2026-07-15 | [Details](docs/catalog_details.md#nexforge--paper-nexforge) | Compiles real requirements into tasks, retrieves or builds supporting files and runtimes, and collects expert demonstrations. | SFT / trajectory training: Requirement-grounded task construction and expert demonstrations, with task-specific execution resources. | Terminal and office task counts are separate from trajectory counts; model releases do not establish generator availability. |
| [CLI-Universe](https://arxiv.org/abs/2606.22883) | 2026-06-22 | [Details](docs/catalog_details.md#cli-universe--paper-cli-universe) | Turns capability taxonomies and demand analysis into task blueprints, Docker environments and rubric-gated verifiers. | SFT / trajectory training: Rubric-gated task checks and fail-to-pass testing, including filtering misleading hints. | Executable and fail-to-pass checks do not by themselves establish real-world representativeness; no official code confirmed. |
| [EnvFactory](https://arxiv.org/abs/2605.18703) | 2026-05-18 | [Code](https://github.com/LARK-AI-Lab/EnvFactory) · [Details](docs/catalog_details.md#envfactory--paper-envfactory) | Builds and verifies stateful tools from real resources, then synthesizes trajectories using tool topology and calibrated query refinement. | RL and SFT experiments: Generated task verifiers plus construction or solvability validation. | Executable correctness and natural task intent require separate checks; the release includes framework-specific training dependencies. |
| [ClawEnvKit](https://arxiv.org/abs/2604.18543) | 2026-04-20 | [Code](https://github.com/xirui-li/ClawEnvKit) · [Details](docs/catalog_details.md#clawenvkit--paper-clawenvkit) | Parses natural-language requests into task specifications, mock tools and scoring rules, then validates generated evaluation environments. | Evaluation substrate: Config validation, mock-service audit logs and structured rule checks, with an optional LLM-judge check type. | Mock services and mixed rule/model checks are not live enterprise systems; training potential is not evidence of reported RL gains. |
| [ScaleEnv](https://arxiv.org/abs/2602.06820) | 2026-02-06 | [Details](docs/catalog_details.md#scaleenv--paper-scaleenv) | Constructs interactive tool environments from scratch, testing implementations and validating solvable tasks through executable action sequences. | RL experiments: Generated task verifiers plus construction or solvability validation. | Distinct from Scale AI AgentEnv; no confirmed official code link was found in the reviewed paper and targeted search. |
| [Endless Terminals](https://arxiv.org/abs/2601.16443) | 2026-01-23 | [Code](https://github.com/kanishkg/endless-terminals) · [Details](docs/catalog_details.md#endless-terminals--paper-endless-terminals) | Generates task descriptions, builds and validates containers, creates completion tests and filters for solvability before PPO training. | RL experiments: Executable initial/final-state or fail-to-pass tests; reference solutions establish solvability. | Generation, execution and optimization are separate stages; reported gains do not prove arbitrary generated tests are reliable. |
| [AutoForge](https://arxiv.org/abs/2512.22857) | 2025-12-28 | [Details](docs/catalog_details.md#autoforge--paper-autoforge) | Organizes synthetic state structures and tool dependencies before generating tool-use environments for agent RL. | RL experiments: Generated task verifiers plus construction or solvability validation. | Many unrelated repositories share the name; no unverified AutoForge repository is treated as official code. |
| [SWE-Playground](https://arxiv.org/abs/2512.12216) | 2025-12-13 | [Code](https://github.com/neulab/SWE-Playground) · [Details](docs/catalog_details.md#swe-playground--paper-swe-playground) | Synthesizes software projects, tasks and execution trajectories from scratch, including test creation and library implementation. | SFT / trajectory training: Separate test-writing and implementation agents mutually validate generated software tasks. | Synthetic project diversity differs from real-repository realism; execution requires model and runtime dependencies. |
| [AutoEnv](https://arxiv.org/abs/2511.19304) | 2025-11-24 | [Code](https://github.com/FoundationAgents/AutoEnv) · [Details](docs/catalog_details.md#autoenv--paper-autoenv) | Factorizes transition, observation and reward distributions to generate heterogeneous worlds for cross-environment learning studies. | Environment / task generation: Generated task verifiers plus construction or solvability validation. | Generated levels measure transfer under designed distributions, not unrestricted real-world generalization. |

**Repositories**

| Project | Links | Stars | Tags | Summary |
| --- | --- | --- | --- | --- |
| Endless Terminals | [GitHub](https://github.com/kanishkg/endless-terminals) · [Details](docs/catalog_details.md#endless-terminals--project-endless-terminals) | ★ 147 | requirement-synthesis | Generates task descriptions, builds and validates containers, creates completion tests and filters for solvability before PPO training. |
| EnvFactory | [GitHub](https://github.com/LARK-AI-Lab/EnvFactory) · [Details](docs/catalog_details.md#envfactory--project-envfactory) | ★ 96 | executable, rl+sft | Builds and verifies stateful tools from real resources, then synthesizes trajectories using tool topology and calibrated query refinement. |
| AutoEnv | [GitHub](https://github.com/FoundationAgents/AutoEnv) · [Details](docs/catalog_details.md#autoenv--project-autoenv) | ★ 68 | mixed, generation | Factorizes transition, observation and reward distributions to generate heterogeneous worlds for cross-environment learning studies. |
| ClawEnvKit | [GitHub](https://github.com/xirui-li/ClawEnvKit) · [Details](docs/catalog_details.md#clawenvkit--project-clawenvkit) | ★ 62 | requirement-synthesis | Parses natural-language requests into task specifications, mock tools and scoring rules, then validates generated evaluation environments. |
| SWE-Playground | [GitHub](https://github.com/neulab/SWE-Playground) · [Details](docs/catalog_details.md#swe-playground--project-swe-playground) | ★ 22 | requirement-synthesis | Synthesizes software projects, tasks and execution trajectories from scratch, including test creation and library implementation. |
| LiteCoder | [GitHub](https://github.com/icip-cas/LiteCoder) · [Details](docs/catalog_details.md#litecoder--project-litecoder) | ★ 17 | requirement-synthesis | Releases terminal trajectories and Harbor-format environments; documents a five-stage instruction-to-environment synthesis recipe. |

**Blogs**

| Article | Publisher | Date | Summary | Evidence |
| --- | --- | --- | --- | --- |
| [Announcing LiteCoder-Terminal Preview](https://huggingface.co/blog/Lite-Coder/litecoder-terminal-preview) | Lite-Coder / ICIP-CAS contributors | 2025-12-18 | Details taxonomy-driven task sampling, feasibility filtering, initial-state construction in Docker and trajectory collection. | [Details](docs/catalog_details.md#announcing-litecoder-terminal-preview--blog-litecoder) |

### Repository-derived Construction

**Papers**

| Paper | Date | Resources | Environment / task contribution | Feedback / evidence | Release boundary |
| --- | --- | --- | --- | --- | --- |
| [DeNovoSWE](https://arxiv.org/abs/2606.10728) | 2026-06-09 | [Partial / associated code](https://github.com/AweAI-Team/DeNovoSWE) · [Details](docs/catalog_details.md#denovoswe--paper-denovoswe) | Constructs documentation-to-repository tasks with sandboxed decomposition, critique/repair and difficulty-aware trajectory filtering. | SFT / trajectory training: Unit tests, critic-repair during construction and difficulty-aware filtering of successful trajectories. | The agent writes a repository from scratch, but task construction is grounded in existing packages; only part of the data is declared released. |
| [daVinci-Env / OpenSWE](https://arxiv.org/abs/2603.13023) | 2026-03-13 | [Code](https://github.com/GAIR-NLP/OpenSWE) · [Details](docs/catalog_details.md#davinci-env--openswe--paper-openswe) | Automates repository exploration, Docker setup and test generation, then filters environments by solvability and useful difficulty. | SFT / trajectory training: Task-specific execution tests or verifier scores; consult the resource for the exact split. | The title says daVinci-Env while the released framework is OpenSWE; construction and rollout costs are substantial. |
| [SWE-rebench V2](https://arxiv.org/abs/2602.23866) | 2026-02-27 | [Code](https://github.com/SWE-rebench/SWE-rebench-V2) · [Details](docs/catalog_details.md#swe-rebench-v2--paper-swe-rebench) | Harvests multilingual repository tasks and generates installation and test procedures to build reproducible training environments. | Environment / task generation: Task-specific execution tests or verifier scores; consult the resource for the exact split. | Fully built environments and additional task metadata have different release scope; tests can be underspecified or restrictive. |
| [ScaleSWE](https://arxiv.org/abs/2602.09892) | 2026-02-10 | [Partial / associated code](https://github.com/AweAI-Team/ScaleSWE) · [Public data collection](https://huggingface.co/collections/AweAI-Team/scale-swe) · [Details](docs/catalog_details.md#scaleswe--paper-scaleswe) | Coordinates environment setup, test generation and problem synthesis agents to curate PR-derived SWE tasks and demonstrations. | SFT / trajectory training: Fail-to-pass reproduction tests plus pass-to-pass regression checks on restored repository states. | Paper scale is 100k instances; the repository explicitly describes an initial 20k-instance public subset and uses a separate execution harness. |
| [SWE-Universe](https://arxiv.org/abs/2602.02361) | 2026-02-02 | [Details](docs/catalog_details.md#swe-universe--paper-swe-universe) | A trained building agent converts PRs into verifiable SWE environments using iterative self-checks and in-loop hacking detection. | RL experiments: Iterative build verification and in-loop hacking detection before using executable tasks for learning. | The paper reports 807,693 instances; these are not independent environment families, and official construction code was not confirmed. |
| [TerminalTraj](https://arxiv.org/abs/2602.01244) | 2026-02-01 | [Details](docs/catalog_details.md#terminaltraj--paper-terminaltraj) | Builds Dockerized repository environments, aligned terminal tasks and executable verifiers to collect large-scale trajectories. | SFT / trajectory training: Synthesizes executable validation code for Docker-aligned tasks and filters resulting trajectories. | Docker images, tasks and trajectories are distinct counting units; the paper-linked repository returned 404 in this review. |
| [SWE-smith](https://arxiv.org/abs/2504.21798) | 2025-04-30 | [Code](https://github.com/SWE-bench/SWE-smith) · [Details](docs/catalog_details.md#swe-smith--paper-swe-smith) | Turns repositories into execution environments and creates repair tasks by deliberately breaking existing tests. | SFT / trajectory training: Task-specific execution tests or verifier scores; consult the resource for the exact split. | Mutation-generated failures differ from naturally reported bugs; separate repository splits and hidden tests remain important. |
| [R2E-Gym](https://arxiv.org/abs/2504.07164) | 2025-04-09 | [Code](https://github.com/R2E-Gym/R2E-Gym) · [Details](docs/catalog_details.md#r2e-gym--paper-r2e-gym) | Procedurally curates executable software tasks from commits and studies complementary execution-based and learned verifiers. | SFT / trajectory training: Task-specific execution tests or verifier scores; consult the resource for the exact split. | The paper's early abstract uses AgentGym terminology; this is a separate project from WooooDyy/AgentGym. |
| [SWE-Gym](https://arxiv.org/abs/2412.21139) | 2024-12-30 | [Code](https://github.com/SWE-Gym/SWE-Gym) · [Details](docs/catalog_details.md#swe-gym--paper-swe-gym) | Pairs repository issues with runnable environments and unit tests, enabling agent fine-tuning and verifier training. | SFT / trajectory training: Task-specific execution tests or verifier scores; consult the resource for the exact split. | The initial corpus centers on Python; environment executability does not imply broad language coverage. |

**Repositories**

| Project | Links | Stars | Tags | Summary |
| --- | --- | --- | --- | --- |
| SWE-smith | [GitHub](https://github.com/SWE-bench/SWE-smith) · [Details](docs/catalog_details.md#swe-smith--project-swe-smith) | ★ 795 | executable, sft | Turns repositories into execution environments and creates repair tasks by deliberately breaking existing tests. |
| SWE-Gym | [GitHub](https://github.com/SWE-Gym/SWE-Gym) · [Details](docs/catalog_details.md#swe-gym--project-swe-gym) | ★ 748 | executable, sft | Pairs repository issues with runnable environments and unit tests, enabling agent fine-tuning and verifier training. |
| R2E-Gym | [GitHub](https://github.com/R2E-Gym/R2E-Gym) · [Details](docs/catalog_details.md#r2e-gym--project-r2e-gym) | ★ 337 | executable, sft | Procedurally curates executable software tasks from commits and studies complementary execution-based and learned verifiers. |
| daVinci-Env / OpenSWE | [GitHub](https://github.com/GAIR-NLP/OpenSWE) · [Details](docs/catalog_details.md#davinci-env--openswe--project-openswe) | ★ 211 | executable, sft | Automates repository exploration, Docker setup and test generation, then filters environments by solvability and useful difficulty. |
| ScaleSWE | [GitHub](https://github.com/AweAI-Team/ScaleSWE) · [Details](docs/catalog_details.md#scaleswe--project-scaleswe) | ★ 95 | repo-synthesis | Coordinates environment setup, test generation and problem synthesis agents to curate PR-derived SWE tasks and demonstrations. |
| SWE-rebench V2 | [GitHub](https://github.com/SWE-rebench/SWE-rebench-V2) · [Details](docs/catalog_details.md#swe-rebench-v2--project-swe-rebench) | ★ 85 | executable, generation | Harvests multilingual repository tasks and generates installation and test procedures to build reproducible training environments. |
| DeNovoSWE | [GitHub](https://github.com/AweAI-Team/DeNovoSWE) · [Details](docs/catalog_details.md#denovoswe--project-denovoswe) | ★ 47 | repo-synthesis | Constructs documentation-to-repository tasks with sandboxed decomposition, critique/repair and difficulty-aware trajectory filtering. |

### Web & GUI Environment / Task Synthesis

**Papers**

| Paper | Date | Resources | Environment / task contribution | Feedback / evidence | Release boundary |
| --- | --- | --- | --- | --- | --- |
| [WebForge](https://arxiv.org/abs/2604.10988) | 2026-04-13 | [Partial / associated code](https://github.com/yuandaxia2001/WebForge) · [Benchmark websites and tasks](https://huggingface.co/datasets/yuandaxia/WebForge) · [Details](docs/catalog_details.md#webforge--paper-webforge) | Coordinates planning, website generation, refinement and validation to construct self-contained browser benchmarks with difficulty controls. | Evaluation substrate: Generated-site validation followed by LLM comparison of final answers or website-computed operation codes. | Public code primarily covers evaluation; final answers or operation codes are judged by an LLM, not universally deterministic state checks. |
| [Gym-Anything / CUA-World](https://arxiv.org/abs/2604.06126) | 2026-04-07 | [Code](https://github.com/cmu-l3/gym-anything) · [Details](docs/catalog_details.md#gym-anything--cua-world--paper-gym-anything) | Automates software installation and realistic task setup with a separate auditing agent, releasing a cross-software CUA corpus. | SFT / trajectory training: State, artifact or rubric evaluation after interaction; evaluator type varies by task. | VMs, application dependencies and rubric judging add operational cost; setup evidence is not perfect task verification. |
| [InfiniteWeb](https://arxiv.org/abs/2601.04126) | 2026-01-07 | [Details](docs/catalog_details.md#infiniteweb--paper-infiniteweb) | Generates multi-page functional websites with task-centered tests and verifiable evaluators for GUI-agent RL. | RL experiments: State, artifact or rubric evaluation after interaction; evaluator type varies by task. | Generated websites need functional and visual realism checks; availability of the full artifact release is separate. |
| [AgentSynth](https://arxiv.org/abs/2506.14205) | 2025-06-17 | [Code](https://github.com/sunblaze-ucb/AgentSynth) · [Details](docs/catalog_details.md#agentsynth--paper-agentsynth) | Composes executed subtasks into harder long-horizon computer tasks and trajectory datasets. | Environment / task generation: State, artifact or rubric evaluation after interaction; evaluator type varies by task. | Primarily task and trajectory synthesis on existing environments, rather than a new general runtime. |

**Repositories**

| Project | Links | Stars | Tags | Summary |
| --- | --- | --- | --- | --- |
| Gym-Anything / CUA-World | [GitHub](https://github.com/cmu-l3/gym-anything) · [Details](docs/catalog_details.md#gym-anything--cua-world--project-gym-anything) | ★ 292 | desktop, sft | Automates software installation and realistic task setup with a separate auditing agent, releasing a cross-software CUA corpus. |
| AgentSynth | [GitHub](https://github.com/sunblaze-ucb/AgentSynth) · [Details](docs/catalog_details.md#agentsynth--project-agentsynth) | ★ 53 | desktop, generation | Composes executed subtasks into harder long-horizon computer tasks and trajectory datasets. |
| WebForge | [GitHub](https://github.com/yuandaxia2001/WebForge) · [Details](docs/catalog_details.md#webforge--project-webforge) | ★ 14 | web-synthesis | Coordinates planning, website generation, refinement and validation to construct self-contained browser benchmarks with difficulty controls. |

### Structured Tools & Business Worlds

**Papers**

| Paper | Date | Resources | Environment / task contribution | Feedback / evidence | Release boundary |
| --- | --- | --- | --- | --- | --- |
| [CompoWorld](https://arxiv.org/abs/2609.33665) | 2026-09-27 | [Home](https://github.com/AllSpark-Research/AgentEnv) · [Partial / associated code](https://github.com/AllSpark-Research/AgentEnv) · [CompoWorld examples](https://github.com/AllSpark-Research/AgentEnv/blob/main/CompoWorld/README.md) · [Details](docs/catalog_details.md#compoworld--paper-compoworld) | Composes verified services through shared typed state and interfaces; synthesizes cross-service tasks from dependency graphs. | RL and SFT experiments: Completion and rubric checks; SFT and RL experiments. | Services and tools are not independent environments. The associated repository exposes examples; full reproduction is not established. |
| [AgentMercury](https://arxiv.org/abs/2608.20634) | 2026-08-21 | [Public corpus sample](https://huggingface.co/datasets/Minbyul/AgentMercury-corpus-sample) · [Details](docs/catalog_details.md#agentmercury--paper-agentmercury) | Instantiates persistent business worlds with state, tools and cross-service invariants before deriving tasks and trajectories. | RL and SFT experiments: Executable cross-service invariants constrain generated worlds; policy RL and construction-trace tuning are evaluated separately. | Public corpus samples are not the complete executable world library; construction-model tuning and policy RL are separate experiments. |
| [Agent-World](https://arxiv.org/abs/2604.18292) | 2026-04-20 | [Partial / associated code](https://github.com/RUC-NLPIR/Agent-World) · [Details](docs/catalog_details.md#agent-world--paper-agent-world) | Discovers stateful tool ecosystems and generates verifiable tasks, linking multi-environment learning to capability-gap-driven task evolution. | RL and SFT experiments: Generated task verifiers plus construction or solvability validation. | The public repository releases a selected environment subset and requires RL adaptation; it is not the entire paper corpus. |
| [Agent World Model](https://arxiv.org/abs/2602.10090) | 2026-02-10 | [Code](https://github.com/Snowflake-Labs/agent-world-model) · [Details](docs/catalog_details.md#agent-world-model--paper-awm) | Synthesizes code-driven, SQL-backed tool worlds with inspectable state and rewards for multi-turn RL and transfer studies. | RL experiments: Database-state-aware task verification. | Synthetic database consistency does not establish fidelity to every real service or production failure mode. |
| [EnvScaler](https://arxiv.org/abs/2601.05808) | 2026-01-09 | [Code](https://github.com/RUC-NLPIR/EnvScaler) · [Details](docs/catalog_details.md#envscaler--paper-envscaler) | Separates environment skeleton construction from scenario generation and rule-based trajectory validation. | RL and SFT experiments: Rule-based trajectory and final-state checks. | Rule coverage and environment realism must be assessed independently; released RL integration uses ROLL and GEM. |
| [CodeGym](https://arxiv.org/abs/2509.17325) | 2025-09-22 | [Code](https://github.com/StigLidu/CodeGym) · [Details](docs/catalog_details.md#codegym--paper-codegym) | Extracts callable functions from coding problems to synthesize controllable multi-turn tool-use tasks with executable rewards. | RL experiments: Code execution against task reference behavior. | Code-derived workflows are useful abstractions, but do not fully capture real enterprise service semantics. |
| [RandomWorld](https://arxiv.org/abs/2506.11045) | 2025-05-21 | [Code](https://github.com/coli-saar/randomworld) · [Details](docs/catalog_details.md#randomworld--paper-randomworld) | Procedurally generates interactive tools and compositional tool-use data for both supervised and reinforcement learning. | RL and SFT experiments: Executable synthetic tool interactions and compositional task outcomes provide supervised and RL signals. | Synthetic tool semantics do not establish fidelity to production APIs; the public repository has limited user-facing documentation. |

**Repositories**

| Project | Links | Stars | Tags | Summary |
| --- | --- | --- | --- | --- |
| Agent World Model | [GitHub](https://github.com/Snowflake-Labs/agent-world-model) · [Details](docs/catalog_details.md#agent-world-model--project-awm) | ★ 465 | executable, rl | Synthesizes code-driven, SQL-backed tool worlds with inspectable state and rewards for multi-turn RL and transfer studies. |
| EnvScaler | [GitHub](https://github.com/RUC-NLPIR/EnvScaler) · [Details](docs/catalog_details.md#envscaler--project-envscaler) | ★ 199 | executable, rl+sft | Separates environment skeleton construction from scenario generation and rule-based trajectory validation. |
| CodeGym | [GitHub](https://github.com/StigLidu/CodeGym) · [Details](docs/catalog_details.md#codegym--project-codegym) | ★ 41 | executable, rl | Extracts callable functions from coding problems to synthesize controllable multi-turn tool-use tasks with executable rewards. |
| Agent-World | [GitHub](https://github.com/RUC-NLPIR/Agent-World) · [Details](docs/catalog_details.md#agent-world--project-agent-world) | ★ 7 | executable, rl+sft | Discovers stateful tool ecosystems and generates verifiable tasks, linking multi-environment learning to capability-gap-driven task evolution. |
| RandomWorld | [GitHub](https://github.com/coli-saar/randomworld) · [Details](docs/catalog_details.md#randomworld--project-randomworld) | ★ 3 | structured-synthesis | Procedurally generates interactive tools and compositional tool-use data for both supervised and reinforcement learning. |

**Blogs**

| Article | Publisher | Date | Summary | Evidence |
| --- | --- | --- | --- | --- |
| [Agent World Model: Infinity Synthetic Environments for Agentic Reinforcement Learning](https://www.snowflake.com/en/blog/engineering/agent-world-model-for-agentic-reinforment-learning/) | Snowflake AI Research and collaborators | 2026-02-13 | Explains executable SQL-backed world synthesis, consistent state transitions and reward construction for tool-use RL. | [Details](docs/catalog_details.md#agent-world-model-infinity-synthetic-environments-for-agentic-reinforcement-learning--blog-awm-blog) |
| [Magentic Marketplace: an open-source simulation environment for studying agentic markets](https://www.microsoft.com/en-us/research/blog/magentic-marketplace-an-open-source-simulation-environment-for-studying-agentic-markets/) | Microsoft Research | 2025-11-05 | A shared REST environment supports buyer/seller discovery, communication and simulated transactions, with synthetic market data for reproducible experiments. | [Details](docs/catalog_details.md#magentic-marketplace-an-open-source-simulation-environment-for-studying-agentic-markets--blog-microsoft-marketplace) |

### Procedural Task Generators

**Papers**

| Paper | Date | Resources | Environment / task contribution | Feedback / evidence | Release boundary |
| --- | --- | --- | --- | --- | --- |
| [Reasoning Gym](https://arxiv.org/abs/2505.24760) | 2025-05-30 | [Code](https://github.com/open-thought/reasoning-gym) · [Details](docs/catalog_details.md#reasoning-gym--paper-reasoning-gym) | Generates adjustable-difficulty reasoning tasks with deterministic verifiers instead of relying on a fixed dataset. | RL experiments: Procedural reference answers and task-specific scoring functions. | Many tasks are single-turn; procedural task diversity is different from stateful tool-interaction diversity. |

**Repositories**

| Project | Links | Stars | Tags | Summary |
| --- | --- | --- | --- | --- |
| Reasoning Gym | [GitHub](https://github.com/open-thought/reasoning-gym) · [Details](docs/catalog_details.md#reasoning-gym--project-reasoning-gym) | ★ 1,522 | procedural, rl | Generates adjustable-difficulty reasoning tasks with deterministic verifiers instead of relying on a fixed dataset. |

### Learned Interaction Simulators

**Papers**

| Paper | Date | Resources | Environment / task contribution | Feedback / evidence | Release boundary |
| --- | --- | --- | --- | --- | --- |
| [EnvACE](https://arxiv.org/abs/2608.06197) | 2026-08-06 | [Code](https://github.com/Within-yao/EnvACE) · [Details](docs/catalog_details.md#envace--paper-envace) | Trains a shared policy to act and rehearse environment responses, internalizing dynamics through role-wise RL. | RL experiments: Simulated observations or task-success rewards; real-environment transfer is evaluated separately. | Rehearsed observations are model outputs; simulated consistency needs checking against external execution. |
| [WebWorld](https://arxiv.org/abs/2602.14721) | 2026-02-16 | [Code](https://github.com/QwenLM/WebWorld) · [Details](docs/catalog_details.md#webworld--paper-webworld) | Learns an open-web simulator from interaction trajectories and uses simulated rollouts for web-agent training and planning. | SFT / trajectory training: Simulated observations or task-success rewards; real-environment transfer is evaluated separately. | Simulation quality and real-browser transfer are separate measurements; distinct from later same-name web-code papers. |
| [GenEnv](https://arxiv.org/abs/2512.19682) | 2025-12-22 | [Code](https://github.com/Gen-Verse/GenEnv) · [Details](docs/catalog_details.md#genenv--paper-genenv) | Co-evolves a generative simulator and agent using a difficulty-aligned curriculum reward. | RL experiments: Simulated observations or task-success rewards; real-environment transfer is evaluated separately. | Learned simulation can drift from executable reality; reported gains concern the paper's selected tasks. |
| [SynthTools](https://arxiv.org/abs/2511.09572) | 2025-11-11 | [Code](https://github.com/namkoong-lab/SynthTools) · [Details](docs/catalog_details.md#synthtools--paper-synthtools) | Separates synthetic tool generation, response simulation and tool auditing to scale controllable tool ecosystems. | Environment / task generation: LLM-simulated tool observations with a separate audit stage. | Tool responses are simulated by LLMs; audit accuracy is not a proof of deterministic state transitions. |
| [DreamGym](https://arxiv.org/abs/2511.03773) | 2025-11-05 | [Details](docs/catalog_details.md#dreamgym--paper-dreamgym) | Uses a reasoning-based experience model, replay buffer and adaptive task generation to train agents with synthetic interactions. | RL experiments: Simulated observations or task-success rewards; real-environment transfer is evaluated separately. | Sim-to-real transfer is empirical; a third-party reproduction is not official author code. |

**Repositories**

| Project | Links | Stars | Tags | Summary |
| --- | --- | --- | --- | --- |
| GenEnv | [GitHub](https://github.com/Gen-Verse/GenEnv) · [Details](docs/catalog_details.md#genenv--project-genenv) | ★ 67 | neural, rl | Co-evolves a generative simulator and agent using a difficulty-aligned curriculum reward. |
| WebWorld | [GitHub](https://github.com/QwenLM/WebWorld) · [Details](docs/catalog_details.md#webworld--project-webworld) | ★ 61 | neural, sft | Learns an open-web simulator from interaction trajectories and uses simulated rollouts for web-agent training and planning. |
| EnvACE | [GitHub](https://github.com/Within-yao/EnvACE) · [Details](docs/catalog_details.md#envace--project-envace) | ★ 24 | neural, rl | Trains a shared policy to act and rehearse environment responses, internalizing dynamics through role-wise RL. |
| SynthTools | [GitHub](https://github.com/namkoong-lab/SynthTools) · [Details](docs/catalog_details.md#synthtools--project-synthtools) | ★ 9 | neural, generation | Separates synthetic tool generation, response simulation and tool auditing to scale controllable tool ecosystems. |

**Blogs**

| Article | Publisher | Date | Summary | Evidence |
| --- | --- | --- | --- | --- |
| [Genie 3: A new frontier for world models](https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/) | Google DeepMind | 2025-08-05 | Generates interactive visual worlds from prompts for exploration and agent research. | [Details](docs/catalog_details.md#genie-3-a-new-frontier-for-world-models--blog-deepmind-genie3) |
| [Genie 2: A large-scale foundation world model](https://deepmind.google/blog/genie-2-a-large-scale-foundation-world-model/) | Google DeepMind | 2024-12-04 | Generates action-responsive interactive worlds from an image and alternative trajectories from the same initial frame for agent training and evaluation. | [Details](docs/catalog_details.md#genie-2-a-large-scale-foundation-world-model--blog-deepmind-genie2) |

## Interaction Data & Experience

### Exploration, Replay & Reverse Synthesis

**Papers**

| Paper | Date | Resources | Environment / task contribution | Feedback / evidence | Release boundary |
| --- | --- | --- | --- | --- | --- |
| [TerminalWorld (recordings)](https://arxiv.org/abs/2605.22535) | 2026-05-21 | [Code](https://github.com/EuniAI/TerminalWorld) · [Details](docs/catalog_details.md#terminalworld-recordings--paper-terminalworld-recordings) | Reverse-engineers real terminal recordings into reproducible environments, executable tasks and validated benchmark instances. | Evaluation substrate: Automated reconstruction/validation with a separately human-verified benchmark subset. | Distinct from skill-driven Terminal-World; automatically validated and human-verified subsets have different assurance levels. |
| [CLI-Gym](https://arxiv.org/abs/2602.10999) | 2026-02-11 | [Code](https://github.com/LiberCoders/CLI-Gym) · [Details](docs/catalog_details.md#cli-gym--paper-cli-gym) | Explores healthy environment histories and inverts them into reproducible runtime failures, then packages repair tasks and successful traces. | SFT / trajectory training: Executable initial/final-state or fail-to-pass tests; reference solutions establish solvability. | Produces environment-intensive tasks from existing repositories; instance counts exceed repository/image counts and must not be conflated. |
| [InSTA](https://arxiv.org/abs/2502.06776) | 2025-02-10 | [Code](https://github.com/data-for-agents/insta) · [Details](docs/catalog_details.md#insta--paper-insta) | Annotates websites with tasks, runs agents and filters successful trajectories to build web-interaction data at scale. | SFT / trajectory training: An LLM judges task success and filters collected browser trajectories. | Live-site drift and model-judge error remain; website counts are not counts of newly synthesized environments. |
| [OS-Genesis](https://arxiv.org/abs/2412.19723) | 2024-12-27 | [Code](https://github.com/OS-Copilot/OS-Genesis) · [Details](docs/catalog_details.md#os-genesis--paper-os-genesis) | Explores GUI environments before reverse-synthesizing tasks and scores trajectory quality with a trajectory reward model. | SFT / trajectory training: Reverse-synthesized task consistency and a trajectory reward model for quality selection. | Constructs tasks and trajectories over existing desktop/mobile environments rather than a new operating-system simulator. |
| [AgentTrek](https://arxiv.org/abs/2412.09605) | 2024-12-12 | [Code](https://github.com/xlang-ai/AgentTrek) · [Trajectory dataset](https://huggingface.co/datasets/xlangai/AgentTrek) · [Details](docs/catalog_details.md#agenttrek--paper-agenttrek) | Harvests web tutorials, derives task instructions and guides browser replay, then filters trajectories for training. | SFT / trajectory training: Tutorial-guided browser replay with model-based trajectory verification. | Tutorial replay uses existing websites; it does not synthesize independent website backends, and model judges can err. |

**Repositories**

| Project | Links | Stars | Tags | Summary |
| --- | --- | --- | --- | --- |
| OS-Genesis | [GitHub](https://github.com/OS-Copilot/OS-Genesis) · [Details](docs/catalog_details.md#os-genesis--project-os-genesis) | ★ 190 | replay-exploration | Explores GUI environments before reverse-synthesizing tasks and scores trajectory quality with a trajectory reward model. |
| CLI-Gym | [GitHub](https://github.com/LiberCoders/CLI-Gym) · [Details](docs/catalog_details.md#cli-gym--project-cli-gym) | ★ 141 | replay-exploration | Explores healthy environment histories and inverts them into reproducible runtime failures, then packages repair tasks and successful traces. |
| AgentTrek | [GitHub](https://github.com/xlang-ai/AgentTrek) · [Details](docs/catalog_details.md#agenttrek--project-agenttrek) | ★ 60 | replay-exploration | Harvests web tutorials, derives task instructions and guides browser replay, then filters trajectories for training. |
| InSTA | [GitHub](https://github.com/data-for-agents/insta) · [Details](docs/catalog_details.md#insta--project-insta) | ★ 56 | replay-exploration | Annotates websites with tasks, runs agents and filters successful trajectories to build web-interaction data at scale. |
| TerminalWorld (recordings) | [GitHub](https://github.com/EuniAI/TerminalWorld) · [Details](docs/catalog_details.md#terminalworld-recordings--project-terminalworld-recordings) | ★ 48 | replay-exploration | Reverse-engineers real terminal recordings into reproducible environments, executable tasks and validated benchmark instances. |

### Trajectory Curation & Data Recipes

**Papers**

| Paper | Date | Resources | Environment / task contribution | Feedback / evidence | Release boundary |
| --- | --- | --- | --- | --- | --- |
| [OpenThoughts-Agent](https://arxiv.org/abs/2606.24855) | 2026-06-23 | [Code](https://github.com/open-thoughts/OpenThoughts-Agent) · [Details](docs/catalog_details.md#openthoughts-agent--paper-openthoughts-agent) | Studies task sources, mixtures, teachers, rollout and filtering choices through controlled ablations for terminal-agent data. | SFT / trajectory training: Controlled source, teacher and filtering ablations; the launch RL recipe also verifies tasks in sandboxes. | The 2025 launch blog and 2026 paper describe different release stages; training outcomes depend on the whole data recipe. |

**Repositories**

| Project | Links | Stars | Tags | Summary |
| --- | --- | --- | --- | --- |
| OpenThoughts-Agent | [GitHub](https://github.com/open-thoughts/OpenThoughts-Agent) · [Details](docs/catalog_details.md#openthoughts-agent--project-openthoughts-agent) | ★ 301 | data-curation | Studies task sources, mixtures, teachers, rollout and filtering choices through controlled ablations for terminal-agent data. |

**Blogs**

| Article | Publisher | Date | Summary | Evidence |
| --- | --- | --- | --- | --- |
| [General Agent: A Self-Evolving, Synthetic Agent Environment](https://www.primeintellect.ai/blog/general-agent) | Prime Intellect | 2026-05-18 | Uses synthesizer–solver interaction to build database-backed tool tasks with gold solutions and calibrated difficulty bands. | [Details](docs/catalog_details.md#general-agent-a-self-evolving-synthetic-agent-environment--blog-general-agent) |
| [Launching OpenThoughts-Agent](https://www.openthoughts.ai/blog/agent) | OpenThoughts team | 2025-12-05 | Describes the initial task/teacher ablations, SFT trajectories and a verified NL2Bash RL data pipeline. | [Details](docs/catalog_details.md#launching-openthoughts-agent--blog-openthoughts-agent) |

### Trace Capture & Inspection

**Blogs**

| Article | Publisher | Date | Summary | Evidence |
| --- | --- | --- | --- | --- |
| [Tracing Agent Harness Behavior with NVIDIA NeMo Relay](https://developer.nvidia.com/blog/?p=123038) | NVIDIA / Hermes contributors | 2026-09-30 | Demonstrates ordered event and trajectory capture, paired with task verification and harness-behavior comparisons. | [Details](docs/catalog_details.md#tracing-agent-harness-behavior-with-nvidia-nemo-relay--blog-nemo-relay-tracing) |

## Environment Infrastructure

### Interfaces, Adapters & Registries

**Papers**

| Paper | Date | Resources | Environment / task contribution | Feedback / evidence | Release boundary |
| --- | --- | --- | --- | --- | --- |
| [GEM](https://arxiv.org/abs/2510.01051) | 2025-10-01 | [Code](https://github.com/axon-rl/gem) · [Details](docs/catalog_details.md#gem--paper-gem) | Provides a common agent–environment API, asynchronous vectorization and examples connecting varied environments to RL trainers. | RL experiments: Delegates task reward and correctness to environment authors or connected libraries. | Reward timing and per-turn credit assignment differ across trainers; adapters are not interchangeable without checking semantics. |
| [Meta ARE](https://arxiv.org/abs/2509.17158) | 2025-09-21 | [Code](https://github.com/facebookresearch/meta-agents-research-environments) · [Details](docs/catalog_details.md#meta-are--paper-are) | Separates apps, events and scenarios to simulate dynamic worlds and evaluate agents under asynchronous changes. | Evaluation substrate: Delegates task reward and correctness to environment authors or connected libraries. | ARE is distinct from OpenEnv; Gaia2 results primarily establish evaluation behavior, not a released RL training recipe. |
| [AgentGym-RL](https://arxiv.org/abs/2509.08755) | 2025-09-10 | [Code](https://github.com/WooooDyy/AgentGym-RL) · [Details](docs/catalog_details.md#agentgym-rl--paper-agentgym-rl) | Decouples training and environment services and expands interaction horizons progressively for multi-turn RL. | RL experiments: Delegates task reward and correctness to environment authors or connected libraries. | Requires configuring each underlying environment and its services; it is not a single dependency-free simulator. |
| [AgentGym](https://arxiv.org/abs/2406.04151) | 2024-06-06 | [Code](https://github.com/WooooDyy/AgentGym) · [Details](docs/catalog_details.md#agentgym--paper-agentgym) | Standardizes diverse environment servers and trajectories for generalist agent exploration and iterative learning. | SFT / trajectory training: Delegates task reward and correctness to environment authors or connected libraries. | The original AgentEvol study and later AgentGym-RL release use different learning pipelines. |

**Repositories**

| Project | Links | Stars | Tags | Summary |
| --- | --- | --- | --- | --- |
| Verifiers | [GitHub](https://github.com/PrimeIntellect-ai/verifiers) · [Details](docs/catalog_details.md#verifiers--project-verifiers) | ★ 4,679 | framework, rollout | Builds training and evaluation environments with composable tasksets, harnesses, rubrics and runtimes. |
| OpenEnv | [GitHub](https://github.com/huggingface/OpenEnv) · [Details](docs/catalog_details.md#openenv--project-openenv) | ★ 2,674 | framework, rollout | Standardizes isolated environment deployment and interaction through Gym-style APIs and remote services. |
| NeMo Gym | [GitHub](https://github.com/NVIDIA-NeMo/Gym) · [Details](docs/catalog_details.md#nemo-gym--project-nemo-gym) | ★ 1,225 | framework, rollout | Provides environment services, verifiers, sandbox adapters and scalable rollout collection for agent post-training. |
| AgentGym-RL | [GitHub](https://github.com/WooooDyy/AgentGym-RL) · [Details](docs/catalog_details.md#agentgym-rl--project-agentgym-rl) | ★ 874 | mixed, rl | Decouples training and environment services and expands interaction horizons progressively for multi-turn RL. |
| AgentGym | [GitHub](https://github.com/WooooDyy/AgentGym) · [Details](docs/catalog_details.md#agentgym--project-agentgym) | ★ 850 | mixed, sft | Standardizes diverse environment servers and trajectories for generalist agent exploration and iterative learning. |
| Meta ARE | [GitHub](https://github.com/facebookresearch/meta-agents-research-environments) · [Details](docs/catalog_details.md#meta-are--project-are) | ★ 561 | mixed, evaluation | Separates apps, events and scenarios to simulate dynamic worlds and evaluate agents under asynchronous changes. |
| GEM | [GitHub](https://github.com/axon-rl/gem) · [Details](docs/catalog_details.md#gem--project-gem) | ★ 510 | mixed, rl | Provides a common agent–environment API, asynchronous vectorization and examples connecting varied environments to RL trainers. |
| AgentEnv (Scale) | [GitHub](https://github.com/scaleapi/agentenv-framework) · [Details](docs/catalog_details.md#agentenv-scale--project-scale-agentenv) | ★ 165 | framework, rollout | SDK and CLI for versioned environment images, composable task execution, plugins and agent grading. |

**Blogs**

| Article | Publisher | Date | Summary | Evidence |
| --- | --- | --- | --- | --- |
| [Introducing AgentEnv: An Open-Source Framework for Building RL Environments](https://labs.scale.com/blog/introducing-agentenv) | Scale Labs | 2026-10-05 | Explains reusable environment blocks, artifacts, rules and task DAGs with agent- and sandbox-independent execution. | [Details](docs/catalog_details.md#introducing-agentenv-an-open-source-framework-for-building-rl-environments--blog-scale-agentenv) |
| [Welcome RL Environments to the hub](https://huggingface.co/blog/rl-environments) | Hugging Face | 2026-09-28 | Defines dataset tags and framework compatibility metadata for discovering and versioning RL tasksets on the Hub. | [Details](docs/catalog_details.md#welcome-rl-environments-to-the-hub--blog-hf-env-hub) |
| [Multi-Agent Systems in PRIME-RL](https://www.primeintellect.ai/blog/multi-agent-systems) | Prime Intellect | 2026-08-07 | Adds programmable agent interactions, trainable-role selection and credit assignment for self-play, user simulation and judging. | [Details](docs/catalog_details.md#multi-agent-systems-in-prime-rl--blog-multi-agent-rl) |
| [Training a coding agent using the OpenCode harness in remote HF sandboxes with TRL and OpenEnv](https://huggingface.co/blog/sergiopaniego/trl-openenv-harness-training) | Sergio Paniego / author technical blog | 2026-08-05 | Shows one sandbox per rollout, proxy capture of token-faithful traces and workspace-based reward for AsyncGRPO. | [Details](docs/catalog_details.md#training-a-coding-agent-using-the-opencode-harness-in-remote-hf-sandboxes-with-trl-and-openenv--blog-trl-openenv) |
| [Scaling Agentic RL: 365,000+ Environments for SWE, Terminal, and Search](https://www.primeintellect.ai/blog/scaling-agentic-rl) | Prime Intellect | 2026-07-22 | Normalizes taskset lifecycle and sandboxes while retaining upstream scoring logic and withholding grading materials during rollouts. | [Details](docs/catalog_details.md#scaling-agentic-rl-365000-environments-for-swe-terminal-and-search--blog-prime-scale) |
| [verifiers v1: Decomposing Tasksets and Harnesses for Agentic RL & Evaluations](https://www.primeintellect.ai/blog/verifiers-v1) | Prime Intellect | 2026-07-12 | Splits tasksets, harnesses and runtimes while preserving branching traces and training tokens. | [Details](docs/catalog_details.md#verifiers-v1-decomposing-tasksets-and-harnesses-for-agentic-rl--evaluations--blog-verifiers-v1) |
| [The Open Source Community is backing OpenEnv for Agentic RL](https://huggingface.co/blog/openenv-agentic-rl) | OpenEnv contributors / Hugging Face | 2026-06-08 | Clarifies OpenEnv as an interoperability layer across environment libraries, agent harnesses and trainers. | [Details](docs/catalog_details.md#the-open-source-community-is-backing-openenv-for-agentic-rl--blog-openenv-community) |
| [Scaling OpenEnv: From Free Usage to Thousands of Concurrent Environments](https://huggingface.co/blog/burtenshaw/openenv-scaling) | Ben Burtenshaw / author technical blog | 2026-01-20 | Benchmarks deployment tiers from Spaces and Docker to clustered concurrent environment sessions. | [Details](docs/catalog_details.md#scaling-openenv-from-free-usage-to-thousands-of-concurrent-environments--blog-openenv-scaling) |
| [How to Train Scientific Agents with Reinforcement Learning](https://developer.nvidia.com/blog/how-to-train-scientific-agents-with-reinforcement-learning/) | NVIDIA / Edison Scientific | 2025-12-15 | Walks through model, resource and agent servers, using Aviary to build and verify scientific rollouts. | [Details](docs/catalog_details.md#how-to-train-scientific-agents-with-reinforcement-learning--blog-nemo-science) |
| [The Building Blocks of Agentic AI: From Kernels to Clusters](https://ai.meta.com/blog/introducing-pytorch-native-agentic-stack/) | Meta | 2025-10-24 | The OpenEnv section introduces a shared environment hub, tool/observation interfaces and human or model interaction before training. | [Details](docs/catalog_details.md#the-building-blocks-of-agentic-ai-from-kernels-to-clusters--blog-meta-openenv) |
| [Building the Open Agent Ecosystem Together: Introducing OpenEnv](https://huggingface.co/blog/openenv) | Meta-PyTorch / Hugging Face | 2025-10-23 | Introduces the environment contract, container packaging and shared hub for agent interaction. | [Details](docs/catalog_details.md#building-the-open-agent-ecosystem-together-introducing-openenv--blog-openenv-launch) |
| [Environments Hub: A Community Hub To Scale RL To Open AGI](https://www.primeintellect.ai/blog/environments) | Prime Intellect | 2025-08-27 | Describes publishing reusable verifiers environments with tasks, feedback and training integration. | [Details](docs/catalog_details.md#environments-hub-a-community-hub-to-scale-rl-to-open-agi--blog-environments-hub) |

### Sandboxes & Rollout Execution

**Papers**

| Paper | Date | Resources | Environment / task contribution | Feedback / evidence | Release boundary |
| --- | --- | --- | --- | --- | --- |
| [DeepSeek Elastic Compute (DSec)](https://arxiv.org/abs/2609.22978) | 2026-09-19 | [Details](docs/catalog_details.md#deepseek-elastic-compute-dsec--paper-dsec) | Unifies function calls, containers, microVMs and full VMs; supports agent-built reusable environments and pause/resume for long-running rollouts. | Environment infrastructure: Operational evidence for construction, isolation and lifecycle management; not a standalone task benchmark. | A production infrastructure paper; no official public DSec implementation is confirmed. Related projects such as 3FS are not the complete DSec platform. |

**Repositories**

| Project | Links | Stars | Tags | Summary |
| --- | --- | --- | --- | --- |
| Harbor | [GitHub](https://github.com/harbor-framework/harbor) · [Details](docs/catalog_details.md#harbor--project-harbor) | ★ 5,891 | framework, rollout | Runs containerized tasks across agents and sandbox providers, supporting parallel evaluation and RL rollout generation. |
| MiMo-V2.6 RL OSS Environments (XiaomiMiMo/verl) | [GitHub](https://github.com/XiaomiMiMo/verl) · [RL OSS dataset](https://huggingface.co/datasets/XiaomiMiMo/MiMo-V2.6-RL-oss) · [Docker images](https://hub.docker.com/r/xiaomimimo/mimo-v2.6-rl-oss) · [Technical report (companion)](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL/blob/main/MiMo_V2_6_technical_report.pdf) · [Community explorer (unofficial)](https://huggingface.co/spaces/FineEnvs/MiMo-RL-Envs-Explorer) · [Details](docs/catalog_details.md#mimo-v26-rl-oss-environments-xiaomimimoverl--project-xiaomi-mimo-verl) | ★ 666 | agentic-rl, multi-domain, mimo-oss | Publishes five domain-specific RL environment recipes with task data, Docker images and verifier integration on a verl fork. |
| MiMo Agent (mimoagent) | [GitHub](https://github.com/XiaomiMiMo/mimoagent) · [Details](docs/catalog_details.md#mimo-agent-mimoagent--project-xiaomi-mimoagent) | ★ 39 | agentic-rl, multi-domain, mimo-oss | Separates agents, model protocols, execution backends and dataset graders, capturing training trajectories and grading final environment state. |

**Blogs**

| Article | Publisher | Date | Summary | Evidence |
| --- | --- | --- | --- | --- |
| [Prime Sandboxes: MicroVMs for Agentic RL Training at Scale](https://www.primeintellect.ai/blog/sandboxes) | Prime Intellect | 2026-09-23 | Explains VM-backed rollout isolation, image reuse and scaling many concurrent training environments. | [Details](docs/catalog_details.md#prime-sandboxes-microvms-for-agentic-rl-training-at-scale--blog-prime-sandboxes) |
| [Custom reward functions for multi-turn reinforcement learning with Amazon Nova Forge](https://aws.amazon.com/blogs/machine-learning/custom-reward-functions-for-multi-turn-reinforcement-learning-with-amazon-nova-forge/) | Amazon / AWS | 2026-08-14 | BYOO containers manage multi-turn state, user simulation, execution and verification, returning completed episodes and aggregate rewards. | [Details](docs/catalog_details.md#custom-reward-functions-for-multi-turn-reinforcement-learning-with-amazon-nova-forge--blog-aws-nova-rewards) |
| [Deploying Multi-Turn RL Infrastructure for Amazon Nova on Amazon SageMaker HyperPod](https://aws.amazon.com/blogs/machine-learning/deploying-multi-turn-rl-infrastructure-for-amazon-nova-on-amazon-sagemaker-hyperpod/) | Amazon / AWS | 2026-07-06 | Uses Wordle to separate HyperPod training, ECS reward environments and stateful message routing, with per-run resource lifecycles. | [Details](docs/catalog_details.md#deploying-multi-turn-rl-infrastructure-for-amazon-nova-on-amazon-sagemaker-hyperpod--blog-aws-nova-infra) |
| [Introducing SWE-1.5: Our Fast Agent Model](https://cognition.com/blog/swe-1-5) | Cognition | 2025-10-29 | Describes real-task RL with Cascade and otterlink VMs for code execution, browsing and high concurrency aligned with Devin production. | [Details](docs/catalog_details.md#introducing-swe-15-our-fast-agent-model--blog-cognition-swe15) |

## Domain Environments & Benchmarks

### Software, Terminal & Executable Skills

**Papers**

| Paper | Date | Resources | Environment / task contribution | Feedback / evidence | Release boundary |
| --- | --- | --- | --- | --- | --- |
| [SkillScriptBench](https://arxiv.org/abs/2610.04008) | 2026-10-02 | [Details](docs/catalog_details.md#skillscriptbench--paper-skillscriptbench) | Constructs executable skill-package tests with injected script faults and controlled package-editing cases. | Evaluation substrate: Controlled fault injection and executable package-editing tests distinguish script repair from documentation changes. | A benchmark for executable skill repair, not a general world generator; official code was not confirmed. |
| [Terminal-Bench](https://arxiv.org/abs/2601.11868) | 2026-01-17 | [Code](https://github.com/harbor-framework/terminal-bench) · [Details](docs/catalog_details.md#terminal-bench--paper-terminal-bench) | Packages realistic terminal tasks with isolated execution environments, reference solutions and outcome tests. | Evaluation substrate: Task-specific execution tests or verifier scores; consult the resource for the exact split. | This paper describes Terminal-Bench 2.0; evaluation tasks must remain held out from training. |

**Repositories**

| Project | Links | Stars | Tags | Summary |
| --- | --- | --- | --- | --- |
| Terminal-Bench | [GitHub](https://github.com/harbor-framework/terminal-bench) · [Details](docs/catalog_details.md#terminal-bench--project-terminal-bench) | ★ 852 | executable, evaluation | Packages realistic terminal tasks with isolated execution environments, reference solutions and outcome tests. |

**Blogs**

| Article | Publisher | Date | Summary | Evidence |
| --- | --- | --- | --- | --- |
| [Introducing SWE-bench Verified](https://openai.com/index/introducing-swe-bench-verified/) | OpenAI | 2024-08-13 | Human review of specifications, test validity and solvability filters SWE-bench tasks, with Docker execution improving reproducibility. | [Details](docs/catalog_details.md#introducing-swe-bench-verified--blog-openai-swe-verified) |

### Browser, Desktop & Mobile

**Papers**

| Paper | Date | Resources | Environment / task contribution | Feedback / evidence | Release boundary |
| --- | --- | --- | --- | --- | --- |
| [BrowserGym](https://arxiv.org/abs/2412.05467) | 2024-12-06 | [Code](https://github.com/ServiceNow/BrowserGym) · [Details](docs/catalog_details.md#browsergym--paper-browsergym) | Unifies browser observations, actions and benchmark interfaces; AgentLab adds experiment management. | Evaluation substrate: State, artifact or rubric evaluation after interaction; evaluator type varies by task. | A common interface does not make every included benchmark an approved training split. |
| [AndroidWorld](https://arxiv.org/abs/2405.14573) | 2024-05-23 | [Code](https://github.com/google-research/android_world) · [Details](docs/catalog_details.md#androidworld--paper-androidworld) | Builds parameterized Android tasks with emulator setup and programmatic state-based success checks. | Evaluation substrate: State, artifact or rubric evaluation after interaction; evaluator type varies by task. | App versions and emulator configuration affect reproducibility; benchmark success is not a demonstrated training result. |
| [OSWorld](https://arxiv.org/abs/2404.07972) | 2024-04-11 | [Code](https://github.com/xlang-ai/OSWorld) · [Details](docs/catalog_details.md#osworld--paper-osworld) | Provides real desktop task initialization and execution-based evaluators across applications. | Evaluation substrate: State, artifact or rubric evaluation after interaction; evaluator type varies by task. | GUI execution is expensive and platform-sensitive; the benchmark split should not become RL practice data. |
| [WebArena](https://arxiv.org/abs/2307.13854) | 2023-07-25 | [Code](https://github.com/web-arena-x/webarena) · [Details](docs/catalog_details.md#webarena--paper-webarena) | Hosts reproducible websites and checks task outcomes to evaluate realistic multi-step web actions. | Evaluation substrate: State, artifact or rubric evaluation after interaction; evaluator type varies by task. | Resetting sites and maintaining deployment images are necessary; published test tasks need contamination controls. |

**Repositories**

| Project | Links | Stars | Tags | Summary |
| --- | --- | --- | --- | --- |
| OSWorld | [GitHub](https://github.com/xlang-ai/OSWorld) · [Details](docs/catalog_details.md#osworld--project-osworld) | ★ 3,179 | desktop, evaluation | Provides real desktop task initialization and execution-based evaluators across applications. |
| WebArena | [GitHub](https://github.com/web-arena-x/webarena) · [Details](docs/catalog_details.md#webarena--project-webarena) | ★ 1,619 | browser, evaluation | Hosts reproducible websites and checks task outcomes to evaluate realistic multi-step web actions. |
| BrowserGym | [GitHub](https://github.com/ServiceNow/BrowserGym) · [Details](docs/catalog_details.md#browsergym--project-browsergym) | ★ 1,390 | browser, evaluation | Unifies browser observations, actions and benchmark interfaces; AgentLab adds experiment management. |
| AndroidWorld | [GitHub](https://github.com/google-research/android_world) · [Details](docs/catalog_details.md#androidworld--project-androidworld) | ★ 945 | mobile, evaluation | Builds parameterized Android tasks with emulator setup and programmatic state-based success checks. |
| benchmark | [GitHub](https://github.com/browser-use/benchmark) · [Details](docs/catalog_details.md#benchmark--project-browser-use-bench) | ★ 149 | gui-bench | Explains live-web task selection, encrypted test distribution and model-based success judging for BU Bench. |

**Blogs**

| Article | Publisher | Date | Summary | Evidence |
| --- | --- | --- | --- | --- |
| [Browser Use benchmark construction](https://browser-use.com/posts/ai-browser-agent-benchmark) | Browser Use | 2026-01-31 | Explains live-web task selection, encrypted test distribution and model-based success judging for BU Bench. | [Details](docs/catalog_details.md#browser-use-benchmark-construction--blog-browser-use-bench) |

### Tools & Enterprise Workflows

**Papers**

| Paper | Date | Resources | Environment / task contribution | Feedback / evidence | Release boundary |
| --- | --- | --- | --- | --- | --- |
| [MM-ToolSandBox](https://arxiv.org/abs/2607.11818) | 2026-07-13 | [Code](https://github.com/apple-aiml-research/ml-mmtoolsandbox) · [Details](docs/catalog_details.md#mm-toolsandbox--paper-mm-toolsandbox) | Extends stateful tool evaluation to visual inputs, scenario generation and multi-turn state changes. | Evaluation substrate: Task state, trajectory milestones or rubric-based evaluation. | A visual tool-call benchmark, not proof of an RL-trained agent; image extraction errors require separate analysis. |
| [C-World (formerly ToolGym)](https://arxiv.org/abs/2601.06328) | 2026-01-09 | [Code](https://github.com/Ziqiao-git/C-World) · [Details](docs/catalog_details.md#c-world-formerly-toolgym--paper-c-world) | Creates computer-use tool environments with task generation, perturbable transitions, and executable or simulated tool responses. | SFT / trajectory training: Task state, trajectory milestones or rubric-based evaluation. | The current paper is named C-World while the project page and README retain ToolGym; distinguish live APIs from simulation and account for model-based judging. |
| [τ²-bench](https://arxiv.org/abs/2506.07982) | 2025-06-09 | [Code](https://github.com/sierra-research/tau2-bench) · [Details](docs/catalog_details.md#τ²-bench--paper-tau2) | Models shared state changed by both assistant and simulated user, with compositional tasks and outcome evaluation. | Evaluation substrate: Shared-world task outcome and policy-adherence checks. | User-simulator behavior affects results; treat benchmark tasks as held-out evaluation rather than free training data. |
| [TheAgentCompany](https://arxiv.org/abs/2412.14161) | 2024-12-18 | [Code](https://github.com/TheAgentCompany/TheAgentCompany) · [Details](docs/catalog_details.md#theagentcompany--paper-theagentcompany) | Creates a self-contained workplace of websites, files and simulated coworkers for long-horizon professional tasks. | Evaluation substrate: Task state, trajectory milestones or rubric-based evaluation. | A workplace benchmark does not by itself establish train/test separation or reliable RL rewards for new tasks. |
| [ToolSandbox](https://arxiv.org/abs/2408.04682) | 2024-08-08 | [Code](https://github.com/apple-aiml-research/ToolSandbox) · [Details](docs/catalog_details.md#toolsandbox--paper-toolsandbox) | Combines stateful tool execution, user simulation and milestone-based checks over full conversational trajectories. | Evaluation substrate: Intermediate milestones and final state over the trajectory. | Stateful evaluation infrastructure is reusable, but the paper's main evidence is evaluation rather than policy training. |
| [AppWorld](https://arxiv.org/abs/2407.18901) | 2024-07-26 | [Code](https://github.com/StonyBrookNLP/appworld) · [Details](docs/catalog_details.md#appworld--paper-appworld) | Simulates interconnected personal apps through executable APIs and validates final state plus unintended side effects. | Evaluation substrate: State-based unit tests including collateral changes. | Train/development/test tasks and software/data licenses have distinct roles; preserve the official split policy. |
| [WorkArena](https://arxiv.org/abs/2403.07718) | 2024-03-12 | [Code](https://github.com/ServiceNow/WorkArena) · [Details](docs/catalog_details.md#workarena--paper-workarena) | Uses ServiceNow workflows as browser tasks with programmatic validation of enterprise actions. | Evaluation substrate: Task state, trajectory milestones or rubric-based evaluation. | Requires suitable ServiceNow instances and credentials; this is not a self-contained offline app simulator. |
| [WebShop](https://arxiv.org/abs/2207.01206) | 2022-07-04 | [Code](https://github.com/princeton-nlp/WebShop) · [Details](docs/catalog_details.md#webshop--paper-webshop) | Builds a shopping environment with natural-language goals and product-attribute reward signals for interactive learning. | RL experiments: Task state, trajectory milestones or rubric-based evaluation. | Product catalogs and website behavior are simplified; shopping success is a narrow capability measure. |

**Repositories**

| Project | Links | Stars | Tags | Summary |
| --- | --- | --- | --- | --- |
| τ²-bench | [GitHub](https://github.com/sierra-research/tau2-bench) · [Details](docs/catalog_details.md#τ²-bench--project-tau2) | ★ 2,181 | executable, evaluation | Models shared state changed by both assistant and simulated user, with compositional tasks and outcome evaluation. |
| TheAgentCompany | [GitHub](https://github.com/TheAgentCompany/TheAgentCompany) · [Details](docs/catalog_details.md#theagentcompany--project-theagentcompany) | ★ 792 | mixed, evaluation | Creates a self-contained workplace of websites, files and simulated coworkers for long-horizon professional tasks. |
| WebShop | [GitHub](https://github.com/princeton-nlp/WebShop) · [Details](docs/catalog_details.md#webshop--project-webshop) | ★ 602 | browser, rl | Builds a shopping environment with natural-language goals and product-attribute reward signals for interactive learning. |
| AppWorld | [GitHub](https://github.com/StonyBrookNLP/appworld) · [Details](docs/catalog_details.md#appworld--project-appworld) | ★ 529 | executable, evaluation | Simulates interconnected personal apps through executable APIs and validates final state plus unintended side effects. |
| ToolSandbox | [GitHub](https://github.com/apple-aiml-research/ToolSandbox) · [Details](docs/catalog_details.md#toolsandbox--project-toolsandbox) | ★ 287 | executable, evaluation | Combines stateful tool execution, user simulation and milestone-based checks over full conversational trajectories. |
| WorkArena | [GitHub](https://github.com/ServiceNow/WorkArena) · [Details](docs/catalog_details.md#workarena--project-workarena) | ★ 274 | browser, evaluation | Uses ServiceNow workflows as browser tasks with programmatic validation of enterprise actions. |
| MM-ToolSandBox | [GitHub](https://github.com/apple-aiml-research/ml-mmtoolsandbox) · [Details](docs/catalog_details.md#mm-toolsandbox--project-mm-toolsandbox) | ★ 29 | executable, evaluation | Extends stateful tool evaluation to visual inputs, scenario generation and multi-turn state changes. |
| C-World (formerly ToolGym) | [GitHub](https://github.com/Ziqiao-git/C-World) · [Details](docs/catalog_details.md#c-world-formerly-toolgym--project-c-world) | ★ 10 | mixed, sft | Creates computer-use tool environments with task generation, perturbable transitions, and executable or simulated tool responses. |

**Blogs**

| Article | Publisher | Date | Summary | Evidence |
| --- | --- | --- | --- | --- |
| [OpenEnv in Practice: Evaluating Tool-Using Agents in Real-World Environments](https://huggingface.co/blog/openenv-turing) | Turing / Hugging Face | 2026-02-12 | Uses calendar tasks to expose state, permissions, temporal reasoning and recovery requirements in tool environments. | [Details](docs/catalog_details.md#openenv-in-practice-evaluating-tool-using-agents-in-real-world-environments--blog-calendar-gym) |
| [Scaling Enterprise Agent Performance with Reinforcement Learning via Verifiable Feedback Loops](https://labs.scale.com/blog/scaling-enterprise-agent-performance-with-reinforcement-learning-via-verifiable-feedback-loops) | Scale Labs | 2025-11-17 | Examines environment design and verifiable feedback for domain-specific SQL and enterprise reasoning training. | [Details](docs/catalog_details.md#scaling-enterprise-agent-performance-with-reinforcement-learning-via-verifiable-feedback-loops--blog-scale-enterprise) |

### Games & Interactive Reasoning

**Papers**

| Paper | Date | Resources | Environment / task contribution | Feedback / evidence | Release boundary |
| --- | --- | --- | --- | --- | --- |
| [TextArena](https://arxiv.org/abs/2504.11442) | 2025-04-15 | [Code](https://github.com/TextArena/TextArena) · [Details](docs/catalog_details.md#textarena--paper-textarena) | Packages text games with rules, multi-player interaction and reward interfaces for agent training and evaluation. | Trainable interface: Task-specific reference answers or game-rule outcomes. | Game win rates depend on opponents and rules; they are not direct measurements of workplace competence. |

**Repositories**

| Project | Links | Stars | Tags | Summary |
| --- | --- | --- | --- | --- |
| TextArena | [GitHub](https://github.com/TextArena/TextArena) · [Details](docs/catalog_details.md#textarena--project-textarena) | ★ 430 | game, rl-ready | Packages text games with rules, multi-player interaction and reward interfaces for agent training and evaluation. |

**Blogs**

| Article | Publisher | Date | Summary | Evidence |
| --- | --- | --- | --- | --- |
| [SIMA 2: An agent that plays, reasons, and learns with you in virtual 3D worlds](https://deepmind.google/blog/sima-2-an-agent-that-plays-reasons-and-learns-with-you-in-virtual-3d-worlds/) | Google DeepMind | 2025-11-13 | Uses diverse virtual worlds for embodied interaction and examines generalization to Genie-generated worlds. | [Details](docs/catalog_details.md#sima-2-an-agent-that-plays-reasons-and-learns-with-you-in-virtual-3d-worlds--blog-deepmind-sima2) |

### Science & Embodied Environments

**Papers**

| Paper | Date | Resources | Environment / task contribution | Feedback / evidence | Release boundary |
| --- | --- | --- | --- | --- | --- |
| [Aviary](https://arxiv.org/abs/2412.21154) | 2024-12-30 | [Code](https://github.com/Future-House/aviary) · [Details](docs/catalog_details.md#aviary--paper-aviary) | Defines language-agent environments with scientific tools and rewards, including literature, cloning and protein tasks. | RL experiments: Domain-specific goal and scientific-task checks. | Domain tools and external services add dependencies; simulated scientific success is not laboratory validation. |
| [ScienceWorld](https://arxiv.org/abs/2203.07540) | 2022-03-14 | [Code](https://github.com/allenai/ScienceWorld) · [Details](docs/catalog_details.md#scienceworld--paper-scienceworld) | Offers an interactive text science world with compositional experiments and environment-based goal checks. | Evaluation substrate: Domain-specific goal and scientific-task checks. | A simplified simulator is useful for planning research but does not reproduce physical laboratory dynamics. |
| [ALFWorld](https://arxiv.org/abs/2010.03768) | 2020-10-08 | [Code](https://github.com/alfworld/alfworld) · [Details](docs/catalog_details.md#alfworld--paper-alfworld) | Aligns symbolic text interactions with embodied household tasks; BUTLER learns with DAgger imitation learning and transfers the learned policy. | Imitation learning: Domain-specific goal and scientific-task checks. | Text and embodied versions differ in perception and execution costs; treat this as foundational context. |

**Repositories**

| Project | Links | Stars | Tags | Summary |
| --- | --- | --- | --- | --- |
| ALFWorld | [GitHub](https://github.com/alfworld/alfworld) · [Details](docs/catalog_details.md#alfworld--project-alfworld) | ★ 881 | game, imitation | Aligns symbolic text interactions with embodied household tasks; BUTLER learns with DAgger imitation learning and transfers the learned policy. |
| ScienceWorld | [GitHub](https://github.com/allenai/ScienceWorld) · [Details](docs/catalog_details.md#scienceworld--project-scienceworld) | ★ 395 | game, evaluation | Offers an interactive text science world with compositional experiments and environment-based goal checks. |
| Aviary | [GitHub](https://github.com/Future-House/aviary) · [Details](docs/catalog_details.md#aviary--project-aviary) | ★ 284 | executable, rl | Defines language-agent environments with scientific tools and rewards, including literature, cloning and protein tasks. |

**Blogs**

| Article | Publisher | Date | Summary | Evidence |
| --- | --- | --- | --- | --- |
| [PaperBench: Evaluating AI’s Ability to Replicate AI Research](https://openai.com/index/paperbench/) | OpenAI | 2025-04-02 | Decomposes paper replication into hierarchical rubrics co-developed with authors and separately evaluates automated judges. | [Details](docs/catalog_details.md#paperbench-evaluating-ais-ability-to-replicate-ai-research--blog-openai-paperbench) |

## Adaptation & Quality

### Curricula & Co-evolving Environments

**Papers**

| Paper | Date | Resources | Environment / task contribution | Feedback / evidence | Release boundary |
| --- | --- | --- | --- | --- | --- |
| [VERA](https://arxiv.org/abs/2610.05923) | 2026-10-05 | [Details](docs/catalog_details.md#vera--paper-vera) | Builds resumable sandboxes from trajectories, filters them with checks, and alternates policy training with harness-skill updates. | RL and harness learning: Rubric rewards, executable checks and development-set acceptance gates. | Very recent preprint; the reviewed abstract and full text do not expose a confirmed official repository. |
| [EnvHarness](https://arxiv.org/abs/2608.19880) | 2026-08-20 | [Code](https://github.com/google-research/envharness) · [Details](docs/catalog_details.md#envharness--paper-envharness) | Wraps fixed environments with programmable setup, interaction and composition layers, adapting practice while retaining original verifiers. | RL and harness learning: Original environment verifiers plus held-out task evaluation. | Transfers are measured on selected benchmarks; retaining a verifier does not prove every generated wrapper preserves task semantics. |
| [SPADE](https://arxiv.org/abs/2608.19197) | 2026-08-19 | [Code](https://github.com/spade-rl/spade) · [Details](docs/catalog_details.md#spade--paper-spade) | Co-trains one policy as environment designer and solver; executable reset/step worlds are selected using hint-based regret. | RL experiments: Executable environment rewards and a hint-based regret signal for the designer. | Grounding corpora, memory and feasibility controls remain necessary; experiments do not establish unbounded improvement. |
| [Envs-FORGE](https://arxiv.org/abs/2608.14312) | 2026-08-14 | [Partial / associated code](https://github.com/DataArcTech/DataArc-SynData-Toolkit) · [Details](docs/catalog_details.md#envs-forge--paper-envs-forge) | Uses verifier pass rates to choose per-seed synthesis actions and jointly rewrite tasks, fixtures, tests and Docker environments. | RL experiments: Task success feeds difficulty adaptation; see method-specific verification details. | The linked repository is a broader toolkit; a complete paper-specific reproduction path was not established in its root README. |
| [CalibForge](https://arxiv.org/abs/2608.06352) | 2026-08-06 | [Partial / associated code](https://github.com/AweAI-Team/CalibForge) · [Details](docs/catalog_details.md#calibforge--paper-calibforge) | Revises terminal tasks using verified solver disagreement or strong-pass/weak-fail contrasts to target a learnable difficulty zone. | SFT / trajectory training: Verified solver outcomes target either solver disagreement or strong-pass/weak-fail relations. | Calibration is solver-relative, not an absolute hardness score; public data and agent recipes are not the full synthesis engine. |
| [Beyond Simply Environment Scaling](https://arxiv.org/abs/2608.03571) | 2026-08-04 | [Code](https://github.com/GaryStack/Beyond-MMEnv-Scaling) · [Details](docs/catalog_details.md#beyond-simply-environment-scaling--paper-beyond-mm-scaling) | Studies environment distributions through ability-aware selection and a hierarchy of interaction difficulty and state size. | RL experiments: Task success feeds difficulty adaptation; see method-specific verification details. | Environment count alone is not the treatment; benefits depend on the evaluated diversity and difficulty settings. |
| [EvoEnv](https://arxiv.org/abs/2605.14392) | 2026-05-14 | [Details](docs/catalog_details.md#evoenv--paper-evoenv) | Synthesizes reusable Python generators and verifiers, exploiting solve–verify asymmetry to sustain reasoning training signals. | RL experiments: Generated executable oracles with staged admission checks. | A work-in-progress technical report; verifiable reasoning generators do not automatically constitute real multi-tool workflows. |
| [RLVE](https://arxiv.org/abs/2511.07317) | 2025-11-10 | [Code](https://github.com/Zhiyuan-Zeng/RLVE) · [Details](docs/catalog_details.md#rlve--paper-rlve) | Adapts procedural task difficulty to the current policy across a manually engineered suite of verifiable reasoning environments. | RL experiments: Algorithmic answer verification and adaptive solve-rate calibration. | Environment engineering is still manual; procedural reasoning results should not be extrapolated to GUI or enterprise workflows. |
| [Environment Tuning](https://arxiv.org/abs/2510.10197) | 2025-10-11 | [Code](https://github.com/inclusionAI/AWorld-RL) · [Details](docs/catalog_details.md#environment-tuning--paper-env-tuning) | Combines a task curriculum, corrective environment feedback and progress rewards to stabilize sparse-data tool-use learning. | RL experiments: Task success feeds difficulty adaptation; see method-specific verification details. | Augmented feedback is part of training; deployment must be evaluated without assuming the same privileged help. |

**Repositories**

| Project | Links | Stars | Tags | Summary |
| --- | --- | --- | --- | --- |
| EnvHarness | [GitHub](https://github.com/google-research/envharness) · [Details](docs/catalog_details.md#envharness--project-envharness) | ★ 621 | executable, rl+harness | Wraps fixed environments with programmable setup, interaction and composition layers, adapting practice while retaining original verifiers. |
| RLVE | [GitHub](https://github.com/Zhiyuan-Zeng/RLVE) · [Details](docs/catalog_details.md#rlve--project-rlve) | ★ 235 | procedural, rl | Adapts procedural task difficulty to the current policy across a manually engineered suite of verifiable reasoning environments. |
| Environment Tuning | [GitHub](https://github.com/inclusionAI/AWorld-RL) · [Details](docs/catalog_details.md#environment-tuning--project-env-tuning) | ★ 127 | executable, rl | Combines a task curriculum, corrective environment feedback and progress rewards to stabilize sparse-data tool-use learning. |
| SPADE | [GitHub](https://github.com/spade-rl/spade) · [Details](docs/catalog_details.md#spade--project-spade) | ★ 114 | executable, rl | Co-trains one policy as environment designer and solver; executable reset/step worlds are selected using hint-based regret. |
| Beyond Simply Environment Scaling | [GitHub](https://github.com/GaryStack/Beyond-MMEnv-Scaling) · [Details](docs/catalog_details.md#beyond-simply-environment-scaling--project-beyond-mm-scaling) | ★ 15 | mixed, rl | Studies environment distributions through ability-aware selection and a hierarchy of interaction difficulty and state size. |
| CalibForge | [GitHub](https://github.com/AweAI-Team/CalibForge) · [Details](docs/catalog_details.md#calibforge--project-calibforge) | ★ 10 | curriculum | Revises terminal tasks using verified solver disagreement or strong-pass/weak-fail contrasts to target a learnable difficulty zone. |

### Verifiers, Contracts & Failure Audits

**Papers**

| Paper | Date | Resources | Environment / task contribution | Feedback / evidence | Release boundary |
| --- | --- | --- | --- | --- | --- |
| [Grounded Skill-Following](https://arxiv.org/abs/2610.05161) | 2026-10-04 | [Details](docs/catalog_details.md#grounded-skill-following--paper-skill-contracts) | Defines runtime skill contracts with admissible actions, state transitions and termination conditions to supply verified progress feedback. | RL experiments: Checks admissible actions, contract-state transitions and termination to assign verified progress credit. | Contracts constrain existing tasks; the paper-linked repository was not accessible in this review, so no implementation is counted. |
| [Terminal Task Hardness Audit](https://arxiv.org/abs/2609.26826) | 2026-09-20 | [Details](docs/catalog_details.md#terminal-task-hardness-audit--paper-fake-hardness) | Separates genuinely unsolved tasks from broken oracles, infrastructure failures and verifier bypasses using execution evidence. | Quality / failure study: Studies quality of the scoring signal rather than defining a universal reward. | An adjudicated corpus study does not prove intrinsic task hardness or verifier completeness. |
| [Hack-Verifiable Environments](https://arxiv.org/abs/2605.20744) | 2026-05-20 | [Code](https://github.com/MajoRoth/hack-verifiable-environments) · [Details](docs/catalog_details.md#hack-verifiable-environments--paper-hack-verifiable) | Embeds detectable reward-hacking opportunities in TextArena to measure proxy exploitation deterministically. | Evaluation substrate: Deterministic indicators of planted reward-hacking exploits. | Designed exploits support measurement; coverage does not exhaust real-world reward hacking. |

**Repositories**

| Project | Links | Stars | Tags | Summary |
| --- | --- | --- | --- | --- |
| Hack-Verifiable Environments | [GitHub](https://github.com/MajoRoth/hack-verifiable-environments) · [Details](docs/catalog_details.md#hack-verifiable-environments--project-hack-verifiable) | ★ 10 | game, evaluation | Embeds detectable reward-hacking opportunities in TextArena to measure proxy exploitation deterministically. |

**Blogs**

| Article | Publisher | Date | Summary | Evidence |
| --- | --- | --- | --- | --- |
| [How to Evaluate AI Agents From Tool Calls to Task Completion](https://developer.nvidia.com/blog/how-to-evaluate-ai-agents-from-tool-calls-to-task-completion/) | NVIDIA | 2026-09-21 | Separates step-level process scoring from end-state task completion and links reliability to stateful evaluation design. | [Details](docs/catalog_details.md#how-to-evaluate-ai-agents-from-tool-calls-to-task-completion--blog-nvidia-agent-evaluation) |
| [Rubric Dropout: A Simple Way to Mitigate Reward Hacking in Rubric-as-Reward RL](https://labs.scale.com/blog/rubric-dropout) | Scale Labs | 2026-09-10 | Randomly removes rubric criteria during reward computation to reduce overfitting to a fixed grading proxy. | [Details](docs/catalog_details.md#rubric-dropout-a-simple-way-to-mitigate-reward-hacking-in-rubric-as-reward-rl--blog-rubric-dropout) |
| [Who Grades the Graders? Rethinking Verifier Design for Computer Use Agents](https://labs.scale.com/blog/verifier-design-for-cua) | Scale Labs | 2026-09-02 | Compares brittle programmatic checks with model judges and argues for decomposed, hybrid verification of professional artifacts. | [Details](docs/catalog_details.md#who-grades-the-graders-rethinking-verifier-design-for-computer-use-agents--blog-scale-grader) |
| [Systematic Reward Hacking and Prime Sprints](https://www.primeintellect.ai/blog/reward-hacking) | Prime Intellect | 2026-05-20 | Studies competing visible and hidden rewards in designed backdoor-IFEval environments during RL. | [Details](docs/catalog_details.md#systematic-reward-hacking-and-prime-sprints--blog-reward-hacking) |
| [Measuring and improving coding audit realism with deployment resources](https://alignment.anthropic.com/2026/coding-audit-realism/) | Anthropic | 2026-03-23 | Grounds coding-audit simulations in deployment prompts, tool definitions and repository resources, measuring realism improvements. | [Details](docs/catalog_details.md#measuring-and-improving-coding-audit-realism-with-deployment-resources--blog-anthropic-petri-realism) |
| [Agentic Rubrics: Teaching AI to Verify Code the Way Developers Do](https://labs.scale.com/blog/agentic-rubrics) | Scale Labs | 2026-03-11 | Builds repository-grounded checklists for scoring candidate patches without executing tests. | [Details](docs/catalog_details.md#agentic-rubrics-teaching-ai-to-verify-code-the-way-developers-do--blog-agentic-rubrics) |
| [Why SWE-bench Verified no longer measures frontier coding capabilities](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/) | OpenAI | 2026-02-23 | Audits overly narrow tests, underspecification and contamination, showing why executable tests alone do not ensure valid task grading. | [Details](docs/catalog_details.md#why-swe-bench-verified-no-longer-measures-frontier-coding-capabilities--blog-openai-swe-audit) |
| [Quantifying infrastructure noise in agentic coding evals](https://www.anthropic.com/engineering/infrastructure-noise) | Anthropic | 2026-02-05 | Controlled resource-allocation experiments show that sandbox limits change reliability and what coding evaluations measure. | [Details](docs/catalog_details.md#quantifying-infrastructure-noise-in-agentic-coding-evals--blog-anthropic-infra-noise) |
| [Petri 2.0: New Scenarios, New Model Comparisons, and Improved Eval-Awareness Mitigations](https://alignment.anthropic.com/2026/petri-v2/) | Anthropic | 2026-01-22 | Adds scenarios and realism filtering to reduce implausible tool outputs and cues that reveal the evaluation setting. | [Details](docs/catalog_details.md#petri-20-new-scenarios-new-model-comparisons-and-improved-eval-awareness-mitigations--blog-anthropic-petri-v2) |
| [Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) | Anthropic | 2026-01-09 | Separates tasks, trials, graders and outcomes; discusses clean isolated environments and state-based checks. | [Details](docs/catalog_details.md#demystifying-evals-for-ai-agents--blog-anthropic-evals) |
| [From shortcuts to sabotage: natural emergent misalignment from reward hacking](https://www.anthropic.com/research/emergent-misalignment-reward-hacking) | Anthropic | 2025-11-21 | Studies reward hacking in vulnerable coding RL environments and how the learned behavior generalizes to other tasks. | [Details](docs/catalog_details.md#from-shortcuts-to-sabotage-natural-emergent-misalignment-from-reward-hacking--blog-anthropic-reward-hacking) |
| [Petri: An open-source auditing tool to accelerate AI safety research](https://www.anthropic.com/research/petri-open-source-auditing) | Anthropic | 2025-10-06 | An auditor turns seed scenarios into multi-turn simulated user, tool and environment interactions that a judge analyzes. | [Details](docs/catalog_details.md#petri-an-open-source-auditing-tool-to-accelerate-ai-safety-research--blog-anthropic-petri) |
| [Training a Misaligned Reward Seeker](https://alignment.anthropic.com/2026/reward-seeker/) | Anthropic | Unconfirmed | A deliberately adversarial training study uses vulnerable environments to examine reward exploitation and its detection. | [Details](docs/catalog_details.md#training-a-misaligned-reward-seeker--blog-anthropic-reward-seeker) |

## Surveys & Research Maps

### Environment Scaling & Evolution Surveys

**Papers**

| Paper | Date | Resources | Environment / task contribution | Feedback / evidence | Release boundary |
| --- | --- | --- | --- | --- | --- |
| [Agentic Environment Engineering Survey](https://arxiv.org/abs/2606.12191) | 2026-06-10 | [Details](docs/catalog_details.md#agentic-environment-engineering-survey--paper-aee-survey) | Organizes environment modeling, synthesis, evaluation and agent–environment evolution across domains. | Survey: Conceptual synthesis; no new task reward is specified here. | A survey is a discovery map; cited implementation and experimental claims should be checked at original sources. |
| [Environment Scaling Survey](https://arxiv.org/abs/2511.09586) | 2025-11-12 | [Details](docs/catalog_details.md#environment-scaling-survey--paper-scaling-survey) | Frames interactive experience collection through task generation, execution and feedback, with environment-scaling strategies. | Survey: Conceptual synthesis; no new task reward is specified here. | The current title differs from the initial release; a taxonomy is not independent validation of its cited systems. |

## Maintenance

Edit `data/projects.yaml`, then regenerate and validate. Automated metadata refreshes never renew human review dates. Tests and link checks do not reproduce research results.

```bash
.venv/bin/python scripts/render_readme.py
.venv/bin/python scripts/verify_catalog.py
.venv/bin/python -m unittest discover -s tests
.venv/bin/python scripts/verify_catalog.py --links
```

- [YAML](data/projects.yaml) · [JSON](data/catalog.json) · [BibTeX](references.bib)
- [Verification / 核验报告](reports/verification/2026-10-08.md)
- [Sources / 来源核验](docs/sources_and_verification.md) · [Contributing](CONTRIBUTING.md)
