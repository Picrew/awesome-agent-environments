# 目录详情与证据

[← 主目录](../README_zh.md)

每项资源保留独立开放边界，配套链接不额外算作项目。

## VERA — paper-vera

**[VERA: Scaling Verifiable Environments for Agentic co-Evolution](https://arxiv.org/abs/2610.05923)**

`paper` · `vera` · 2026-10-05 · RL 与 harness 学习

从轨迹构建可恢复沙箱，经检查筛选后交替更新模型权重与 harness 技能。

**反馈／验收：** rubric 奖励、可执行检查和开发集准入门槛。

**开放边界：** 近期预印本；已读摘要和正文未提供可确认的官方仓库。

**实现状态：** 未确认

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2610.05923) · 2026-10-08 · “Competent agents need precise and verifiable environments, such as sandboxes that are resumable at any stage”

## Skill2Env — paper-skill2env

**[Skill2Env: Capability-Oriented Environment Synthesis from Skills for General Agents](https://arxiv.org/abs/2609.33772)**

`paper` · `skill2env` · 2026-09-27 · SFT／轨迹训练

将技能转为能力导向的任务蓝图、可执行工作区和 rubric 评估器，并根据求解轨迹加难。

**反馈／验收：** rubric 评估器及用于任务加难的求解证据。

**开放边界：** 实验展示 SFT。当前研究主页提供示例任务和模型链接；这些样例不能证明完整合成与训练流水线已经开放。

**实现状态：** 部分／关联代码

[主页](https://github.com/AllSpark-Research/AgentEnv) · [部分／关联代码](https://github.com/AllSpark-Research/AgentEnv) · [示例任务](https://github.com/AllSpark-Research/AgentEnv/tree/main/Skill2Env) · [模型](https://huggingface.co/AllSpark-Research/Skill2Env)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2609.33772) · 2026-10-08 · “Executable environments are critical for post-training agents on tasks that require tool use and multi-step interaction,”
- [primary-source-content](https://arxiv.org/html/2609.33772v2) · 2026-10-08 · “Skill2Env”
- [primary-source-content](https://github.com/AllSpark-Research/AgentEnv) · 2026-10-08 · “Research homepage for environment and data synthesis for general agents.”

## AutoGym — paper-autogym

**[AutoGym: Blueprint-First Generation of Verifiable Agent Gyms](https://arxiv.org/abs/2609.22592)**

`paper` · `autogym` · 2026-09-18 · 环境／任务生成

先定义解空间与验证条件，再生成完整 gym，并按模型表现校准生成参数。

**反馈／验收：** 生成的任务验证器及构建或可解性验证。

**开放边界：** 展示生成环境的难度；不能据此推断已发布端到端 RL 系统或持续训练增益。

**实现状态：** 未确认

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2609.22592) · 2026-10-08 · “Training agents with reinforcement learning requires a gym, comprising a task, an executable environment in which”

## EnvHarness — paper-envharness

**[EnvHarness: Awakening Static Worlds for Agent Learning](https://arxiv.org/abs/2608.19880)**

`paper` · `envharness` · 2026-08-20 · RL 与 harness 学习

用可编程的初始化、交互和组合层包装固定环境，在保留原验证器的前提下调整练习。

**反馈／验收：** 原环境验证器及留出任务评测。

**开放边界：** 迁移结果限于所测基准；保留验证器不等于每个新包装层都保持任务语义。

**实现状态：** 代码

[代码](https://github.com/google-research/envharness)

同组资源：[EnvHarness (project)](#envharness--project-envharness)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2608.19880) · 2026-10-08 · “LLM agents learn by interacting with environments, yet these environments are hand-built and static: blind to”

## SPADE — paper-spade

**[SPADE: Self-Play in Adaptive Synthetic Executable Environments](https://arxiv.org/abs/2608.19197)**

`paper` · `spade` · 2026-08-19 · RL 实验

同一策略同时扮演环境设计者与求解者，用提示辅助的 regret 信号选择可执行 reset/step 世界。

**反馈／验收：** 可执行环境奖励及设计者使用的提示辅助 regret 信号。

**开放边界：** 仍依赖语料、记忆和可解性控制；实验不能证明无界改进。

**实现状态：** 代码

[代码](https://github.com/spade-rl/spade)

同组资源：[SPADE (project)](#spade--project-spade)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2608.19197) · 2026-10-08 · “Continuous self-improvement requires an ever-expanding pool of self-generated, diverse, adaptive goals. For language agents, existing training”

## Envs-FORGE — paper-envs-forge

**[Envs-FORGE: Frontier-Optimized Reward-Grounded Environment Synthesis for Agent RL](https://arxiv.org/abs/2608.14312)**

`paper` · `envs-forge` · 2026-08-14 · RL 实验

用验证通过率决定每个种子的合成操作，同步改写任务、数据、测试和 Docker 环境。

**反馈／验收：** 任务成功情况反馈到难度调整；验证细节以具体方法为准。

**开放边界：** 论文链接的是综合工具包；根 README 中未确认完整的论文专属复现入口。

**实现状态：** 部分／关联代码

[部分／关联代码](https://github.com/DataArcTech/DataArc-SynData-Toolkit)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2608.14312) · 2026-10-08 · “Reinforcement learning (RL) for terminal agents needs executable training environments with reliable rewards and useful difficulty.”

## Beyond Simply Environment Scaling — paper-beyond-mm-scaling

**[Beyond Simply Environment Scaling: Designing Effective Environment Distributions for Multimodal Agent Learning](https://arxiv.org/abs/2608.03571)**

`paper` · `beyond-mm-scaling` · 2026-08-04 · RL 实验

通过能力导向选择、交互难度与状态规模的分层课程，研究训练环境分布。

**反馈／验收：** 任务成功情况反馈到难度调整；验证细节以具体方法为准。

**开放边界：** 环境数量不是唯一变量；效果取决于所测多样性与难度设置。

**实现状态：** 代码

[代码](https://github.com/GaryStack/Beyond-MMEnv-Scaling)

同组资源：[Beyond Simply Environment Scaling (project)](#beyond-simply-environment-scaling--project-beyond-mm-scaling)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2608.03571) · 2026-10-08 · “Recent works train agents by constructing large-scale multimodal environment pools. However, we find that simply increasing”

## EvoEnv — paper-evoenv

**[Learning to Build the Environment: Self-Evolving Reasoning RL via Verifiable Environment Synthesis](https://arxiv.org/abs/2605.14392)**

`paper` · `evoenv` · 2026-05-14 · RL 实验

合成可复用的 Python 生成器与验证器，利用求解与验证的难度差维持推理训练信号。

**反馈／验收：** 生成的可执行 oracle 及分阶段准入检查。

**开放边界：** 进行中的技术报告；可验证推理生成器不自动等价于真实的多工具工作环境。

**实现状态：** 未确认

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2605.14392) · 2026-10-08 · “We pursue a vision for self-improving language models in which the model does not merely generate”

## RLVE — paper-rlve

**[RLVE: Scaling Up Reinforcement Learning for Language Models with Adaptive Verifiable Environments](https://arxiv.org/abs/2511.07317)**

`paper` · `rlve` · 2025-11-10 · RL 实验

在人工设计的可验证推理环境集合中，按当前策略能力自适应调整程序化任务难度。

**反馈／验收：** 算法式答案验证及自适应求解率校准。

**开放边界：** 环境工程仍是人工完成；程序化推理结果不宜外推至 GUI 或企业工作流。

**实现状态：** 代码

[代码](https://github.com/Zhiyuan-Zeng/RLVE)

同组资源：[RLVE (project)](#rlve--project-rlve)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2511.07317) · 2026-10-08 · “We introduce Reinforcement Learning (RL) with Adaptive Verifiable Environments (RLVE), an approach using verifiable environments that”

## Environment Tuning — paper-env-tuning

**[Don't Just Fine-tune the Agent, Tune the Environment](https://arxiv.org/abs/2510.10197)**

`paper` · `env-tuning` · 2025-10-11 · RL 实验

结合任务课程、环境纠错反馈和进度奖励，稳定少数据下的工具使用学习。

**反馈／验收：** 任务成功情况反馈到难度调整；验证细节以具体方法为准。

**开放边界：** 增强反馈属于训练条件；部署评测不能假定仍有同样的额外帮助。

**实现状态：** 代码

[代码](https://github.com/inclusionAI/AWorld-RL)

同组资源：[Environment Tuning (project)](#environment-tuning--project-env-tuning)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2510.10197) · 2026-10-08 · “Large Language Model (LLM) agents show great promise for complex, multi-turn tool-use tasks, but their development”

## EnvFactory — paper-envfactory

**[EnvFactory: Scaling Tool-Use Agents via Executable Environments Synthesis and Robust RL](https://arxiv.org/abs/2605.18703)**

`paper` · `envfactory` · 2026-05-18 · RL 与 SFT 实验

从真实资源构建并验证有状态工具，再按工具拓扑与查询校准合成轨迹。

**反馈／验收：** 生成的任务验证器及构建或可解性验证。

**开放边界：** 可执行正确性与自然任务意图需分别检查；发布物依赖特定训练框架。

**实现状态：** 代码

[代码](https://github.com/LARK-AI-Lab/EnvFactory)

同组资源：[EnvFactory (project)](#envfactory--project-envfactory)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2605.18703) · 2026-10-08 · “Equipping LLMs with tool-use capabilities via Agentic Reinforcement Learning (Agentic RL) is bottlenecked by two challenges:”

## Agent-World — paper-agent-world

**[Agent-World: Scaling Real-World Environment Synthesis for Evolving General Agent Intelligence](https://arxiv.org/abs/2604.18292)**

`paper` · `agent-world` · 2026-04-20 · RL 与 SFT 实验

发现有状态工具生态并生成可验证任务，将多环境学习与能力缺口驱动的任务演化连接起来。

**反馈／验收：** 生成的任务验证器及构建或可解性验证。

**开放边界：** 公开仓库仅发布筛选后的环境子集，RL 接入仍需适配，并非论文完整语料。

**实现状态：** 部分／关联代码

[部分／关联代码](https://github.com/RUC-NLPIR/Agent-World)

同组资源：[Agent-World (project)](#agent-world--project-agent-world)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2604.18292) · 2026-10-08 · “Large language models are increasingly expected to serve as general-purpose agents that interact with external, stateful”

## Agent World Model — paper-awm

**[Agent World Model: Infinity Synthetic Environments for Agentic Reinforcement Learning](https://arxiv.org/abs/2602.10090)**

`paper` · `awm` · 2026-02-10 · RL 实验

合成由代码驱动、SQL 数据库支撑的工具世界，提供可检查状态与奖励，用于多轮 RL 和迁移研究。

**反馈／验收：** 利用数据库状态进行任务验证。

**开放边界：** 合成数据库的一致性不代表覆盖所有真实服务行为与生产故障。

**实现状态：** 代码

[代码](https://github.com/Snowflake-Labs/agent-world-model)

同组资源：[Agent World Model: Infinity Synthetic Environments for Agentic Reinforcement Learning (blog)](#agent-world-model-infinity-synthetic-environments-for-agentic-reinforcement-learning--blog-awm-blog) · [Agent World Model (project)](#agent-world-model--project-awm)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2602.10090) · 2026-10-08 · “Recent advances in large language model (LLM) have empowered autonomous agents to perform multi-turn interactions with”

## ScaleEnv — paper-scaleenv

**[ScaleEnv: Scaling Environment Synthesis from Scratch for Generalist Interactive Tool-Use Agent Training](https://arxiv.org/abs/2602.06820)**

`paper` · `scaleenv` · 2026-02-06 · RL 实验

从零构建交互工具环境，通过实现测试和可执行动作序列验证任务可解性。

**反馈／验收：** 生成的任务验证器及构建或可解性验证。

**开放边界：** 与 Scale AI AgentEnv 不同；已读论文及定向搜索未确认官方代码链接。

**实现状态：** 未确认

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2602.06820) · 2026-10-08 · “Training generalist agents capable of adapting to diverse scenarios requires interactive environments for self-exploration. However, interactive”

## EnvScaler — paper-envscaler

**[EnvScaler: Scaling Tool-Interactive Environments for LLM Agent via Programmatic Synthesis](https://arxiv.org/abs/2601.05808)**

`paper` · `envscaler` · 2026-01-09 · RL 与 SFT 实验

将环境骨架构建、场景生成和基于规则的轨迹验证分开。

**反馈／验收：** 基于规则的轨迹及最终状态检查。

**开放边界：** 规则覆盖与环境真实性需独立评估；公开 RL 接入使用 ROLL 与 GEM。

**实现状态：** 代码

[代码](https://github.com/RUC-NLPIR/EnvScaler)

同组资源：[EnvScaler (project)](#envscaler--project-envscaler)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2601.05808) · 2026-10-08 · “Large language models (LLMs) are expected to be trained to act as agents in various real-world”

## AutoForge — paper-autoforge

**[AutoForge: Automated Environment Synthesis for Agentic Reinforcement Learning](https://arxiv.org/abs/2512.22857)**

`paper` · `autoforge` · 2025-12-28 · RL 实验

先组织合成状态结构和工具依赖，再生成用于 agent RL 的工具环境。

**反馈／验收：** 生成的任务验证器及构建或可解性验证。

**开放边界：** 存在多个无关同名仓库；未将未经确认的 AutoForge 项目当作官方代码。

**实现状态：** 未确认

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2512.22857) · 2026-10-08 · “Conducting reinforcement learning (RL) in simulated environments offers a cost-effective and highly scalable way to enhance”

## AutoEnv — paper-autoenv

**[AutoEnv: Automated Environments for Measuring Cross-Environment Agent Learning](https://arxiv.org/abs/2511.19304)**

`paper` · `autoenv` · 2025-11-24 · 环境／任务生成

将转移、观察和奖励分布因子化，生成异构世界以研究跨环境学习。

**反馈／验收：** 生成的任务验证器及构建或可解性验证。

**开放边界：** 生成关卡衡量的是设计分布下的迁移，并非无限制真实世界泛化。

**实现状态：** 代码

[代码](https://github.com/FoundationAgents/AutoEnv)

同组资源：[AutoEnv (project)](#autoenv--project-autoenv)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2511.19304) · 2026-10-08 · “Humans naturally adapt to diverse environments by learning underlying rules across worlds with different dynamics, observations,”

## EnvACE — paper-envace

**[EnvACE: Internalizing Environment Dynamics via World Rehearsal for Agentic Reinforcement Learning](https://arxiv.org/abs/2608.06197)**

`paper` · `envace` · 2026-08-06 · RL 实验

用按角色计算的 RL 信号训练共享策略，让它既执行动作又模拟环境响应，从而内化动态。

**反馈／验收：** 模拟观察或任务成功奖励；真实环境迁移另行评测。

**开放边界：** 预演观察是模型输出；模拟的一致性需要外部执行验证。

**实现状态：** 代码

[代码](https://github.com/Within-yao/EnvACE)

同组资源：[EnvACE (project)](#envace--project-envace)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2608.06197) · 2026-10-08 · “Training large language model agents for long-horizon tool use typically relies on interactions with real or”

## WebWorld — paper-webworld

**[WebWorld: A Large-Scale World Model for Web Agent Training](https://arxiv.org/abs/2602.14721)**

`paper` · `webworld` · 2026-02-16 · SFT／轨迹训练

从交互轨迹学习开放网页模拟器，并用模拟 rollout 训练和规划网页代理。

**反馈／验收：** 模拟观察或任务成功奖励；真实环境迁移另行评测。

**开放边界：** 模拟质量与真实浏览器迁移是不同指标；勿与后续同名网页代码论文混淆。

**实现状态：** 代码

[代码](https://github.com/QwenLM/WebWorld)

同组资源：[WebWorld (project)](#webworld--project-webworld)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2602.14721) · 2026-10-08 · “Web agents require massive trajectories to generalize, yet real-world training is constrained by network latency, rate”

## GenEnv — paper-genenv

**[GenEnv: Difficulty-Aligned Co-Evolution Between LLM Agents and Environment Simulators](https://arxiv.org/abs/2512.19682)**

`paper` · `genenv` · 2025-12-22 · RL 实验

通过难度对齐的课程奖励，共同演化生成式模拟器与代理。

**反馈／验收：** 模拟观察或任务成功奖励；真实环境迁移另行评测。

**开放边界：** 学习式模拟可能偏离可执行现实；结果限于论文所选任务。

**实现状态：** 代码

[代码](https://github.com/Gen-Verse/GenEnv)

同组资源：[GenEnv (project)](#genenv--project-genenv)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2512.19682) · 2026-10-08 · “Training capable Large Language Model (LLM) agents is critically bottlenecked by the high cost and static”

## SynthTools — paper-synthtools

**[SynthTools: A Framework for Scaling Synthetic Tools for Agent Development](https://arxiv.org/abs/2511.09572)**

`paper` · `synthtools` · 2025-11-11 · 环境／任务生成

分离合成工具生成、响应模拟和工具审计，以扩展可控工具生态。

**反馈／验收：** LLM 模拟的工具观察及独立审计阶段。

**开放边界：** 工具响应由 LLM 模拟；审计准确率不等于状态转移的确定性保证。

**实现状态：** 代码

[代码](https://github.com/namkoong-lab/SynthTools)

同组资源：[SynthTools (project)](#synthtools--project-synthtools)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2511.09572) · 2026-10-08 · “For agentic systems to use external tools to solve complex, long-horizon tasks, we need a large”

## DreamGym — paper-dreamgym

**[Scaling Agent Learning via Experience Synthesis](https://arxiv.org/abs/2511.03773)**

`paper` · `dreamgym` · 2025-11-05 · RL 实验

结合推理式经验模型、回放缓冲区与自适应任务生成，通过合成交互训练代理。

**反馈／验收：** 模拟观察或任务成功奖励；真实环境迁移另行评测。

**开放边界：** 从模拟到现实的迁移是经验结果；第三方复现不能当作作者官方代码。

**实现状态：** 未确认

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2511.03773) · 2026-10-08 · “While reinforcement learning (RL) can empower autonomous agents by enabling self-improvement through interaction, its practical adoption”

## daVinci-Env / OpenSWE — paper-openswe

**[daVinci-Env: Open SWE Environment Synthesis at Scale](https://arxiv.org/abs/2603.13023)**

`paper` · `openswe` · 2026-03-13 · SFT／轨迹训练

自动完成仓库探索、Docker 配置和测试生成，再按可解性及有效难度筛选环境。

**反馈／验收：** 任务专属执行测试或验证器评分；具体划分以各项来源为准。

**开放边界：** 论文标题为 daVinci-Env，发布框架名为 OpenSWE；构建和轨迹采样成本较高。

**实现状态：** 代码

[代码](https://github.com/GAIR-NLP/OpenSWE)

同组资源：[daVinci-Env / OpenSWE (project)](#davinci-env--openswe--project-openswe)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2603.13023) · 2026-10-08 · “Training capable software engineering (SWE) agents demands large-scale, executable, and verifiable environments that provide dynamic feedback”

## SWE-rebench V2 — paper-swe-rebench

**[SWE-rebench V2: Language-Agnostic SWE Task Collection at Scale](https://arxiv.org/abs/2602.23866)**

`paper` · `swe-rebench` · 2026-02-27 · 环境／任务生成

采集多语言仓库任务，生成安装与测试流程，构建可复现训练环境。

**反馈／验收：** 任务专属执行测试或验证器评分；具体划分以各项来源为准。

**开放边界：** 完整构建环境与额外任务元数据的发布范围不同；测试可能不足或过度约束。

**实现状态：** 代码

[代码](https://github.com/SWE-rebench/SWE-rebench-V2)

同组资源：[SWE-rebench V2 (project)](#swe-rebench-v2--project-swe-rebench)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2602.23866) · 2026-10-08 · “Software engineering agents (SWE) are improving rapidly, with recent gains largely driven by reinforcement learning (RL).”

## SWE-smith — paper-swe-smith

**[SWE-smith: Scaling Data for Software Engineering Agents](https://arxiv.org/abs/2504.21798)**

`paper` · `swe-smith` · 2025-04-30 · SFT／轨迹训练

将仓库转为执行环境，主动破坏现有测试来生成修复任务。

**反馈／验收：** 任务专属执行测试或验证器评分；具体划分以各项来源为准。

**开放边界：** 变异产生的故障与真实报告的 bug 不同，仍需仓库划分与隐藏测试。

**实现状态：** 代码

[代码](https://github.com/SWE-bench/SWE-smith)

同组资源：[SWE-smith (project)](#swe-smith--project-swe-smith)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2504.21798) · 2026-10-08 · “Despite recent progress in Language Models (LMs) for software engineering, collecting training data remains a significant”

## R2E-Gym — paper-r2e-gym

**[R2E-Gym: Procedural Environments and Hybrid Verifiers for Scaling Open-Weights SWE Agents](https://arxiv.org/abs/2504.07164)**

`paper` · `r2e-gym` · 2025-04-09 · SFT／轨迹训练

从提交程序化整理可执行软件任务，并研究执行验证器与学习式验证器的互补性。

**反馈／验收：** 任务专属执行测试或验证器评分；具体划分以各项来源为准。

**开放边界：** 早期摘要使用 AgentGym 名称，但它与 WooooDyy/AgentGym 是不同项目。

**实现状态：** 代码

[代码](https://github.com/R2E-Gym/R2E-Gym)

同组资源：[R2E-Gym (project)](#r2e-gym--project-r2e-gym)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2504.07164) · 2026-10-08 · “Improving open-source models on real-world SWE tasks (solving GITHUB issues) faces two key challenges: 1) scalable”

## SWE-Gym — paper-swe-gym

**[Training Software Engineering Agents and Verifiers with SWE-Gym](https://arxiv.org/abs/2412.21139)**

`paper` · `swe-gym` · 2024-12-30 · SFT／轨迹训练

将仓库问题与可运行环境、单元测试配对，支持代理微调和验证器训练。

**反馈／验收：** 任务专属执行测试或验证器评分；具体划分以各项来源为准。

**开放边界：** 初始语料以 Python 为中心；环境可运行不意味着广泛语言覆盖。

**实现状态：** 代码

[代码](https://github.com/SWE-Gym/SWE-Gym)

同组资源：[SWE-Gym (project)](#swe-gym--project-swe-gym)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2412.21139) · 2026-10-08 · “We present SWE-Gym, the first environment for training real-world software engineering (SWE) agents. SWE-Gym contains 2,438”

## Terminal-Bench — paper-terminal-bench

**[Terminal-Bench: Benchmarking Agents on Hard, Realistic Tasks in Command Line Interfaces](https://arxiv.org/abs/2601.11868)**

`paper` · `terminal-bench` · 2026-01-17 · 评测环境

将真实终端任务与隔离执行环境、参考解和结果测试打包。

**反馈／验收：** 任务专属执行测试或验证器评分；具体划分以各项来源为准。

**开放边界：** 本论文描述 Terminal-Bench 2.0；评测任务必须与训练数据隔离。

**实现状态：** 代码

[代码](https://github.com/harbor-framework/terminal-bench)

同组资源：[Terminal-Bench (project)](#terminal-bench--project-terminal-bench)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2601.11868) · 2026-10-08 · “AI agents may soon become capable of autonomously completing valuable, long-horizon tasks in diverse domains. Current”

## Gym-Anything / CUA-World — paper-gym-anything

**[Gym-Anything: Turn any Software into an Agent Environment](https://arxiv.org/abs/2604.06126)**

`paper` · `gym-anything` · 2026-04-07 · SFT／轨迹训练

用独立审计代理检查软件安装及真实任务配置，发布跨软件的计算机使用环境语料。

**反馈／验收：** 交互后的状态、产物或 rubric 评估，具体类型依任务而异。

**开放边界：** 虚拟机、应用依赖和 rubric 评判增加成本；配置证据不等于完美的任务验证。

**实现状态：** 代码

[代码](https://github.com/cmu-l3/gym-anything)

同组资源：[Gym-Anything / CUA-World (project)](#gym-anything--cua-world--project-gym-anything)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2604.06126) · 2026-10-08 · “Computer-use agents hold the promise of assisting in a wide range of digital economic activities. However,”

## InfiniteWeb — paper-infiniteweb

**[InfiniteWeb: Scalable Web Environment Synthesis for GUI Agent Training](https://arxiv.org/abs/2601.04126)**

`paper` · `infiniteweb` · 2026-01-07 · RL 实验

生成多页面可交互网站，配套任务中心测试和可验证评估器，用于 GUI 代理 RL。

**反馈／验收：** 交互后的状态、产物或 rubric 评估，具体类型依任务而异。

**开放边界：** 生成网站仍需功能与视觉真实性检查；完整发布物可用性需另行确认。

**实现状态：** 未确认

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2601.04126) · 2026-10-08 · “GUI agents that interact with graphical interfaces on behalf of users represent a promising direction for”

## AgentSynth — paper-agentsynth

**[AgentSynth: Scalable Task Generation for Generalist Computer-Use Agents](https://arxiv.org/abs/2506.14205)**

`paper` · `agentsynth` · 2025-06-17 · 环境／任务生成

将已执行子任务组合成更难的长程计算机任务与轨迹数据集。

**反馈／验收：** 交互后的状态、产物或 rubric 评估，具体类型依任务而异。

**开放边界：** 主要在现有环境上合成任务和轨迹，并非新通用运行时。

**实现状态：** 代码

[代码](https://github.com/sunblaze-ucb/AgentSynth)

同组资源：[AgentSynth (project)](#agentsynth--project-agentsynth)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2506.14205) · 2026-10-08 · “We introduce AgentSynth, a scalable and cost-efficient pipeline for automatically synthesizing high-quality tasks and trajectory datasets”

## BrowserGym — paper-browsergym

**[The BrowserGym Ecosystem for Web Agent Research](https://arxiv.org/abs/2412.05467)**

`paper` · `browsergym` · 2024-12-06 · 评测环境

统一浏览器观察、动作和基准接口，配合 AgentLab 管理实验。

**反馈／验收：** 交互后的状态、产物或 rubric 评估，具体类型依任务而异。

**开放边界：** 统一接口不意味着其中每个基准都可作为训练集。

**实现状态：** 代码

[代码](https://github.com/ServiceNow/BrowserGym)

同组资源：[BrowserGym (project)](#browsergym--project-browsergym)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2412.05467) · 2026-10-08 · “The BrowserGym ecosystem addresses the growing need for efficient evaluation and benchmarking of web agents, particularly”

## AndroidWorld — paper-androidworld

**[AndroidWorld: A Dynamic Benchmarking Environment for Autonomous Agents](https://arxiv.org/abs/2405.14573)**

`paper` · `androidworld` · 2024-05-23 · 评测环境

在 Android 模拟器中提供可参数化任务、初始化和基于状态的成功检查。

**反馈／验收：** 交互后的状态、产物或 rubric 评估，具体类型依任务而异。

**开放边界：** 应用版本与模拟器配置影响复现；基准成功率不是训练效果证据。

**实现状态：** 代码

[代码](https://github.com/google-research/android_world)

同组资源：[AndroidWorld (project)](#androidworld--project-androidworld)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2405.14573) · 2026-10-08 · “Autonomous agents that execute human tasks by controlling computers can enhance human productivity and application accessibility.”

## OSWorld — paper-osworld

**[OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](https://arxiv.org/abs/2404.07972)**

`paper` · `osworld` · 2024-04-11 · 评测环境

提供真实桌面任务初始化与跨应用的执行式评估器。

**反馈／验收：** 交互后的状态、产物或 rubric 评估，具体类型依任务而异。

**开放边界：** GUI 执行昂贵且依赖平台；评测划分不应直接转为 RL 练习数据。

**实现状态：** 代码

[代码](https://github.com/xlang-ai/OSWorld)

同组资源：[OSWorld (project)](#osworld--project-osworld)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2404.07972) · 2026-10-08 · “Autonomous agents that accomplish complex computer tasks with minimal human interventions have the potential to transform”

## WorkArena — paper-workarena

**[WorkArena: How Capable Are Web Agents at Solving Common Knowledge Work Tasks?](https://arxiv.org/abs/2403.07718)**

`paper` · `workarena` · 2024-03-12 · 评测环境

将 ServiceNow 工作流转为浏览器任务，以程序化方式验证企业操作。

**反馈／验收：** 任务状态、轨迹里程碑或 rubric 评估。

**开放边界：** 需要合适的 ServiceNow 实例和凭据，并非完全离线自包含模拟器。

**实现状态：** 代码

[代码](https://github.com/ServiceNow/WorkArena)

同组资源：[WorkArena (project)](#workarena--project-workarena)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2403.07718) · 2026-10-08 · “We study the use of large language model-based agents for interacting with software via web browsers.”

## WebArena — paper-webarena

**[WebArena: A Realistic Web Environment for Building Autonomous Agents](https://arxiv.org/abs/2307.13854)**

`paper` · `webarena` · 2023-07-25 · 评测环境

托管可复现网站并检查任务结果，评测真实多步网页操作。

**反馈／验收：** 交互后的状态、产物或 rubric 评估，具体类型依任务而异。

**开放边界：** 必须维护网站重置及部署镜像，并控制公开测试任务的污染。

**实现状态：** 代码

[代码](https://github.com/web-arena-x/webarena)

同组资源：[WebArena (project)](#webarena--project-webarena)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2307.13854) · 2026-10-08 · “With advances in generative AI, there is now potential for autonomous agents to manage daily tasks”

## MM-ToolSandBox — paper-mm-toolsandbox

**[MM-ToolSandBox: A Unified Framework for Evaluating Visual Tool-Calling Agents](https://arxiv.org/abs/2607.11818)**

`paper` · `mm-toolsandbox` · 2026-07-13 · 评测环境

将有状态工具评测扩展到视觉输入、场景生成和多轮状态变化。

**反馈／验收：** 任务状态、轨迹里程碑或 rubric 评估。

**开放边界：** 这是视觉工具调用基准，不代表已完成 RL 训练；图像信息提取错误需单独分析。

**实现状态：** 代码

[代码](https://github.com/apple-aiml-research/ml-mmtoolsandbox)

同组资源：[MM-ToolSandBox (project)](#mm-toolsandbox--project-mm-toolsandbox)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2607.11818) · 2026-10-08 · “We introduce MM-ToolSandBox, a benchmark and evaluation framework for visually grounded tool-calling agents. The framework provides”

## C-World (formerly ToolGym) — paper-c-world

**[C-World: A Computer Use Agent Environment Creator](https://arxiv.org/abs/2601.06328)**

`paper` · `c-world` · 2026-01-09 · SFT／轨迹训练

生成计算机工具使用环境，包含任务生成、可扰动转移以及真实执行或模拟工具响应。

**反馈／验收：** 任务状态、轨迹里程碑或 rubric 评估。

**开放边界：** 当前论文已改名 C-World，项目页与 README 仍保留 ToolGym 名称；真实 API 与模拟模式需区分，评分使用模型评审。

**实现状态：** 代码

[代码](https://github.com/Ziqiao-git/C-World)

同组资源：[C-World (formerly ToolGym) (project)](#c-world-formerly-toolgym--project-c-world)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2601.06328) · 2026-10-08 · “To close the gap between LLM-based agents and humans in planning and reasoning, agents need large-scale,”

## CodeGym — paper-codegym

**[Generalizable End-to-End Tool-Use RL with Synthetic CodeGym](https://arxiv.org/abs/2509.17325)**

`paper` · `codegym` · 2025-09-22 · RL 实验

从编程问题提取可调用函数，合成可控多轮工具任务并用执行结果评分。

**反馈／验收：** 代码执行结果对照任务参考行为。

**开放边界：** 代码派生工作流提供有用抽象，但不完整覆盖真实企业服务语义。

**实现状态：** 代码

[代码](https://github.com/StigLidu/CodeGym)

同组资源：[CodeGym (project)](#codegym--project-codegym)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2509.17325) · 2026-10-08 · “Tool-augmented large language models (LLMs), hereafter LLM agents, leverage external tools to solve diverse tasks and”

## τ²-bench — paper-tau2

**[$\tau^2$-Bench: Evaluating Conversational Agents in a Dual-Control Environment](https://arxiv.org/abs/2506.07982)**

`paper` · `tau2` · 2025-06-09 · 评测环境

建模助手与模拟用户共同修改的状态，提供组合任务与结果评估。

**反馈／验收：** 共享世界任务结果及规则遵循检查。

**开放边界：** 用户模拟器行为影响结果；基准任务应作为留出评测，而非直接训练数据。

**实现状态：** 代码

[代码](https://github.com/sierra-research/tau2-bench)

同组资源：[τ²-bench (project)](#τ²-bench--project-tau2)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2506.07982) · 2026-10-08 · “Existing benchmarks for conversational AI agents simulate single-control environments, where only the AI agent can use”

## TheAgentCompany — paper-theagentcompany

**[TheAgentCompany: Benchmarking LLM Agents on Consequential Real World Tasks](https://arxiv.org/abs/2412.14161)**

`paper` · `theagentcompany` · 2024-12-18 · 评测环境

构建由网站、文件和模拟同事组成的自包含工作场所，评测长程职业任务。

**反馈／验收：** 任务状态、轨迹里程碑或 rubric 评估。

**开放边界：** 工作场所基准本身不保证新任务的训练评测隔离或可靠 RL 奖励。

**实现状态：** 代码

[代码](https://github.com/TheAgentCompany/TheAgentCompany)

同组资源：[TheAgentCompany (project)](#theagentcompany--project-theagentcompany)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2412.14161) · 2026-10-08 · “We interact with computers on an everyday basis, be it in everyday life or work, and”

## ToolSandbox — paper-toolsandbox

**[ToolSandbox: A Stateful, Conversational, Interactive Evaluation Benchmark for LLM Tool Use Capabilities](https://arxiv.org/abs/2408.04682)**

`paper` · `toolsandbox` · 2024-08-08 · 评测环境

结合有状态工具执行、用户模拟与整段对话轨迹上的里程碑检查。

**反馈／验收：** 轨迹中间里程碑与最终状态。

**开放边界：** 有状态评测基础设施可复用，但论文主要证据是评测，而非策略训练。

**实现状态：** 代码

[代码](https://github.com/apple-aiml-research/ToolSandbox)

同组资源：[ToolSandbox (project)](#toolsandbox--project-toolsandbox)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2408.04682) · 2026-10-08 · “Recent large language models (LLMs) advancements sparked a growing research interest in tool assisted LLMs solving”

## AppWorld — paper-appworld

**[AppWorld: A Controllable World of Apps and People for Benchmarking Interactive Coding Agents](https://arxiv.org/abs/2407.18901)**

`paper` · `appworld` · 2024-07-26 · 评测环境

通过可执行 API 模拟互联个人应用，检查最终状态及非预期副作用。

**反馈／验收：** 基于状态的单元测试，包含副作用检查。

**开放边界：** 训练、开发和测试任务及软件、数据许可各有边界，需遵循官方划分政策。

**实现状态：** 代码

[代码](https://github.com/StonyBrookNLP/appworld)

同组资源：[AppWorld (project)](#appworld--project-appworld)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2407.18901) · 2026-10-08 · “Autonomous agents that address day-to-day digital tasks (e.g., ordering groceries for a household), must not only”

## WebShop — paper-webshop

**[WebShop: Towards Scalable Real-World Web Interaction with Grounded Language Agents](https://arxiv.org/abs/2207.01206)**

`paper` · `webshop` · 2022-07-04 · RL 实验

构建带自然语言目标和商品属性奖励的购物环境，用于交互学习。

**反馈／验收：** 任务状态、轨迹里程碑或 rubric 评估。

**开放边界：** 商品目录与网站行为经过简化；购物成功率衡量的能力范围较窄。

**实现状态：** 代码

[代码](https://github.com/princeton-nlp/WebShop)

同组资源：[WebShop (project)](#webshop--project-webshop)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2207.01206) · 2026-10-08 · “Existing benchmarks for grounding language in interactive environments either lack real-world linguistic elements, or prove difficult”

## GEM — paper-gem

**[GEM: A Gym for Agentic LLMs](https://arxiv.org/abs/2510.01051)**

`paper` · `gem` · 2025-10-01 · RL 实验

提供统一代理环境 API、异步向量化执行和多环境接入 RL 训练器的示例。

**反馈／验收：** 任务奖励与正确性由环境作者或接入库定义。

**开放边界：** 不同训练器的奖励时序与逐轮归因不同；不能忽略语义直接替换适配器。

**实现状态：** 代码

[代码](https://github.com/axon-rl/gem)

同组资源：[GEM (project)](#gem--project-gem)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2510.01051) · 2026-10-08 · “The training paradigm for large language models (LLMs) is moving from static datasets to experience-based learning,”

## Meta ARE — paper-are

**[ARE: Scaling Up Agent Environments and Evaluations](https://arxiv.org/abs/2509.17158)**

`paper` · `are` · 2025-09-21 · 评测环境

将应用、事件与场景分离，模拟动态世界并在异步变化下评测代理。

**反馈／验收：** 任务奖励与正确性由环境作者或接入库定义。

**开放边界：** ARE 与 OpenEnv 不同；Gaia2 结果主要说明评测行为，而非已发布 RL 训练配方。

**实现状态：** 代码

[代码](https://github.com/facebookresearch/meta-agents-research-environments)

同组资源：[Meta ARE (project)](#meta-are--project-are)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2509.17158) · 2026-10-08 · “We introduce Meta Agents Research Environments (ARE), a research platform for scalable creation of environments, integration”

## AgentGym-RL — paper-agentgym-rl

**[AgentGym-RL: Training LLM Agents for Long-Horizon Decision Making through Multi-Turn Reinforcement Learning](https://arxiv.org/abs/2509.08755)**

`paper` · `agentgym-rl` · 2025-09-10 · RL 实验

解耦训练与环境服务，通过逐步扩大交互时长进行多轮 RL。

**反馈／验收：** 任务奖励与正确性由环境作者或接入库定义。

**开放边界：** 需要逐个配置底层环境及其服务，并非无依赖的单体模拟器。

**实现状态：** 代码

[代码](https://github.com/WooooDyy/AgentGym-RL)

同组资源：[AgentGym-RL (project)](#agentgym-rl--project-agentgym-rl)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2509.08755) · 2026-10-08 · “Developing autonomous LLM agents capable of making a series of intelligent decisions to solve complex, real-world”

## AgentGym — paper-agentgym

**[AgentGym: Evolving Large Language Model-based Agents across Diverse Environments](https://arxiv.org/abs/2406.04151)**

`paper` · `agentgym` · 2024-06-06 · SFT／轨迹训练

标准化多类环境服务与轨迹，支持通用代理探索及迭代学习。

**反馈／验收：** 任务奖励与正确性由环境作者或接入库定义。

**开放边界：** 原始 AgentEvol 研究与后续 AgentGym-RL 发布使用不同学习流程。

**实现状态：** 代码

[代码](https://github.com/WooooDyy/AgentGym)

同组资源：[AgentGym (project)](#agentgym--project-agentgym)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2406.04151) · 2026-10-08 · “Building generalist agents that can handle diverse tasks and evolve themselves across different environments is a”

## Reasoning Gym — paper-reasoning-gym

**[REASONING GYM: Reasoning Environments for Reinforcement Learning with Verifiable Rewards](https://arxiv.org/abs/2505.24760)**

`paper` · `reasoning-gym` · 2025-05-30 · RL 实验

以可调难度生成推理任务并配套确定性验证器，替代固定数据集。

**反馈／验收：** 程序化参考答案与任务专属评分函数。

**开放边界：** 许多任务是单轮问题；程序化任务多样性不同于有状态工具交互多样性。

**实现状态：** 代码

[代码](https://github.com/open-thought/reasoning-gym)

同组资源：[Reasoning Gym (project)](#reasoning-gym--project-reasoning-gym)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2505.24760) · 2026-10-08 · “We introduce Reasoning Gym (RG), a library of reasoning environments for reinforcement learning with verifiable rewards.”

## TextArena — paper-textarena

**[TextArena](https://arxiv.org/abs/2504.11442)**

`paper` · `textarena` · 2025-04-15 · 可训练接口

将文字游戏、规则、多玩家交互和奖励接口打包，用于代理训练与评测。

**反馈／验收：** 任务参考答案或游戏规则决定的结果。

**开放边界：** 胜率依赖对手与规则，不能直接衡量工作场景能力。

**实现状态：** 代码

[代码](https://github.com/TextArena/TextArena)

同组资源：[TextArena (project)](#textarena--project-textarena)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2504.11442) · 2026-10-08 · “TextArena is an open-source collection of competitive text-based games for training and evaluation of agentic behavior”

## Aviary — paper-aviary

**[Aviary: training language agents on challenging scientific tasks](https://arxiv.org/abs/2412.21154)**

`paper` · `aviary` · 2024-12-30 · RL 实验

定义带科学工具及奖励的语言代理环境，覆盖文献、分子克隆和蛋白质任务。

**反馈／验收：** 领域目标和科学任务检查。

**开放边界：** 领域工具与外部服务增加依赖；模拟科学任务成功不等于实验室验证。

**实现状态：** 代码

[代码](https://github.com/Future-House/aviary)

同组资源：[Aviary (project)](#aviary--project-aviary)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2412.21154) · 2026-10-08 · “Solving complex real-world tasks requires cycles of actions and observations. This is particularly true in science,”

## ScienceWorld — paper-scienceworld

**[ScienceWorld: Is your Agent Smarter than a 5th Grader?](https://arxiv.org/abs/2203.07540)**

`paper` · `scienceworld` · 2022-03-14 · 评测环境

提供可组合实验及环境目标检查的交互式文字科学世界。

**反馈／验收：** 领域目标和科学任务检查。

**开放边界：** 简化模拟器适合规划研究，但不复现物理实验室的完整动态。

**实现状态：** 代码

[代码](https://github.com/allenai/ScienceWorld)

同组资源：[ScienceWorld (project)](#scienceworld--project-scienceworld)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2203.07540) · 2026-10-08 · “We present ScienceWorld, a benchmark to test agents' scientific reasoning abilities in a new interactive text”

## ALFWorld — paper-alfworld

**[ALFWorld: Aligning Text and Embodied Environments for Interactive Learning](https://arxiv.org/abs/2010.03768)**

`paper` · `alfworld` · 2020-10-08 · 模仿学习

对齐符号化文字交互与具身家务任务；BUTLER 通过 DAgger 模仿学习训练并迁移已学策略。

**反馈／验收：** 领域目标和科学任务检查。

**开放边界：** 文字版与具身版的感知及执行成本不同；此项作为基础脉络收录。

**实现状态：** 代码

[代码](https://github.com/alfworld/alfworld)

同组资源：[ALFWorld (project)](#alfworld--project-alfworld)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2010.03768) · 2026-10-08 · “Given a simple request like Put a washed apple in the kitchen fridge, humans can reason”
- [primary-source-content](https://arxiv.org/html/2010.03768) · 2026-10-08 · “The agent is trained in an imitation learning setting with DAgger”

## Terminal Task Hardness Audit — paper-fake-hardness

**[What Makes a Terminal-Bench Task Hard? Separating Genuine Hardness from Fake-Hardness on an Adjudicated Agentic Corpus](https://arxiv.org/abs/2609.26826)**

`paper` · `fake-hardness` · 2026-09-20 · 质量／失败研究

用执行证据区分真正未解任务、错误参考解、基础设施故障和验证器绕过。

**反馈／验收：** 研究评分信号质量，而非定义通用奖励。

**开放边界：** 经过裁定的语料研究仍不能证明任务的内在难度或验证器完备性。

**实现状态：** 未确认

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2609.26826) · 2026-10-08 · “Frontier benchmarks need tasks that current models cannot solve. But a task that no model solves”

## Hack-Verifiable Environments — paper-hack-verifiable

**[Hack-Verifiable Environments: Towards Evaluating Reward Hacking at Scale](https://arxiv.org/abs/2605.20744)**

`paper` · `hack-verifiable` · 2026-05-20 · 评测环境

在 TextArena 中植入可检测的奖励投机机会，以确定性方式测量代理对评分漏洞的利用。

**反馈／验收：** 对预置奖励漏洞利用行为的确定性检测。

**开放边界：** 人为设计的漏洞支持测量，但不能穷尽真实奖励投机类型。

**实现状态：** 代码

[代码](https://github.com/MajoRoth/hack-verifiable-environments)

同组资源：[Hack-Verifiable Environments (project)](#hack-verifiable-environments--project-hack-verifiable)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2605.20744) · 2026-10-08 · “Aligning autonomous agents with human intent remains a central challenge in modern AI. A key manifestation”

## Agentic Environment Engineering Survey — paper-aee-survey

**[Agentic Environment Engineering for Large Language Models: A Survey of Environment Modeling, Synthesis, Evaluation, and Application](https://arxiv.org/abs/2606.12191)**

`paper` · `aee-survey` · 2026-06-10 · 综述

跨领域组织环境建模、合成、评估及代理环境演化研究。

**反馈／验收：** 概念梳理；不在此定义新的任务奖励。

**开放边界：** 综述用于发现线索；实现和实验结论仍需回到原始来源核验。

**实现状态：** —

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2606.12191) · 2026-10-08 · “Environments serve as interactive systems for large language model (LLM) based agents across diverse scenarios and”

## Environment Scaling Survey — paper-scaling-survey

**[Environment Scaling for Interactive Agentic Experience Collection: A Survey](https://arxiv.org/abs/2511.09586)**

`paper` · `scaling-survey` · 2025-11-12 · 综述

以任务生成、执行、反馈组织交互经验采集，并梳理环境扩展策略。

**反馈／验收：** 概念梳理；不在此定义新的任务奖励。

**开放边界：** 当前标题与早期发布不同；分类体系不是对引用系统的独立验证。

**实现状态：** —

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2511.09586) · 2026-10-08 · “LLM-based agents can autonomously accomplish complex tasks across various domains. However, to further cultivate capabilities such”

## Introducing AgentEnv: An Open-Source Framework for Building RL Environments — blog-scale-agentenv

**[Introducing AgentEnv: An Open-Source Framework for Building RL Environments](https://labs.scale.com/blog/introducing-agentenv)**

`blog` · `scale-agentenv` · 2026-10-05 · 技术报告

介绍可复用环境块、数据工件、世界规则和任务 DAG，以及跨代理和沙箱的执行方式。

**反馈／验收：** 任务奖励与正确性由环境作者或接入库定义。

**开放边界：** 部分任务刻意不含评分；使用框架不等于自动获得可训练奖励。

同组资源：[AgentEnv (Scale) (project)](#agentenv-scale--project-scale-agentenv)

**来源证据**

- [primary-source-content](https://labs.scale.com/blog/introducing-agentenv) · 2026-10-08 · “BACK 10/5/2026 Introducing AgentEnv: An Open-Source Framework for Building RL Environments By Edgar Arakelyan , Tejas”

## The Open Source Community is backing OpenEnv for Agentic RL — blog-openenv-community

**[The Open Source Community is backing OpenEnv for Agentic RL](https://huggingface.co/blog/openenv-agentic-rl)**

`blog` · `openenv` · 2026-06-08 · 技术报告

明确 OpenEnv 是连接环境库、代理 harness 与训练器的互操作层。

**反馈／验收：** 任务奖励与正确性由环境作者或接入库定义。

**开放边界：** 奖励定义和训练算法仍由接入的库负责。

同组资源：[Building the Open Agent Ecosystem Together: Introducing OpenEnv (blog)](#building-the-open-agent-ecosystem-together-introducing-openenv--blog-openenv-launch) · [Scaling OpenEnv: From Free Usage to Thousands of Concurrent Environments (blog)](#scaling-openenv-from-free-usage-to-thousands-of-concurrent-environments--blog-openenv-scaling) · [Training a coding agent using the OpenCode harness in remote HF sandboxes with TRL and OpenEnv (blog)](#training-a-coding-agent-using-the-opencode-harness-in-remote-hf-sandboxes-with-trl-and-openenv--blog-trl-openenv) · [OpenEnv (project)](#openenv--project-openenv) · [The Building Blocks of Agentic AI: From Kernels to Clusters (blog)](#the-building-blocks-of-agentic-ai-from-kernels-to-clusters--blog-meta-openenv)

**来源证据**

- [primary-source-content](https://huggingface.co/blog/openenv-agentic-rl) · 2026-10-08 · “Back to Articles The Open Source Community is backing OpenEnv for Agentic RL Published June 8,”

## Building the Open Agent Ecosystem Together: Introducing OpenEnv — blog-openenv-launch

**[Building the Open Agent Ecosystem Together: Introducing OpenEnv](https://huggingface.co/blog/openenv)**

`blog` · `openenv` · 2025-10-23 · 技术报告

介绍代理交互的环境契约、容器打包及共享中心。

**反馈／验收：** 任务奖励与正确性由环境作者或接入库定义。

**开放边界：** 这是历史发布规范；仓库迁移和 API 变化以现行文档为准。

同组资源：[The Open Source Community is backing OpenEnv for Agentic RL (blog)](#the-open-source-community-is-backing-openenv-for-agentic-rl--blog-openenv-community) · [Scaling OpenEnv: From Free Usage to Thousands of Concurrent Environments (blog)](#scaling-openenv-from-free-usage-to-thousands-of-concurrent-environments--blog-openenv-scaling) · [Training a coding agent using the OpenCode harness in remote HF sandboxes with TRL and OpenEnv (blog)](#training-a-coding-agent-using-the-opencode-harness-in-remote-hf-sandboxes-with-trl-and-openenv--blog-trl-openenv) · [OpenEnv (project)](#openenv--project-openenv) · [The Building Blocks of Agentic AI: From Kernels to Clusters (blog)](#the-building-blocks-of-agentic-ai-from-kernels-to-clusters--blog-meta-openenv)

**来源证据**

- [primary-source-content](https://huggingface.co/blog/openenv) · 2026-10-08 · “Back to Articles Building the Open Agent Ecosystem Together: Introducing OpenEnv Published October 23, 2025 Update”

## verifiers v1: Decomposing Tasksets and Harnesses for Agentic RL & Evaluations — blog-verifiers-v1

**[verifiers v1: Decomposing Tasksets and Harnesses for Agentic RL & Evaluations](https://www.primeintellect.ai/blog/verifiers-v1)**

`blog` · `verifiers` · 2026-07-12 · 技术报告

分离任务集、harness 和运行时，同时保留分支轨迹及训练 token。

**反馈／验收：** 任务奖励与正确性由环境作者或接入库定义。

**开放边界：** 文章宣布的是 0.2.0 中的 v1 预览命名空间，并非语义版本 1.0 发布。

同组资源：[Environments Hub: A Community Hub To Scale RL To Open AGI (blog)](#environments-hub-a-community-hub-to-scale-rl-to-open-agi--blog-environments-hub) · [Multi-Agent Systems in PRIME-RL (blog)](#multi-agent-systems-in-prime-rl--blog-multi-agent-rl) · [Verifiers (project)](#verifiers--project-verifiers)

**来源证据**

- [primary-source-content](https://www.primeintellect.ai/blog/verifiers-v1) · 2026-10-08 · “verifiers v1: Decomposing Tasksets and Harnesses for Agentic RL & Evaluations Today, we are launching verifiers”

## Environments Hub: A Community Hub To Scale RL To Open AGI — blog-environments-hub

**[Environments Hub: A Community Hub To Scale RL To Open AGI](https://www.primeintellect.ai/blog/environments)**

`blog` · `verifiers` · 2025-08-27 · 技术报告

介绍将任务、反馈与训练接入打包为可发布复用的 verifiers 环境。

**反馈／验收：** 任务奖励与正确性由环境作者或接入库定义。

**开放边界：** 进入 Hub 不证明任务质量，也不代表允许训练评测划分。

同组资源：[verifiers v1: Decomposing Tasksets and Harnesses for Agentic RL & Evaluations (blog)](#verifiers-v1-decomposing-tasksets-and-harnesses-for-agentic-rl--evaluations--blog-verifiers-v1) · [Multi-Agent Systems in PRIME-RL (blog)](#multi-agent-systems-in-prime-rl--blog-multi-agent-rl) · [Verifiers (project)](#verifiers--project-verifiers)

**来源证据**

- [primary-source-content](https://www.primeintellect.ai/blog/environments) · 2026-10-08 · “Environments Hub: A Community Hub To Scale RL To Open AGI RL environments are the playgrounds”

## Welcome RL Environments to the hub — blog-hf-env-hub

**[Welcome RL Environments to the hub](https://huggingface.co/blog/rl-environments)**

`blog` · `hf-env-hub` · 2026-09-28 · 技术报告

通过数据集标签和框架兼容元数据，在 Hub 发现与版本化 RL 任务集。

**反馈／验收：** 任务奖励与正确性由环境作者或接入库定义。

**开放边界：** 该发布重点是任务集；标签本身不启动运行时，也不保证跨框架兼容。

**来源证据**

- [primary-source-content](https://huggingface.co/blog/rl-environments) · 2026-10-08 · “Back to Articles Welcome RL Environments to the hub Published September 28, 2026 Update on GitHub”

## Scaling OpenEnv: From Free Usage to Thousands of Concurrent Environments — blog-openenv-scaling

**[Scaling OpenEnv: From Free Usage to Thousands of Concurrent Environments](https://huggingface.co/blog/burtenshaw/openenv-scaling)**

`blog` · `openenv` · 2026-01-20 · 技术报告

比较从 Spaces、Docker 到集群的环境会话并发部署方案。

**反馈／验收：** 任务奖励与正确性由环境作者或接入库定义。

**开放边界：** 吞吐结果依赖工作负载；轻量会话容量不等于 GUI 或 SWE 吞吐保证。

同组资源：[The Open Source Community is backing OpenEnv for Agentic RL (blog)](#the-open-source-community-is-backing-openenv-for-agentic-rl--blog-openenv-community) · [Building the Open Agent Ecosystem Together: Introducing OpenEnv (blog)](#building-the-open-agent-ecosystem-together-introducing-openenv--blog-openenv-launch) · [Training a coding agent using the OpenCode harness in remote HF sandboxes with TRL and OpenEnv (blog)](#training-a-coding-agent-using-the-opencode-harness-in-remote-hf-sandboxes-with-trl-and-openenv--blog-trl-openenv) · [OpenEnv (project)](#openenv--project-openenv) · [The Building Blocks of Agentic AI: From Kernels to Clusters (blog)](#the-building-blocks-of-agentic-ai-from-kernels-to-clusters--blog-meta-openenv)

**来源证据**

- [primary-source-content](https://huggingface.co/blog/burtenshaw/openenv-scaling) · 2026-10-08 · “Back to Articles Scaling OpenEnv: From Free Usage to Thousands of Concurrent Environments Community Article Published”

## How to Train Scientific Agents with Reinforcement Learning — blog-nemo-science

**[How to Train Scientific Agents with Reinforcement Learning](https://developer.nvidia.com/blog/how-to-train-scientific-agents-with-reinforcement-learning/)**

`blog` · `nemo-gym` · 2025-12-15 · 技术报告

以 Aviary 为例介绍模型、资源和代理服务，构建并验证科学任务 rollout。

**反馈／验收：** 任务奖励与正确性由环境作者或接入库定义。

**支撑资料：** 为环境执行、评测、模拟或质量控制提供参考，但本次正文重点没有直接落在规模化环境生产或有效训练数据生产上，放回相应分类作支撑。

**文章研究问题：** 科学任务如何接入 rollout？

**具体内容**

- 模型、资源、agent 服务职责
- 以 Aviary 连接科学任务工具
- 任务执行与结果验证

**开放边界：** 这是特定时期的教程；新版 Gym 已调整环境服务抽象。

同组资源：[NeMo Gym (project)](#nemo-gym--project-nemo-gym) · [Mastering Agentic Techniques: AI Agent Reinforcement Learning (blog)](#mastering-agentic-techniques-ai-agent-reinforcement-learning--blog-nvidia-agent-rl)

**来源证据**

- [primary-source-content](https://developer.nvidia.com/blog/how-to-train-scientific-agents-with-reinforcement-learning/) · 2026-10-08 · “Agentic AI / Generative AI English 中文 How to Train Scientific Agents with Reinforcement Learning Dec”

## Prime Sandboxes: MicroVMs for Agentic RL Training at Scale — blog-prime-sandboxes

**[Prime Sandboxes: MicroVMs for Agentic RL Training at Scale](https://www.primeintellect.ai/blog/sandboxes)**

`blog` · `prime-sandboxes` · 2026-09-23 · 技术报告

介绍基于虚拟机的 rollout 隔离、镜像复用及大规模训练环境并发。

**反馈／验收：** 任务奖励与正确性由环境作者或接入库定义。

**开放边界：** 属于商业托管运行时；容量与成本为厂商报告，本目录未独立测试。

**来源证据**

- [primary-source-content](https://www.primeintellect.ai/blog/sandboxes) · 2026-10-08 · “Prime Sandboxes: MicroVMs for Agentic RL Training at Scale In agentic RL, the sandbox is the”

## Multi-Agent Systems in PRIME-RL — blog-multi-agent-rl

**[Multi-Agent Systems in PRIME-RL](https://www.primeintellect.ai/blog/multi-agent-systems)**

`blog` · `verifiers` · 2026-08-07 · 技术报告

为自博弈、用户模拟与评判增加可编程代理交互、学习角色选择及归因。

**反馈／验收：** 任务奖励与正确性由环境作者或接入库定义。

**开放边界：** 多代理 API 本身不证明每种交互模式都有收益。

同组资源：[verifiers v1: Decomposing Tasksets and Harnesses for Agentic RL & Evaluations (blog)](#verifiers-v1-decomposing-tasksets-and-harnesses-for-agentic-rl--evaluations--blog-verifiers-v1) · [Environments Hub: A Community Hub To Scale RL To Open AGI (blog)](#environments-hub-a-community-hub-to-scale-rl-to-open-agi--blog-environments-hub) · [Verifiers (project)](#verifiers--project-verifiers)

**来源证据**

- [primary-source-content](https://www.primeintellect.ai/blog/multi-agent-systems) · 2026-10-08 · “Multi-Agent Systems in PRIME-RL Today, the Prime Intellect RL stack expands from training individual agents to”

## Training a coding agent using the OpenCode harness in remote HF sandboxes with TRL and OpenEnv — blog-trl-openenv

**[Training a coding agent using the OpenCode harness in remote HF sandboxes with TRL and OpenEnv](https://huggingface.co/blog/sergiopaniego/trl-openenv-harness-training)**

`blog` · `openenv` · 2026-08-05 · 技术报告

展示每个 rollout 独立沙箱、代理捕获精确 token 轨迹，以及基于工作区评分的 AsyncGRPO。

**反馈／验收：** 任务奖励与正确性由环境作者或接入库定义。

**开放边界：** 10 月更新已将示例迁至 Harbor 接入；旧 opencode_env 命令已被替代。

同组资源：[The Open Source Community is backing OpenEnv for Agentic RL (blog)](#the-open-source-community-is-backing-openenv-for-agentic-rl--blog-openenv-community) · [Building the Open Agent Ecosystem Together: Introducing OpenEnv (blog)](#building-the-open-agent-ecosystem-together-introducing-openenv--blog-openenv-launch) · [Scaling OpenEnv: From Free Usage to Thousands of Concurrent Environments (blog)](#scaling-openenv-from-free-usage-to-thousands-of-concurrent-environments--blog-openenv-scaling) · [OpenEnv (project)](#openenv--project-openenv) · [The Building Blocks of Agentic AI: From Kernels to Clusters (blog)](#the-building-blocks-of-agentic-ai-from-kernels-to-clusters--blog-meta-openenv)

**来源证据**

- [primary-source-content](https://huggingface.co/blog/sergiopaniego/trl-openenv-harness-training) · 2026-10-08 · “Back to Articles Training a coding agent using the OpenCode harness in remote HF sandboxes with”

## Scaling Agentic RL: 365,000+ Environments for SWE, Terminal, and Search — blog-prime-scale

**[Scaling Agentic RL: 365,000+ Environments for SWE, Terminal, and Search](https://www.primeintellect.ai/blog/scaling-agentic-rl)**

`blog` · `prime-research-envs` · 2026-07-22 · 技术报告

统一任务集生命周期与沙箱，保留上游评分逻辑，并在 rollout 期间隔离评分材料。

**反馈／验收：** 生成的任务验证器及构建或可解性验证。

**开放边界：** 标题约 36.5 万指 23 个任务集中的任务，不是独立环境家族；评测集仍需留出。

**来源证据**

- [primary-source-content](https://www.primeintellect.ai/blog/scaling-agentic-rl) · 2026-10-08 · “Scaling Agentic RL: 365,000+ Environments for SWE, Terminal, and Search The open research ecosystem has produced”

## General Agent: A Self-Evolving, Synthetic Agent Environment — blog-general-agent

**[General Agent: A Self-Evolving, Synthetic Agent Environment](https://www.primeintellect.ai/blog/general-agent)**

`blog` · `general-agent` · 2026-05-18 · 技术报告

通过合成者与求解者交互，生成数据库工具任务、参考解与校准难度区间。

**反馈／验收：** 生成的任务验证器及构建或可解性验证。

**开放边界：** 本文版本离线生成固定语料；在线联合多代理训练在文章中仍是未来工作。

**来源证据**

- [primary-source-content](https://www.primeintellect.ai/blog/general-agent) · 2026-10-08 · “General Agent: A Self-Evolving, Synthetic Agent Environment Training capable agents requires exposure to diverse tasks and”

## Agent World Model: Infinity Synthetic Environments for Agentic Reinforcement Learning — blog-awm-blog

**[Agent World Model: Infinity Synthetic Environments for Agentic Reinforcement Learning](https://www.snowflake.com/en/blog/engineering/agent-world-model-for-agentic-reinforment-learning/)**

`blog` · `awm` · 2026-02-13 · 技术报告

解释可执行 SQL 世界合成、一致状态转移及工具使用 RL 的奖励构建。

**反馈／验收：** 利用数据库状态进行任务验证。

**开放边界：** 这是 AWM 论文和代码的配套说明，不是实验结果的独立佐证。

同组资源：[Agent World Model (paper)](#agent-world-model--paper-awm) · [Agent World Model (project)](#agent-world-model--project-awm)

**来源证据**

- [primary-source-content](https://www.snowflake.com/en/blog/engineering/agent-world-model-for-agentic-reinforment-learning/) · 2026-10-08 · “Agent World Model (AWM) for Scalable Agentic RL Environments Skip to content Blog / Gen AI”

## CoderForge-Preview — blog-coderforge

**[CoderForge-Preview](https://www.together.ai/blog/coderforge-preview)**

`blog` · `coderforge` · 日期未确认 · 技术报告

介绍基于可执行仓库任务的大规模测试验证代码轨迹及微调。

**反馈／验收：** 任务专属执行测试或验证器评分；具体划分以各项来源为准。

**文章研究问题：** 如何由仓库任务生产训练轨迹？

**具体内容**

- 以可执行仓库任务承载交互
- 用测试验证代码轨迹
- 发布轨迹并用于微调

**开放边界：** 公开发布重点是轨迹；不能把轨迹数量等同于新发布的环境实现数量。

**来源证据**

- [primary-source-content](https://www.together.ai/blog/coderforge-preview) · 2026-10-08 · “We release CoderForge-Preview - the largest open test-verified coding agent dataset. By leveraging it to fine-tune”

## A technical report on Composer 2 — blog-composer2

**[A technical report on Composer 2](https://cursor.com/blog/composer-2-technical-report)**

`blog` · `composer2` · 2026-03-27 · 技术报告

将贴近部署的真实工具会话与异步 RL、大规模沙箱基础设施连接起来。

**反馈／验收：** 任务专属执行测试或验证器评分；具体划分以各项来源为准。

**文章研究问题：** 如何执行贴近部署的训练任务？

**具体内容**

- 真实工具会话中的多步任务
- 沙箱支持并发执行
- 将执行反馈接入异步 RL

**开放边界：** 属于工业界一手报告；内部训练环境集群并未作为开放环境库发布。

**来源证据**

- [primary-source-content](https://cursor.com/blog/composer-2-technical-report) · 2026-10-08 · “Blog / research We posted to the arXiv a technical report on the training of Composer”

## OpenEnv in Practice: Evaluating Tool-Using Agents in Real-World Environments — blog-calendar-gym

**[OpenEnv in Practice: Evaluating Tool-Using Agents in Real-World Environments](https://huggingface.co/blog/openenv-turing)**

`blog` · `openenv-calendar` · 2026-02-12 · 技术报告

用日历任务揭示工具环境中的状态、权限、时间推理和故障恢复要求。

**反馈／验收：** 任务状态、轨迹里程碑或 rubric 评估。

**开放边界：** 所报实验是评测；文章本身并不证明已训练出日历策略。

**来源证据**

- [primary-source-content](https://huggingface.co/blog/openenv-turing) · 2026-10-08 · “Back to Articles OpenEnv in Practice: Evaluating Tool-Using Agents in Real-World Environments Published February 12, 2026”

## Scaling Enterprise Agent Performance with Reinforcement Learning via Verifiable Feedback Loops — blog-scale-enterprise

**[Scaling Enterprise Agent Performance with Reinforcement Learning via Verifiable Feedback Loops](https://labs.scale.com/blog/scaling-enterprise-agent-performance-with-reinforcement-learning-via-verifiable-feedback-loops)**

`blog` · `scale-enterprise` · 2025-11-17 · 技术报告

讨论领域 SQL 与企业推理训练中的环境设计和可验证反馈。

**反馈／验收：** 任务状态、轨迹里程碑或 rubric 评估。

**开放边界：** 属于厂商领域实验；底层私有工作流不是通用公开环境发布。

**来源证据**

- [primary-source-content](https://labs.scale.com/blog/scaling-enterprise-agent-performance-with-reinforcement-learning-via-verifiable-feedback-loops) · 2026-10-08 · “BACK Post-Training Agents Enterprise 11/17/2025 Scaling Enterprise Agent Performance with Reinforcement Learning via Verifiable Feedback Loops”

## Who Grades the Graders? Rethinking Verifier Design for Computer Use Agents — blog-scale-grader

**[Who Grades the Graders? Rethinking Verifier Design for Computer Use Agents](https://labs.scale.com/blog/verifier-design-for-cua)**

`blog` · `scale-grader` · 2026-09-02 · 技术报告

比较脆弱程序检查与模型评判，讨论对专业产物使用分解、混合验证的方法。

**反馈／验收：** 研究评分信号质量，而非定义通用奖励。

**开放边界：** 分析基于选定任务；程序检查和 VLM 评判都不普遍可靠。

**来源证据**

- [primary-source-content](https://labs.scale.com/blog/verifier-design-for-cua) · 2026-10-08 · “BACK Agents 9/2/2026 Who Grades the Graders? Rethinking Verifier Design for Computer Use Agents By Mark”

## Rubric Dropout: A Simple Way to Mitigate Reward Hacking in Rubric-as-Reward RL — blog-rubric-dropout

**[Rubric Dropout: A Simple Way to Mitigate Reward Hacking in Rubric-as-Reward RL](https://labs.scale.com/blog/rubric-dropout)**

`blog` · `rubric-dropout` · 2026-09-10 · 技术报告

在奖励计算时随机移除 rubric 条目，降低对固定评分代理的过拟合。

**反馈／验收：** 研究评分信号质量，而非定义通用奖励。

**开放边界：** 缓解效果仅在特定领域与规模验证；不能让学习式评判器变成客观验证器。

**来源证据**

- [primary-source-content](https://labs.scale.com/blog/rubric-dropout) · 2026-10-08 · “BACK Evaluation and Alignment 9/10/2026 RUBRIC DROPOUT: A SIMPLE WAY TO MITIGATE REWARD HACKING IN RUBRIC-AS-REWARD”

## Agentic Rubrics: Teaching AI to Verify Code the Way Developers Do — blog-agentic-rubrics

**[Agentic Rubrics: Teaching AI to Verify Code the Way Developers Do](https://labs.scale.com/blog/agentic-rubrics)**

`blog` · `agentic-rubrics` · 2026-03-11 · 技术报告

根据仓库生成有上下文依据的检查清单，在不运行测试时评分候选补丁。

**反馈／验收：** 研究评分信号质量，而非定义通用奖励。

**开放边界：** 属于非执行式验证和候选选择；评分不能等同于通过可执行测试。

**来源证据**

- [primary-source-content](https://labs.scale.com/blog/agentic-rubrics) · 2026-10-08 · “BACK Agents Evaluation and Alignment 3/11/2026 Agentic Rubrics: Teaching AI to Verify Code the Way Developers”

## Systematic Reward Hacking and Prime Sprints — blog-reward-hacking

**[Systematic Reward Hacking and Prime Sprints](https://www.primeintellect.ai/blog/reward-hacking)**

`blog` · `prime-hacking` · 2026-05-20 · 技术报告

在构造的 backdoor-IFEval 环境中研究 RL 过程中显式与隐藏奖励的竞争。

**反馈／验收：** 研究评分信号质量，而非定义通用奖励。

**开放边界：** 刻意植入的奖励捷径有助诊断，但不代表所有生产失效模式。

**来源证据**

- [primary-source-content](https://www.primeintellect.ai/blog/reward-hacking) · 2026-10-08 · “Systematic Reward Hacking and Prime Sprints Detecting and mitigating reward hacking is one of the key”

## EnvHarness — project-envharness

**[EnvHarness](https://github.com/google-research/envharness)**

`project` · `envharness` · 日期未确认 · RL 与 harness 学习

用可编程的初始化、交互和组合层包装固定环境，在保留原验证器的前提下调整练习。

**反馈／验收：** 原环境验证器及留出任务评测。

**开放边界：** 迁移结果限于所测基准；保留验证器不等于每个新包装层都保持任务语义。

GitHub: ★ 621 · push 2026-08-21 · `Apache-2.0` · active

[GitHub](https://github.com/google-research/envharness)

同组资源：[EnvHarness (paper)](#envharness--paper-envharness)

**来源证据**

- [primary-source-content](https://github.com/google-research/envharness) · 2026-10-08 · “EnvHarness : Awakening Static Worlds for Agent Learning Check out our paper and webpage for more”

## SPADE — project-spade

**[SPADE](https://github.com/spade-rl/spade)**

`project` · `spade` · 日期未确认 · RL 实验

同一策略同时扮演环境设计者与求解者，用提示辅助的 regret 信号选择可执行 reset/step 世界。

**反馈／验收：** 可执行环境奖励及设计者使用的提示辅助 regret 信号。

**开放边界：** 仍依赖语料、记忆和可解性控制；实验不能证明无界改进。

GitHub: ★ 114 · push 2026-08-26 · `MIT` · active

[GitHub](https://github.com/spade-rl/spade)

同组资源：[SPADE (paper)](#spade--paper-spade)

**来源证据**

- [primary-source-content](https://github.com/spade-rl/spade) · 2026-10-08 · “SPADE ♠ Self-Play in Adaptive Synthetic Executable Environments 🤗 Models & Data | ♠ SPADE on”

## Beyond Simply Environment Scaling — project-beyond-mm-scaling

**[Beyond Simply Environment Scaling](https://github.com/GaryStack/Beyond-MMEnv-Scaling)**

`project` · `beyond-mm-scaling` · 日期未确认 · RL 实验

通过能力导向选择、交互难度与状态规模的分层课程，研究训练环境分布。

**反馈／验收：** 任务成功情况反馈到难度调整；验证细节以具体方法为准。

**开放边界：** 环境数量不是唯一变量；效果取决于所测多样性与难度设置。

GitHub: ★ 15 · push 2026-08-04 · `Apache-2.0` · reference

[GitHub](https://github.com/GaryStack/Beyond-MMEnv-Scaling)

同组资源：[Beyond Simply Environment Scaling (paper)](#beyond-simply-environment-scaling--paper-beyond-mm-scaling)

**来源证据**

- [primary-source-content](https://github.com/GaryStack/Beyond-MMEnv-Scaling) · 2026-10-08 · “Beyond-MMEnv-Scaling Beyond Simply Environment Scaling: Designing Effective Environment Distributions for Multimodal Agent Learning ⚠️ Status: Work”

## RLVE — project-rlve

**[RLVE](https://github.com/Zhiyuan-Zeng/RLVE)**

`project` · `rlve` · 日期未确认 · RL 实验

在人工设计的可验证推理环境集合中，按当前策略能力自适应调整程序化任务难度。

**反馈／验收：** 算法式答案验证及自适应求解率校准。

**开放边界：** 环境工程仍是人工完成；程序化推理结果不宜外推至 GUI 或企业工作流。

GitHub: ★ 235 · push 2026-04-30 · `MIT` · reference

[GitHub](https://github.com/Zhiyuan-Zeng/RLVE)

同组资源：[RLVE (paper)](#rlve--paper-rlve)

**来源证据**

- [primary-source-content](https://github.com/Zhiyuan-Zeng/RLVE) · 2026-10-08 · “RLVE: Scaling Up Reinforcement Learning for Language Models with Adaptive Verifiable Environments Zhiyuan Zeng*, Hamish Ivison*,”

## Environment Tuning — project-env-tuning

**[Environment Tuning](https://github.com/inclusionAI/AWorld-RL)**

`project` · `env-tuning` · 日期未确认 · RL 实验

结合任务课程、环境纠错反馈和进度奖励，稳定少数据下的工具使用学习。

**反馈／验收：** 任务成功情况反馈到难度调整；验证细节以具体方法为准。

**开放边界：** 增强反馈属于训练条件；部署评测不能假定仍有同样的额外帮助。

GitHub: ★ 127 · push 2026-06-18 · `MIT` · reference

[GitHub](https://github.com/inclusionAI/AWorld-RL)

同组资源：[Environment Tuning (paper)](#environment-tuning--paper-env-tuning)

**来源证据**

- [primary-source-content](https://github.com/inclusionAI/AWorld-RL) · 2026-10-08 · “Agentic Learning Powered by AWorld arXiv(HardGen) arXiv(V2P) ｜ arXiv(RAG-R1) ｜ arXiv(FunReason) ｜ arXiv(RODS) ｜ arXiv(EnvTuning) ｜”

## EnvFactory — project-envfactory

**[EnvFactory](https://github.com/LARK-AI-Lab/EnvFactory)**

`project` · `envfactory` · 日期未确认 · RL 与 SFT 实验

从真实资源构建并验证有状态工具，再按工具拓扑与查询校准合成轨迹。

**反馈／验收：** 生成的任务验证器及构建或可解性验证。

**开放边界：** 可执行正确性与自然任务意图需分别检查；发布物依赖特定训练框架。

GitHub: ★ 96 · push 2026-08-28 · `none` · active

[GitHub](https://github.com/LARK-AI-Lab/EnvFactory)

同组资源：[EnvFactory (paper)](#envfactory--paper-envfactory)

**来源证据**

- [primary-source-content](https://github.com/LARK-AI-Lab/EnvFactory) · 2026-10-08 · “EnvFactory EnvFactory: Scaling Tool-Use Agents via Executable Environments Synthesis and Robust RL 📒 Models & Dataset”

## Agent-World — project-agent-world

**[Agent-World](https://github.com/RUC-NLPIR/Agent-World)**

`project` · `agent-world` · 日期未确认 · RL 与 SFT 实验

发现有状态工具生态并生成可验证任务，将多环境学习与能力缺口驱动的任务演化连接起来。

**反馈／验收：** 生成的任务验证器及构建或可解性验证。

**开放边界：** 公开仓库仅发布筛选后的环境子集，RL 接入仍需适配，并非论文完整语料。

GitHub: ★ 7 · push 2026-10-06 · `MIT` · active

[GitHub](https://github.com/RUC-NLPIR/Agent-World)

同组资源：[Agent-World (paper)](#agent-world--paper-agent-world)

**来源证据**

- [primary-source-content](https://github.com/RUC-NLPIR/Agent-World) · 2026-10-08 · “🌐 Agent-World Real Environments. Verifiable Tasks. Evolving Agents. English | 简体中文 A self-evolving training arena that”

## Agent World Model — project-awm

**[Agent World Model](https://github.com/Snowflake-Labs/agent-world-model)**

`project` · `awm` · 日期未确认 · RL 实验

合成由代码驱动、SQL 数据库支撑的工具世界，提供可检查状态与奖励，用于多轮 RL 和迁移研究。

**反馈／验收：** 利用数据库状态进行任务验证。

**开放边界：** 合成数据库的一致性不代表覆盖所有真实服务行为与生产故障。

GitHub: ★ 465 · push 2026-05-28 · `none` · reference

[GitHub](https://github.com/Snowflake-Labs/agent-world-model)

同组资源：[Agent World Model (paper)](#agent-world-model--paper-awm) · [Agent World Model: Infinity Synthetic Environments for Agentic Reinforcement Learning (blog)](#agent-world-model-infinity-synthetic-environments-for-agentic-reinforcement-learning--blog-awm-blog)

**来源证据**

- [primary-source-content](https://github.com/Snowflake-Labs/agent-world-model) · 2026-10-08 · “Agent World Model Infinity Synthetic Environments for Agentic Reinforcement Learning Zhaoyang Wang 1 , Canwen Xu”

## EnvScaler — project-envscaler

**[EnvScaler](https://github.com/RUC-NLPIR/EnvScaler)**

`project` · `envscaler` · 日期未确认 · RL 与 SFT 实验

将环境骨架构建、场景生成和基于规则的轨迹验证分开。

**反馈／验收：** 基于规则的轨迹及最终状态检查。

**开放边界：** 规则覆盖与环境真实性需独立评估；公开 RL 接入使用 ROLL 与 GEM。

GitHub: ★ 199 · push 2026-09-03 · `MIT` · active

[GitHub](https://github.com/RUC-NLPIR/EnvScaler)

同组资源：[EnvScaler (paper)](#envscaler--paper-envscaler)

**来源证据**

- [primary-source-content](https://github.com/RUC-NLPIR/EnvScaler) · 2026-10-08 · “EnvScaler: Scaling Tool-Interactive Environments for LLM Agent via Programmatic Synthesis 中文 | English If you like”

## AutoEnv — project-autoenv

**[AutoEnv](https://github.com/FoundationAgents/AutoEnv)**

`project` · `autoenv` · 日期未确认 · 环境／任务生成

将转移、观察和奖励分布因子化，生成异构世界以研究跨环境学习。

**反馈／验收：** 生成的任务验证器及构建或可解性验证。

**开放边界：** 生成关卡衡量的是设计分布下的迁移，并非无限制真实世界泛化。

GitHub: ★ 68 · push 2026-03-26 · `MIT` · reference

[GitHub](https://github.com/FoundationAgents/AutoEnv)

同组资源：[AutoEnv (paper)](#autoenv--paper-autoenv)

**来源证据**

- [primary-source-content](https://github.com/FoundationAgents/AutoEnv) · 2026-10-08 · “AutoEnv: Automating Environment Generation For Language Model Agents If you encounter any difficulties in usingthe code,”

## EnvACE — project-envace

**[EnvACE](https://github.com/Within-yao/EnvACE)**

`project` · `envace` · 日期未确认 · RL 实验

用按角色计算的 RL 信号训练共享策略，让它既执行动作又模拟环境响应，从而内化动态。

**反馈／验收：** 模拟观察或任务成功奖励；真实环境迁移另行评测。

**开放边界：** 预演观察是模型输出；模拟的一致性需要外部执行验证。

GitHub: ★ 24 · push 2026-09-07 · `Apache-2.0` · active

[GitHub](https://github.com/Within-yao/EnvACE)

同组资源：[EnvACE (paper)](#envace--paper-envace)

**来源证据**

- [primary-source-content](https://github.com/Within-yao/EnvACE) · 2026-10-08 · “EnvACE: Internalizing Environment Dynamics via World Rehearsal for Agentic RL EnvACE is an agentic RL framework”

## WebWorld — project-webworld

**[WebWorld](https://github.com/QwenLM/WebWorld)**

`project` · `webworld` · 日期未确认 · SFT／轨迹训练

从交互轨迹学习开放网页模拟器，并用模拟 rollout 训练和规划网页代理。

**反馈／验收：** 模拟观察或任务成功奖励；真实环境迁移另行评测。

**开放边界：** 模拟质量与真实浏览器迁移是不同指标；勿与后续同名网页代码论文混淆。

GitHub: ★ 61 · push 2026-02-25 · `none` · reference

[GitHub](https://github.com/QwenLM/WebWorld)

同组资源：[WebWorld (paper)](#webworld--paper-webworld)

**来源证据**

- [primary-source-content](https://github.com/QwenLM/WebWorld) · 2026-10-08 · “WebWorld Introduction Web agents require massive trajectories to generalize, yet real-world training is constrained by network”

## GenEnv — project-genenv

**[GenEnv](https://github.com/Gen-Verse/GenEnv)**

`project` · `genenv` · 日期未确认 · RL 实验

通过难度对齐的课程奖励，共同演化生成式模拟器与代理。

**反馈／验收：** 模拟观察或任务成功奖励；真实环境迁移另行评测。

**开放边界：** 学习式模拟可能偏离可执行现实；结果限于论文所选任务。

GitHub: ★ 67 · push 2026-09-25 · `Apache-2.0` · active

[GitHub](https://github.com/Gen-Verse/GenEnv)

同组资源：[GenEnv (paper)](#genenv--paper-genenv)

**来源证据**

- [primary-source-content](https://github.com/Gen-Verse/GenEnv) · 2026-10-08 · “GenEnv: Difficulty-Aligned Co-Evolution Between LLM Agents and Environment Simulators (NeurIPS 2026) 🌟 Introduction GenEnv is a”

## SynthTools — project-synthtools

**[SynthTools](https://github.com/namkoong-lab/SynthTools)**

`project` · `synthtools` · 日期未确认 · 环境／任务生成

分离合成工具生成、响应模拟和工具审计，以扩展可控工具生态。

**反馈／验收：** LLM 模拟的工具观察及独立审计阶段。

**开放边界：** 工具响应由 LLM 模拟；审计准确率不等于状态转移的确定性保证。

GitHub: ★ 9 · push 2026-07-20 · `none` · reference

[GitHub](https://github.com/namkoong-lab/SynthTools)

同组资源：[SynthTools (paper)](#synthtools--paper-synthtools)

**来源证据**

- [primary-source-content](https://github.com/namkoong-lab/SynthTools) · 2026-10-08 · “SynthTools SynthTools is a fully LLM-based pipeline for building, validating, and exercising synthetic tool-use environments at”

## daVinci-Env / OpenSWE — project-openswe

**[daVinci-Env / OpenSWE](https://github.com/GAIR-NLP/OpenSWE)**

`project` · `openswe` · 日期未确认 · SFT／轨迹训练

自动完成仓库探索、Docker 配置和测试生成，再按可解性及有效难度筛选环境。

**反馈／验收：** 任务专属执行测试或验证器评分；具体划分以各项来源为准。

**开放边界：** 论文标题为 daVinci-Env，发布框架名为 OpenSWE；构建和轨迹采样成本较高。

GitHub: ★ 211 · push 2026-03-16 · `NOASSERTION` · reference

[GitHub](https://github.com/GAIR-NLP/OpenSWE)

同组资源：[daVinci-Env / OpenSWE (paper)](#davinci-env--openswe--paper-openswe)

**来源证据**

- [primary-source-content](https://github.com/GAIR-NLP/OpenSWE) · 2026-10-08 · “OpenSWE: Efficient SWE Environment Synthesis at Scale OpenSWE is the largest fully transparent framework for SWE”

## SWE-rebench V2 — project-swe-rebench

**[SWE-rebench V2](https://github.com/SWE-rebench/SWE-rebench-V2)**

`project` · `swe-rebench` · 日期未确认 · 环境／任务生成

采集多语言仓库任务，生成安装与测试流程，构建可复现训练环境。

**反馈／验收：** 任务专属执行测试或验证器评分；具体划分以各项来源为准。

**开放边界：** 完整构建环境与额外任务元数据的发布范围不同；测试可能不足或过度约束。

GitHub: ★ 85 · push 2026-03-12 · `MIT` · reference

[GitHub](https://github.com/SWE-rebench/SWE-rebench-V2)

同组资源：[SWE-rebench V2 (paper)](#swe-rebench-v2--paper-swe-rebench)

**来源证据**

- [primary-source-content](https://github.com/SWE-rebench/SWE-rebench-V2) · 2026-10-08 · “SWE-rebench-v2 builder Tools and prompt templates used to build and evaluate SWE-rebench-v2 tasks for the paper.”

## SWE-smith — project-swe-smith

**[SWE-smith](https://github.com/SWE-bench/SWE-smith)**

`project` · `swe-smith` · 日期未确认 · SFT／轨迹训练

将仓库转为执行环境，主动破坏现有测试来生成修复任务。

**反馈／验收：** 任务专属执行测试或验证器评分；具体划分以各项来源为准。

**开放边界：** 变异产生的故障与真实报告的 bug 不同，仍需仓库划分与隐藏测试。

GitHub: ★ 795 · push 2026-10-05 · `MIT` · active

[GitHub](https://github.com/SWE-bench/SWE-smith)

同组资源：[SWE-smith (paper)](#swe-smith--paper-swe-smith)

**来源证据**

- [primary-source-content](https://github.com/SWE-bench/SWE-smith) · 2026-10-08 · “NeurIPS 2025 Datasets & Benchmarks Track - Spotlight 🔦 SWE-smith is a toolkit for training SWE-agents”

## R2E-Gym — project-r2e-gym

**[R2E-Gym](https://github.com/R2E-Gym/R2E-Gym)**

`project` · `r2e-gym` · 日期未确认 · SFT／轨迹训练

从提交程序化整理可执行软件任务，并研究执行验证器与学习式验证器的互补性。

**反馈／验收：** 任务专属执行测试或验证器评分；具体划分以各项来源为准。

**开放边界：** 早期摘要使用 AgentGym 名称，但它与 WooooDyy/AgentGym 是不同项目。

GitHub: ★ 337 · push 2025-07-13 · `Apache-2.0` · reference

[GitHub](https://github.com/R2E-Gym/R2E-Gym)

同组资源：[R2E-Gym (paper)](#r2e-gym--paper-r2e-gym)

**来源证据**

- [primary-source-content](https://github.com/R2E-Gym/R2E-Gym) · 2026-10-08 · “R2E-Gym: Procedural Environment Generation and Hybrid Verifiers for Scaling Open-Weights SWE Agents Naman Jain *,1 ,”

## SWE-Gym — project-swe-gym

**[SWE-Gym](https://github.com/SWE-Gym/SWE-Gym)**

`project` · `swe-gym` · 日期未确认 · SFT／轨迹训练

将仓库问题与可运行环境、单元测试配对，支持代理微调和验证器训练。

**反馈／验收：** 任务专属执行测试或验证器评分；具体划分以各项来源为准。

**开放边界：** 初始语料以 Python 为中心；环境可运行不意味着广泛语言覆盖。

GitHub: ★ 748 · push 2025-07-29 · `Apache-2.0` · reference

[GitHub](https://github.com/SWE-Gym/SWE-Gym)

同组资源：[SWE-Gym (paper)](#swe-gym--paper-swe-gym)

**来源证据**

- [primary-source-content](https://github.com/SWE-Gym/SWE-Gym) · 2026-10-08 · “Training Software Engineering Agents and Verifiers with SWE-Gym Jiayi Pan *,1 , Xingyao Wang *,2 ,”

## Terminal-Bench — project-terminal-bench

**[Terminal-Bench](https://github.com/harbor-framework/terminal-bench)**

`project` · `terminal-bench` · 日期未确认 · 评测环境

将真实终端任务与隔离执行环境、参考解和结果测试打包。

**反馈／验收：** 任务专属执行测试或验证器评分；具体划分以各项来源为准。

**开放边界：** 本论文描述 Terminal-Bench 2.0；评测任务必须与训练数据隔离。

GitHub: ★ 852 · push 2026-10-07 · `Apache-2.0` · active

[GitHub](https://github.com/harbor-framework/terminal-bench)

同组资源：[Terminal-Bench (paper)](#terminal-bench--paper-terminal-bench)

**来源证据**

- [primary-source-content](https://github.com/harbor-framework/terminal-bench) · 2026-10-08 · “Terminal-Bench Terminal-Bench is a benchmark designed to measure the frontier of agent work with a diverse,”

## Gym-Anything / CUA-World — project-gym-anything

**[Gym-Anything / CUA-World](https://github.com/cmu-l3/gym-anything)**

`project` · `gym-anything` · 日期未确认 · SFT／轨迹训练

用独立审计代理检查软件安装及真实任务配置，发布跨软件的计算机使用环境语料。

**反馈／验收：** 交互后的状态、产物或 rubric 评估，具体类型依任务而异。

**开放边界：** 虚拟机、应用依赖和 rubric 评判增加成本；配置证据不等于完美的任务验证。

GitHub: ★ 292 · push 2026-09-26 · `MIT` · active

[GitHub](https://github.com/cmu-l3/gym-anything)

同组资源：[Gym-Anything / CUA-World (paper)](#gym-anything--cua-world--paper-gym-anything)

**来源证据**

- [primary-source-content](https://github.com/cmu-l3/gym-anything) · 2026-10-08 · “Gym-Anything: Turn Any Software into an Agent Environment Gym-Anything lets you test AI agents on real”

## AgentSynth — project-agentsynth

**[AgentSynth](https://github.com/sunblaze-ucb/AgentSynth)**

`project` · `agentsynth` · 日期未确认 · 环境／任务生成

将已执行子任务组合成更难的长程计算机任务与轨迹数据集。

**反馈／验收：** 交互后的状态、产物或 rubric 评估，具体类型依任务而异。

**开放边界：** 主要在现有环境上合成任务和轨迹，并非新通用运行时。

GitHub: ★ 53 · push 2026-04-17 · `Apache-2.0` · reference

[GitHub](https://github.com/sunblaze-ucb/AgentSynth)

同组资源：[AgentSynth (paper)](#agentsynth--paper-agentsynth)

**来源证据**

- [primary-source-content](https://github.com/sunblaze-ucb/AgentSynth) · 2026-10-08 · “AgentSynth AgentSynth: Scalable Task Generation for Generalist Computer-Use Agents [ICLR 2026] Below are instructions to run”

## BrowserGym — project-browsergym

**[BrowserGym](https://github.com/ServiceNow/BrowserGym)**

`project` · `browsergym` · 日期未确认 · 评测环境

统一浏览器观察、动作和基准接口，配合 AgentLab 管理实验。

**反馈／验收：** 交互后的状态、产物或 rubric 评估，具体类型依任务而异。

**开放边界：** 统一接口不意味着其中每个基准都可作为训练集。

GitHub: ★ 1,390 · push 2026-10-05 · `NOASSERTION` · active

[GitHub](https://github.com/ServiceNow/BrowserGym)

同组资源：[BrowserGym (paper)](#browsergym--paper-browsergym)

**来源证据**

- [primary-source-content](https://github.com/ServiceNow/BrowserGym) · 2026-10-08 · “🛠️ Setup - 🏋 Usage - 💻 Demo - 🌐 Ecosystem - 🚀 AgentLab - 🌟”

## AndroidWorld — project-androidworld

**[AndroidWorld](https://github.com/google-research/android_world)**

`project` · `androidworld` · 日期未确认 · 评测环境

在 Android 模拟器中提供可参数化任务、初始化和基于状态的成功检查。

**反馈／验收：** 交互后的状态、产物或 rubric 评估，具体类型依任务而异。

**开放边界：** 应用版本与模拟器配置影响复现；基准成功率不是训练效果证据。

GitHub: ★ 945 · push 2026-10-05 · `Apache-2.0` · active

[GitHub](https://github.com/google-research/android_world)

同组资源：[AndroidWorld (paper)](#androidworld--paper-androidworld)

**来源证据**

- [primary-source-content](https://github.com/google-research/android_world) · 2026-10-08 · “AndroidWorld Website • Paper • Tasks • Leaderboard AndroidWorld is an environment for building and benchmarking”

## OSWorld — project-osworld

**[OSWorld](https://github.com/xlang-ai/OSWorld)**

`project` · `osworld` · 日期未确认 · 评测环境

提供真实桌面任务初始化与跨应用的执行式评估器。

**反馈／验收：** 交互后的状态、产物或 rubric 评估，具体类型依任务而异。

**开放边界：** GUI 执行昂贵且依赖平台；评测划分不应直接转为 RL 练习数据。

GitHub: ★ 3,179 · push 2026-09-14 · `Apache-2.0` · active

[GitHub](https://github.com/xlang-ai/OSWorld)

同组资源：[OSWorld (paper)](#osworld--paper-osworld)

**来源证据**

- [primary-source-content](https://github.com/xlang-ai/OSWorld) · 2026-10-08 · “Website • Paper • Doc • Data • Data Viewer • Discord • Cache 📢 Updates”

## WorkArena — project-workarena

**[WorkArena](https://github.com/ServiceNow/WorkArena)**

`project` · `workarena` · 日期未确认 · 评测环境

将 ServiceNow 工作流转为浏览器任务，以程序化方式验证企业操作。

**反馈／验收：** 任务状态、轨迹里程碑或 rubric 评估。

**开放边界：** 需要合适的 ServiceNow 实例和凭据，并非完全离线自包含模拟器。

GitHub: ★ 274 · push 2026-09-28 · `NOASSERTION` · active

[GitHub](https://github.com/ServiceNow/WorkArena)

同组资源：[WorkArena (paper)](#workarena--paper-workarena)

**来源证据**

- [primary-source-content](https://github.com/ServiceNow/WorkArena) · 2026-10-08 · “WorkArena: A Benchmark for Evaluating Agents on Knowledge Work Tasks [Benchmark Contents] ♦ [Getting Started] ♦”

## WebArena — project-webarena

**[WebArena](https://github.com/web-arena-x/webarena)**

`project` · `webarena` · 日期未确认 · 评测环境

托管可复现网站并检查任务结果，评测真实多步网页操作。

**反馈／验收：** 交互后的状态、产物或 rubric 评估，具体类型依任务而异。

**开放边界：** 必须维护网站重置及部署镜像，并控制公开测试任务的污染。

GitHub: ★ 1,619 · push 2025-11-26 · `Apache-2.0` · reference

[GitHub](https://github.com/web-arena-x/webarena)

同组资源：[WebArena (paper)](#webarena--paper-webarena)

**来源证据**

- [primary-source-content](https://github.com/web-arena-x/webarena) · 2026-10-08 · “WebArena: A Realistic Web Environment for Building Autonomous Agents WebArena is a standalone, self-hostable web environment”

## MM-ToolSandBox — project-mm-toolsandbox

**[MM-ToolSandBox](https://github.com/apple-aiml-research/ml-mmtoolsandbox)**

`project` · `mm-toolsandbox` · 日期未确认 · 评测环境

将有状态工具评测扩展到视觉输入、场景生成和多轮状态变化。

**反馈／验收：** 任务状态、轨迹里程碑或 rubric 评估。

**开放边界：** 这是视觉工具调用基准，不代表已完成 RL 训练；图像信息提取错误需单独分析。

GitHub: ★ 29 · push 2026-09-11 · `NOASSERTION` · active

[GitHub](https://github.com/apple-aiml-research/ml-mmtoolsandbox)

同组资源：[MM-ToolSandBox (paper)](#mm-toolsandbox--paper-mm-toolsandbox)

**来源证据**

- [primary-source-content](https://github.com/apple/ml-mmtoolsandbox) · 2026-10-08 · “MM-ToolSandbox: A Unified Framework for Evaluating Visual Tool-Calling Agents 📖 Paper We propose MM-ToolSandbox, a benchmark”

## CodeGym — project-codegym

**[CodeGym](https://github.com/StigLidu/CodeGym)**

`project` · `codegym` · 日期未确认 · RL 实验

从编程问题提取可调用函数，合成可控多轮工具任务并用执行结果评分。

**反馈／验收：** 代码执行结果对照任务参考行为。

**开放边界：** 代码派生工作流提供有用抽象，但不完整覆盖真实企业服务语义。

GitHub: ★ 41 · push 2025-10-14 · `NOASSERTION` · reference

[GitHub](https://github.com/StigLidu/CodeGym)

同组资源：[CodeGym (paper)](#codegym--paper-codegym)

**来源证据**

- [primary-source-content](https://github.com/StigLidu/CodeGym) · 2026-10-08 · “Generalizable End-to-End Tool-Use RL with Synthetic CodeGym Weihua Du, Hailei Gong, Zhan Ling, Kang Liu, Lingfeng”

## τ²-bench — project-tau2

**[τ²-bench](https://github.com/sierra-research/tau2-bench)**

`project` · `tau2` · 日期未确认 · 评测环境

建模助手与模拟用户共同修改的状态，提供组合任务与结果评估。

**反馈／验收：** 共享世界任务结果及规则遵循检查。

**开放边界：** 用户模拟器行为影响结果；基准任务应作为留出评测，而非直接训练数据。

GitHub: ★ 2,181 · push 2026-10-07 · `MIT` · active

[GitHub](https://github.com/sierra-research/tau2-bench)

同组资源：[τ²-bench (paper)](#τ²-bench--paper-tau2)

**来源证据**

- [primary-source-content](https://github.com/sierra-research/tau2-bench) · 2026-10-08 · “$\tau$ -Bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains 🚀 τ³-bench is here! From text-only”

## TheAgentCompany — project-theagentcompany

**[TheAgentCompany](https://github.com/TheAgentCompany/TheAgentCompany)**

`project` · `theagentcompany` · 日期未确认 · 评测环境

构建由网站、文件和模拟同事组成的自包含工作场所，评测长程职业任务。

**反馈／验收：** 任务状态、轨迹里程碑或 rubric 评估。

**开放边界：** 工作场所基准本身不保证新任务的训练评测隔离或可靠 RL 奖励。

GitHub: ★ 792 · push 2025-11-17 · `MIT` · reference

[GitHub](https://github.com/TheAgentCompany/TheAgentCompany)

同组资源：[TheAgentCompany (paper)](#theagentcompany--paper-theagentcompany)

**来源证据**

- [primary-source-content](https://github.com/TheAgentCompany/TheAgentCompany) · 2026-10-08 · “The Agent Company: Benchmarking LLM Agents on Consequential Real World Tasks Website • Paper • Leaderboard”

## ToolSandbox — project-toolsandbox

**[ToolSandbox](https://github.com/apple-aiml-research/ToolSandbox)**

`project` · `toolsandbox` · 日期未确认 · 评测环境

结合有状态工具执行、用户模拟与整段对话轨迹上的里程碑检查。

**反馈／验收：** 轨迹中间里程碑与最终状态。

**开放边界：** 有状态评测基础设施可复用，但论文主要证据是评测，而非策略训练。

GitHub: ★ 287 · push 2026-09-11 · `NOASSERTION` · active

[GitHub](https://github.com/apple-aiml-research/ToolSandbox)

同组资源：[ToolSandbox (paper)](#toolsandbox--paper-toolsandbox)

**来源证据**

- [primary-source-content](https://github.com/apple/ToolSandbox) · 2026-10-08 · “ToolSandbox: A Stateful, Conversational, Interactive Evaluation Benchmark for LLM Tool Use Capabilities This software project accompanies”

## AppWorld — project-appworld

**[AppWorld](https://github.com/StonyBrookNLP/appworld)**

`project` · `appworld` · 日期未确认 · 评测环境

通过可执行 API 模拟互联个人应用，检查最终状态及非预期副作用。

**反馈／验收：** 基于状态的单元测试，包含副作用检查。

**开放边界：** 训练、开发和测试任务及软件、数据许可各有边界，需遵循官方划分政策。

GitHub: ★ 529 · push 2026-09-04 · `Apache-2.0` · active

[GitHub](https://github.com/StonyBrookNLP/appworld)

同组资源：[AppWorld (paper)](#appworld--paper-appworld)

**来源证据**

- [primary-source-content](https://github.com/stonybrooknlp/appworld) · 2026-10-08 · “A Controllable World of Apps and People for Benchmarking Function Calling & Interactive Coding Agents 🏆”

## WebShop — project-webshop

**[WebShop](https://github.com/princeton-nlp/WebShop)**

`project` · `webshop` · 日期未确认 · RL 实验

构建带自然语言目标和商品属性奖励的购物环境，用于交互学习。

**反馈／验收：** 任务状态、轨迹里程碑或 rubric 评估。

**开放边界：** 商品目录与网站行为经过简化；购物成功率衡量的能力范围较窄。

GitHub: ★ 602 · push 2024-09-06 · `MIT` · reference

[GitHub](https://github.com/princeton-nlp/WebShop)

同组资源：[WebShop (paper)](#webshop--paper-webshop)

**来源证据**

- [primary-source-content](https://github.com/princeton-nlp/WebShop) · 2026-10-08 · “🛒 WebShop Implementation of the WebShop environment and search agents for the paper: WebShop: Towards Scalable”

## GEM — project-gem

**[GEM](https://github.com/axon-rl/gem)**

`project` · `gem` · 日期未确认 · RL 实验

提供统一代理环境 API、异步向量化执行和多环境接入 RL 训练器的示例。

**反馈／验收：** 任务奖励与正确性由环境作者或接入库定义。

**开放边界：** 不同训练器的奖励时序与逐轮归因不同；不能忽略语义直接替换适配器。

GitHub: ★ 510 · push 2026-01-21 · `Apache-2.0` · reference

[GitHub](https://github.com/axon-rl/gem)

同组资源：[GEM (paper)](#gem--paper-gem)

**来源证据**

- [primary-source-content](https://github.com/axon-rl/gem) · 2026-10-08 · “🌍 GEM: A Gym for Agentic LLMs Overview We’re entering the era of experience , where”

## Meta ARE — project-are

**[Meta ARE](https://github.com/facebookresearch/meta-agents-research-environments)**

`project` · `are` · 日期未确认 · 评测环境

将应用、事件与场景分离，模拟动态世界并在异步变化下评测代理。

**反馈／验收：** 任务奖励与正确性由环境作者或接入库定义。

**开放边界：** ARE 与 OpenEnv 不同；Gaia2 结果主要说明评测行为，而非已发布 RL 训练配方。

GitHub: ★ 561 · push 2026-09-30 · `MIT` · active

[GitHub](https://github.com/facebookresearch/meta-agents-research-environments)

同组资源：[Meta ARE (paper)](#meta-are--paper-are)

**来源证据**

- [primary-source-content](https://github.com/facebookresearch/meta-agents-research-environments) · 2026-10-08 · “Meta Agents Research Environments (ARE) A research environment for simulating complex, real-life tasks that require multi-step”

## AgentGym-RL — project-agentgym-rl

**[AgentGym-RL](https://github.com/WooooDyy/AgentGym-RL)**

`project` · `agentgym-rl` · 日期未确认 · RL 实验

解耦训练与环境服务，通过逐步扩大交互时长进行多轮 RL。

**反馈／验收：** 任务奖励与正确性由环境作者或接入库定义。

**开放边界：** 需要逐个配置底层环境及其服务，并非无依赖的单体模拟器。

GitHub: ★ 874 · push 2026-02-15 · `MIT` · reference

[GitHub](https://github.com/WooooDyy/AgentGym-RL)

同组资源：[AgentGym-RL (paper)](#agentgym-rl--paper-agentgym-rl)

**来源证据**

- [primary-source-content](https://github.com/WooooDyy/AgentGym-RL) · 2026-10-08 · “AgentGym-RL: Training LLM Agents for Long-Horizon Decision Making through Multi-Turn Reinforcement Learning 📃 Paper • 🌐”

## AgentGym — project-agentgym

**[AgentGym](https://github.com/WooooDyy/AgentGym)**

`project` · `agentgym` · 日期未确认 · SFT／轨迹训练

标准化多类环境服务与轨迹，支持通用代理探索及迭代学习。

**反馈／验收：** 任务奖励与正确性由环境作者或接入库定义。

**开放边界：** 原始 AgentEvol 研究与后续 AgentGym-RL 发布使用不同学习流程。

GitHub: ★ 850 · push 2026-05-30 · `MIT` · reference

[GitHub](https://github.com/WooooDyy/AgentGym)

同组资源：[AgentGym (paper)](#agentgym--paper-agentgym)

**来源证据**

- [primary-source-content](https://github.com/WooooDyy/AgentGym) · 2026-10-08 · “AgentGym: Evolving Large Language Model-based Agents across Diverse Environments 📃 Paper • 🌐 Project Page •”

## Reasoning Gym — project-reasoning-gym

**[Reasoning Gym](https://github.com/open-thought/reasoning-gym)**

`project` · `reasoning-gym` · 日期未确认 · RL 实验

以可调难度生成推理任务并配套确定性验证器，替代固定数据集。

**反馈／验收：** 程序化参考答案与任务专属评分函数。

**开放边界：** 许多任务是单轮问题；程序化任务多样性不同于有状态工具交互多样性。

GitHub: ★ 1,522 · push 2026-04-17 · `Apache-2.0` · reference

[GitHub](https://github.com/open-thought/reasoning-gym)

同组资源：[Reasoning Gym (paper)](#reasoning-gym--paper-reasoning-gym)

**来源证据**

- [primary-source-content](https://github.com/open-thought/reasoning-gym) · 2026-10-08 · “Reasoning Gym 🧠 About Reasoning Gym is a community-created Python library of procedural dataset generators and”

## TextArena — project-textarena

**[TextArena](https://github.com/TextArena/TextArena)**

`project` · `textarena` · 日期未确认 · 可训练接口

将文字游戏、规则、多玩家交互和奖励接口打包，用于代理训练与评测。

**反馈／验收：** 任务参考答案或游戏规则决定的结果。

**开放边界：** 胜率依赖对手与规则，不能直接衡量工作场景能力。

GitHub: ★ 430 · push 2026-10-05 · `MIT` · active

[GitHub](https://github.com/TextArena/TextArena)

同组资源：[TextArena (paper)](#textarena--paper-textarena)

**来源证据**

- [primary-source-content](https://github.com/TextArena/TextArena) · 2026-10-08 · “A suite of 100+ single-, two-, and multi-player text-based games for benchmarking and training LLMs. Play”

## Aviary — project-aviary

**[Aviary](https://github.com/Future-House/aviary)**

`project` · `aviary` · 日期未确认 · RL 实验

定义带科学工具及奖励的语言代理环境，覆盖文献、分子克隆和蛋白质任务。

**反馈／验收：** 领域目标和科学任务检查。

**开放边界：** 领域工具与外部服务增加依赖；模拟科学任务成功不等于实验室验证。

GitHub: ★ 284 · push 2026-10-06 · `Apache-2.0` · active

[GitHub](https://github.com/Future-House/aviary)

同组资源：[Aviary (paper)](#aviary--paper-aviary)

**来源证据**

- [primary-source-content](https://github.com/Future-House/aviary) · 2026-10-08 · “Aviary Aviary 1 is a gymnasium for defining custom language agent RL environments. The library features”

## ScienceWorld — project-scienceworld

**[ScienceWorld](https://github.com/allenai/ScienceWorld)**

`project` · `scienceworld` · 日期未确认 · 评测环境

提供可组合实验及环境目标检查的交互式文字科学世界。

**反馈／验收：** 领域目标和科学任务检查。

**开放边界：** 简化模拟器适合规划研究，但不复现物理实验室的完整动态。

GitHub: ★ 395 · push 2026-08-20 · `Apache-2.0` · active

[GitHub](https://github.com/allenai/ScienceWorld)

同组资源：[ScienceWorld (paper)](#scienceworld--paper-scienceworld)

**来源证据**

- [primary-source-content](https://github.com/allenai/ScienceWorld) · 2026-10-08 · “ScienceWorld ScienceWorld is a text-based virtual environment centered around accomplishing tasks from the standardized elementary science”

## ALFWorld — project-alfworld

**[ALFWorld](https://github.com/alfworld/alfworld)**

`project` · `alfworld` · 日期未确认 · 模仿学习

对齐符号化文字交互与具身家务任务；BUTLER 通过 DAgger 模仿学习训练并迁移已学策略。

**反馈／验收：** 领域目标和科学任务检查。

**开放边界：** 文字版与具身版的感知及执行成本不同；此项作为基础脉络收录。

GitHub: ★ 881 · push 2026-02-08 · `MIT` · reference

[GitHub](https://github.com/alfworld/alfworld)

同组资源：[ALFWorld (paper)](#alfworld--paper-alfworld)

**来源证据**

- [primary-source-content](https://github.com/alfworld/alfworld) · 2026-10-08 · “ALFWorld Aligning Text and Embodied Environments for Interactive Learning Mohit Shridhar , Xingdi (Eric) Yuan ,”

## Hack-Verifiable Environments — project-hack-verifiable

**[Hack-Verifiable Environments](https://github.com/MajoRoth/hack-verifiable-environments)**

`project` · `hack-verifiable` · 日期未确认 · 评测环境

在 TextArena 中植入可检测的奖励投机机会，以确定性方式测量代理对评分漏洞的利用。

**反馈／验收：** 对预置奖励漏洞利用行为的确定性检测。

**开放边界：** 人为设计的漏洞支持测量，但不能穷尽真实奖励投机类型。

GitHub: ★ 10 · push 2026-09-21 · `MIT` · active

[GitHub](https://github.com/MajoRoth/hack-verifiable-environments)

同组资源：[Hack-Verifiable Environments (paper)](#hack-verifiable-environments--paper-hack-verifiable)

**来源证据**

- [primary-source-content](https://github.com/MajoRoth/hack-verifiable-environments) · 2026-10-08 · “Hack-Verifiable Environments: Towards Evaluating Reward Hacking at Scale Introduction Hack-Verifiable Environments is a new paradigm for”

## AgentEnv (Scale) — project-scale-agentenv

**[AgentEnv (Scale)](https://github.com/scaleapi/agentenv-framework)**

`project` · `scale-agentenv` · 日期未确认 · 环境基础设施

提供版本化环境镜像、可组合任务执行、插件与代理评分的 SDK 和 CLI。

**反馈／验收：** 任务奖励与正确性由环境作者或接入库定义。

**开放边界：** 任务作者仍需提供领域状态与奖励逻辑；其他 agentenv 包并非此框架。

GitHub: ★ 165 · push 2026-10-07 · `Apache-2.0` · active

[GitHub](https://github.com/scaleapi/agentenv-framework)

同组资源：[Introducing AgentEnv: An Open-Source Framework for Building RL Environments (blog)](#introducing-agentenv-an-open-source-framework-for-building-rl-environments--blog-scale-agentenv)

**来源证据**

- [primary-source-content](https://github.com/scaleapi/agentenv-framework) · 2026-10-08 · “AgentEnv Framework is a Python SDK and CLI for building, deploying and running agentic environments and”

## OpenEnv — project-openenv

**[OpenEnv](https://github.com/huggingface/OpenEnv)**

`project` · `openenv` · 日期未确认 · 环境基础设施

通过 Gym 风格 API 和远程服务统一隔离环境的部署与交互。

**反馈／验收：** 任务奖励与正确性由环境作者或接入库定义。

**开放边界：** 协议兼容不保证奖励质量；需要固定 API 与环境版本。

GitHub: ★ 2,674 · push 2026-10-07 · `BSD-3-Clause` · active

[GitHub](https://github.com/huggingface/OpenEnv)

同组资源：[The Open Source Community is backing OpenEnv for Agentic RL (blog)](#the-open-source-community-is-backing-openenv-for-agentic-rl--blog-openenv-community) · [Building the Open Agent Ecosystem Together: Introducing OpenEnv (blog)](#building-the-open-agent-ecosystem-together-introducing-openenv--blog-openenv-launch) · [Scaling OpenEnv: From Free Usage to Thousands of Concurrent Environments (blog)](#scaling-openenv-from-free-usage-to-thousands-of-concurrent-environments--blog-openenv-scaling) · [Training a coding agent using the OpenCode harness in remote HF sandboxes with TRL and OpenEnv (blog)](#training-a-coding-agent-using-the-opencode-harness-in-remote-hf-sandboxes-with-trl-and-openenv--blog-trl-openenv) · [The Building Blocks of Agentic AI: From Kernels to Clusters (blog)](#the-building-blocks-of-agentic-ai-from-kernels-to-clusters--blog-meta-openenv)

**来源证据**

- [primary-source-content](https://github.com/huggingface/OpenEnv) · 2026-10-08 · “OpenEnv: Agentic Execution Environments An e2e framework for creating, deploying and using isolated execution environments for”

## NeMo Gym — project-nemo-gym

**[NeMo Gym](https://github.com/NVIDIA-NeMo/Gym)**

`project` · `nemo-gym` · 日期未确认 · 环境基础设施

为代理后训练提供环境服务、验证器、沙箱适配和可扩展 rollout 采集。

**反馈／验收：** 任务奖励与正确性由环境作者或接入库定义。

**开放边界：** Gym 提供交互与奖励，策略优化由 RL 训练器处理；0.7.0 调整了服务 API。

GitHub: ★ 1,225 · push 2026-10-07 · `Apache-2.0` · active

[GitHub](https://github.com/NVIDIA-NeMo/Gym)

同组资源：[How to Train Scientific Agents with Reinforcement Learning (blog)](#how-to-train-scientific-agents-with-reinforcement-learning--blog-nemo-science) · [Mastering Agentic Techniques: AI Agent Reinforcement Learning (blog)](#mastering-agentic-techniques-ai-agent-reinforcement-learning--blog-nvidia-agent-rl)

**来源证据**

- [primary-source-content](https://github.com/NVIDIA-NeMo/Gym) · 2026-10-08 · “NeMo Gym Requirements • Quick Start • Environment Tutorials • Available Environments • Documentation & Resources”

## Verifiers — project-verifiers

**[Verifiers](https://github.com/PrimeIntellect-ai/verifiers)**

`project` · `verifiers` · 日期未确认 · 环境基础设施

用可组合任务集、harness、rubric 和运行时构建训练及评测环境。

**反馈／验收：** 任务奖励与正确性由环境作者或接入库定义。

**开放边界：** 旧版单轮接口与当前 v1 抽象不同；示例需与选用版本对齐。

GitHub: ★ 4,679 · push 2026-10-07 · `MIT` · active

[GitHub](https://github.com/PrimeIntellect-ai/verifiers)

同组资源：[verifiers v1: Decomposing Tasksets and Harnesses for Agentic RL & Evaluations (blog)](#verifiers-v1-decomposing-tasksets-and-harnesses-for-agentic-rl--evaluations--blog-verifiers-v1) · [Environments Hub: A Community Hub To Scale RL To Open AGI (blog)](#environments-hub-a-community-hub-to-scale-rl-to-open-agi--blog-environments-hub) · [Multi-Agent Systems in PRIME-RL (blog)](#multi-agent-systems-in-prime-rl--blog-multi-agent-rl)

**来源证据**

- [primary-source-content](https://github.com/PrimeIntellect-ai/verifiers) · 2026-10-08 · “Overview verifiers is our library for creating environments to train and evaluate LLMs. verifiers is tightly”

## Harbor — project-harbor

**[Harbor](https://github.com/harbor-framework/harbor)**

`project` · `harbor` · 日期未确认 · 环境基础设施

跨代理与沙箱提供方运行容器化任务，支持并行评测和 RL rollout 生成。

**反馈／验收：** 任务奖励与正确性由环境作者或接入库定义。

**开放边界：** Harbor 是执行框架；评分语义和划分限制属于各任务集。

GitHub: ★ 5,891 · push 2026-10-07 · `Apache-2.0` · active

[GitHub](https://github.com/harbor-framework/harbor)

**来源证据**

- [primary-source-content](https://github.com/harbor-framework/harbor) · 2026-10-08 · “Harbor Harbor is a framework from the creators of Terminal-Bench for evaluating and optimizing agents and”

## C-World (formerly ToolGym) — project-c-world

**[C-World: A Computer Use Agent Environment Creator](https://github.com/Ziqiao-git/C-World)**

`project` · `c-world` · 日期未确认 · SFT／轨迹训练

生成计算机工具使用环境，包含任务生成、可扰动转移以及真实执行或模拟工具响应。

**反馈／验收：** 任务状态、轨迹里程碑或 rubric 评估。

**开放边界：** 当前论文已改名 C-World，项目页与 README 仍保留 ToolGym 名称；真实 API 与模拟模式需区分，评分使用模型评审。

GitHub: ★ 10 · push 2026-01-20 · `none` · reference

[GitHub](https://github.com/Ziqiao-git/C-World)

同组资源：[C-World (formerly ToolGym) (paper)](#c-world-formerly-toolgym--paper-c-world)

**来源证据**

- [primary-source-content](https://github.com/Ziqiao-git/ToolGym) · 2026-10-08 · “ToolGym is a large-scale, open-world benchmark for evaluating LLM agents”

## MiMo-V2.6 RL OSS Environments (XiaomiMiMo/verl) — project-xiaomi-mimo-verl

**[MiMo-V2.6 RL OSS Environments (XiaomiMiMo/verl)](https://github.com/XiaomiMiMo/verl)**

`project` · `xiaomi-mimo-rl-oss` · 日期未确认 · 环境基础设施

在 verl 分支发布五类 RL 环境配方，关联任务数据、Docker 镜像和验证器。

**反馈／验收：** 各领域分别采用执行测试、规则、rubric 或视觉评分。

**开放边界：** mimo-oss 分支需要逐领域配置和子模块；公开配方不代表本目录已复现 MiMo 训练。 FineEnvs Explorer 是非官方社区配套，浏览任务并支持提交 rollout，不代表小米官方托管服务。

GitHub: ★ 666 · push 2026-09-26 · `Apache-2.0` · active

[GitHub](https://github.com/XiaomiMiMo/verl) · [RL OSS 数据](https://huggingface.co/datasets/XiaomiMiMo/MiMo-V2.6-RL-oss) · [Docker 镜像](https://hub.docker.com/r/xiaomimimo/mimo-v2.6-rl-oss) · [技术报告（配套）](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL/blob/main/MiMo_V2_6_technical_report.pdf) · [社区 Explorer（非官方）](https://huggingface.co/spaces/FineEnvs/MiMo-RL-Envs-Explorer)

同组资源：[MiMo Agent (mimoagent) (project)](#mimo-agent-mimoagent--project-xiaomi-mimoagent) · [MiMo-V2.6 (report)](#mimo-v26--report-mimo-v26)

**来源证据**

- [primary-source-content](https://github.com/XiaomiMiMo/verl) · 2026-10-08 · “This fork adds reproduction code for five RL environments”
- [primary-source-content](https://huggingface.co/spaces/FineEnvs/MiMo-RL-Envs-Explorer/raw/main/README.md) · 2026-10-08 · “An unofficial explorer for XiaomiMiMo/MiMo-V2.6-RL-oss”

## MiMo Agent (mimoagent) — project-xiaomi-mimoagent

**[MiMo Agent: environment backends, rollout and grading](https://github.com/XiaomiMiMo/mimoagent)**

`project` · `xiaomi-mimo-rl-oss` · 日期未确认 · 环境基础设施

分离代理、模型协议、执行后端和数据评分器，记录训练轨迹并对环境终态评分。

**反馈／验收：** 由数据集对应的评分器检查最终执行环境。

**开放边界：** 属于同套 MiMo 发布的 rollout 库；支持某个后端不代表每个任务均自包含或已经独立复现。

GitHub: ★ 39 · push 2026-09-21 · `MIT` · active

[GitHub](https://github.com/XiaomiMiMo/mimoagent)

同组资源：[MiMo-V2.6 RL OSS Environments (XiaomiMiMo/verl) (project)](#mimo-v26-rl-oss-environments-xiaomimimoverl--project-xiaomi-mimo-verl) · [MiMo-V2.6 (report)](#mimo-v26--report-mimo-v26)

**来源证据**

- [primary-source-content](https://github.com/XiaomiMiMo/mimoagent) · 2026-10-08 · “It connects agents, tools, environments, datasets and graders, and manages rollouts at scale.”

## Terminal-World (skills) — paper-terminal-world-skills

**[Terminal-World: Scaling Terminal-Agent Environments via Agent Skills](https://arxiv.org/abs/2605.20876)**

`paper` · `terminal-world-skills` · 2026-05-20 · SFT／轨迹训练

以技能及其依赖图共同生成终端任务、可执行环境和教师轨迹。

**反馈／验收：** 对齐共同生成的任务、运行环境与教师轨迹；下游证据是轨迹训练。

**开放边界：** 与录制还原路线的 TerminalWorld 不同；SFT 实验不等于在线 RL 已就绪，本轮未确认生成器开放。

**实现状态：** 未确认

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2605.20876) · 2026-10-08 · “Terminal agents extend Large Language Models with the ability to execute tasks directly in command-line environments, but their progress is”

## SkillSynth — paper-skillsynth

**[Toward Scalable Terminal Task Synthesis via Skill Graphs](https://arxiv.org/abs/2604.25727)**

`paper` · `skillsynth` · 2026-04-28 · SFT／轨迹训练

通过场景连接技能图，将技能组合转成可执行终端任务及多样解题轨迹。

**反馈／验收：** 验证可执行任务实例，并从场景—技能组合与求解轨迹衡量多样性。

**开放边界：** 技能覆盖、轨迹多样性与独立环境家族数量不同；本轮未确认官方代码。

**实现状态：** 未确认

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2604.25727) · 2026-10-08 · “Terminal agents have demonstrated strong potential for autonomous command-line execution, yet their training remains constrained by the scarcity of high-quality”

## Terminal-Task-Gen / Nemotron-Terminal — paper-terminal-task-gen

**[On Data Engineering for Scaling LLM Terminal Capabilities](https://arxiv.org/abs/2602.21193)**

`paper` · `terminal-task-gen` · 2026-02-24 · SFT／轨迹训练

把种子任务与技能驱动生成、环境适配和轨迹筛选组合为 Terminal-Corpus 数据工程流程。

**反馈／验收：** 任务与轨迹筛选、环境适配，以及数据混合／课程实验。

**开放边界：** 已关联模型／数据集合，但不能据此推断完整生成流水线已开放。

**实现状态：** 未确认

[模型与数据集合](https://huggingface.co/collections/nvidia/nemotron-terminal)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2602.21193) · 2026-10-08 · “Despite rapid recent progress in the terminal capabilities of large language models, the training data strategies behind state-of-the-art terminal agents”

## SKT — paper-skt

**[SKT: Skill-Use Training at Scale via Verified Synthetic Data Generation](https://arxiv.org/abs/2608.02287)**

`paper` · `skt` · 2026-08-03 · SFT／轨迹训练

构造技能条件化任务包，在采集 SFT 轨迹前同时检查执行成功与所需技能确实被使用。

**反馈／验收：** 规则与智能体检查、迭代修复，并验证所要求的技能实际被使用。

**开放边界：** 任务成功不自动证明技能被使用；本轮未确认官方流水线代码。

**实现状态：** 未确认

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2608.02287) · 2026-10-08 · “Agent skills have become an important mechanism for equipping language-model agents with reusable procedural knowledge. However, providing skills alone does”

## NexForge — paper-nexforge

**[NexForge: Scaling Agent Capabilities through Requirement-Driven Task Synthesis for LLMs](https://arxiv.org/abs/2607.14186)**

`paper` · `nexforge` · 2026-07-15 · SFT／轨迹训练

从真实需求编译任务，检索或构建配套文件及运行环境，再采集专家示范。

**反馈／验收：** 以需求约束任务构造，准备各任务执行资源并采集专家示范。

**开放边界：** 终端与办公任务数需要和轨迹数分开；模型发布不代表生成器开放。

**实现状态：** 未确认

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2607.14186) · 2026-10-08 · “Scaling executable agent training data for LLM post-training is bottlenecked by substrate-bound methods that tie task generation to predefined tools,”

## SkillScriptBench — paper-skillscriptbench

**[SkillScriptBench: Benchmarking Self-Evolution of Executable Agent Skill Packages Beyond Markdown](https://arxiv.org/abs/2610.04008)**

`paper` · `skillscriptbench` · 2026-10-02 · 评测环境

构造可执行技能包测试，包含脚本故障注入及受控的包编辑场景。

**反馈／验收：** 通过受控故障注入及可执行包编辑测试，区分脚本修复和文档修改。

**开放边界：** 属于可执行技能修复基准，而非通用世界生成器；本轮未确认官方代码。

**实现状态：** 未确认

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2610.04008) · 2026-10-08 · “Executable Agent Skills combine natural-language instructions and scripts into reusable packages for LLM agents, and revising them requires fixing errors”

## Grounded Skill-Following — paper-skill-contracts

**[Beyond Instruction Following: Learning Grounded Skill-Following with Skill Contracts](https://arxiv.org/abs/2610.05161)**

`paper` · `skill-contracts` · 2026-10-04 · RL 实验

用允许动作、状态转移与终止条件定义运行时技能契约，提供可核验的进度反馈。

**反馈／验收：** 检查允许动作、契约状态转移与终止，按可核验进度分配反馈。

**开放边界：** 契约约束已有任务；论文所链仓库本轮无法访问，未计入可用实现。

**实现状态：** 未确认

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2610.05161) · 2026-10-08 · “Instruction following typically enforces discrete, response-level requirements, whereas an expert-authored skill prescribes procedural requirements spanning multiple phases and environment interactions.”

## CLI-Universe — paper-cli-universe

**[CLI-Universe: Towards Verifiable Task Synthesis Engine for Terminal Agents](https://arxiv.org/abs/2606.22883)**

`paper` · `cli-universe` · 2026-06-22 · SFT／轨迹训练

从能力分类与需求分析产生任务蓝图、Docker 环境和按评分要求筛选的验证器。

**反馈／验收：** 按评分要求筛选任务并执行 fail-to-pass 测试，同时过滤误导性提示。

**开放边界：** 可执行与 fail-to-pass 检查本身不能证明真实分布代表性；本轮未确认官方代码。

**实现状态：** 未确认

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2606.22883) · 2026-10-08 · “While recent LLM-based terminal agents have demonstrated promising capabilities, the scarcity of high-quality, executable training data remains a critical bottleneck.”

## OpenThoughts-Agent — paper-openthoughts-agent

**[OpenThoughts-Agent: Data Recipes for Agentic Models](https://arxiv.org/abs/2606.24855)**

`paper` · `openthoughts-agent` · 2026-06-23 · SFT／轨迹训练

通过控制实验研究任务来源、混合比例、教师、rollout 与过滤策略，形成终端智能体数据配方。

**反馈／验收：** 控制任务来源、教师与过滤策略做消融；早期 RL 配方还在沙箱中验证任务。

**开放边界：** 2025 年发布博客和 2026 年论文属于不同发布阶段；结果取决于完整数据配方。

**实现状态：** 代码

[代码](https://github.com/open-thoughts/OpenThoughts-Agent)

同组资源：[OpenThoughts-Agent (project)](#openthoughts-agent--project-openthoughts-agent) · [Launching OpenThoughts-Agent (blog)](#launching-openthoughts-agent--blog-openthoughts-agent)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2606.24855) · 2026-10-08 · “Agentic language models dramatically expand the applications of AI yet little is publicly known about how to curate training data”

## OpenThoughts-Agent — project-openthoughts-agent

**[OpenThoughts-Agent: Data Recipes for Agentic Models](https://github.com/open-thoughts/OpenThoughts-Agent)**

`project` · `openthoughts-agent` · 日期未确认 · SFT／轨迹训练

通过控制实验研究任务来源、混合比例、教师、rollout 与过滤策略，形成终端智能体数据配方。

**反馈／验收：** 控制任务来源、教师与过滤策略做消融；早期 RL 配方还在沙箱中验证任务。

**开放边界：** 2025 年发布博客和 2026 年论文属于不同发布阶段；结果取决于完整数据配方。

GitHub: ★ 301 · push 2026-09-28 · `Apache-2.0` · active

[GitHub](https://github.com/open-thoughts/OpenThoughts-Agent)

同组资源：[OpenThoughts-Agent (paper)](#openthoughts-agent--paper-openthoughts-agent) · [Launching OpenThoughts-Agent (blog)](#launching-openthoughts-agent--blog-openthoughts-agent)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2606.24855) · 2026-10-08 · “Agentic language models dramatically expand the applications of AI yet little is publicly known about how to curate training data”

## TerminalTraj — paper-terminaltraj

**[Large-Scale Terminal Agentic Trajectory Generation from Dockerized Environments](https://arxiv.org/abs/2602.01244)**

`paper` · `terminaltraj` · 2026-02-01 · SFT／轨迹训练

从仓库构造 Docker 环境、配套终端任务与可执行验证器，批量采集交互轨迹。

**反馈／验收：** 为与 Docker 环境对齐的任务合成可执行验证代码，并筛选轨迹。

**开放边界：** 镜像、任务和轨迹是不同计数单位；论文所链仓库本轮返回 404，未计入公开实现。

**实现状态：** 未确认

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2602.01244) · 2026-10-08 · “Training agentic models for terminal-based tasks critically depends on high-quality terminal trajectories that capture realistic long-horizon interactions across diverse domains.”

## AgentTrek — paper-agenttrek

**[AgentTrek: Agent Trajectory Synthesis via Guiding Replay with Web Tutorials](https://arxiv.org/abs/2412.09605)**

`paper` · `agenttrek` · 2024-12-12 · SFT／轨迹训练

采集网页教程并提炼任务指令，引导浏览器回放，再筛选用于训练的轨迹。

**反馈／验收：** 教程指导的浏览器回放，配合模型对轨迹进行验证。

**开放边界：** 教程回放利用已有网站，不代表生成独立网站后端；模型判定也可能出错。

**实现状态：** 代码

[代码](https://github.com/xlang-ai/AgentTrek) · [轨迹数据集](https://huggingface.co/datasets/xlangai/AgentTrek)

同组资源：[AgentTrek (project)](#agenttrek--project-agenttrek)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2412.09605) · 2026-10-08 · “Graphical User Interface (GUI) agents can automate complex tasks across digital environments, but their development is hindered by the scarcity”

## AgentTrek — project-agenttrek

**[AgentTrek: Agent Trajectory Synthesis via Guiding Replay with Web Tutorials](https://github.com/xlang-ai/AgentTrek)**

`project` · `agenttrek` · 日期未确认 · SFT／轨迹训练

采集网页教程并提炼任务指令，引导浏览器回放，再筛选用于训练的轨迹。

**反馈／验收：** 教程指导的浏览器回放，配合模型对轨迹进行验证。

**开放边界：** 教程回放利用已有网站，不代表生成独立网站后端；模型判定也可能出错。

GitHub: ★ 60 · push 2025-02-21 · `none` · reference

[GitHub](https://github.com/xlang-ai/AgentTrek)

同组资源：[AgentTrek (paper)](#agenttrek--paper-agenttrek)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2412.09605) · 2026-10-08 · “Graphical User Interface (GUI) agents can automate complex tasks across digital environments, but their development is hindered by the scarcity”

## OS-Genesis — paper-os-genesis

**[OS-Genesis: Automating GUI Agent Trajectory Construction via Reverse Task Synthesis](https://arxiv.org/abs/2412.19723)**

`paper` · `os-genesis` · 2024-12-27 · SFT／轨迹训练

先探索 GUI 环境，再反向合成任务，并用轨迹奖励模型筛选交互质量。

**反馈／验收：** 检查反向合成任务与交互的一致性，以轨迹奖励模型做质量筛选。

**开放边界：** 主要在已有桌面／移动环境上构造任务与轨迹，不是新操作系统模拟器。

**实现状态：** 代码

[代码](https://github.com/OS-Copilot/OS-Genesis)

同组资源：[OS-Genesis (project)](#os-genesis--project-os-genesis)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2412.19723) · 2026-10-08 · “Graphical User Interface (GUI) agents powered by Vision-Language Models (VLMs) have demonstrated human-like computer control capability. Despite their utility in”

## OS-Genesis — project-os-genesis

**[OS-Genesis: Automating GUI Agent Trajectory Construction via Reverse Task Synthesis](https://github.com/OS-Copilot/OS-Genesis)**

`project` · `os-genesis` · 日期未确认 · SFT／轨迹训练

先探索 GUI 环境，再反向合成任务，并用轨迹奖励模型筛选交互质量。

**反馈／验收：** 检查反向合成任务与交互的一致性，以轨迹奖励模型做质量筛选。

**开放边界：** 主要在已有桌面／移动环境上构造任务与轨迹，不是新操作系统模拟器。

GitHub: ★ 190 · push 2025-10-08 · `none` · reference

[GitHub](https://github.com/OS-Copilot/OS-Genesis)

同组资源：[OS-Genesis (paper)](#os-genesis--paper-os-genesis)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2412.19723) · 2026-10-08 · “Graphical User Interface (GUI) agents powered by Vision-Language Models (VLMs) have demonstrated human-like computer control capability. Despite their utility in”

## WebForge — paper-webforge

**[WebForge: Breaking the Realism-Reproducibility-Scalability Trilemma in Browser Agent Benchmark](https://arxiv.org/abs/2604.10988)**

`paper` · `webforge` · 2026-04-13 · 评测环境

协同规划、网站生成、修订与验证，构造自包含且可调难度的浏览器基准。

**反馈／验收：** 先验证生成网站，再由 LLM 比较终态答案或网站计算的操作码。

**开放边界：** 公开代码主要覆盖评测端；终态答案或操作码由 LLM 比较，并非全部使用确定性状态验证。

**实现状态：** 部分／关联代码

[部分／关联代码](https://github.com/yuandaxia2001/WebForge) · [基准网站与任务](https://huggingface.co/datasets/yuandaxia/WebForge)

同组资源：[WebForge (project)](#webforge--project-webforge)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2604.10988) · 2026-10-08 · “Existing browser agent benchmarks face a fundamental trilemma: real-website benchmarks lack reproducibility due to content drift, controlled environments sacrifice realism”

## WebForge — project-webforge

**[WebForge: Breaking the Realism-Reproducibility-Scalability Trilemma in Browser Agent Benchmark](https://github.com/yuandaxia2001/WebForge)**

`project` · `webforge` · 日期未确认 · 评测环境

协同规划、网站生成、修订与验证，构造自包含且可调难度的浏览器基准。

**反馈／验收：** 先验证生成网站，再由 LLM 比较终态答案或网站计算的操作码。

**开放边界：** 公开代码主要覆盖评测端；终态答案或操作码由 LLM 比较，并非全部使用确定性状态验证。

GitHub: ★ 14 · push 2026-04-14 · `Apache-2.0` · reference

[GitHub](https://github.com/yuandaxia2001/WebForge)

同组资源：[WebForge (paper)](#webforge--paper-webforge)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2604.10988) · 2026-10-08 · “Existing browser agent benchmarks face a fundamental trilemma: real-website benchmarks lack reproducibility due to content drift, controlled environments sacrifice realism”

## SWE-Universe — paper-swe-universe

**[SWE-Universe: Scale Real-World Verifiable Environments to Millions](https://arxiv.org/abs/2602.02361)**

`paper` · `swe-universe` · 2026-02-02 · RL 实验

由训练过的构建智能体把 PR 转成可核验 SWE 环境，加入迭代自检与构建环内的作弊检测。

**反馈／验收：** 在使用可执行任务学习前进行迭代构建验证与构建环内作弊检测。

**开放边界：** 论文报告 807,693 个实例，并非独立环境家族；本轮未确认官方构建代码。

**实现状态：** 未确认

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2602.02361) · 2026-10-08 · “We propose SWE-Universe, a scalable and efficient framework for automatically constructing real-world software engineering (SWE) verifiable environments from GitHub pull”

## ScaleSWE — paper-scaleswe

**[Immersion in the GitHub Universe: Scaling Coding Agents to Mastery](https://arxiv.org/abs/2602.09892)**

`paper` · `scaleswe` · 2026-02-10 · SFT／轨迹训练

协同环境配置、测试生成和问题描述智能体，构建来自 PR 的 SWE 任务及示范数据。

**反馈／验收：** 在恢复的仓库状态上执行 fail-to-pass 复现测试与 pass-to-pass 回归检查。

**开放边界：** 论文规模为 100k 实例；仓库明确说明初始公开子集为 20k 实例，执行依赖另一个 harness。

**实现状态：** 部分／关联代码

[部分／关联代码](https://github.com/AweAI-Team/ScaleSWE) · [公开数据集合](https://huggingface.co/collections/AweAI-Team/scale-swe)

同组资源：[ScaleSWE (project)](#scaleswe--project-scaleswe)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2602.09892) · 2026-10-08 · “Achieving mastery in real world software engineering tasks is fundamentally bottlenecked by the scarcity of large scale, high quality training”

## ScaleSWE — project-scaleswe

**[Immersion in the GitHub Universe: Scaling Coding Agents to Mastery](https://github.com/AweAI-Team/ScaleSWE)**

`project` · `scaleswe` · 日期未确认 · SFT／轨迹训练

协同环境配置、测试生成和问题描述智能体，构建来自 PR 的 SWE 任务及示范数据。

**反馈／验收：** 在恢复的仓库状态上执行 fail-to-pass 复现测试与 pass-to-pass 回归检查。

**开放边界：** 论文规模为 100k 实例；仓库明确说明初始公开子集为 20k 实例，执行依赖另一个 harness。

GitHub: ★ 95 · push 2026-07-21 · `NOASSERTION` · reference

[GitHub](https://github.com/AweAI-Team/ScaleSWE)

同组资源：[ScaleSWE (paper)](#scaleswe--paper-scaleswe)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2602.09892) · 2026-10-08 · “Achieving mastery in real world software engineering tasks is fundamentally bottlenecked by the scarcity of large scale, high quality training”

## InSTA — paper-insta

**[InSTA: Towards Internet-Scale Training For Agents](https://arxiv.org/abs/2502.06776)**

`paper` · `insta` · 2025-02-10 · SFT／轨迹训练

为网站自动标注任务、执行智能体并过滤成功轨迹，规模化构建网页交互数据。

**反馈／验收：** 用 LLM 判断任务成功并筛选采集的浏览器轨迹。

**开放边界：** 仍受线上网站变化与模型判定误差影响；网站数量不等于新合成环境数量。

**实现状态：** 代码

[代码](https://github.com/data-for-agents/insta)

同组资源：[InSTA (project)](#insta--project-insta)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2502.06776) · 2026-10-08 · “The predominant approach for training web navigation agents is to gather human demonstrations for a set of popular websites and”

## InSTA — project-insta

**[InSTA: Towards Internet-Scale Training For Agents](https://github.com/data-for-agents/insta)**

`project` · `insta` · 日期未确认 · SFT／轨迹训练

为网站自动标注任务、执行智能体并过滤成功轨迹，规模化构建网页交互数据。

**反馈／验收：** 用 LLM 判断任务成功并筛选采集的浏览器轨迹。

**开放边界：** 仍受线上网站变化与模型判定误差影响；网站数量不等于新合成环境数量。

GitHub: ★ 56 · push 2025-07-11 · `MIT` · reference

[GitHub](https://github.com/data-for-agents/insta)

同组资源：[InSTA (paper)](#insta--paper-insta)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2502.06776) · 2026-10-08 · “The predominant approach for training web navigation agents is to gather human demonstrations for a set of popular websites and”

## RandomWorld — paper-randomworld

**[Procedural Environment Generation for Tool-Use Agents](https://arxiv.org/abs/2506.11045)**

`paper` · `randomworld` · 2025-05-21 · RL 与 SFT 实验

程序化生成可交互工具及组合式工具使用数据，同时用于监督学习与强化学习。

**反馈／验收：** 可执行的合成工具交互与组合任务结果提供监督和 RL 信号。

**开放边界：** 合成工具语义不代表生产 API 保真度；公开仓库的使用文档较少。

**实现状态：** 代码

[代码](https://github.com/coli-saar/randomworld)

同组资源：[RandomWorld (project)](#randomworld--project-randomworld)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2506.11045) · 2026-10-08 · “Although the power of LLM tool-use agents has ignited a flurry of recent research in this area, the curation of”

## RandomWorld — project-randomworld

**[Procedural Environment Generation for Tool-Use Agents](https://github.com/coli-saar/randomworld)**

`project` · `randomworld` · 日期未确认 · RL 与 SFT 实验

程序化生成可交互工具及组合式工具使用数据，同时用于监督学习与强化学习。

**反馈／验收：** 可执行的合成工具交互与组合任务结果提供监督和 RL 信号。

**开放边界：** 合成工具语义不代表生产 API 保真度；公开仓库的使用文档较少。

GitHub: ★ 3 · push 2025-05-02 · `none` · reference

[GitHub](https://github.com/coli-saar/randomworld)

同组资源：[RandomWorld (paper)](#randomworld--paper-randomworld)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2506.11045) · 2026-10-08 · “Although the power of LLM tool-use agents has ignited a flurry of recent research in this area, the curation of”

## ClawEnvKit — paper-clawenvkit

**[ClawEnvKit: Automatic Environment Generation for Claw-Like Agents](https://arxiv.org/abs/2604.18543)**

`paper` · `clawenvkit` · 2026-04-20 · 评测环境

把自然语言需求解析为任务规格、模拟工具和评分规则，再验证生成的评测环境。

**反馈／验收：** 配置验证、模拟服务审计日志与结构化规则检查，并包含 LLM 判定类型。

**开放边界：** 模拟服务与规则／模型混合检查不等于真实企业系统；可用于训练不等于已报告 RL 收益。

**实现状态：** 代码

[代码](https://github.com/xirui-li/ClawEnvKit)

同组资源：[ClawEnvKit (project)](#clawenvkit--project-clawenvkit)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2604.18543) · 2026-10-08 · “Constructing environments for training and evaluating claw-like agents remains a manual, human-intensive process that does not scale. We argue that”

## ClawEnvKit — project-clawenvkit

**[ClawEnvKit: Automatic Environment Generation for Claw-Like Agents](https://github.com/xirui-li/ClawEnvKit)**

`project` · `clawenvkit` · 日期未确认 · 评测环境

把自然语言需求解析为任务规格、模拟工具和评分规则，再验证生成的评测环境。

**反馈／验收：** 配置验证、模拟服务审计日志与结构化规则检查，并包含 LLM 判定类型。

**开放边界：** 模拟服务与规则／模型混合检查不等于真实企业系统；可用于训练不等于已报告 RL 收益。

GitHub: ★ 62 · push 2026-05-07 · `MIT` · reference

[GitHub](https://github.com/xirui-li/ClawEnvKit)

同组资源：[ClawEnvKit (paper)](#clawenvkit--paper-clawenvkit)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2604.18543) · 2026-10-08 · “Constructing environments for training and evaluating claw-like agents remains a manual, human-intensive process that does not scale. We argue that”

## TerminalWorld (recordings) — paper-terminalworld-recordings

**[TerminalWorld: Benchmarking Agents on Real-World Terminal Tasks](https://arxiv.org/abs/2605.22535)**

`paper` · `terminalworld-recordings` · 2026-05-21 · 评测环境

从真实终端录制反向还原可复现环境、可执行任务及经过验证的基准实例。

**反馈／验收：** 自动还原与验证，并单独提供经过人工核验的基准子集。

**开放边界：** 与技能驱动的 Terminal-World 不同；自动验证集和人工核验子集的证据强度不同。

**实现状态：** 代码

[代码](https://github.com/EuniAI/TerminalWorld)

同组资源：[TerminalWorld (recordings) (project)](#terminalworld-recordings--project-terminalworld-recordings)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2605.22535) · 2026-10-08 · “We introduce TerminalWorld, a scalable data engine that automatically reverse-engineers high-fidelity evaluation tasks from "in-the-wild" terminal recordings. Processing 80,870 terminal”

## TerminalWorld (recordings) — project-terminalworld-recordings

**[TerminalWorld: Benchmarking Agents on Real-World Terminal Tasks](https://github.com/EuniAI/TerminalWorld)**

`project` · `terminalworld-recordings` · 日期未确认 · 评测环境

从真实终端录制反向还原可复现环境、可执行任务及经过验证的基准实例。

**反馈／验收：** 自动还原与验证，并单独提供经过人工核验的基准子集。

**开放边界：** 与技能驱动的 Terminal-World 不同；自动验证集和人工核验子集的证据强度不同。

GitHub: ★ 48 · push 2026-05-31 · `Apache-2.0` · reference

[GitHub](https://github.com/EuniAI/TerminalWorld)

同组资源：[TerminalWorld (recordings) (paper)](#terminalworld-recordings--paper-terminalworld-recordings)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2605.22535) · 2026-10-08 · “We introduce TerminalWorld, a scalable data engine that automatically reverse-engineers high-fidelity evaluation tasks from "in-the-wild" terminal recordings. Processing 80,870 terminal”

## CalibForge — paper-calibforge

**[CalibForge: Adversarial Solver Calibration for Scaling Learnable Terminal Tasks](https://arxiv.org/abs/2608.06352)**

`paper` · `calibforge` · 2026-08-06 · SFT／轨迹训练

利用经验证的求解器分歧，或强模型通过／弱模型失败的对比，修订终端任务的可学习难度。

**反馈／验收：** 根据经过验证的求解结果，选择求解器分歧或强通过／弱失败区间。

**开放边界：** 难度校准相对于选定求解器，不是绝对难度；公开数据及 agent 配方不等于完整合成引擎。

**实现状态：** 部分／关联代码

[部分／关联代码](https://github.com/AweAI-Team/CalibForge)

同组资源：[CalibForge (project)](#calibforge--project-calibforge)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2608.06352) · 2026-10-08 · “Training terminal agents requires executable and verifiable tasks that are not merely solvable, but appropriately challenging for learning. Executable validation”

## CalibForge — project-calibforge

**[CalibForge: Adversarial Solver Calibration for Scaling Learnable Terminal Tasks](https://github.com/AweAI-Team/CalibForge)**

`project` · `calibforge` · 日期未确认 · SFT／轨迹训练

利用经验证的求解器分歧，或强模型通过／弱模型失败的对比，修订终端任务的可学习难度。

**反馈／验收：** 根据经过验证的求解结果，选择求解器分歧或强通过／弱失败区间。

**开放边界：** 难度校准相对于选定求解器，不是绝对难度；公开数据及 agent 配方不等于完整合成引擎。

GitHub: ★ 10 · push 2026-08-07 · `none` · reference

[GitHub](https://github.com/AweAI-Team/CalibForge)

同组资源：[CalibForge (paper)](#calibforge--paper-calibforge)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2608.06352) · 2026-10-08 · “Training terminal agents requires executable and verifiable tasks that are not merely solvable, but appropriately challenging for learning. Executable validation”

## DeNovoSWE — paper-denovoswe

**[DeNovoSWE: Scaling Long-Horizon Environments for Generating Entire Repositories from Scratch](https://arxiv.org/abs/2606.10728)**

`paper` · `denovoswe` · 2026-06-09 · SFT／轨迹训练

通过沙箱中的任务拆解、批判修复与难度感知轨迹过滤，构建文档到完整仓库的任务。

**反馈／验收：** 单元测试、构造时的批判修复，以及按难度筛选成功轨迹。

**开放边界：** 从零写仓库描述的是智能体任务，构造过程仍依托已有包；仓库声明公开部分数据。

**实现状态：** 部分／关联代码

[部分／关联代码](https://github.com/AweAI-Team/DeNovoSWE)

同组资源：[DeNovoSWE (project)](#denovoswe--project-denovoswe)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2606.10728) · 2026-10-08 · “As the capabilities of LLM-based code agents continue to advance, their expected role is expanding beyond localized bug fixing in”

## DeNovoSWE — project-denovoswe

**[DeNovoSWE: Scaling Long-Horizon Environments for Generating Entire Repositories from Scratch](https://github.com/AweAI-Team/DeNovoSWE)**

`project` · `denovoswe` · 日期未确认 · SFT／轨迹训练

通过沙箱中的任务拆解、批判修复与难度感知轨迹过滤，构建文档到完整仓库的任务。

**反馈／验收：** 单元测试、构造时的批判修复，以及按难度筛选成功轨迹。

**开放边界：** 从零写仓库描述的是智能体任务，构造过程仍依托已有包；仓库声明公开部分数据。

GitHub: ★ 47 · push 2026-08-07 · `Apache-2.0` · reference

[GitHub](https://github.com/AweAI-Team/DeNovoSWE)

同组资源：[DeNovoSWE (paper)](#denovoswe--paper-denovoswe)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2606.10728) · 2026-10-08 · “As the capabilities of LLM-based code agents continue to advance, their expected role is expanding beyond localized bug fixing in”

## SWE-Playground — paper-swe-playground

**[Training Versatile Coding Agents in Synthetic Environments](https://arxiv.org/abs/2512.12216)**

`paper` · `swe-playground` · 2025-12-13 · SFT／轨迹训练

从零合成软件项目、任务与执行轨迹，覆盖测试编写及库实现等场景。

**反馈／验收：** 分别由测试编写与功能实现智能体相互检验生成的软件任务。

**开放边界：** 合成项目多样性与真实仓库保真度不同；执行需要模型和运行后端依赖。

**实现状态：** 代码

[代码](https://github.com/neulab/SWE-Playground)

同组资源：[SWE-Playground (project)](#swe-playground--project-swe-playground)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2512.12216) · 2026-10-08 · “Prior works on training software engineering agents have explored utilizing existing resources such as issues on GitHub repositories to construct”

## AgentMercury — paper-agentmercury

**[AgentMercury: Your Agent Can Synthesize Verifiable Environments for Business Scenarios at scale](https://arxiv.org/abs/2608.20634)**

`paper` · `agentmercury` · 2026-08-21 · RL 与 SFT 实验

先构建包含持久状态、工具和跨服务不变量的业务世界，再从中派生任务与轨迹。

**反馈／验收：** 可执行跨服务不变量约束生成世界；策略 RL 与构建轨迹微调分别评估。

**开放边界：** 公开语料样本不等于完整可执行世界库；构建模型微调与策略 RL 是不同实验。

**实现状态：** 未确认

[公开语料样本](https://huggingface.co/datasets/Minbyul/AgentMercury-corpus-sample)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2608.20634) · 2026-10-08 · “Agents learn to act through interaction with environments, yet the environments used for training are often manually constructed or synthesized”

## Launching OpenThoughts-Agent — blog-openthoughts-agent

**[Launching the OpenThoughts-Agent Project | OpenThoughts](https://www.openthoughts.ai/blog/agent)**

`blog` · `openthoughts-agent` · 2025-12-05 · RL 与 SFT 实验

介绍早期任务／教师消融、SFT 轨迹，以及经过执行筛选的 NL2Bash RL 数据流水线。

**反馈／验收：** 控制任务来源、教师与过滤策略做消融；早期 RL 配方还在沙箱中验证任务。

**开放边界：** 这篇发布文章早于 2026 年论文，不能推断文中计划的所有生成组件在当时已开放。

同组资源：[OpenThoughts-Agent (paper)](#openthoughts-agent--paper-openthoughts-agent) · [OpenThoughts-Agent (project)](#openthoughts-agent--project-openthoughts-agent)

**来源证据**

- [primary-source-content](https://www.openthoughts.ai/blog/agent) · 2026-10-08 · “Launching the OpenThoughts-Agent Project | OpenThoughts”

## Browser Use benchmark construction — blog-browser-use-bench

**[Browser Agent Benchmark: Comparing LLM Models for Web Automation](https://browser-use.com/posts/ai-browser-agent-benchmark)**

`blog` · `browser-use-bench` · 2026-01-31 · 评测环境

介绍 BU Bench 的真实网页任务筛选、加密测试分发和模型成功判定。

**反馈／验收：** 对真实网页执行进行模型成功判定，文章报告了与人工判断的一致性检查。

**开放边界：** 真实网站会变化，LLM 判定与人类可能不一致；测试任务集不是新生成的离线世界集合。

同组资源：[benchmark (project)](#benchmark--project-browser-use-bench)

**来源证据**

- [primary-source-content](https://browser-use.com/posts/ai-browser-agent-benchmark) · 2026-10-08 · “Browser Agent Benchmark: Comparing LLM Models for Web Automation”

## benchmark — project-browser-use-bench

**[Browser Agent Benchmark: Comparing LLM Models for Web Automation](https://github.com/browser-use/benchmark)**

`project` · `browser-use-bench` · 日期未确认 · 评测环境

介绍 BU Bench 的真实网页任务筛选、加密测试分发和模型成功判定。

**反馈／验收：** 对真实网页执行进行模型成功判定，文章报告了与人工判断的一致性检查。

**开放边界：** 真实网站会变化，LLM 判定与人类可能不一致；测试任务集不是新生成的离线世界集合。

GitHub: ★ 149 · push 2026-10-01 · `none` · active

[GitHub](https://github.com/browser-use/benchmark)

同组资源：[Browser Use benchmark construction (blog)](#browser-use-benchmark-construction--blog-browser-use-bench)

**来源证据**

- [primary-source-content](https://browser-use.com/posts/ai-browser-agent-benchmark) · 2026-10-08 · “Browser Use benchmark construction”

## Tracing Agent Harness Behavior with NVIDIA NeMo Relay — blog-nemo-relay-tracing

**[Tracing Agent Harness Behavior with NVIDIA NeMo Relay | NVIDIA Technical Blog](https://developer.nvidia.com/blog/?p=123038)**

`blog` · `nemo-relay-tracing` · 2026-09-30 · 技术报告

展示有序事件与轨迹采集，并与任务验证结果、harness 行为对比结合分析。

**反馈／验收：** 将任务特定成功检查，与有序事件、轨迹和过程／成本观测配对。

**开放边界：** 可观测性记录行为；完整轨迹既不等于新环境，也不自动证明任务完成。

**来源证据**

- [primary-source-content](https://developer.nvidia.com/blog/?p=123038) · 2026-10-08 · “Tracing Agent Harness Behavior with NVIDIA NeMo Relay”

## How to Evaluate AI Agents From Tool Calls to Task Completion — blog-nvidia-agent-evaluation

**[How to Evaluate AI Agents From Tool Calls to Task Completion | NVIDIA Technical Blog](https://developer.nvidia.com/blog/how-to-evaluate-ai-agents-from-tool-calls-to-task-completion/)**

`blog` · `nvidia-agent-evaluation` · 2026-09-21 · 质量／失败研究

区分步骤级过程评分与终态任务完成，并把可靠性分析放回有状态评测设计。

**反馈／验收：** 区分过程评分和依据环境终态验证的任务完成。

**开放边界：** 属于设计方法文章，不是独立复现或通用环境生成器。

**来源证据**

- [primary-source-content](https://developer.nvidia.com/blog/how-to-evaluate-ai-agents-from-tool-calls-to-task-completion/) · 2026-10-08 · “How to Evaluate AI Agents From Tool Calls to Task Completion”

## Announcing LiteCoder-Terminal Preview — blog-litecoder

**[Announcing LiteCoder-Terminal: Lightweight Terminal Agents with <1k Synthesized Trajectories](https://huggingface.co/blog/Lite-Coder/litecoder-terminal-preview)**

`blog` · `litecoder` · 2025-12-18 · SFT／轨迹训练

详述按领域分类采样任务、可行性筛选、Docker 初态构造和轨迹采集。

**反馈／验收：** 可行性判定及 Docker 初态构造；后续发布增加参考解和验证测试套件。

**开放边界：** 预览博客与后续仓库发布规模不同；LLM 可行性判定本身不是可执行验证器。

同组资源：[LiteCoder (project)](#litecoder--project-litecoder)

**来源证据**

- [primary-source-content](https://huggingface.co/blog/Lite-Coder/litecoder-terminal-preview) · 2026-10-08 · “Announcing LiteCoder-Terminal: Lightweight Terminal Agents with <1k Synthesized Trajectories”

## LiteCoder — project-litecoder

**[Announcing LiteCoder-Terminal: Lightweight Terminal Agents with <1k Synthesized Trajectories](https://github.com/icip-cas/LiteCoder)**

`project` · `litecoder` · 日期未确认 · SFT／轨迹训练

发布终端轨迹与 Harbor 格式环境，并说明从指令到环境的五阶段合成流程。

**反馈／验收：** 可行性判定及 Docker 初态构造；后续发布增加参考解和验证测试套件。

**开放边界：** 当前 README 描述 11,255 条轨迹与 602 个环境，属于后续发布，不是预览博客中的不足 1k 规模。

GitHub: ★ 17 · push 2026-05-29 · `none` · reference

[GitHub](https://github.com/icip-cas/LiteCoder)

同组资源：[Announcing LiteCoder-Terminal Preview (blog)](#announcing-litecoder-terminal-preview--blog-litecoder)

**来源证据**

- [primary-source-content](https://huggingface.co/blog/Lite-Coder/litecoder-terminal-preview) · 2026-10-08 · “Announcing LiteCoder-Terminal Preview”

## Endless Terminals — paper-endless-terminals

**[Endless Terminals: Scaling RL Environments for Terminal Agents](https://arxiv.org/abs/2601.16443)**

`paper` · `endless-terminals` · 2026-01-23 · RL 实验

依次生成任务描述、构建并验证容器、生成完成测试并筛选可解任务，再进行 PPO 训练。

**反馈／验收：** 用初末状态或 fail-to-pass 测试检查执行，参考解用于验证可解性。

**开放边界：** 生成、执行与策略优化是不同阶段；已报告收益不能证明任意生成测试都可靠。

**实现状态：** 代码

[代码](https://github.com/kanishkg/endless-terminals)

同组资源：[Endless Terminals (project)](#endless-terminals--project-endless-terminals)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2601.16443) · 2026-10-08 · “Environments are the bottleneck for self-improving agents. Current terminal benchmarks were built for evaluation, not training; reinforcement learning requires a”

## Endless Terminals — project-endless-terminals

**[Endless Terminals: Scaling RL Environments for Terminal Agents](https://github.com/kanishkg/endless-terminals)**

`project` · `endless-terminals` · 日期未确认 · RL 实验

依次生成任务描述、构建并验证容器、生成完成测试并筛选可解任务，再进行 PPO 训练。

**反馈／验收：** 用初末状态或 fail-to-pass 测试检查执行，参考解用于验证可解性。

**开放边界：** 生成、执行与策略优化是不同阶段；已报告收益不能证明任意生成测试都可靠。

GitHub: ★ 147 · push 2026-03-31 · `Apache-2.0` · reference

[GitHub](https://github.com/kanishkg/endless-terminals)

同组资源：[Endless Terminals (paper)](#endless-terminals--paper-endless-terminals)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2601.16443) · 2026-10-08 · “Environments are the bottleneck for self-improving agents. Current terminal benchmarks were built for evaluation, not training; reinforcement learning requires a”

## CLI-Gym — paper-cli-gym

**[CLI-Gym: Scalable CLI Task Generation via Agentic Environment Inversion](https://arxiv.org/abs/2602.10999)**

`paper` · `cli-gym` · 2026-02-11 · SFT／轨迹训练

探索健康环境的历史并反转为可复现运行故障，再打包修复任务及成功轨迹。

**反馈／验收：** 用初末状态或 fail-to-pass 测试检查执行，参考解用于验证可解性。

**开放边界：** 在已有仓库上构造环境修复任务；任务实例数大于仓库／镜像数，不能混计。

**实现状态：** 代码

[代码](https://github.com/LiberCoders/CLI-Gym)

同组资源：[CLI-Gym (project)](#cli-gym--project-cli-gym)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2602.10999) · 2026-10-08 · “Agentic coding requires agents to effectively interact with runtime environments, e.g., command line interfaces (CLI), so as to complete tasks”

## CLI-Gym — project-cli-gym

**[CLI-Gym: Scalable CLI Task Generation via Agentic Environment Inversion](https://github.com/LiberCoders/CLI-Gym)**

`project` · `cli-gym` · 日期未确认 · SFT／轨迹训练

探索健康环境的历史并反转为可复现运行故障，再打包修复任务及成功轨迹。

**反馈／验收：** 用初末状态或 fail-to-pass 测试检查执行，参考解用于验证可解性。

**开放边界：** 在已有仓库上构造环境修复任务；任务实例数大于仓库／镜像数，不能混计。

GitHub: ★ 141 · push 2026-06-30 · `MIT` · reference

[GitHub](https://github.com/LiberCoders/CLI-Gym)

同组资源：[CLI-Gym (paper)](#cli-gym--paper-cli-gym)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2602.10999) · 2026-10-08 · “Agentic coding requires agents to effectively interact with runtime environments, e.g., command line interfaces (CLI), so as to complete tasks”

## SWE-Playground — project-swe-playground

**[Training Versatile Coding Agents in Synthetic Environments](https://github.com/neulab/SWE-Playground)**

`project` · `swe-playground` · 日期未确认 · SFT／轨迹训练

从零合成软件项目、任务与执行轨迹，覆盖测试编写及库实现等场景。

**反馈／验收：** 分别由测试编写与功能实现智能体相互检验生成的软件任务。

**开放边界：** 合成项目多样性与真实仓库保真度不同；执行需要模型和运行后端依赖。

GitHub: ★ 22 · push 2026-01-11 · `MIT` · reference

[GitHub](https://github.com/neulab/SWE-Playground)

同组资源：[SWE-Playground (paper)](#swe-playground--paper-swe-playground)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2512.12216) · 2026-10-08 · “Prior works on training software engineering agents have explored utilizing existing resources such as issues on GitHub repositories to construct”

## CompoWorld — paper-compoworld

**[CompoWorld: Compositional Environment Scaling for General Agents](https://arxiv.org/abs/2609.33665)**

`paper` · `compoworld` · 2026-09-27 · RL 与 SFT 实验

以共享类型状态与接口组合已验证服务，从依赖图合成跨服务任务。

**反馈／验收：** 完成度与 rubric 检查；报告 SFT 和 RL 实验。

**开放边界：** 服务数、工具数不能当作独立环境数；关联仓库提供样例，未确认完整复现流程。

**实现状态：** 部分／关联代码

[主页](https://github.com/AllSpark-Research/AgentEnv) · [部分／关联代码](https://github.com/AllSpark-Research/AgentEnv) · [CompoWorld 样例](https://github.com/AllSpark-Research/AgentEnv/blob/main/CompoWorld/README.md)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2609.33665) · 2026-10-08 · “CompoWorld”

## Kimi K3 — report-kimi-k3

**[Kimi K3: Open Frontier Intelligence](https://arxiv.org/abs/2607.24653)**

`report` · `kimi-k3` · 2026-07-27 · 技术报告

介绍可组合 Agent 环境、任务合成和长交互中的持久沙箱状态。

**开放边界：** 报告不等于完整训练环境发布；AgentENV 是报告单独关联的沙箱实现。

**实现状态：** 未确认

[主页](https://github.com/MoonshotAI/Kimi-K3) · [AgentENV 沙箱代码](https://github.com/kvcache-ai/AgentENV)

同组资源：[Kimi K3 Tech Blog: Open Frontier Intelligence (blog)](#kimi-k3-tech-blog-open-frontier-intelligence--blog-kimi-k3)

[报告章节索引](technical_report_sections_zh.md#kimi-k3)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2607.24653) · 2026-10-08 · “Kimi K3”

## DeepSeek V4 — report-deepseek-v4

**[DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence](https://arxiv.org/abs/2606.19348)**

`report` · `deepseek-v4` · 2026-04-26 · 技术报告

在模型报告中披露 DSec 执行后端与支持中断恢复的 rollout 服务。

**开放边界：** 本报告描述较早的命令日志恢复方案；后续 DSec 论文介绍解耦后的 rollout 执行，不能混作同一版本。

**实现状态：** 未确认

[主页](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)

[报告章节索引](technical_report_sections_zh.md#deepseek-v4)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2606.19348) · 2026-10-08 · “DeepSeek V4”

## GLM-4.5 — report-glm45

**[GLM-4.5: Agentic, Reasoning, and Coding (ARC) Foundation Models](https://arxiv.org/abs/2508.06471)**

`report` · `glm45` · 2025-08-08 · 技术报告

介绍任务合成、隔离执行，以及服务 Agent 学习的异步轨迹池。

**开放边界：** 报告披露方法，不代表完整训练任务库已经发布。

**实现状态：** 未确认

[报告章节索引](technical_report_sections_zh.md#glm-45)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2508.06471) · 2026-10-08 · “GLM-4.5”
- [pdf-title-page](https://arxiv.org/pdf/2508.06471v1) · 2026-10-08 · “GLM-4.5 Team”

## DeepSeek Elastic Compute (DSec) — paper-dsec

**[DeepSeek Elastic Compute (DSec): A Sandbox Infrastructure for Effective Agentic Training at Scale](https://arxiv.org/abs/2609.22978)**

`paper` · `dsec` · 2026-09-19 · 环境基础设施

统一函数调用、容器、microVM 与完整 VM；支持 Agent 构建可复用环境，以及长交互任务的挂起和恢复。

**反馈／验收：** 环境构建、隔离与生命周期管理的系统证据；不是独立任务 benchmark。

**开放边界：** 生产基础设施论文；未确认官方公开的 DSec 完整实现，3FS 等关联项目不等于 DSec 平台。

**实现状态：** 未确认

[报告章节索引](technical_report_sections_zh.md#deepseek-elastic-compute-dsec)

**来源证据**

- [primary-source-content](https://arxiv.org/abs/2609.22978) · 2026-10-08 · “DeepSeek Elastic Compute (DSec)”

## Introducing Codex — blog-openai-codex

**[Introducing Codex](https://openai.com/index/introducing-codex/)**

`blog` · `openai-codex` · 2025-05-16 · RL 实验

真实编码任务的执行反馈 RL；每项任务运行于装载仓库的云沙箱。

**仅作背景，不计入入选目录：** 编码产品与训练概览；未充分展开环境构造、任务采样或奖励实现。

**开放边界：** 介绍训练与产品执行方式，未发布内部完整训练环境集。

**来源证据**

- [primary-source-content](https://openai.com/index/introducing-codex/) · 2026-10-08 · “Introducing Codex”

## Computer-Using Agent — blog-openai-cua

**[Computer-Using Agent](https://openai.com/index/computer-using-agent/)**

`blog` · `openai-cua` · 2025-01-23 · RL 实验

以截图观测和鼠标／键盘动作构成计算机交互循环。

**仅作背景，不计入入选目录：** 主要讲计算机使用模型及观测／动作方式；环境生产机制披露有限。

**开放边界：** 模型与产品介绍不等于开放环境生成器。

**来源证据**

- [primary-source-content](https://openai.com/index/computer-using-agent/) · 2026-10-08 · “Computer-Using Agent”

## Demystifying evals for AI agents — blog-anthropic-evals

**[Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)**

`blog` · `anthropic-evals` · 2026-01-09 · 质量／失败研究

区分任务、试验、评分器与结果，讨论干净隔离环境及状态验收。

**支撑资料：** 为环境执行、评测、模拟或质量控制提供参考，但本次正文重点没有直接落在规模化环境生产或有效训练数据生产上，放回相应分类作支撑。

**文章研究问题：** 怎样定义有效的任务验收？

**具体内容**

- 区分 task、trial、grader 与 outcome
- 干净隔离的任务运行环境
- 检查最终状态而非仅看 agent 自述

**开放边界：** 属于评测方法，不是公开训练课程。

**来源证据**

- [primary-source-content](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) · 2026-10-08 · “Demystifying evals for AI agents”

## Quantifying infrastructure noise in agentic coding evals — blog-anthropic-infra-noise

**[Quantifying infrastructure noise in agentic coding evals](https://www.anthropic.com/engineering/infrastructure-noise)**

`blog` · `anthropic-infra-noise` · 2026-02-05 · 质量／失败研究

通过资源配额对照实验说明沙箱限制会改变可靠性及编码评测的测量对象。

**支撑资料：** 为环境执行、评测、模拟或质量控制提供参考，但本次正文重点没有直接落在规模化环境生产或有效训练数据生产上，放回相应分类作支撑。

**文章研究问题：** 资源约束会怎样改变评测？

**具体内容**

- 对照沙箱资源配额
- 分析运行限制带来的测量噪声
- 区分环境故障与模型失败

**开放边界：** 结论对应文中模型与任务，不能把某一配额推广为普适最优。

**来源证据**

- [primary-source-content](https://www.anthropic.com/engineering/infrastructure-noise) · 2026-10-08 · “Quantifying infrastructure noise in agentic coding evals”

## Training a Misaligned Reward Seeker — blog-anthropic-reward-seeker

**[Training a Misaligned Reward Seeker](https://alignment.anthropic.com/2026/reward-seeker/)**

`blog` · `anthropic-reward-seeker` · 2026-08 · 质量／失败研究

在故意设置的对抗性训练研究中，使用有漏洞的环境研究奖励投机与检测。

**支撑资料：** 为环境执行、评测、模拟或质量控制提供参考，但本次正文重点没有直接落在规模化环境生产或有效训练数据生产上，放回相应分类作支撑。

**文章研究问题：** 怎样研究环境漏洞与奖励投机？

**具体内容**

- 刻意设计对抗性训练设置
- 使用有漏洞的环境产生反馈
- 研究投机行为及其检测

**开放边界：** 刻意构造的悲观研究设置，不能当作线上模型的常规训练配置；来源仅确认 2026 年 8 月。

**来源证据**

- [primary-source-content](https://alignment.anthropic.com/2026/reward-seeker/) · 2026-10-08 · “Training a Misaligned Reward Seeker”

## Genie 3: A new frontier for world models — blog-deepmind-genie3

**[Genie 3: A new frontier for world models](https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/)**

`blog` · `deepmind-genie3` · 2025-08-05 · 环境／任务生成

由提示生成可交互视觉世界，供探索与 Agent 研究。

**支撑资料：** 为环境执行、评测、模拟或质量控制提供参考，但本次正文重点没有直接落在规模化环境生产或有效训练数据生产上，放回相应分类作支撑。

**文章研究问题：** 怎样从提示生成可交互世界？

**具体内容**

- 提示驱动视觉世界生成
- 根据动作持续产生后续观测
- 支持探索并暴露一致性边界

**开放边界：** 学习式视觉模拟器；不能等同于确定性物理引擎或已公开环境实现。

**来源证据**

- [primary-source-content](https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/) · 2026-10-08 · “Genie 3: A new frontier for world models”

## SIMA 2: An agent that plays, reasons, and learns with you in virtual 3D worlds — blog-deepmind-sima2

**[SIMA 2: An agent that plays, reasons, and learns with you in virtual 3D worlds](https://deepmind.google/blog/sima-2-an-agent-that-plays-reasons-and-learns-with-you-in-virtual-3d-worlds/)**

`blog` · `deepmind-sima2` · 2025-11-13 · 技术报告

利用多样虚拟世界开展具身交互，并考察向 Genie 生成世界的泛化。

**支撑资料：** 为环境执行、评测、模拟或质量控制提供参考，但本次正文重点没有直接落在规模化环境生产或有效训练数据生产上，放回相应分类作支撑。

**文章研究问题：** 生成世界能否承载有效 agent 交互？

**具体内容**

- 在多种虚拟世界中交互
- 考察对 Genie 生成世界的泛化
- 提供生成环境作为交互场所的使用证据

**开放边界：** 研究预览，文章未发布完整训练环境套件。

**来源证据**

- [primary-source-content](https://deepmind.google/blog/sima-2-an-agent-that-plays-reasons-and-learns-with-you-in-virtual-3d-worlds/) · 2026-10-08 · “SIMA 2: An agent that plays, reasons, and learns with you in virtual 3D worlds”

## Qwen3-Coder: Agentic Coding in the World — blog-qwen3-coder

**[Qwen3-Coder: Agentic Coding in the World](https://qwenlm.github.io/blog/qwen3-coder/)**

`blog` · `qwen3-coder` · 2025-07-22 · RL 实验

扩展执行可验证编码任务；长程 RL 支持 20,000 个独立环境并行。

**仅作背景，不计入入选目录：** 并行环境规模不等于环境构造方法；相关机制披露不足以进入核心表。

**开放边界：** 20,000 指并行环境数，不是任务类型数；Qwen Code 开源不代表完整环境集公开。

**来源证据**

- [primary-source-content](https://qwenlm.github.io/blog/qwen3-coder/) · 2026-10-08 · “Qwen3-Coder: Agentic Coding in the World”

## Kimi K3 Tech Blog: Open Frontier Intelligence — blog-kimi-k3

**[Kimi K3 Tech Blog: Open Frontier Intelligence](https://www.kimi.com/blog/kimi-k3)**

`blog` · `kimi-k3` · 日期未确认 · 技术报告

介绍 Kimi K3 的 Agent 能力与长时间 kernel 任务；环境机制详见技术报告章节。

**仅作背景，不计入入选目录：** 博客为能力概览；环境机制已通过技术报告的具体章节单列。

**开放边界：** 属于概览；环境构建细节以单列的报告章节为准。博客精确日期未确认。

同组资源：[Kimi K3 (report)](#kimi-k3--report-kimi-k3)

**来源证据**

- [primary-source-content](https://www.kimi.com/blog/kimi-k3) · 2026-10-08 · “Kimi K3 Tech Blog: Open Frontier Intelligence”

## MiMo-V2.6 — report-mimo-v26

**[MiMo-V2.6: Scaling Reinforcement Learning Towards Self-Improvement](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL/blob/73875d00b30a89ef8cc353a0b60b0e9f9561952d/MiMo_V2_6_technical_report.pdf)**

`report` · `xiaomi-mimo-rl-oss` · 日期未确认 · RL 实验

介绍跨领域环境与验证器构建、多 harness 执行，以及已发布环境上的实验。

**开放边界：** 公开任务子集与完整训练分布分开理解。PDF 固定到仓库版本；报告首次发布日期未确认。

**实现状态：** 部分／关联代码

[主页](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL) · [部分／关联代码](https://github.com/XiaomiMiMo/verl)

同组资源：[MiMo-V2.6 RL OSS Environments (XiaomiMiMo/verl) (project)](#mimo-v26-rl-oss-environments-xiaomimimoverl--project-xiaomi-mimo-verl) · [MiMo Agent (mimoagent) (project)](#mimo-agent-mimoagent--project-xiaomi-mimoagent)

[报告章节索引](technical_report_sections_zh.md#mimo-v26)

**来源证据**

- [pdf-sections-and-page-locations](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL/resolve/73875d00b30a89ef8cc353a0b60b0e9f9561952d/MiMo_V2_6_technical_report.pdf) · 2026-10-08 · “MiMo-V2.6: Scaling Reinforcement Learning Towards Self-Improvement”

## From model to agent: Equipping the Responses API with a computer environment — blog-openai-computer-env

**[From model to agent: Equipping the Responses API with a computer environment](https://openai.com/index/equip-responses-api-computer-environment/)**

`blog` · `openai-computer-env` · 2026-03-11 · 环境基础设施

介绍容器工作区、shell 执行、网络 sidecar、技能文件和上下文压缩，连接模型与有状态计算机环境。

**仅作背景，不计入入选目录：** 运行时工程细节有参考价值，但正文主要服务 API 执行，未展开环境／任务或交互数据生产。

**相关段落（原文标题／定位说明）：** 正文中的 computer environment、shell、skills 与 compaction 工程段落

**开放边界：** 这是运行时工程披露；未发布训练环境生成器或任务池。

**来源证据**

- [primary-source-content](https://openai.com/index/equip-responses-api-computer-environment/) · 2026-10-08 · “From model to agent”

## Introducing SWE-bench Verified — blog-openai-swe-verified

**[Introducing SWE-bench Verified](https://openai.com/index/introducing-swe-bench-verified/)**

`blog` · `swe-bench-verified` · 2024-08-13 · 评测环境

通过人工核查题意、测试有效性与可解性，筛选 SWE-bench 任务；配合 Docker 执行环境提高评测可靠性。

**支撑资料：** 为环境执行、评测、模拟或质量控制提供参考，但本次正文重点没有直接落在规模化环境生产或有效训练数据生产上，放回相应分类作支撑。

**文章研究问题：** 如何筛出有效的软件评测任务？

**具体内容**

- 人工检查题意与可解性
- 核对测试是否对应需求
- 用 Docker harness 执行筛选后的任务

**相关段落（原文标题／定位说明）：** SWE-bench Verified 的任务筛选与 evaluation harness 部分

**开放边界：** 评测子集构建，不是新增训练任务工厂；原文 2025-02-24 有更新。

**来源证据**

- [primary-source-content](https://openai.com/index/introducing-swe-bench-verified/) · 2026-10-08 · “Introducing SWE-bench Verified”

## Why SWE-bench Verified no longer measures frontier coding capabilities — blog-openai-swe-audit

**[Why SWE-bench Verified no longer measures frontier coding capabilities](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/)**

`blog` · `swe-bench-audit` · 2026-02-23 · 质量／失败研究

审计测试过窄、题意不足与基准污染，说明可执行测试并不自动构成可靠的任务验收器。

**支撑资料：** 为环境执行、评测、模拟或质量控制提供参考，但本次正文重点没有直接落在规模化环境生产或有效训练数据生产上，放回相应分类作支撑。

**文章研究问题：** 为什么可执行测试仍可能误判？

**具体内容**

- 分析过窄测试与题意缺失
- 审查困难任务子集
- 检查污染对测量结论的影响

**相关段落（原文标题／定位说明）：** 测试缺陷审计与 contamination 分析

**开放边界：** 重点分析抽取的困难任务；不能把子集缺陷比例当成整个基准的缺陷率。

**来源证据**

- [primary-source-content](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/) · 2026-10-08 · “Why SWE-bench Verified no longer measures frontier coding capabilities”

## PaperBench: Evaluating AI’s Ability to Replicate AI Research — blog-openai-paperbench

**[PaperBench: Evaluating AI’s Ability to Replicate AI Research](https://openai.com/index/paperbench/)**

`blog` · `paperbench` · 2025-04-02 · 评测环境

将论文复现分解成层级 rubric，与原作者共同定义评分任务，并单独评估自动评判器。

**支撑资料：** 为环境执行、评测、模拟或质量控制提供参考，但本次正文重点没有直接落在规模化环境生产或有效训练数据生产上，放回相应分类作支撑。

**文章研究问题：** 怎样把论文复现变为可评分任务？

**具体内容**

- 把复现目标拆成层级子任务
- 与论文作者共同制定 rubric
- 用单独基准检验自动 judge

**相关段落（原文标题／定位说明）：** 发布正文：任务分解、作者共建 rubric、judge benchmark

**开放边界：** 官方研究发布摘要；完整环境与评分细节需结合链接中的论文和代码。

**来源证据**

- [primary-source-content](https://openai.com/index/paperbench/) · 2026-10-08 · “Rubrics are co-developed with the author(s)”

## Introducing deep research — blog-openai-deep-research

**[Introducing deep research](https://openai.com/index/introducing-deep-research/)**

`blog` · `openai-deep-research` · 2025-02-02 · RL 实验

说明在困难浏览和推理任务上进行端到端 RL，使模型学习检索、使用 Python、回溯和调整搜索路线。

**仅作背景，不计入入选目录：** 说明使用浏览 RL，但未展开训练任务、环境状态或验收器如何构造。

**相关段落（原文标题／定位说明）：** How it works

**开放边界：** 披露训练任务形态；未开放任务分布、浏览环境构造器或奖励实现。

**来源证据**

- [primary-source-content](https://openai.com/index/introducing-deep-research/) · 2026-10-08 · “How it works”

## Introducing ChatGPT agent: bridging research and action — blog-openai-chatgpt-agent

**[Introducing ChatGPT agent: bridging research and action](https://openai.com/index/introducing-chatgpt-agent/)**

`blog` · `openai-chatgpt-agent` · 2025-07-17 · 技术报告

以共享虚拟计算机连接视觉浏览器、文本浏览器、终端与 API，跨工具保留文件和任务上下文。

**仅作背景，不计入入选目录：** 产品能力与共享虚拟电脑概览，缺少可供环境研究分析的构造和验收细节。

**相关段落（原文标题／定位说明）：** An agent that works for you, with you

**开放边界：** 作为历史环境设计材料；官网已标记此发布页过时，不据此描述当前产品入口或训练环境开放情况。

**来源证据**

- [primary-source-content](https://openai.com/index/introducing-chatgpt-agent/) · 2026-10-08 · “its own virtual computer”

## Scaling Managed Agents: Decoupling the brain from the hands — blog-anthropic-managed-agents

**[Scaling Managed Agents: Decoupling the brain from the hands](https://www.anthropic.com/engineering/managed-agents)**

`blog` · `anthropic-managed-agents` · 2026-04-08 · 环境基础设施

将持久会话日志、agent harness 与执行沙箱解耦，支持故障恢复和独立扩缩执行资源。

**仅作背景，不计入入选目录：** 重点是托管 agent 服务的架构拆分；与环境生产链路的联系间接。

**相关段落（原文标题／定位说明）：** 会话、harness 与 sandbox 解耦的架构段落

**开放边界：** 托管运行时架构，不是公开的 RL 任务生成系统。

**来源证据**

- [primary-source-content](https://www.anthropic.com/engineering/managed-agents) · 2026-10-08 · “Decoupling the brain from the hands”

## How we contain Claude across products — blog-anthropic-containment

**[How we contain Claude across products](https://www.anthropic.com/engineering/how-we-contain-claude)**

`blog` · `anthropic-containment` · 2026-05-25 · 环境基础设施

对比 gVisor、操作系统沙箱与完整 VM，并解释文件、网络和凭据的隔离边界。

**仅作背景，不计入入选目录：** 重点是生产产品的隔离边界；作为沙箱背景，不列为环境构建核心文章。

**相关段落（原文标题／定位说明）：** 各产品 containment 机制及文件、网络、凭据边界

**开放边界：** 生产环境隔离设计；不代表数据生成、训练任务或验证器已公开。

**来源证据**

- [primary-source-content](https://www.anthropic.com/engineering/how-we-contain-claude) · 2026-10-08 · “How we contain Claude across products”

## Petri: An open-source auditing tool to accelerate AI safety research — blog-anthropic-petri

**[Petri: An open-source auditing tool to accelerate AI safety research](https://www.anthropic.com/research/petri-open-source-auditing)**

`blog` · `petri` · 2025-10-06 · 环境／任务生成

从种子场景出发，审计 agent 构造多轮用户、工具与模拟环境交互，再由 judge 分析轨迹。

**支撑资料：** 为环境执行、评测、模拟或质量控制提供参考，但本次正文重点没有直接落在规模化环境生产或有效训练数据生产上，放回相应分类作支撑。

**文章研究问题：** 怎样合成可用于审计的交互场景？

**具体内容**

- 从种子场景生成多轮交互
- 模拟用户及工具响应
- 由 judge 检查交互轨迹

**相关段落（原文标题／定位说明）：** Petri 的 auditor、target 与 judge 工作流

**开放边界：** 开放审计工具；模型模拟的响应不等于真实应用的确定性状态转移。

同组资源：[Petri 2.0: New Scenarios, New Model Comparisons, and Improved Eval-Awareness Mitigations (blog)](#petri-20-new-scenarios-new-model-comparisons-and-improved-eval-awareness-mitigations--blog-anthropic-petri-v2)

**来源证据**

- [primary-source-content](https://www.anthropic.com/research/petri-open-source-auditing) · 2026-10-08 · “Petri (Parallel Exploration Tool for Risky Interactions)”

## Petri 2.0: New Scenarios, New Model Comparisons, and Improved Eval-Awareness Mitigations — blog-anthropic-petri-v2

**[Petri 2.0: New Scenarios, New Model Comparisons, and Improved Eval-Awareness Mitigations](https://alignment.anthropic.com/2026/petri-v2/)**

`blog` · `petri` · 2026-01-22 · 质量／失败研究

补充场景与真实性过滤，减少不可信工具输出和场景细节泄露“正在接受测试”的信号。

**支撑资料：** 为环境执行、评测、模拟或质量控制提供参考，但本次正文重点没有直接落在规模化环境生产或有效训练数据生产上，放回相应分类作支撑。

**文章研究问题：** 模拟环境如何减少不真实线索？

**具体内容**

- 加入新场景
- 过滤不可信工具响应
- 缓解被测模型识别评测场景的问题

**相关段落（原文标题／定位说明）：** realism mitigations 与 eval-awareness 分析

**开放边界：** 真实性分类器与评测感知缓解仍有误差；不能据此宣称模拟环境完全逼真。

同组资源：[Petri: An open-source auditing tool to accelerate AI safety research (blog)](#petri-an-open-source-auditing-tool-to-accelerate-ai-safety-research--blog-anthropic-petri)

**来源证据**

- [primary-source-content](https://alignment.anthropic.com/2026/petri-v2/) · 2026-10-08 · “Petri 2.0”

## Measuring and improving coding audit realism with deployment resources — blog-anthropic-petri-realism

**[Measuring and improving coding audit realism with deployment resources](https://alignment.anthropic.com/2026/coding-audit-realism/)**

`blog` · `petri-realism` · 2026-03-23 · 质量／失败研究

把真实部署提示、工具定义和代码库资源引入编码审计模拟，测量并改善生成场景的真实性。

**支撑资料：** 为环境执行、评测、模拟或质量控制提供参考，但本次正文重点没有直接落在规模化环境生产或有效训练数据生产上，放回相应分类作支撑。

**文章研究问题：** 如何把真实部署资源用于模拟？

**具体内容**

- 引入真实提示与工具定义
- 利用代码库资源约束场景
- 用 realism win rate 比较真实性

**相关段落（原文标题／定位说明）：** realism win rate 与 deployment resources 实验

**开放边界：** realism win rate 是模型判别指标，不能直接等同真实部署行为一致性。

**来源证据**

- [primary-source-content](https://alignment.anthropic.com/2026/coding-audit-realism/) · 2026-10-08 · “Measuring and improving coding audit realism”

## From shortcuts to sabotage: natural emergent misalignment from reward hacking — blog-anthropic-reward-hacking

**[From shortcuts to sabotage: natural emergent misalignment from reward hacking](https://www.anthropic.com/research/emergent-misalignment-reward-hacking)**

`blog` · `anthropic-emergent-misalignment` · 2025-11-21 · 质量／失败研究

在含可投机缺陷的编码 RL 环境中研究奖励攻击，以及其向其他任务行为的泛化。

**支撑资料：** 为环境执行、评测、模拟或质量控制提供参考，但本次正文重点没有直接落在规模化环境生产或有效训练数据生产上，放回相应分类作支撑。

**文章研究问题：** 不可靠奖励会怎样改变学习结果？

**具体内容**

- 构造可被投机利用的编码 RL 设置
- 观察模型对奖励漏洞的利用
- 测量向其他任务的行为泛化

**相关段落（原文标题／定位说明）：** 编码 RL 训练设置、奖励投机与泛化结果

**开放边界：** 受控研究设置；不应描述成通常部署模型的必然行为，也不等于环境工具包开放。

**来源证据**

- [primary-source-content](https://www.anthropic.com/research/emergent-misalignment-reward-hacking) · 2026-10-08 · “natural emergent misalignment from reward hacking”

## Effective harnesses for long-running agents — blog-anthropic-long-running

**[Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)**

`blog` · `anthropic-long-running` · 2025-11-26 · 技术报告

用初始化脚本、功能清单、进度日志和 Git 状态恢复跨会话工作区，再通过浏览器端到端测试验收。

**仅作背景，不计入入选目录：** 重点是长期 coding agent 的工作流与跨会话恢复，属于相邻的 harness 工程。

**相关段落（原文标题／定位说明）：** Initializer agent、Coding agent 与环境测试相关段落

**开放边界：** 纳入的是环境初始化、状态恢复和验收机制；并非通用环境合成方法。

**来源证据**

- [primary-source-content](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) · 2026-10-08 · “Effective harnesses for long-running agents”

## The Building Blocks of Agentic AI: From Kernels to Clusters — blog-meta-openenv

**[The Building Blocks of Agentic AI: From Kernels to Clusters](https://ai.meta.com/blog/introducing-pytorch-native-agentic-stack/)**

`blog` · `openenv` · 2025-10-24 · 环境基础设施

OpenEnv 小节介绍共享环境 Hub、工具／观测接口，以及训练前由人或模型直接交互验证环境。

**支撑资料：** 为环境执行、评测、模拟或质量控制提供参考，但本次正文重点没有直接落在规模化环境生产或有效训练数据生产上，放回相应分类作支撑。

**文章研究问题：** 怎样统一环境接口并先验证环境？

**具体内容**

- 定义工具与观测接口
- 共享兼容环境的 Hub
- 允许人或模型在训练前交互检查

**相关段落（原文标题／定位说明）：** OpenEnv (An Open Hub and Spec for RL Environments)

**开放边界：** 对应 OpenEnv 0.1 RFC 发布时点；文章其余 PyTorch 组件不是环境生成器。

同组资源：[The Open Source Community is backing OpenEnv for Agentic RL (blog)](#the-open-source-community-is-backing-openenv-for-agentic-rl--blog-openenv-community) · [Building the Open Agent Ecosystem Together: Introducing OpenEnv (blog)](#building-the-open-agent-ecosystem-together-introducing-openenv--blog-openenv-launch) · [Scaling OpenEnv: From Free Usage to Thousands of Concurrent Environments (blog)](#scaling-openenv-from-free-usage-to-thousands-of-concurrent-environments--blog-openenv-scaling) · [Training a coding agent using the OpenCode harness in remote HF sandboxes with TRL and OpenEnv (blog)](#training-a-coding-agent-using-the-opencode-harness-in-remote-hf-sandboxes-with-trl-and-openenv--blog-trl-openenv) · [OpenEnv (project)](#openenv--project-openenv)

**来源证据**

- [primary-source-content](https://ai.meta.com/blog/introducing-pytorch-native-agentic-stack/) · 2026-10-08 · “OpenEnv (An Open Hub and Spec for RL Environments)”

## Introducing Grok 4.6 — blog-xai-grok46

**[Introducing Grok 4.6](https://x.ai/news/grok-4-6)**

`blog` · `grok46` · 2026-08-12 · RL 与 SFT 实验

介绍跨 harness 重新生成和筛选 SFT 轨迹，并在知识工作、代码、kernel 优化、Web 与 CAD 环境中开展 RL。

**仅作背景，不计入入选目录：** 只披露轨迹再生成和任务领域，缺少环境、任务生成与验证实现细节。

**相关段落（原文标题／定位说明）：** Training Grok 4.6

**开放边界：** 只有任务域与训练流程披露；未给出环境构造器、任务池或验证器实现。

**来源证据**

- [primary-source-content](https://x.ai/news/grok-4-6) · 2026-10-08 · “Training Grok 4.6”

## How to Run an Autoresearch Workflow with RL Agent Skills and NVIDIA NeMo — blog-nvidia-autoresearch-env

**[How to Run an Autoresearch Workflow with RL Agent Skills and NVIDIA NeMo](https://developer.nvidia.com/blog/how-to-run-an-autoresearch-workflow-with-rl-agent-skills-and-nvidia-nemo/)**

`blog` · `nvidia-autoresearch-env` · 2026-07-14 · 环境／任务生成

展示 agent 从零实现星形计数环境，按颜色与画布尺寸合成数据，再连接 NeMo 训练与实验记录。

**文章研究问题：** 如何让 agent 造环境并产合成数据？

**具体内容**

- 实现星形计数环境
- 按颜色与画布尺寸生成图像任务
- 把生成样本接入 SFT 实验

**相关段落（原文标题／定位说明）：** Step 7: 创建 star count 环境；Step 8: SFT campaign

**开放边界：** 该计数示例实际使用 SFT；不能因标题含 RL 就写成新环境上的 RL 实验。

**来源证据**

- [primary-source-content](https://developer.nvidia.com/blog/how-to-run-an-autoresearch-workflow-with-rl-agent-skills-and-nvidia-nemo/) · 2026-10-08 · “star count”

## Mastering Agentic Techniques: AI Agent Reinforcement Learning — blog-nvidia-agent-rl

**[Mastering Agentic Techniques: AI Agent Reinforcement Learning](https://developer.nvidia.com/blog/mastering-agentic-techniques-ai-agent-reinforcement-learning/)**

`blog` · `nemo-gym` · 2026-07-01 · 环境基础设施

连接任务定义、可验证奖励、工具调用环境与 NeMo rollout，讨论将失败行为变为回归测试。

**仅作背景，不计入入选目录：** 通用 RL 方法教程，具体示例较简化；与更直接的 NeMo 环境文章重叠。

**相关段落（原文标题／定位说明）：** A practical first RL training run is small, verifiable and inspectable

**开放边界：** 方法教程与示例；不能将文中简化的单步工具任务泛化成完整企业环境。

同组资源：[How to Train Scientific Agents with Reinforcement Learning (blog)](#how-to-train-scientific-agents-with-reinforcement-learning--blog-nemo-science) · [NeMo Gym (project)](#nemo-gym--project-nemo-gym)

**来源证据**

- [primary-source-content](https://developer.nvidia.com/blog/mastering-agentic-techniques-ai-agent-reinforcement-learning/) · 2026-10-08 · “Verifiable reward environments, rollouts, and evaluation”

## DeepSWE: Training a Fully Open-sourced, State-of-the-Art Coding Agent by Scaling RL — blog-together-deepswe

**[DeepSWE: Training a Fully Open-sourced, State-of-the-Art Coding Agent by Scaling RL](https://www.together.ai/blog/deepswe)**

`blog` · `deepswe` · 2025-07-02 · RL 实验

说明在 R2E-Gym 仓库任务和 Docker 工具环境中进行编码 RL，并通过可执行测试提供奖励。

**文章研究问题：** 已有仓库环境怎样用于在线训练？

**具体内容**

- 在 R2E-Gym 任务中执行工具动作
- 通过 Docker 提供仓库工作区
- 由可执行测试提供 RL 奖励

**相关段落（原文标题／定位说明）：** R2E-Gym 任务环境、训练设置与奖励相关段落

**开放边界：** 是已有环境上的训练配方；不将 DeepSWE 视作独立的新环境合成器。

**来源证据**

- [primary-source-content](https://www.together.ai/blog/deepswe) · 2026-10-08 · “DeepSWE-Preview”

## Introducing SWE-1.5: Our Fast Agent Model — blog-cognition-swe15

**[Introducing SWE-1.5: Our Fast Agent Model](https://cognition.com/blog/swe-1-5)**

`blog` · `swe15` · 2025-10-29 · RL 实验

披露在 Cascade harness 下执行真实任务 RL，并用 otterlink VM 支持代码执行、浏览和高并发，贴近 Devin 生产环境。

**支撑资料：** 为环境执行、评测、模拟或质量控制提供参考，但本次正文重点没有直接落在规模化环境生产或有效训练数据生产上，放回相应分类作支撑。

**文章研究问题：** 怎样让 rollout 环境贴近生产？

**具体内容**

- 使用 Cascade 执行真实任务
- VM 支持代码执行和网页浏览
- 通过 otterlink 扩展并发环境

**相关段落（原文标题／定位说明）：** The Agent-Model Interface；RL rollout 高保真环境与 otterlink 段落

**开放边界：** 机制披露；不等于训练任务、VM 平台或环境构建流水线完整开放。

**来源证据**

- [primary-source-content](https://cognition.com/blog/swe-1-5) · 2026-10-08 · “high-fidelity environments with code execution”

## Custom reward functions for multi-turn reinforcement learning with Amazon Nova Forge — blog-aws-nova-rewards

**[Custom reward functions for multi-turn reinforcement learning with Amazon Nova Forge](https://aws.amazon.com/blogs/machine-learning/custom-reward-functions-for-multi-turn-reinforcement-learning-with-amazon-nova-forge/)**

`blog` · `nova-forge-environments` · 2026-08-14 · 环境基础设施

BYOO 容器管理多轮状态、用户模拟、代码执行和 verifier，再将完整 episode 与聚合奖励送回训练。

**支撑资料：** 为环境执行、评测、模拟或质量控制提供参考，但本次正文重点没有直接落在规模化环境生产或有效训练数据生产上，放回相应分类作支撑。

**文章研究问题：** 多轮环境如何维护状态并返回奖励？

**具体内容**

- BYOO 容器管理多轮状态
- 执行用户模拟、工具或 verifier
- 返回完整 episode 与聚合奖励

**相关段落（原文标题／定位说明）：** Building custom rewards with Amazon Nova Forge；BYOO 环境容器

**开放边界：** 云服务教程与示例；使用依赖 Nova Forge 权限和 AWS 资源，不是离线即用的通用环境库。

同组资源：[Deploying Multi-Turn RL Infrastructure for Amazon Nova on Amazon SageMaker HyperPod (blog)](#deploying-multi-turn-rl-infrastructure-for-amazon-nova-on-amazon-sagemaker-hyperpod--blog-aws-nova-infra)

**来源证据**

- [primary-source-content](https://aws.amazon.com/blogs/machine-learning/custom-reward-functions-for-multi-turn-reinforcement-learning-with-amazon-nova-forge/) · 2026-10-08 · “Building custom rewards with Amazon Nova Forge”

## Deploying Multi-Turn RL Infrastructure for Amazon Nova on Amazon SageMaker HyperPod — blog-aws-nova-infra

**[Deploying Multi-Turn RL Infrastructure for Amazon Nova on Amazon SageMaker HyperPod](https://aws.amazon.com/blogs/machine-learning/deploying-multi-turn-rl-infrastructure-for-amazon-nova-on-amazon-sagemaker-hyperpod/)**

`blog` · `nova-forge-environments` · 2026-07-06 · 环境基础设施

以 Wordle 为例分离 HyperPod 训练、ECS 奖励环境和有状态消息路由，并管理每轮训练的临时资源。

**支撑资料：** 为环境执行、评测、模拟或质量控制提供参考，但本次正文重点没有直接落在规模化环境生产或有效训练数据生产上，放回相应分类作支撑。

**文章研究问题：** 如何编排批量有状态环境？

**具体内容**

- 分离训练与 ECS 奖励环境
- 通过代理层路由多轮消息
- 以 Wordle 展示每次运行的资源生命周期

**相关段落（原文标题／定位说明）：** Solution overview；ECS on Fargate；Nova Forge proxy layer

**开放边界：** Wordle 是替换为自定义任务的示例；不证明企业任务已自动生成。

同组资源：[Custom reward functions for multi-turn reinforcement learning with Amazon Nova Forge (blog)](#custom-reward-functions-for-multi-turn-reinforcement-learning-with-amazon-nova-forge--blog-aws-nova-rewards)

**来源证据**

- [primary-source-content](https://aws.amazon.com/blogs/machine-learning/deploying-multi-turn-rl-infrastructure-for-amazon-nova-on-amazon-sagemaker-hyperpod/) · 2026-10-08 · “Solution overview”

## Magentic Marketplace: an open-source simulation environment for studying agentic markets — blog-microsoft-marketplace

**[Magentic Marketplace: an open-source simulation environment for studying agentic markets](https://www.microsoft.com/en-us/research/blog/magentic-marketplace-an-open-source-simulation-environment-for-studying-agentic-markets/)**

`blog` · `magentic-marketplace` · 2025-11-05 · 评测环境

用共享 REST 环境承载买卖方 agent 的发现、沟通和模拟交易；合成市场数据支持可重复的行为实验。

**支撑资料：** 为环境执行、评测、模拟或质量控制提供参考，但本次正文重点没有直接落在规模化环境生产或有效训练数据生产上，放回相应分类作支撑。

**文章研究问题：** 如何构建可控的业务交互世界？

**具体内容**

- 共享 REST 服务维护市场状态
- 买卖方进行发现、沟通与模拟交易
- 用合成市场数据开展可重复实验

**相关段落（原文标题／定位说明）：** 环境架构三项设计；Setting up the experiments

**开放边界：** 这是模拟市场与评测研究，不是真实支付系统，也不以训练结果为收录前提。

**来源证据**

- [primary-source-content](https://www.microsoft.com/en-us/research/blog/magentic-marketplace-an-open-source-simulation-environment-for-studying-agentic-markets/) · 2026-10-08 · “HTTP/REST client-server architecture”

## Genie 2: A large-scale foundation world model — blog-deepmind-genie2

**[Genie 2: A large-scale foundation world model](https://deepmind.google/blog/genie-2-a-large-scale-foundation-world-model/)**

`blog` · `deepmind-genie2` · 2024-12-04 · 环境／任务生成

由单张图生成可响应键鼠动作的交互世界，并从同一起始帧产生不同动作轨迹，服务 agent 训练与评测。

**支撑资料：** 为环境执行、评测、模拟或质量控制提供参考，但本次正文重点没有直接落在规模化环境生产或有效训练数据生产上，放回相应分类作支撑。

**文章研究问题：** 如何由图像生成动作条件世界？

**具体内容**

- 单张图定义起始场景
- 键鼠动作驱动后续观测
- 同一初始帧生成不同动作轨迹

**相关段落（原文标题／定位说明）：** Action controls；Generating counterfactuals；Long horizon memory

**开放边界：** 学习式模拟存在一致性与时长限制；不能当作确定性引擎或已开放的完整训练平台。

**来源证据**

- [primary-source-content](https://deepmind.google/blog/genie-2-a-large-scale-foundation-world-model/) · 2026-10-08 · “Generating counterfactuals”

## Designing a world-class code execution environment — blog-poolside-code-env

**[Designing a world-class code execution environment](https://poolside.ai/blog/designing-a-world-class-code-execution-environment)**

`blog` · `poolside-code-env` · 2025-08-12 · 技术报告

通过 Saucer 管理仓库版本，用 agent 辅助构建容器镜像，分层复用不同 revision，并大规模运行隔离代码执行反馈。

**文章研究问题：** 怎样把真实仓库变成可执行环境？

**具体内容**

- 用 Saucer 管理仓库修订
- agent 辅助构建可运行镜像
- 分层复用 revision 并执行隔离代码反馈

**相关段落（原文标题／定位说明）：** Saucer；Building images；Handling revisions；Handling execution

**开放边界：** 详细工程披露；不能由文章推断 Saucer、镜像库或完整 RLCEF 平台已开源。

**来源证据**

- [primary-source-content](https://poolside.ai/blog/designing-a-world-class-code-execution-environment) · 2026-10-08 · “Building images”

## Introducing Beam: Reflection’s 501B open-weight model — blog-reflection-beam-env

**[Introducing Beam: Reflection’s 501B open-weight model](https://reflection.ai/blog/introducing-beam)**

`blog` · `reflection-beam` · 2026-10-05 · RL 实验

描述合成、供应商与开源任务来源，按难度及题意、可投机性过滤，再用 RL 暴露问题并迭代环境池；另讨论沙箱与评分基础设施。

**文章研究问题：** 怎样迭代高质量、有难度的环境池？

**具体内容**

- 结合合成、供应商与开源任务
- 过滤过易、不可解、含糊或可投机任务
- 用 RL 发现问题并更新筛选策略

**相关段落（原文标题／定位说明）：** Scaling reinforcement learning environments；Frontier RL infrastructure

**开放边界：** 发布文称权重与报告将在当月稍后发布；截至该文并非全部已开放，更未证明环境池和生成器开放。

**来源证据**

- [primary-source-content](https://reflection.ai/blog/introducing-beam) · 2026-10-08 · “Scaling reinforcement learning environments”

## Introducing North Mini Code: Cohere’s First Model For Developers — blog-cohere-north-mini-code

**[Introducing North Mini Code: Cohere’s First Model For Developers](https://huggingface.co/blog/CohereLabs/introducing-north-mini-code)**

`blog` · `north-mini-code` · 2026-06-09 · RL 与 SFT 实验

介绍容器化仓库与终端任务：将合成 SFT 数据和 RLVR 使用的环境分开，并按仓库来源去重以减少评测泄漏。

**文章研究问题：** 如何组织环境以生产不同训练数据？

**具体内容**

- 仓库与终端任务容器化
- SFT 合成与 RLVR 使用不相交环境子集
- 按仓库来源去重以减少评测泄漏

**相关段落（原文标题／定位说明）：** Post-Training for Coding Excellence；Robustness Across Harnesses

**开放边界：** Cohere 官方团队在 Hugging Face 发布；模型开放不代表全部内部环境与数据流水线开放。

**来源证据**

- [primary-source-content](https://huggingface.co/blog/CohereLabs/introducing-north-mini-code) · 2026-10-08 · “containerised agentic coding environments”
