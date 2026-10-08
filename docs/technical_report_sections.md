# Environment Sections in Technical Reports

[← Catalog](../README.md)

Locations refer to the explicitly named versions. PDF page numbers are one-based viewer pages, checked against PDF text; Kimi K3, DSec and MiMo page layouts were also inspected. These are curated passages, not a claim that every relevant report is covered.

## Kimi K3

[Kimi K3: Open Frontier Intelligence](https://arxiv.org/abs/2607.24653) · **arXiv v2 · 2026-08-07**

The report is not a release of every training environment. AgentENV is a separately linked sandbox implementation.

| Section | Original heading | PDF | Environment content |
| --- | --- | --- | --- |
| [§4.2.1](https://arxiv.org/html/2607.24653v2#S4.SS2.SSS1) | Unified White-Box RL Environment | [pp. 14–15](https://arxiv.org/pdf/2607.24653v2#page=14) | Configurable tools, context and harness modules; training varies configurations. |
| [§4.2.2](https://arxiv.org/html/2607.24653v2#S4.SS2.SSS2) | Knowledge-Graph-Guided Task Synthesis | [pp. 15](https://arxiv.org/pdf/2607.24653v2#page=15) | Build and sample a hierarchical concept DAG to retrieve material and synthesize tasks. |
| [§4.2.3](https://arxiv.org/html/2607.24653v2#S4.SS2.SSS3) | Verifiable Problems in Agentic Environments | [pp. 15–16](https://arxiv.org/pdf/2607.24653v2#page=15) | Search, professional workflows and visual reasoning inside interactive sandboxes. |
| [§4.2.4](https://arxiv.org/html/2607.24653v2#S4.SS2.SSS4) | Kernel Optimization Tasks | [pp. 16](https://arxiv.org/pdf/2607.24653v2#page=16) | Reference correctness plus performance rewards, with reward-hacking detection. |
| [§4.2.5](https://arxiv.org/html/2607.24653v2#S4.SS2.SSS5) | Personal Assistant Tasks | [pp. 16](https://arxiv.org/pdf/2607.24653v2#page=16) | Mock applications share persistent multi-day events; agents construct the initial workspace. |
| [§4.2.6](https://arxiv.org/html/2607.24653v2#S4.SS2.SSS6) | Autonomous Execution Tasks | [pp. 16](https://arxiv.org/pdf/2607.24653v2#page=16) | Initial state, goal, tools and budget; public feedback plus hidden final-state verification. |
| [§4.2.7](https://arxiv.org/html/2607.24653v2#S4.SS2.SSS7) | Web Development Tasks | [pp. 16](https://arxiv.org/pdf/2607.24653v2#page=16) | Containerized tasks across harnesses, evaluated by deterministic checks and model judges. |
| [§5.3.2](https://arxiv.org/html/2607.24653v2#S5.SS3.SSS2) | Sandbox Infrastructure | [pp. 22](https://arxiv.org/pdf/2607.24653v2#page=22) | AgentENV uses microVM checkpoint, pause/resume and fork; the report links its open-source repository. |

[AgentENV sandbox code](https://github.com/kvcache-ai/AgentENV)

## DeepSeek V4

[DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence](https://arxiv.org/abs/2606.19348) · **arXiv v1 · 2026-04-26**

This report describes an earlier command-log recovery design; the later DSec paper describes decoupled rollout execution.

| Section | Original heading | PDF | Environment content |
| --- | --- | --- | --- |
| [§5.2.3](https://arxiv.org/html/2606.19348v1#S5.SS2.SSS3) | Preemptible and Fault-Tolerant Rollout Service | [pp. 34–35](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro/resolve/89d501aed998d33fa4f4702102ec1bb2331e10f6/DeepSeek_V4.pdf#page=34) | Token-level write-ahead logs and KV-cache recovery preserve interrupted generation. |
| [§5.2.5](https://arxiv.org/html/2606.19348v1#S5.SS2.SSS5) | Sandbox Infrastructure for Agentic AI | [pp. 35–36](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro/resolve/89d501aed998d33fa4f4702102ec1bb2331e10f6/DeepSeek_V4.pdf#page=35) | Four DSec backends, layered images and cached command results for resumption. |

## GLM-4.5

[GLM-4.5: Agentic, Reasoning, and Coding (ARC) Foundation Models](https://arxiv.org/abs/2508.06471) · **arXiv v1 · 2025-08-08**

The report discloses methods; it does not establish release of the full training task inventory.

| Section | Original heading | PDF | Environment content |
| --- | --- | --- | --- |
| [§3.3.1](https://arxiv.org/html/2508.06471v1#S3.SS3.SSS1) | Data Collection and Synthesis for Agents | [pp. 10](https://arxiv.org/pdf/2508.06471v1#page=10) | Knowledge-graph search questions and issue/PR-derived software tasks with executable tests. |
| [§3.5](https://arxiv.org/html/2508.06471v1#S3.SS5) | RL Infrastructure | [pp. 12–14](https://arxiv.org/pdf/2508.06471v1#page=12) | Isolated task execution, unified HTTP endpoints and a shared pool for asynchronous rollouts and filtering. |

## DeepSeek Elastic Compute (DSec)

[DeepSeek Elastic Compute (DSec): A Sandbox Infrastructure for Effective Agentic Training at Scale](https://arxiv.org/abs/2609.22978) · **arXiv v1 · 2026-09-19**

A production infrastructure paper; no official public DSec implementation is confirmed. Related projects such as 3FS are not the complete DSec platform.

| Section | Original heading | PDF | Environment content |
| --- | --- | --- | --- |
| [§5.1](https://arxiv.org/html/2609.22978v1#S5.SS1) | Composable Environment Layers | [pp. 14–15](https://arxiv.org/pdf/2609.22978v1#page=14) | Compose reusable read-only layers and writable changes for task environments. |
| [§6.1](https://arxiv.org/html/2609.22978v1#S6.SS1) | Build environments of Agents, by Agents, for Agents | [pp. 17](https://arxiv.org/pdf/2609.22978v1#page=17) | Incremental disk snapshots turn agent construction sessions into reusable, quality-checked environments. |
| [§6.2](https://arxiv.org/html/2609.22978v1#S6.SS2) | Separate agent loop from the RL framework | [pp. 17–18](https://arxiv.org/pdf/2609.22978v1#page=17) | Move the worker and agent sandbox outside preemptible GPU jobs to preserve rollout state. |
| [§6.3](https://arxiv.org/html/2609.22978v1#S6.SS3) | Suspending Sandboxes for Preemptive RL Training | [pp. 18](https://arxiv.org/pdf/2609.22978v1#page=18) | Pause containers or microVMs to reclaim memory, then transparently resume on requests. |

## MiMo-V2.6

[MiMo-V2.6: Scaling Reinforcement Learning Towards Self-Improvement](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL/blob/73875d00b30a89ef8cc353a0b60b0e9f9561952d/MiMo_V2_6_technical_report.pdf) · **HF revision 73875d0 · checked 2026-10-08**

The public task subset is distinct from the full training distribution. PDF pinned to a repository revision; first report publication date unconfirmed.

| Section | Original heading | PDF | Environment content |
| --- | --- | --- | --- |
| [§4.2.1](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL/resolve/73875d00b30a89ef8cc353a0b60b0e9f9561952d/MiMo_V2_6_technical_report.pdf#page=9) | Code Agent Tasks | [pp. 9–11](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL/resolve/73875d00b30a89ef8cc353a0b60b0e9f9561952d/MiMo_V2_6_technical_report.pdf#page=9) | Task synthesis from repositories, specifications and workflows; rollout audits and repeated tests check supervision. |
| [§4.2.2](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL/resolve/73875d00b30a89ef8cc353a0b60b0e9f9561952d/MiMo_V2_6_technical_report.pdf#page=11) | General Agent Tasks | [pp. 11–12](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL/resolve/73875d00b30a89ef8cc353a0b60b0e9f9561952d/MiMo_V2_6_technical_report.pdf#page=11) | Build resettable local workspaces and software mocks, then synthesize tasks and refine verifiable rubrics. |
| [§4.2.3](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL/resolve/73875d00b30a89ef8cc353a0b60b0e9f9561952d/MiMo_V2_6_technical_report.pdf#page=13) | Visual Agent Tasks | [pp. 13](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL/resolve/73875d00b30a89ef8cc353a0b60b0e9f9561952d/MiMo_V2_6_technical_report.pdf#page=13) | Open-ended artifact design and reference replication use distinct visual grading schemes. |
| [§4.2.4](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL/resolve/73875d00b30a89ef8cc353a0b60b0e9f9561952d/MiMo_V2_6_technical_report.pdf#page=13) | Cybersecurity Agent Tasks | [pp. 13–14](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL/resolve/73875d00b30a89ef8cc353a0b60b0e9f9561952d/MiMo_V2_6_technical_report.pdf#page=13) | Controlled vulnerability-reproduction tasks use deterministic checks for the specified defect. |
| [§4.2.5](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL/resolve/73875d00b30a89ef8cc353a0b60b0e9f9561952d/MiMo_V2_6_technical_report.pdf#page=14) | Multi-Harness Training | [pp. 14](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL/resolve/73875d00b30a89ef8cc353a0b60b0e9f9561952d/MiMo_V2_6_technical_report.pdf#page=14) | Recombine minimal prompts, tools and context modules to vary interaction mechanisms. |
| [§4.2.6](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL/resolve/73875d00b30a89ef8cc353a0b60b0e9f9561952d/MiMo_V2_6_technical_report.pdf#page=14) | Reward Hacking Mitigation | [pp. 14–16](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL/resolve/73875d00b30a89ef8cc353a0b60b0e9f9561952d/MiMo_V2_6_technical_report.pdf#page=14) | Clean environment artifacts, adversarially audit prepared tasks, and monitor training trajectories. |
| [§6.1](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL/resolve/73875d00b30a89ef8cc353a0b60b0e9f9561952d/MiMo_V2_6_technical_report.pdf#page=26) | Agentic RL with Fine-grained Learning Signals | [pp. 26–27](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL/resolve/73875d00b30a89ef8cc353a0b60b0e9f9561952d/MiMo_V2_6_technical_report.pdf#page=26) | Agent Loops own setup, interaction, grading and cleanup; trajectory hierarchy separates learning signals from infrastructure failures. |
| [§6.2](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL/resolve/73875d00b30a89ef8cc353a0b60b0e9f9561952d/MiMo_V2_6_technical_report.pdf#page=27) | Harness Pool and Payload Porter: Large-Batch RL with Multiple Harnesses | [pp. 27–29](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL/resolve/73875d00b30a89ef8cc353a0b60b0e9f9561952d/MiMo_V2_6_technical_report.pdf#page=27) | Persistent execution pools separate harness code, agent settings, environment settings and trajectory transport. |
| [§7.2](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL/resolve/73875d00b30a89ef8cc353a0b60b0e9f9561952d/MiMo_V2_6_technical_report.pdf#page=34) | RL with Open Environments | [pp. 34–36](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL/resolve/73875d00b30a89ef8cc353a0b60b0e9f9561952d/MiMo_V2_6_technical_report.pdf#page=34) | Documents released domains, domain-specific GRPO and held-out-harness evaluation; release inventory is in Table 5 on page 33. |
