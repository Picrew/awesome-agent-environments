# 公司文章：主题相关性与取舍

[返回目录](../README_zh.md) · [完整来源证据](catalog_details_zh.md)

公司是检索线索。当前前置主线收敛为大规模构建高质量环境，以及从环境和内容生产有效训练数据；执行、一般评测、泛模拟等作为支撑。以下分层是本目录的编辑判断，不是对文章本身质量的评价。

此前 38 篇公司文章分为：7 篇主线文章、19 篇分类支撑、12 篇背景资料。当前主目录 206 条入选资源；完整证据库保留 218 条记录，背景资料不计入主目录。

[研究主张与实验设想](research_focus_zh.md)

## 核心主题与具体内容

### 主线一：大规模构建高质量环境

怎样从内容、技能、需求与真实软件中，低成本生产大量可执行、可验证、有差异且难度合适的环境与任务？

| 文章／机构 | 核心问题 | 具体内容 | 原文位置 |
| --- | --- | --- | --- |
| [Designing a world-class code execution environment](https://poolside.ai/blog/designing-a-world-class-code-execution-environment) · Poolside | 怎样把真实仓库变成可执行环境？ | 用 Saucer 管理仓库修订；agent 辅助构建可运行镜像；分层复用 revision 并执行隔离代码反馈 | Saucer；Building images；Handling revisions；Handling execution |
| [Introducing Beam: Reflection’s 501B open-weight model](https://reflection.ai/blog/introducing-beam) · Reflection | 怎样迭代高质量、有难度的环境池？ | 结合合成、供应商与开源任务；过滤过易、不可解、含糊或可投机任务；用 RL 发现问题并更新筛选策略 | Scaling reinforcement learning environments；Frontier RL infrastructure |

### 主线二：从环境与内容合成有效训练数据

怎样从环境和内容中构造任务、采集与筛选轨迹，服务 SFT 或 RL，并在独立任务上验证模型是否学得更好？

| 文章／机构 | 核心问题 | 具体内容 | 原文位置 |
| --- | --- | --- | --- |
| [CoderForge-Preview](https://www.together.ai/blog/coderforge-preview) · Together AI | 如何由仓库任务生产训练轨迹？ | 以可执行仓库任务承载交互；用测试验证代码轨迹；发布轨迹并用于微调 | 按正文中的上述机制段落定位；详见来源证据 |
| [A technical report on Composer 2](https://cursor.com/blog/composer-2-technical-report) · Cursor | 如何执行贴近部署的训练任务？ | 真实工具会话中的多步任务；沙箱支持并发执行；将执行反馈接入异步 RL | 按正文中的上述机制段落定位；详见来源证据 |
| [How to Run an Autoresearch Workflow with RL Agent Skills and NVIDIA NeMo](https://developer.nvidia.com/blog/how-to-run-an-autoresearch-workflow-with-rl-agent-skills-and-nvidia-nemo/) · NVIDIA | 如何让 agent 造环境并产合成数据？ | 实现星形计数环境；按颜色与画布尺寸生成图像任务；把生成样本接入 SFT 实验 | Step 7: 创建 star count 环境；Step 8: SFT campaign |
| [DeepSWE: Training a Fully Open-sourced, State-of-the-Art Coding Agent by Scaling RL](https://www.together.ai/blog/deepswe) · Together AI | 已有仓库环境怎样用于在线训练？ | 在 R2E-Gym 任务中执行工具动作；通过 Docker 提供仓库工作区；由可执行测试提供 RL 奖励 | R2E-Gym 任务环境、训练设置与奖励相关段落 |
| [Introducing North Mini Code: Cohere’s First Model For Developers](https://huggingface.co/blog/CohereLabs/introducing-north-mini-code) · Cohere Labs | 如何组织环境以生产不同训练数据？ | 仓库与终端任务容器化；SFT 合成与 RLVR 使用不相交环境子集；按仓库来源去重以减少评测泄漏 | Post-Training for Coding Excellence；Robustness Across Harnesses |

## 分类支撑材料

保留在原有分类表中，可按实现或评测需要查阅；不再与两条生产主线并列。

| 文章 | 机构 | 定位 |
| --- | --- | --- |
| [How to Train Scientific Agents with Reinforcement Learning](https://developer.nvidia.com/blog/how-to-train-scientific-agents-with-reinforcement-learning/) | NVIDIA / Edison Scientific | 为环境执行、评测、模拟或质量控制提供参考，但本次正文重点没有直接落在规模化环境生产或有效训练数据生产上，放回相应分类作支撑。 |
| [Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) | Anthropic | 为环境执行、评测、模拟或质量控制提供参考，但本次正文重点没有直接落在规模化环境生产或有效训练数据生产上，放回相应分类作支撑。 |
| [Quantifying infrastructure noise in agentic coding evals](https://www.anthropic.com/engineering/infrastructure-noise) | Anthropic | 为环境执行、评测、模拟或质量控制提供参考，但本次正文重点没有直接落在规模化环境生产或有效训练数据生产上，放回相应分类作支撑。 |
| [Training a Misaligned Reward Seeker](https://alignment.anthropic.com/2026/reward-seeker/) | Anthropic | 为环境执行、评测、模拟或质量控制提供参考，但本次正文重点没有直接落在规模化环境生产或有效训练数据生产上，放回相应分类作支撑。 |
| [Genie 3: A new frontier for world models](https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/) | Google DeepMind | 为环境执行、评测、模拟或质量控制提供参考，但本次正文重点没有直接落在规模化环境生产或有效训练数据生产上，放回相应分类作支撑。 |
| [SIMA 2: An agent that plays, reasons, and learns with you in virtual 3D worlds](https://deepmind.google/blog/sima-2-an-agent-that-plays-reasons-and-learns-with-you-in-virtual-3d-worlds/) | Google DeepMind | 为环境执行、评测、模拟或质量控制提供参考，但本次正文重点没有直接落在规模化环境生产或有效训练数据生产上，放回相应分类作支撑。 |
| [Introducing SWE-bench Verified](https://openai.com/index/introducing-swe-bench-verified/) | OpenAI | 为环境执行、评测、模拟或质量控制提供参考，但本次正文重点没有直接落在规模化环境生产或有效训练数据生产上，放回相应分类作支撑。 |
| [Why SWE-bench Verified no longer measures frontier coding capabilities](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/) | OpenAI | 为环境执行、评测、模拟或质量控制提供参考，但本次正文重点没有直接落在规模化环境生产或有效训练数据生产上，放回相应分类作支撑。 |
| [PaperBench: Evaluating AI’s Ability to Replicate AI Research](https://openai.com/index/paperbench/) | OpenAI | 为环境执行、评测、模拟或质量控制提供参考，但本次正文重点没有直接落在规模化环境生产或有效训练数据生产上，放回相应分类作支撑。 |
| [Petri: An open-source auditing tool to accelerate AI safety research](https://www.anthropic.com/research/petri-open-source-auditing) | Anthropic | 为环境执行、评测、模拟或质量控制提供参考，但本次正文重点没有直接落在规模化环境生产或有效训练数据生产上，放回相应分类作支撑。 |
| [Petri 2.0: New Scenarios, New Model Comparisons, and Improved Eval-Awareness Mitigations](https://alignment.anthropic.com/2026/petri-v2/) | Anthropic | 为环境执行、评测、模拟或质量控制提供参考，但本次正文重点没有直接落在规模化环境生产或有效训练数据生产上，放回相应分类作支撑。 |
| [Measuring and improving coding audit realism with deployment resources](https://alignment.anthropic.com/2026/coding-audit-realism/) | Anthropic | 为环境执行、评测、模拟或质量控制提供参考，但本次正文重点没有直接落在规模化环境生产或有效训练数据生产上，放回相应分类作支撑。 |
| [From shortcuts to sabotage: natural emergent misalignment from reward hacking](https://www.anthropic.com/research/emergent-misalignment-reward-hacking) | Anthropic | 为环境执行、评测、模拟或质量控制提供参考，但本次正文重点没有直接落在规模化环境生产或有效训练数据生产上，放回相应分类作支撑。 |
| [The Building Blocks of Agentic AI: From Kernels to Clusters](https://ai.meta.com/blog/introducing-pytorch-native-agentic-stack/) | Meta | 为环境执行、评测、模拟或质量控制提供参考，但本次正文重点没有直接落在规模化环境生产或有效训练数据生产上，放回相应分类作支撑。 |
| [Introducing SWE-1.5: Our Fast Agent Model](https://cognition.com/blog/swe-1-5) | Cognition | 为环境执行、评测、模拟或质量控制提供参考，但本次正文重点没有直接落在规模化环境生产或有效训练数据生产上，放回相应分类作支撑。 |
| [Custom reward functions for multi-turn reinforcement learning with Amazon Nova Forge](https://aws.amazon.com/blogs/machine-learning/custom-reward-functions-for-multi-turn-reinforcement-learning-with-amazon-nova-forge/) | Amazon / AWS | 为环境执行、评测、模拟或质量控制提供参考，但本次正文重点没有直接落在规模化环境生产或有效训练数据生产上，放回相应分类作支撑。 |
| [Deploying Multi-Turn RL Infrastructure for Amazon Nova on Amazon SageMaker HyperPod](https://aws.amazon.com/blogs/machine-learning/deploying-multi-turn-rl-infrastructure-for-amazon-nova-on-amazon-sagemaker-hyperpod/) | Amazon / AWS | 为环境执行、评测、模拟或质量控制提供参考，但本次正文重点没有直接落在规模化环境生产或有效训练数据生产上，放回相应分类作支撑。 |
| [Magentic Marketplace: an open-source simulation environment for studying agentic markets](https://www.microsoft.com/en-us/research/blog/magentic-marketplace-an-open-source-simulation-environment-for-studying-agentic-markets/) | Microsoft Research | 为环境执行、评测、模拟或质量控制提供参考，但本次正文重点没有直接落在规模化环境生产或有效训练数据生产上，放回相应分类作支撑。 |
| [Genie 2: A large-scale foundation world model](https://deepmind.google/blog/genie-2-a-large-scale-foundation-world-model/) | Google DeepMind | 为环境执行、评测、模拟或质量控制提供参考，但本次正文重点没有直接落在规模化环境生产或有效训练数据生产上，放回相应分类作支撑。 |

## 相邻背景资料

这些页面保留来源、摘要与核验记录，但从主目录及公司核心表移出。模型报告中有独立环境机制的章节仍按原位置保留，例如 Kimi K3。

| 文章 | 机构 | 未进入核心表的原因 |
| --- | --- | --- |
| [Introducing Codex](https://openai.com/index/introducing-codex/) | OpenAI | 编码产品与训练概览；未充分展开环境构造、任务采样或奖励实现。 |
| [Computer-Using Agent](https://openai.com/index/computer-using-agent/) | OpenAI | 主要讲计算机使用模型及观测／动作方式；环境生产机制披露有限。 |
| [Qwen3-Coder: Agentic Coding in the World](https://qwenlm.github.io/blog/qwen3-coder/) | Qwen | 并行环境规模不等于环境构造方法；相关机制披露不足以进入核心表。 |
| [Kimi K3 Tech Blog: Open Frontier Intelligence](https://www.kimi.com/blog/kimi-k3) | Moonshot AI | 博客为能力概览；环境机制已通过技术报告的具体章节单列。 |
| [From model to agent: Equipping the Responses API with a computer environment](https://openai.com/index/equip-responses-api-computer-environment/) | OpenAI | 运行时工程细节有参考价值，但正文主要服务 API 执行，未展开环境／任务或交互数据生产。 |
| [Introducing deep research](https://openai.com/index/introducing-deep-research/) | OpenAI | 说明使用浏览 RL，但未展开训练任务、环境状态或验收器如何构造。 |
| [Introducing ChatGPT agent: bridging research and action](https://openai.com/index/introducing-chatgpt-agent/) | OpenAI | 产品能力与共享虚拟电脑概览，缺少可供环境研究分析的构造和验收细节。 |
| [Scaling Managed Agents: Decoupling the brain from the hands](https://www.anthropic.com/engineering/managed-agents) | Anthropic | 重点是托管 agent 服务的架构拆分；与环境生产链路的联系间接。 |
| [How we contain Claude across products](https://www.anthropic.com/engineering/how-we-contain-claude) | Anthropic | 重点是生产产品的隔离边界；作为沙箱背景，不列为环境构建核心文章。 |
| [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) | Anthropic | 重点是长期 coding agent 的工作流与跨会话恢复，属于相邻的 harness 工程。 |
| [Introducing Grok 4.6](https://x.ai/news/grok-4-6) | xAI / SpaceXAI | 只披露轨迹再生成和任务领域，缺少环境、任务生成与验证实现细节。 |
| [Mastering Agentic Techniques: AI Agent Reinforcement Learning](https://developer.nvidia.com/blog/mastering-agentic-techniques-ai-agent-reinforcement-learning/) | NVIDIA | 通用 RL 方法教程，具体示例较简化；与更直接的 NeMo 环境文章重叠。 |

## 判定规则

主线文章需要直接回答规模化环境生产或训练数据生产中的具体问题。环境质量研究若与生产、筛选、修复和迭代直接相连，可以进入主线；仅解释通用评测、接口或隔离机制的文章保留为支撑。只列使用领域、模型能力、环境数量或通用服务架构，不足以进入主线。

只使用现成环境训练也可以相关，但必须讲清环境中的执行、反馈或数据生产过程，并明确“使用环境”与“构造环境”的区别。运行基础设施可以入选，但需要直接解释任务／rollout 的状态、隔离、反馈或批量执行，而非泛泛讨论 agent 服务。

文章是否开源与主题相关性是两条独立判断：私有环境的具体构造机制可以研究；开放模型或运行客户端也不能自动算作开放环境。日期、版本、章节和发布边界保留在各条详情。
