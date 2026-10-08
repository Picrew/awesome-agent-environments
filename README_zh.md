# Awesome Agent Environments

系统化收录 AI Agent 环境构建与训练数据合成的研究进展。关注两个核心问题：如何规模化生产高质量环境？如何从环境中提取有效的训练数据？

[English](README.md) | [中文](README_zh.md)

**129 组工作 · 84 篇论文 · 4 篇模型报告 · 50 篇博客 · 68 个 GitHub 项目**

快照：**2026-10-08**。覆盖环境构建、任务合成、交互数据、训练与评测。

另有 12 篇相邻背景文章单独保留，不计入上述数量。

## 两条核心研究主线

| 主题 | 核心问题 |
| --- | --- |
| 主线一：规模化生产高质量环境 | 如何从内容、技能、需求与真实软件中，低成本生产大量可执行、可验证、有差异且难度合适的环境与任务？ |
| 主线二：合成有效的训练数据 | 如何从环境和内容中构造任务、采集与筛选轨迹，用于 SFT 或 RL 训练，并在独立任务上验证模型提升？ |

**研究链路**：内容/技能/仓库 → 环境与任务生成 → 质量验收 → 交互采样与筛选 → SFT 或 RL → 独立评测 → 反馈优化生成策略。

重点是环境生产与数据生产。接口、沙箱、静态基准作为支撑；只有直接解释生产机制或质量保障时才列为重点。

SFT 使用筛选后的示范轨迹；在线 RL 还需要可采样任务分布、可执行环境和可靠奖励。生成得更多、验证通过更多，不等于训练效果更好 —— 需要独立的实验验证。

[研究重点与实验设想](docs/research_focus_zh.md)

## 模型公司文章：按环境贡献归类

这里只收录直接讨论规模化环境生产或训练数据生产的文章。一般性接口、评测和运行设施回到下方分类。

[文章筛选逻辑与背景资料](docs/north_american_company_blogs.md)

### 主线一：规模化生产高质量环境

如何从内容、技能、需求与真实软件中，低成本生产大量可执行、可验证、有差异且难度合适的环境与任务？

| 文章/机构 | 核心问题 | 核心内容 | 日期 | 说明 |
| --- | --- | --- | --- | --- |
| [Introducing Beam: Reflection's 501B open-weight model](https://reflection.ai/blog/introducing-beam) · Reflection | 如何迭代高质量、有难度的环境池？ | 结合合成、供应商与开源任务；过滤过易、不可解、含糊或可投机任务；用 RL 发现问题并更新筛选策略 | 2026-10-05 | 发布文提到权重与报告将在当月稍后发布；截至该文并非全部已开放，环境池和生成器开放情况未明确。[详情](docs/catalog_details_zh.md#introducing-beam-reflections-501b-open-weight-model--blog-reflection-beam-env) |
| [Designing a world-class code execution environment](https://poolside.ai/blog/designing-a-world-class-code-execution-environment) · Poolside | 如何把真实仓库变成可执行环境？ | 用 Saucer 管理仓库修订；agent 辅助构建可运行镜像；分层复用 revision 并执行隔离代码反馈 | 2025-08-12 | 详细的工程披露；文章未说明 Saucer、镜像库或完整 RLCEF 平台是否已开源。[详情](docs/catalog_details_zh.md#designing-a-world-class-code-execution-environment--blog-poolside-code-env) |

### 主线二：合成有效的训练数据

如何从环境和内容中构造任务、采集与筛选轨迹，用于 SFT 或 RL 训练，并在独立任务上验证模型提升？

| 文章/机构 | 核心问题 | 核心内容 | 日期 | 说明 |
| --- | --- | --- | --- | --- |
| [How to Run an Autoresearch Workflow with RL Agent Skills and NVIDIA NeMo](https://developer.nvidia.com/blog/how-to-run-an-autoresearch-workflow-with-rl-agent-skills-and-nvidia-nemo/) · NVIDIA | 如何让 agent 构建环境并生成合成数据？ | 实现星形计数环境；按颜色与画布尺寸生成图像任务；把生成样本接入 SFT 实验 | 2026-07-14 | 该计数示例实际使用 SFT；不要因标题含 RL 就理解为新环境上的 RL 实验。[详情](docs/catalog_details_zh.md#how-to-run-an-autoresearch-workflow-with-rl-agent-skills-and-nvidia-nemo--blog-nvidia-autoresearch-env) |
| [Introducing North Mini Code: Cohere's First Model For Developers](https://huggingface.co/blog/CohereLabs/introducing-north-mini-code) · Cohere Labs | 如何组织环境以生产不同类型训练数据？ | 仓库与终端任务容器化；SFT 合成与 RLVR 使用不相交环境子集；按仓库来源去重以减少评测泄漏 | 2026-06-09 | Cohere 官方团队在 Hugging Face 发布；模型开放不代表全部内部环境与数据流水线开放。[详情](docs/catalog_details_zh.md#introducing-north-mini-code-coheres-first-model-for-developers--blog-cohere-north-mini-code) |
| [A technical report on Composer 2](https://cursor.com/blog/composer-2-technical-report) · Cursor | 如何执行接近真实部署的训练任务？ | 真实工具会话中的多步任务；沙箱支持并发执行；将执行反馈接入异步 RL | 2026-03-27 | 工业界第一手报告；内部训练环境集群未作为开放资源发布。[详情](docs/catalog_details_zh.md#a-technical-report-on-composer-2--blog-composer2) |
| [DeepSWE: Training a Fully Open-sourced, State-of-the-Art Coding Agent by Scaling RL](https://www.together.ai/blog/deepswe) · Together AI | 已有仓库环境如何用于在线训练？ | 在 R2E-Gym 任务中执行工具动作；通过 Docker 提供仓库工作区；由可执行测试提供 RL 奖励 | 2025-07-02 | 在已有环境上的训练配方；DeepSWE 本身不是独立的环境合成器。[详情](docs/catalog_details_zh.md#deepswe-training-a-fully-open-sourced-state-of-the-art-coding-agent-by-scaling-rl--blog-together-deepswe) |
| [CoderForge-Preview](https://www.together.ai/blog/coderforge-preview) · Together AI | 如何从仓库任务生产训练轨迹？ | 以可执行仓库任务承载交互；用测试验证代码轨迹；发布轨迹并用于微调 | 未确认 | 公开发布重点是轨迹数据；轨迹数量不等于新发布的环境实现数量。[详情](docs/catalog_details_zh.md#coderforge-preview--blog-coderforge) |

## 两条主线的重点研究

### 主线一：规模化生产高质量环境

| 工作 | 研究切入点 | 核心方法 | 训练实验 | 注意事项 |
| --- | --- | --- | --- | --- |
| [Envs-FORGE](https://arxiv.org/abs/2608.14312) | 反馈驱动批量合成 | 用验证通过率决定每个种子的合成操作，同步改写任务、数据、测试和 Docker 环境 | RL 实验 | 论文链接的是综合工具包；根 README 中未找到论文专属的完整复现入口。[详情](docs/catalog_details_zh.md#envs-forge--paper-envs-forge) |
| [SWE-Universe](https://arxiv.org/abs/2602.02361) | 自动构建与构建环内质量检查 | 训练构建 agent 把 PR 转成可核验 SWE 环境，加入迭代自检与构建环内的作弊检测 | RL 实验 | 论文报告 807,693 个实例，不是独立环境家族数量；未找到官方构建代码。[详情](docs/catalog_details_zh.md#swe-universe--paper-swe-universe) |
| [daVinci-Env / OpenSWE](https://arxiv.org/abs/2603.13023) | 仓库构建、可解性与有效难度 | 自动完成仓库探索、Docker 配置和测试生成，再按可解性及有效难度筛选环境 | SFT/轨迹训练 | 论文标题为 daVinci-Env，发布框架名为 OpenSWE；构建和轨迹采样成本较高。[详情](docs/catalog_details_zh.md#davinci-env--openswe--paper-openswe) |
| [Agent-World](https://arxiv.org/abs/2604.18292) | 有状态世界与能力缺口驱动演化 | 发现有状态工具生态并生成可验证任务，将多环境学习与能力缺口驱动的任务演化连接起来 | RL 与 SFT 实验 | 公开仓库仅发布筛选后的环境子集，RL 接入仍需适配，不是论文完整语料。[详情](docs/catalog_details_zh.md#agent-world--paper-agent-world) |
| [EnvScaler](https://arxiv.org/abs/2601.05808) | 环境骨架、场景与规则验证 | 将环境骨架构建、场景生成和基于规则的轨迹验证分开 | RL 与 SFT 实验 | 规则覆盖与环境真实性需独立评估；公开 RL 接入使用 ROLL 与 GEM。[详情](docs/catalog_details_zh.md#envscaler--paper-envscaler) |
| [CLI-Universe](https://arxiv.org/abs/2606.22883) | 需求蓝图、执行环境与验证器 | 从能力分类与需求分析产生任务蓝图、Docker 环境和按评分要求筛选的验证器 | SFT/轨迹训练 | 可执行与 fail-to-pass 检查不能直接证明真实分布的代表性；未找到官方代码。[详情](docs/catalog_details_zh.md#cli-universe--paper-cli-universe) |
| [CalibForge](https://arxiv.org/abs/2608.06352) | 可学习难度校准 | 利用验证过的求解器分歧，或强模型通过/弱模型失败的对比，修订终端任务的可学习难度 | SFT/轨迹训练 | 难度校准相对于选定求解器，不是绝对难度；公开数据及 agent 配方不等于完整合成引擎。[详情](docs/catalog_details_zh.md#calibforge--paper-calibforge) |
| [Endless Terminals](https://arxiv.org/abs/2601.16443) | 任务、容器、测试的自动生产 | 依次生成任务描述、构建并验证容器、生成完成测试并筛选可解任务，再进行 PPO 训练 | RL 实验 | 生成、执行与策略优化是不同阶段；论文报告的训练收益不能证明任意生成测试都可靠。[详情](docs/catalog_details_zh.md#endless-terminals--paper-endless-terminals) |

### 主线二：合成有效的训练数据

| 工作 | 研究切入点 | 核心方法 | 训练实验 | 注意事项 |
| --- | --- | --- | --- | --- |
| [Skill2Env](https://arxiv.org/abs/2609.33772) | 技能内容→环境→SFT 轨迹 | 将技能转为能力导向的任务蓝图、可执行工作区和 rubric 评估器，并根据求解轨迹加难 | SFT/轨迹训练 | 论文做的是 SFT 实验。当前研究主页提供示例任务和模型链接；这些样例不能证明完整合成与训练流水线已经开放。[详情](docs/catalog_details_zh.md#skill2env--paper-skill2env) |
| [Terminal-World (skills)](https://arxiv.org/abs/2605.20876) | 技能依赖→任务与教师轨迹 | 以技能及其依赖图共同生成终端任务、可执行环境和教师轨迹 | SFT/轨迹训练 | 与录制还原路线的 TerminalWorld 不同；SFT 实验不等于在线 RL 已就绪，未找到生成器开放信息。[详情](docs/catalog_details_zh.md#terminal-world-skills--paper-terminal-world-skills) |
| [NexForge](https://arxiv.org/abs/2607.14186) | 真实需求→资源与专家示范 | 从真实需求编译任务，检索或构建配套文件及运行环境，再采集专家示范 | SFT/轨迹训练 | 终端任务数和办公任务数需要与轨迹数分开计数；模型发布不代表生成器开放。[详情](docs/catalog_details_zh.md#nexforge--paper-nexforge) |
| [OpenThoughts-Agent](https://arxiv.org/abs/2606.24855) | 任务来源、教师与过滤的受控比较 | 通过控制实验研究任务来源、混合比例、教师、rollout 与过滤策略，形成终端 agent 数据配方 | SFT/轨迹训练 | 2025 年发布博客和 2026 年论文属于不同发布阶段；训练效果取决于完整数据配方。[详情](docs/catalog_details_zh.md#openthoughts-agent--paper-openthoughts-agent) |
| [TerminalTraj](https://arxiv.org/abs/2602.01244) | 仓库→任务、验证器与轨迹 | 从仓库构造 Docker 环境、配套终端任务与可执行验证器，批量采集交互轨迹 | SFT/轨迹训练 | 镜像、任务和轨迹是不同计数单位；论文链接的仓库返回 404，未计入公开实现。[详情](docs/catalog_details_zh.md#terminaltraj--paper-terminaltraj) |
| [AgentTrek](https://arxiv.org/abs/2412.09605) | 教程内容→交互回放与筛选 | 采集网页教程并提炼任务指令，引导浏览器回放，再筛选用于训练的轨迹 | SFT/轨迹训练 | 教程回放利用已有网站，不代表生成独立网站后端；模型判定也可能出错。[详情](docs/catalog_details_zh.md#agenttrek--paper-agenttrek) |
| [OS-Genesis](https://arxiv.org/abs/2412.19723) | 先探索再反推任务与数据 | 先探索 GUI 环境，再反向合成任务，并用轨迹奖励模型筛选交互质量 | SFT/轨迹训练 | 主要在已有桌面/移动环境上构造任务与轨迹，不是新操作系统模拟器。[详情](docs/catalog_details_zh.md#os-genesis--paper-os-genesis) |
| [RandomWorld](https://arxiv.org/abs/2506.11045) | 同类生成工具用于 SFT 与 RL | 程序化生成可交互工具及组合式工具使用数据，同时用于监督学习与强化学习 | RL 与 SFT 实验 | 合成工具语义不代表生产 API 的保真度；公开仓库的使用文档较少。[详情](docs/catalog_details_zh.md#randomworld--paper-randomworld) |
| [DreamGym](https://arxiv.org/abs/2511.03773) | 模拟经验与回放用于 RL | 结合推理式经验模型、回放缓冲区与自适应任务生成，通过合成交互训练代理 | RL 实验 | 从模拟到现实的迁移是实验结果；第三方复现不能当作作者官方代码。[详情](docs/catalog_details_zh.md#dreamgym--paper-dreamgym) |
| [VERA](https://arxiv.org/abs/2610.05923) | 可恢复环境与策略/技能更新 | 从轨迹构建可恢复沙箱，经检查筛选后交替更新模型权重与 harness 技能 | RL 与 harness 学习 | 近期预印本；摘要和正文未提供可确认的官方仓库。[详情](docs/catalog_details_zh.md#vera--paper-vera) |

以上是从既有目录筛出的研究重点，不是性能排名。SFT、RL 与仅构造实验分开记录；本调研没有复现训练结果。

## 技术报告中的环境章节

以下位置对应指定报告版本。PDF 链接定位到首个相关页；章节索引逐节说明内容。模型权重或 Agent 客户端开放，不代表训练环境开放。

| 报告/论文 | 版本 | 相关章节 | 定位 | 内容 |
| --- | --- | --- | --- | --- |
| [Kimi K3](https://arxiv.org/abs/2607.24653) | arXiv v2 · 2026-08-07 | §4.2.1, §4.2.2, §4.2.3, §4.2.4, §4.2.5, §4.2.6, §4.2.7, §5.3.2 | [PDF pp. 14, 15, 16, 22](https://arxiv.org/pdf/2607.24653v2#page=14) · [逐节内容](docs/technical_report_sections_zh.md#kimi-k3) | 介绍可组合 Agent 环境、任务合成和长交互中的持久沙箱状态。 |
| [DeepSeek V4](https://arxiv.org/abs/2606.19348) | arXiv v1 · 2026-04-26 | §5.2.3, §5.2.5 | [PDF pp. 34, 35, 36](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro/resolve/89d501aed998d33fa4f4702102ec1bb2331e10f6/DeepSeek_V4.pdf#page=34) · [逐节内容](docs/technical_report_sections_zh.md#deepseek-v4) | 在模型报告中披露 DSec 执行后端与支持中断恢复的 rollout 服务。 |
| [GLM-4.5](https://arxiv.org/abs/2508.06471) | arXiv v1 · 2025-08-08 | §3.3.1, §3.5 | [PDF pp. 10, 12, 13, 14](https://arxiv.org/pdf/2508.06471v1#page=10) · [逐节内容](docs/technical_report_sections_zh.md#glm-45) | 介绍任务合成、隔离执行，以及服务 Agent 学习的异步轨迹池。 |
| [DeepSeek Elastic Compute (DSec)](https://arxiv.org/abs/2609.22978) | arXiv v1 · 2026-09-19 | §5.1, §6.1, §6.2, §6.3 | [PDF pp. 14, 15, 17, 18](https://arxiv.org/pdf/2609.22978v1#page=14) · [逐节内容](docs/technical_report_sections_zh.md#deepseek-elastic-compute-dsec) | 统一函数调用、容器、microVM 与完整 VM；支持 Agent 构建可复用环境，以及长交互任务的挂起和恢复。 |
| [MiMo-V2.6](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL/blob/73875d00b30a89ef8cc353a0b60b0e9f9561952d/MiMo_V2_6_technical_report.pdf) | HF revision 73875d0 · checked 2026-10-08 | §4.2.1, §4.2.2, §4.2.3, §4.2.4, §4.2.5, §4.2.6, §6.1, §6.2, §7.2 | [PDF pp. 9, 10, 11, 12, 13, 14, 15, 16, 26, 27, 28, 29, 34, 35, 36](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL/resolve/73875d00b30a89ef8cc353a0b60b0e9f9561952d/MiMo_V2_6_technical_report.pdf#page=9) · [逐节内容](docs/technical_report_sections_zh.md#mimo-v26) | 介绍跨领域环境与验证器构建、多 harness 执行，以及已发布环境上的实验。 |

## 分类目录

保留原有 6 个大类、20 个小类以及论文/仓库分表结构，便于查资料。上方两条主线决定本次研究重点；下方接口、运行时、领域基准与审计材料提供支撑，不再全部作为并列研究方向。Stars 为快照，不代表质量排名。

[覆盖审计](docs/coverage_audit.md) · [技能与需求合成](docs/skills_to_environments.md) · [中文综述](docs/research_landscape_zh.md) · [收录标准](docs/curation_policy.md)

- [环境与任务构建](#环境与任务构建)
  - [技能到任务与环境](#技能到任务与环境)
  - [需求到可执行任务](#需求到可执行任务)
  - [仓库驱动的环境构建](#仓库驱动的环境构建)
  - [Web／GUI 环境与任务合成](#webgui-环境与任务合成)
  - [结构化工具与业务世界](#结构化工具与业务世界)
  - [程序化任务生成](#程序化任务生成)
  - [学习式交互模拟器](#学习式交互模拟器)
- [交互数据与经验生产](#交互数据与经验生产)
  - [探索、回放与反向合成](#探索回放与反向合成)
  - [轨迹筛选与数据配方](#轨迹筛选与数据配方)
  - [轨迹采集与检查](#轨迹采集与检查)
- [环境基础设施](#环境基础设施)
  - [接口、适配器与注册库](#接口适配器与注册库)
  - [沙箱与交互执行](#沙箱与交互执行)
- [领域环境与评测基准](#领域环境与评测基准)
  - [软件、终端与可执行技能](#软件终端与可执行技能)
  - [浏览器、桌面与移动端](#浏览器桌面与移动端)
  - [工具与企业工作流](#工具与企业工作流)
  - [游戏与交互推理](#游戏与交互推理)
  - [科学与具身环境](#科学与具身环境)
- [自适应与质量控制](#自适应与质量控制)
  - [课程与环境共演化](#课程与环境共演化)
  - [验证器、契约与失败审计](#验证器契约与失败审计)
- [综述与研究地图](#综述与研究地图)
  - [环境扩展与演化综述](#环境扩展与演化综述)

## 环境与任务构建

### 技能到任务与环境

**论文**

| 论文 | 日期 | 资源 | 环境／任务贡献 | 质量保障 | 代码情况 |
| --- | --- | --- | --- | --- | --- |
| [Skill2Env](https://arxiv.org/abs/2609.33772) | 2026-09-27 | [主页](https://github.com/AllSpark-Research/AgentEnv) · [部分／关联代码](https://github.com/AllSpark-Research/AgentEnv) · [示例任务](https://github.com/AllSpark-Research/AgentEnv/tree/main/Skill2Env) · [模型](https://huggingface.co/AllSpark-Research/Skill2Env) · [详情](docs/catalog_details_zh.md#skill2env--paper-skill2env) | 将技能转为能力导向的任务蓝图、可执行工作区和 rubric 评估器，并根据求解轨迹加难。 | SFT／轨迹训练: rubric 评估器及用于任务加难的求解证据。 | 实验展示 SFT。当前研究主页提供示例任务和模型链接；这些样例不能说明完整合成与训练流水线已经开放。 |
| [SKT](https://arxiv.org/abs/2608.02287) | 2026-08-03 | [详情](docs/catalog_details_zh.md#skt--paper-skt) | 构造技能条件化任务包，在采集 SFT 轨迹前同时检查执行成功与所需技能确实被使用。 | SFT／轨迹训练: 规则与智能体检查、迭代修复，并验证所要求的技能实际被使用。 | 任务成功不自动证明技能被使用；未找到官方流水线代码。 |
| [Terminal-World (skills)](https://arxiv.org/abs/2605.20876) | 2026-05-20 | [详情](docs/catalog_details_zh.md#terminal-world-skills--paper-terminal-world-skills) | 以技能及其依赖图共同生成终端任务、可执行环境和教师轨迹。 | SFT／轨迹训练: 对齐共同生成的任务、运行环境与教师轨迹；下游证据是轨迹训练。 | 与录制还原路线的 TerminalWorld 不同；SFT 实验不等于在线 RL 已就绪，未找到生成器开放。 |
| [SkillSynth](https://arxiv.org/abs/2604.25727) | 2026-04-28 | [详情](docs/catalog_details_zh.md#skillsynth--paper-skillsynth) | 通过场景连接技能图，将技能组合转成可执行终端任务及多样解题轨迹。 | SFT／轨迹训练: 验证可执行任务实例，并从场景—技能组合与求解轨迹衡量多样性。 | 技能覆盖、轨迹多样性与独立环境家族数量不同；未找到官方代码。 |
| [Terminal-Task-Gen / Nemotron-Terminal](https://arxiv.org/abs/2602.21193) | 2026-02-24 | [模型与数据集合](https://huggingface.co/collections/nvidia/nemotron-terminal) · [详情](docs/catalog_details_zh.md#terminal-task-gen--nemotron-terminal--paper-terminal-task-gen) | 把种子任务与技能驱动生成、环境适配和轨迹筛选组合为 Terminal-Corpus 数据工程流程。 | SFT／轨迹训练: 任务与轨迹筛选、环境适配，以及数据混合／课程实验。 | 已关联模型／数据集合，但不能说明完整生成流水线已开放。 |

### 需求到可执行任务

**论文**

| 论文 | 日期 | 资源 | 环境／任务贡献 | 质量保障 | 代码情况 |
| --- | --- | --- | --- | --- | --- |
| [AutoGym](https://arxiv.org/abs/2609.22592) | 2026-09-18 | [详情](docs/catalog_details_zh.md#autogym--paper-autogym) | 先定义解空间与验证条件，再生成完整 gym，并按模型表现校准生成参数。 | 环境／任务生成: 生成的任务验证器及构建或可解性验证。 | 展示生成环境的难度；不能说明已发布端到端 RL 系统或持续训练增益。 |
| [NexForge](https://arxiv.org/abs/2607.14186) | 2026-07-15 | [详情](docs/catalog_details_zh.md#nexforge--paper-nexforge) | 从真实需求编译任务，检索或构建配套文件及运行环境，再采集专家示范。 | SFT／轨迹训练: 以需求约束任务构造，准备各任务执行资源并采集专家示范。 | 终端与办公任务数需要和轨迹数分开；模型发布不代表生成器开放。 |
| [CLI-Universe](https://arxiv.org/abs/2606.22883) | 2026-06-22 | [详情](docs/catalog_details_zh.md#cli-universe--paper-cli-universe) | 从能力分类与需求分析产生任务蓝图、Docker 环境和按评分要求筛选的验证器。 | SFT／轨迹训练: 按评分要求筛选任务并执行 fail-to-pass 测试，同时过滤误导性提示。 | 可执行与 fail-to-pass 检查不能直接说明真实分布代表性；未找到官方代码。 |
| [EnvFactory](https://arxiv.org/abs/2605.18703) | 2026-05-18 | [代码](https://github.com/LARK-AI-Lab/EnvFactory) · [详情](docs/catalog_details_zh.md#envfactory--paper-envfactory) | 从真实资源构建并验证有状态工具，再按工具拓扑与查询校准合成轨迹。 | RL 与 SFT 实验: 生成的任务验证器及构建或可解性验证。 | 可执行正确性与自然任务意图需分别检查；发布物依赖特定训练框架。 |
| [ClawEnvKit](https://arxiv.org/abs/2604.18543) | 2026-04-20 | [代码](https://github.com/xirui-li/ClawEnvKit) · [详情](docs/catalog_details_zh.md#clawenvkit--paper-clawenvkit) | 把自然语言需求解析为任务规格、模拟工具和评分规则，再验证生成的评测环境。 | 评测环境: 配置验证、模拟服务审计日志与结构化规则检查，并包含 LLM 判定类型。 | 模拟服务与规则／模型混合检查不等于真实企业系统；可用于训练不等于已报告 RL 收益。 |
| [ScaleEnv](https://arxiv.org/abs/2602.06820) | 2026-02-06 | [详情](docs/catalog_details_zh.md#scaleenv--paper-scaleenv) | 从零构建交互工具环境，通过实现测试和可执行动作序列验证任务可解性。 | RL 实验: 生成的任务验证器及构建或可解性验证。 | 与 Scale AI AgentEnv 不同；已读论文及定向搜索未确认官方代码链接。 |
| [Endless Terminals](https://arxiv.org/abs/2601.16443) | 2026-01-23 | [代码](https://github.com/kanishkg/endless-terminals) · [详情](docs/catalog_details_zh.md#endless-terminals--paper-endless-terminals) | 依次生成任务描述、构建并验证容器、生成完成测试并筛选可解任务，再进行 PPO 训练。 | RL 实验: 用初末状态或 fail-to-pass 测试检查执行，参考解用于验证可解性。 | 生成、执行与策略优化是不同阶段；已报告收益不能说明任意生成测试都可靠。 |
| [AutoForge](https://arxiv.org/abs/2512.22857) | 2025-12-28 | [详情](docs/catalog_details_zh.md#autoforge--paper-autoforge) | 先组织合成状态结构和工具依赖，再生成用于 agent RL 的工具环境。 | RL 实验: 生成的任务验证器及构建或可解性验证。 | 存在多个无关同名仓库；未将未经确认的 AutoForge 项目当作官方代码。 |
| [SWE-Playground](https://arxiv.org/abs/2512.12216) | 2025-12-13 | [代码](https://github.com/neulab/SWE-Playground) · [详情](docs/catalog_details_zh.md#swe-playground--paper-swe-playground) | 从零合成软件项目、任务与执行轨迹，覆盖测试编写及库实现等场景。 | SFT／轨迹训练: 分别由测试编写与功能实现智能体相互检验生成的软件任务。 | 合成项目多样性与真实仓库保真度不同；执行需要模型和运行后端依赖。 |
| [AutoEnv](https://arxiv.org/abs/2511.19304) | 2025-11-24 | [代码](https://github.com/FoundationAgents/AutoEnv) · [详情](docs/catalog_details_zh.md#autoenv--paper-autoenv) | 将转移、观察和奖励分布因子化，生成异构世界以研究跨环境学习。 | 环境／任务生成: 生成的任务验证器及构建或可解性验证。 | 生成关卡衡量的是设计分布下的迁移，并非无限制真实世界泛化。 |

**仓库**

| 项目 | 链接 | Stars | 标签 | 摘要 |
| --- | --- | --- | --- | --- |
| Endless Terminals | [GitHub](https://github.com/kanishkg/endless-terminals) · [详情](docs/catalog_details_zh.md#endless-terminals--project-endless-terminals) | ★ 147 | requirement-synthesis | 依次生成任务描述、构建并验证容器、生成完成测试并筛选可解任务，再进行 PPO 训练。 |
| EnvFactory | [GitHub](https://github.com/LARK-AI-Lab/EnvFactory) · [详情](docs/catalog_details_zh.md#envfactory--project-envfactory) | ★ 96 | executable, rl+sft | 从真实资源构建并验证有状态工具，再按工具拓扑与查询校准合成轨迹。 |
| AutoEnv | [GitHub](https://github.com/FoundationAgents/AutoEnv) · [详情](docs/catalog_details_zh.md#autoenv--project-autoenv) | ★ 68 | mixed, generation | 将转移、观察和奖励分布因子化，生成异构世界以研究跨环境学习。 |
| ClawEnvKit | [GitHub](https://github.com/xirui-li/ClawEnvKit) · [详情](docs/catalog_details_zh.md#clawenvkit--project-clawenvkit) | ★ 62 | requirement-synthesis | 把自然语言需求解析为任务规格、模拟工具和评分规则，再验证生成的评测环境。 |
| SWE-Playground | [GitHub](https://github.com/neulab/SWE-Playground) · [详情](docs/catalog_details_zh.md#swe-playground--project-swe-playground) | ★ 22 | requirement-synthesis | 从零合成软件项目、任务与执行轨迹，覆盖测试编写及库实现等场景。 |
| LiteCoder | [GitHub](https://github.com/icip-cas/LiteCoder) · [详情](docs/catalog_details_zh.md#litecoder--project-litecoder) | ★ 17 | requirement-synthesis | 发布终端轨迹与 Harbor 格式环境，并说明从指令到环境的五阶段合成流程。 |

**博客**

| 文章 | 发布方 | 日期 | 摘要 | 证据 |
| --- | --- | --- | --- | --- |
| [Announcing LiteCoder-Terminal Preview](https://huggingface.co/blog/Lite-Coder/litecoder-terminal-preview) | Lite-Coder / ICIP-CAS contributors | 2025-12-18 | 详述按领域分类采样任务、可行性筛选、Docker 初态构造和轨迹采集。 | [详情](docs/catalog_details_zh.md#announcing-litecoder-terminal-preview--blog-litecoder) |

### 仓库驱动的环境构建

**论文**

| 论文 | 日期 | 资源 | 环境／任务贡献 | 质量保障 | 代码情况 |
| --- | --- | --- | --- | --- | --- |
| [DeNovoSWE](https://arxiv.org/abs/2606.10728) | 2026-06-09 | [部分／关联代码](https://github.com/AweAI-Team/DeNovoSWE) · [详情](docs/catalog_details_zh.md#denovoswe--paper-denovoswe) | 通过沙箱中的任务拆解、批判修复与难度感知轨迹过滤，构建文档到完整仓库的任务。 | SFT／轨迹训练: 单元测试、构造时的批判修复，以及按难度筛选成功轨迹。 | 从零写仓库描述的是智能体任务，构造过程仍依托已有包；仓库声明公开部分数据。 |
| [daVinci-Env / OpenSWE](https://arxiv.org/abs/2603.13023) | 2026-03-13 | [代码](https://github.com/GAIR-NLP/OpenSWE) · [详情](docs/catalog_details_zh.md#davinci-env--openswe--paper-openswe) | 自动完成仓库探索、Docker 配置和测试生成，再按可解性及有效难度筛选环境。 | SFT／轨迹训练: 任务专属执行测试或验证器评分；具体划分以各项来源为准。 | 论文标题为 daVinci-Env，发布框架名为 OpenSWE；构建和轨迹采样成本较高。 |
| [SWE-rebench V2](https://arxiv.org/abs/2602.23866) | 2026-02-27 | [代码](https://github.com/SWE-rebench/SWE-rebench-V2) · [详情](docs/catalog_details_zh.md#swe-rebench-v2--paper-swe-rebench) | 采集多语言仓库任务，生成安装与测试流程，构建可复现训练环境。 | 环境／任务生成: 任务专属执行测试或验证器评分；具体划分以各项来源为准。 | 完整构建环境与额外任务元数据的发布范围不同；测试可能不足或过度约束。 |
| [ScaleSWE](https://arxiv.org/abs/2602.09892) | 2026-02-10 | [部分／关联代码](https://github.com/AweAI-Team/ScaleSWE) · [公开数据集合](https://huggingface.co/collections/AweAI-Team/scale-swe) · [详情](docs/catalog_details_zh.md#scaleswe--paper-scaleswe) | 协同环境配置、测试生成和问题描述智能体，构建来自 PR 的 SWE 任务及示范数据。 | SFT／轨迹训练: 在恢复的仓库状态上执行 fail-to-pass 复现测试与 pass-to-pass 回归检查。 | 论文规模为 100k 实例；仓库明确说明初始公开子集为 20k 实例，执行依赖另一个 harness。 |
| [SWE-Universe](https://arxiv.org/abs/2602.02361) | 2026-02-02 | [详情](docs/catalog_details_zh.md#swe-universe--paper-swe-universe) | 由训练过的构建智能体把 PR 转成可核验 SWE 环境，加入迭代自检与构建环内的作弊检测。 | RL 实验: 在使用可执行任务学习前进行迭代构建验证与构建环内作弊检测。 | 论文报告 807,693 个实例，并非独立环境家族；未找到官方构建代码。 |
| [TerminalTraj](https://arxiv.org/abs/2602.01244) | 2026-02-01 | [详情](docs/catalog_details_zh.md#terminaltraj--paper-terminaltraj) | 从仓库构造 Docker 环境、配套终端任务与可执行验证器，批量采集交互轨迹。 | SFT／轨迹训练: 为与 Docker 环境对齐的任务合成可执行验证代码，并筛选轨迹。 | 镜像、任务和轨迹是不同计数单位；论文所链仓库本轮返回 404，未计入公开实现。 |
| [SWE-smith](https://arxiv.org/abs/2504.21798) | 2025-04-30 | [代码](https://github.com/SWE-bench/SWE-smith) · [详情](docs/catalog_details_zh.md#swe-smith--paper-swe-smith) | 将仓库转为执行环境，主动破坏现有测试来生成修复任务。 | SFT／轨迹训练: 任务专属执行测试或验证器评分；具体划分以各项来源为准。 | 变异产生的故障与真实报告的 bug 不同，仍需仓库划分与隐藏测试。 |
| [R2E-Gym](https://arxiv.org/abs/2504.07164) | 2025-04-09 | [代码](https://github.com/R2E-Gym/R2E-Gym) · [详情](docs/catalog_details_zh.md#r2e-gym--paper-r2e-gym) | 从提交程序化整理可执行软件任务，并研究执行验证器与学习式验证器的互补性。 | SFT／轨迹训练: 任务专属执行测试或验证器评分；具体划分以各项来源为准。 | 早期摘要使用 AgentGym 名称，但它与 WooooDyy/AgentGym 是不同项目。 |
| [SWE-Gym](https://arxiv.org/abs/2412.21139) | 2024-12-30 | [代码](https://github.com/SWE-Gym/SWE-Gym) · [详情](docs/catalog_details_zh.md#swe-gym--paper-swe-gym) | 将仓库问题与可运行环境、单元测试配对，支持代理微调和验证器训练。 | SFT／轨迹训练: 任务专属执行测试或验证器评分；具体划分以各项来源为准。 | 初始语料以 Python 为中心；环境可运行不意味着广泛语言覆盖。 |

**仓库**

| 项目 | 链接 | Stars | 标签 | 摘要 |
| --- | --- | --- | --- | --- |
| SWE-smith | [GitHub](https://github.com/SWE-bench/SWE-smith) · [详情](docs/catalog_details_zh.md#swe-smith--project-swe-smith) | ★ 795 | executable, sft | 将仓库转为执行环境，主动破坏现有测试来生成修复任务。 |
| SWE-Gym | [GitHub](https://github.com/SWE-Gym/SWE-Gym) · [详情](docs/catalog_details_zh.md#swe-gym--project-swe-gym) | ★ 748 | executable, sft | 将仓库问题与可运行环境、单元测试配对，支持代理微调和验证器训练。 |
| R2E-Gym | [GitHub](https://github.com/R2E-Gym/R2E-Gym) · [详情](docs/catalog_details_zh.md#r2e-gym--project-r2e-gym) | ★ 337 | executable, sft | 从提交程序化整理可执行软件任务，并研究执行验证器与学习式验证器的互补性。 |
| daVinci-Env / OpenSWE | [GitHub](https://github.com/GAIR-NLP/OpenSWE) · [详情](docs/catalog_details_zh.md#davinci-env--openswe--project-openswe) | ★ 211 | executable, sft | 自动完成仓库探索、Docker 配置和测试生成，再按可解性及有效难度筛选环境。 |
| ScaleSWE | [GitHub](https://github.com/AweAI-Team/ScaleSWE) · [详情](docs/catalog_details_zh.md#scaleswe--project-scaleswe) | ★ 95 | repo-synthesis | 协同环境配置、测试生成和问题描述智能体，构建来自 PR 的 SWE 任务及示范数据。 |
| SWE-rebench V2 | [GitHub](https://github.com/SWE-rebench/SWE-rebench-V2) · [详情](docs/catalog_details_zh.md#swe-rebench-v2--project-swe-rebench) | ★ 85 | executable, generation | 采集多语言仓库任务，生成安装与测试流程，构建可复现训练环境。 |
| DeNovoSWE | [GitHub](https://github.com/AweAI-Team/DeNovoSWE) · [详情](docs/catalog_details_zh.md#denovoswe--project-denovoswe) | ★ 47 | repo-synthesis | 通过沙箱中的任务拆解、批判修复与难度感知轨迹过滤，构建文档到完整仓库的任务。 |

### Web／GUI 环境与任务合成

**论文**

| 论文 | 日期 | 资源 | 环境／任务贡献 | 质量保障 | 代码情况 |
| --- | --- | --- | --- | --- | --- |
| [WebForge](https://arxiv.org/abs/2604.10988) | 2026-04-13 | [部分／关联代码](https://github.com/yuandaxia2001/WebForge) · [基准网站与任务](https://huggingface.co/datasets/yuandaxia/WebForge) · [详情](docs/catalog_details_zh.md#webforge--paper-webforge) | 协同规划、网站生成、修订与验证，构造自包含且可调难度的浏览器基准。 | 评测环境: 先验证生成网站，再由 LLM 比较终态答案或网站计算的操作码。 | 公开代码主要覆盖评测端；终态答案或操作码由 LLM 比较，并非全部使用确定性状态验证。 |
| [Gym-Anything / CUA-World](https://arxiv.org/abs/2604.06126) | 2026-04-07 | [代码](https://github.com/cmu-l3/gym-anything) · [详情](docs/catalog_details_zh.md#gym-anything--cua-world--paper-gym-anything) | 用独立审计代理检查软件安装及真实任务配置，发布跨软件的计算机使用环境语料。 | SFT／轨迹训练: 交互后的状态、产物或 rubric 评估，具体类型依任务而异。 | 虚拟机、应用依赖和 rubric 评判增加成本；配置证据不等于完美的任务验证。 |
| [InfiniteWeb](https://arxiv.org/abs/2601.04126) | 2026-01-07 | [详情](docs/catalog_details_zh.md#infiniteweb--paper-infiniteweb) | 生成多页面可交互网站，配套任务中心测试和可验证评估器，用于 GUI 代理 RL。 | RL 实验: 交互后的状态、产物或 rubric 评估，具体类型依任务而异。 | 生成网站仍需功能与视觉真实性检查；完整发布物可用性需另行确认。 |
| [AgentSynth](https://arxiv.org/abs/2506.14205) | 2025-06-17 | [代码](https://github.com/sunblaze-ucb/AgentSynth) · [详情](docs/catalog_details_zh.md#agentsynth--paper-agentsynth) | 将已执行子任务组合成更难的长程计算机任务与轨迹数据集。 | 环境／任务生成: 交互后的状态、产物或 rubric 评估，具体类型依任务而异。 | 主要在现有环境上合成任务和轨迹，并非新通用运行时。 |

**仓库**

| 项目 | 链接 | Stars | 标签 | 摘要 |
| --- | --- | --- | --- | --- |
| Gym-Anything / CUA-World | [GitHub](https://github.com/cmu-l3/gym-anything) · [详情](docs/catalog_details_zh.md#gym-anything--cua-world--project-gym-anything) | ★ 292 | desktop, sft | 用独立审计代理检查软件安装及真实任务配置，发布跨软件的计算机使用环境语料。 |
| AgentSynth | [GitHub](https://github.com/sunblaze-ucb/AgentSynth) · [详情](docs/catalog_details_zh.md#agentsynth--project-agentsynth) | ★ 53 | desktop, generation | 将已执行子任务组合成更难的长程计算机任务与轨迹数据集。 |
| WebForge | [GitHub](https://github.com/yuandaxia2001/WebForge) · [详情](docs/catalog_details_zh.md#webforge--project-webforge) | ★ 14 | web-synthesis | 协同规划、网站生成、修订与验证，构造自包含且可调难度的浏览器基准。 |

### 结构化工具与业务世界

**论文**

| 论文 | 日期 | 资源 | 环境／任务贡献 | 质量保障 | 代码情况 |
| --- | --- | --- | --- | --- | --- |
| [CompoWorld](https://arxiv.org/abs/2609.33665) | 2026-09-27 | [主页](https://github.com/AllSpark-Research/AgentEnv) · [部分／关联代码](https://github.com/AllSpark-Research/AgentEnv) · [CompoWorld 样例](https://github.com/AllSpark-Research/AgentEnv/blob/main/CompoWorld/README.md) · [详情](docs/catalog_details_zh.md#compoworld--paper-compoworld) | 以共享类型状态与接口组合已验证服务，从依赖图合成跨服务任务。 | RL 与 SFT 实验: 完成度与 rubric 检查；报告 SFT 和 RL 实验。 | 服务数、工具数不能当作独立环境数；关联仓库提供样例，未确认完整复现流程。 |
| [AgentMercury](https://arxiv.org/abs/2608.20634) | 2026-08-21 | [公开语料样本](https://huggingface.co/datasets/Minbyul/AgentMercury-corpus-sample) · [详情](docs/catalog_details_zh.md#agentmercury--paper-agentmercury) | 先构建包含持久状态、工具和跨服务不变量的业务世界，再从中派生任务与轨迹。 | RL 与 SFT 实验: 可执行跨服务不变量约束生成世界；策略 RL 与构建轨迹微调分别评估。 | 公开语料样本不等于完整可执行世界库；构建模型微调与策略 RL 是不同实验。 |
| [Agent-World](https://arxiv.org/abs/2604.18292) | 2026-04-20 | [部分／关联代码](https://github.com/RUC-NLPIR/Agent-World) · [详情](docs/catalog_details_zh.md#agent-world--paper-agent-world) | 发现有状态工具生态并生成可验证任务，将多环境学习与能力缺口驱动的任务演化连接起来。 | RL 与 SFT 实验: 生成的任务验证器及构建或可解性验证。 | 公开仓库仅发布筛选后的环境子集，RL 接入仍需适配，并非论文完整语料。 |
| [Agent World Model](https://arxiv.org/abs/2602.10090) | 2026-02-10 | [代码](https://github.com/Snowflake-Labs/agent-world-model) · [详情](docs/catalog_details_zh.md#agent-world-model--paper-awm) | 合成由代码驱动、SQL 数据库支撑的工具世界，提供可检查状态与奖励，用于多轮 RL 和迁移研究。 | RL 实验: 利用数据库状态进行任务验证。 | 合成数据库的一致性不代表覆盖所有真实服务行为与生产故障。 |
| [EnvScaler](https://arxiv.org/abs/2601.05808) | 2026-01-09 | [代码](https://github.com/RUC-NLPIR/EnvScaler) · [详情](docs/catalog_details_zh.md#envscaler--paper-envscaler) | 将环境骨架构建、场景生成和基于规则的轨迹验证分开。 | RL 与 SFT 实验: 基于规则的轨迹及最终状态检查。 | 规则覆盖与环境真实性需独立评估；公开 RL 接入使用 ROLL 与 GEM。 |
| [CodeGym](https://arxiv.org/abs/2509.17325) | 2025-09-22 | [代码](https://github.com/StigLidu/CodeGym) · [详情](docs/catalog_details_zh.md#codegym--paper-codegym) | 从编程问题提取可调用函数，合成可控多轮工具任务并用执行结果评分。 | RL 实验: 代码执行结果对照任务参考行为。 | 代码派生工作流提供有用抽象，但不完整覆盖真实企业服务语义。 |
| [RandomWorld](https://arxiv.org/abs/2506.11045) | 2025-05-21 | [代码](https://github.com/coli-saar/randomworld) · [详情](docs/catalog_details_zh.md#randomworld--paper-randomworld) | 程序化生成可交互工具及组合式工具使用数据，同时用于监督学习与强化学习。 | RL 与 SFT 实验: 可执行的合成工具交互与组合任务结果提供监督和 RL 信号。 | 合成工具语义不代表生产 API 保真度；公开仓库的使用文档较少。 |

**仓库**

| 项目 | 链接 | Stars | 标签 | 摘要 |
| --- | --- | --- | --- | --- |
| Agent World Model | [GitHub](https://github.com/Snowflake-Labs/agent-world-model) · [详情](docs/catalog_details_zh.md#agent-world-model--project-awm) | ★ 465 | executable, rl | 合成由代码驱动、SQL 数据库支撑的工具世界，提供可检查状态与奖励，用于多轮 RL 和迁移研究。 |
| EnvScaler | [GitHub](https://github.com/RUC-NLPIR/EnvScaler) · [详情](docs/catalog_details_zh.md#envscaler--project-envscaler) | ★ 199 | executable, rl+sft | 将环境骨架构建、场景生成和基于规则的轨迹验证分开。 |
| CodeGym | [GitHub](https://github.com/StigLidu/CodeGym) · [详情](docs/catalog_details_zh.md#codegym--project-codegym) | ★ 41 | executable, rl | 从编程问题提取可调用函数，合成可控多轮工具任务并用执行结果评分。 |
| Agent-World | [GitHub](https://github.com/RUC-NLPIR/Agent-World) · [详情](docs/catalog_details_zh.md#agent-world--project-agent-world) | ★ 7 | executable, rl+sft | 发现有状态工具生态并生成可验证任务，将多环境学习与能力缺口驱动的任务演化连接起来。 |
| RandomWorld | [GitHub](https://github.com/coli-saar/randomworld) · [详情](docs/catalog_details_zh.md#randomworld--project-randomworld) | ★ 3 | structured-synthesis | 程序化生成可交互工具及组合式工具使用数据，同时用于监督学习与强化学习。 |

**博客**

| 文章 | 发布方 | 日期 | 摘要 | 证据 |
| --- | --- | --- | --- | --- |
| [Agent World Model: Infinity Synthetic Environments for Agentic Reinforcement Learning](https://www.snowflake.com/en/blog/engineering/agent-world-model-for-agentic-reinforment-learning/) | Snowflake AI Research and collaborators | 2026-02-13 | 解释可执行 SQL 世界合成、一致状态转移及工具使用 RL 的奖励构建。 | [详情](docs/catalog_details_zh.md#agent-world-model-infinity-synthetic-environments-for-agentic-reinforcement-learning--blog-awm-blog) |
| [Magentic Marketplace: an open-source simulation environment for studying agentic markets](https://www.microsoft.com/en-us/research/blog/magentic-marketplace-an-open-source-simulation-environment-for-studying-agentic-markets/) | Microsoft Research | 2025-11-05 | 用共享 REST 环境承载买卖方 agent 的发现、沟通和模拟交易；合成市场数据支持可重复的行为实验。 | [详情](docs/catalog_details_zh.md#magentic-marketplace-an-open-source-simulation-environment-for-studying-agentic-markets--blog-microsoft-marketplace) |

### 程序化任务生成

**论文**

| 论文 | 日期 | 资源 | 环境／任务贡献 | 质量保障 | 代码情况 |
| --- | --- | --- | --- | --- | --- |
| [Reasoning Gym](https://arxiv.org/abs/2505.24760) | 2025-05-30 | [代码](https://github.com/open-thought/reasoning-gym) · [详情](docs/catalog_details_zh.md#reasoning-gym--paper-reasoning-gym) | 以可调难度生成推理任务并配套确定性验证器，替代固定数据集。 | RL 实验: 程序化参考答案与任务专属评分函数。 | 许多任务是单轮问题；程序化任务多样性不同于有状态工具交互多样性。 |

**仓库**

| 项目 | 链接 | Stars | 标签 | 摘要 |
| --- | --- | --- | --- | --- |
| Reasoning Gym | [GitHub](https://github.com/open-thought/reasoning-gym) · [详情](docs/catalog_details_zh.md#reasoning-gym--project-reasoning-gym) | ★ 1,522 | procedural, rl | 以可调难度生成推理任务并配套确定性验证器，替代固定数据集。 |

### 学习式交互模拟器

**论文**

| 论文 | 日期 | 资源 | 环境／任务贡献 | 质量保障 | 代码情况 |
| --- | --- | --- | --- | --- | --- |
| [EnvACE](https://arxiv.org/abs/2608.06197) | 2026-08-06 | [代码](https://github.com/Within-yao/EnvACE) · [详情](docs/catalog_details_zh.md#envace--paper-envace) | 用按角色计算的 RL 信号训练共享策略，让它既执行动作又模拟环境响应，从而内化动态。 | RL 实验: 模拟观察或任务成功奖励；真实环境迁移另行评测。 | 预演观察是模型输出；模拟的一致性需要外部执行验证。 |
| [WebWorld](https://arxiv.org/abs/2602.14721) | 2026-02-16 | [代码](https://github.com/QwenLM/WebWorld) · [详情](docs/catalog_details_zh.md#webworld--paper-webworld) | 从交互轨迹学习开放网页模拟器，并用模拟 rollout 训练和规划网页代理。 | SFT／轨迹训练: 模拟观察或任务成功奖励；真实环境迁移另行评测。 | 模拟质量与真实浏览器迁移是不同指标；勿与后续同名网页代码论文混淆。 |
| [GenEnv](https://arxiv.org/abs/2512.19682) | 2025-12-22 | [代码](https://github.com/Gen-Verse/GenEnv) · [详情](docs/catalog_details_zh.md#genenv--paper-genenv) | 通过难度对齐的课程奖励，共同演化生成式模拟器与代理。 | RL 实验: 模拟观察或任务成功奖励；真实环境迁移另行评测。 | 学习式模拟可能偏离可执行现实；结果限于论文所选任务。 |
| [SynthTools](https://arxiv.org/abs/2511.09572) | 2025-11-11 | [代码](https://github.com/namkoong-lab/SynthTools) · [详情](docs/catalog_details_zh.md#synthtools--paper-synthtools) | 分离合成工具生成、响应模拟和工具审计，以扩展可控工具生态。 | 环境／任务生成: LLM 模拟的工具观察及独立审计阶段。 | 工具响应由 LLM 模拟；审计准确率不等于状态转移的确定性保证。 |
| [DreamGym](https://arxiv.org/abs/2511.03773) | 2025-11-05 | [详情](docs/catalog_details_zh.md#dreamgym--paper-dreamgym) | 结合推理式经验模型、回放缓冲区与自适应任务生成，通过合成交互训练代理。 | RL 实验: 模拟观察或任务成功奖励；真实环境迁移另行评测。 | 从模拟到现实的迁移是经验结果；第三方复现不能当作作者官方代码。 |

**仓库**

| 项目 | 链接 | Stars | 标签 | 摘要 |
| --- | --- | --- | --- | --- |
| GenEnv | [GitHub](https://github.com/Gen-Verse/GenEnv) · [详情](docs/catalog_details_zh.md#genenv--project-genenv) | ★ 67 | neural, rl | 通过难度对齐的课程奖励，共同演化生成式模拟器与代理。 |
| WebWorld | [GitHub](https://github.com/QwenLM/WebWorld) · [详情](docs/catalog_details_zh.md#webworld--project-webworld) | ★ 61 | neural, sft | 从交互轨迹学习开放网页模拟器，并用模拟 rollout 训练和规划网页代理。 |
| EnvACE | [GitHub](https://github.com/Within-yao/EnvACE) · [详情](docs/catalog_details_zh.md#envace--project-envace) | ★ 24 | neural, rl | 用按角色计算的 RL 信号训练共享策略，让它既执行动作又模拟环境响应，从而内化动态。 |
| SynthTools | [GitHub](https://github.com/namkoong-lab/SynthTools) · [详情](docs/catalog_details_zh.md#synthtools--project-synthtools) | ★ 9 | neural, generation | 分离合成工具生成、响应模拟和工具审计，以扩展可控工具生态。 |

**博客**

| 文章 | 发布方 | 日期 | 摘要 | 证据 |
| --- | --- | --- | --- | --- |
| [Genie 3: A new frontier for world models](https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/) | Google DeepMind | 2025-08-05 | 由提示生成可交互视觉世界，供探索与 Agent 研究。 | [详情](docs/catalog_details_zh.md#genie-3-a-new-frontier-for-world-models--blog-deepmind-genie3) |
| [Genie 2: A large-scale foundation world model](https://deepmind.google/blog/genie-2-a-large-scale-foundation-world-model/) | Google DeepMind | 2024-12-04 | 由单张图生成可响应键鼠动作的交互世界，并从同一起始帧产生不同动作轨迹，服务 agent 训练与评测。 | [详情](docs/catalog_details_zh.md#genie-2-a-large-scale-foundation-world-model--blog-deepmind-genie2) |

## 交互数据与经验生产

### 探索、回放与反向合成

**论文**

| 论文 | 日期 | 资源 | 环境／任务贡献 | 质量保障 | 代码情况 |
| --- | --- | --- | --- | --- | --- |
| [TerminalWorld (recordings)](https://arxiv.org/abs/2605.22535) | 2026-05-21 | [代码](https://github.com/EuniAI/TerminalWorld) · [详情](docs/catalog_details_zh.md#terminalworld-recordings--paper-terminalworld-recordings) | 从真实终端录制反向还原可复现环境、可执行任务及经过验证的基准实例。 | 评测环境: 自动还原与验证，并单独提供经过人工核验的基准子集。 | 与技能驱动的 Terminal-World 不同；自动验证集和人工核验子集的证据强度不同。 |
| [CLI-Gym](https://arxiv.org/abs/2602.10999) | 2026-02-11 | [代码](https://github.com/LiberCoders/CLI-Gym) · [详情](docs/catalog_details_zh.md#cli-gym--paper-cli-gym) | 探索健康环境的历史并反转为可复现运行故障，再打包修复任务及成功轨迹。 | SFT／轨迹训练: 用初末状态或 fail-to-pass 测试检查执行，参考解用于验证可解性。 | 在已有仓库上构造环境修复任务；任务实例数大于仓库／镜像数，不能混计。 |
| [InSTA](https://arxiv.org/abs/2502.06776) | 2025-02-10 | [代码](https://github.com/data-for-agents/insta) · [详情](docs/catalog_details_zh.md#insta--paper-insta) | 为网站自动标注任务、执行智能体并过滤成功轨迹，规模化构建网页交互数据。 | SFT／轨迹训练: 用 LLM 判断任务成功并筛选采集的浏览器轨迹。 | 仍受线上网站变化与模型判定误差影响；网站数量不等于新合成环境数量。 |
| [OS-Genesis](https://arxiv.org/abs/2412.19723) | 2024-12-27 | [代码](https://github.com/OS-Copilot/OS-Genesis) · [详情](docs/catalog_details_zh.md#os-genesis--paper-os-genesis) | 先探索 GUI 环境，再反向合成任务，并用轨迹奖励模型筛选交互质量。 | SFT／轨迹训练: 检查反向合成任务与交互的一致性，以轨迹奖励模型做质量筛选。 | 主要在已有桌面／移动环境上构造任务与轨迹，不是新操作系统模拟器。 |
| [AgentTrek](https://arxiv.org/abs/2412.09605) | 2024-12-12 | [代码](https://github.com/xlang-ai/AgentTrek) · [轨迹数据集](https://huggingface.co/datasets/xlangai/AgentTrek) · [详情](docs/catalog_details_zh.md#agenttrek--paper-agenttrek) | 采集网页教程并提炼任务指令，引导浏览器回放，再筛选用于训练的轨迹。 | SFT／轨迹训练: 教程指导的浏览器回放，配合模型对轨迹进行验证。 | 教程回放利用已有网站，不代表生成独立网站后端；模型判定也可能出错。 |

**仓库**

| 项目 | 链接 | Stars | 标签 | 摘要 |
| --- | --- | --- | --- | --- |
| OS-Genesis | [GitHub](https://github.com/OS-Copilot/OS-Genesis) · [详情](docs/catalog_details_zh.md#os-genesis--project-os-genesis) | ★ 190 | replay-exploration | 先探索 GUI 环境，再反向合成任务，并用轨迹奖励模型筛选交互质量。 |
| CLI-Gym | [GitHub](https://github.com/LiberCoders/CLI-Gym) · [详情](docs/catalog_details_zh.md#cli-gym--project-cli-gym) | ★ 141 | replay-exploration | 探索健康环境的历史并反转为可复现运行故障，再打包修复任务及成功轨迹。 |
| AgentTrek | [GitHub](https://github.com/xlang-ai/AgentTrek) · [详情](docs/catalog_details_zh.md#agenttrek--project-agenttrek) | ★ 60 | replay-exploration | 采集网页教程并提炼任务指令，引导浏览器回放，再筛选用于训练的轨迹。 |
| InSTA | [GitHub](https://github.com/data-for-agents/insta) · [详情](docs/catalog_details_zh.md#insta--project-insta) | ★ 56 | replay-exploration | 为网站自动标注任务、执行智能体并过滤成功轨迹，规模化构建网页交互数据。 |
| TerminalWorld (recordings) | [GitHub](https://github.com/EuniAI/TerminalWorld) · [详情](docs/catalog_details_zh.md#terminalworld-recordings--project-terminalworld-recordings) | ★ 48 | replay-exploration | 从真实终端录制反向还原可复现环境、可执行任务及经过验证的基准实例。 |

### 轨迹筛选与数据配方

**论文**

| 论文 | 日期 | 资源 | 环境／任务贡献 | 质量保障 | 代码情况 |
| --- | --- | --- | --- | --- | --- |
| [OpenThoughts-Agent](https://arxiv.org/abs/2606.24855) | 2026-06-23 | [代码](https://github.com/open-thoughts/OpenThoughts-Agent) · [详情](docs/catalog_details_zh.md#openthoughts-agent--paper-openthoughts-agent) | 通过控制实验研究任务来源、混合比例、教师、rollout 与过滤策略，形成终端智能体数据配方。 | SFT／轨迹训练: 控制任务来源、教师与过滤策略做消融；早期 RL 配方还在沙箱中验证任务。 | 2025 年发布博客和 2026 年论文属于不同发布阶段；结果取决于完整数据配方。 |

**仓库**

| 项目 | 链接 | Stars | 标签 | 摘要 |
| --- | --- | --- | --- | --- |
| OpenThoughts-Agent | [GitHub](https://github.com/open-thoughts/OpenThoughts-Agent) · [详情](docs/catalog_details_zh.md#openthoughts-agent--project-openthoughts-agent) | ★ 301 | data-curation | 通过控制实验研究任务来源、混合比例、教师、rollout 与过滤策略，形成终端智能体数据配方。 |

**博客**

| 文章 | 发布方 | 日期 | 摘要 | 证据 |
| --- | --- | --- | --- | --- |
| [General Agent: A Self-Evolving, Synthetic Agent Environment](https://www.primeintellect.ai/blog/general-agent) | Prime Intellect | 2026-05-18 | 通过合成者与求解者交互，生成数据库工具任务、参考解与校准难度区间。 | [详情](docs/catalog_details_zh.md#general-agent-a-self-evolving-synthetic-agent-environment--blog-general-agent) |
| [Launching OpenThoughts-Agent](https://www.openthoughts.ai/blog/agent) | OpenThoughts team | 2025-12-05 | 介绍早期任务／教师消融、SFT 轨迹，以及经过执行筛选的 NL2Bash RL 数据流水线。 | [详情](docs/catalog_details_zh.md#launching-openthoughts-agent--blog-openthoughts-agent) |

### 轨迹采集与检查

**博客**

| 文章 | 发布方 | 日期 | 摘要 | 证据 |
| --- | --- | --- | --- | --- |
| [Tracing Agent Harness Behavior with NVIDIA NeMo Relay](https://developer.nvidia.com/blog/?p=123038) | NVIDIA / Hermes contributors | 2026-09-30 | 展示有序事件与轨迹采集，并与任务验证结果、harness 行为对比结合分析。 | [详情](docs/catalog_details_zh.md#tracing-agent-harness-behavior-with-nvidia-nemo-relay--blog-nemo-relay-tracing) |

## 环境基础设施

### 接口、适配器与注册库

**论文**

| 论文 | 日期 | 资源 | 环境／任务贡献 | 质量保障 | 代码情况 |
| --- | --- | --- | --- | --- | --- |
| [GEM](https://arxiv.org/abs/2510.01051) | 2025-10-01 | [代码](https://github.com/axon-rl/gem) · [详情](docs/catalog_details_zh.md#gem--paper-gem) | 提供统一代理环境 API、异步向量化执行和多环境接入 RL 训练器的示例。 | RL 实验: 任务奖励与正确性由环境作者或接入库定义。 | 不同训练器的奖励时序与逐轮归因不同；不能忽略语义直接替换适配器。 |
| [Meta ARE](https://arxiv.org/abs/2509.17158) | 2025-09-21 | [代码](https://github.com/facebookresearch/meta-agents-research-environments) · [详情](docs/catalog_details_zh.md#meta-are--paper-are) | 将应用、事件与场景分离，模拟动态世界并在异步变化下评测代理。 | 评测环境: 任务奖励与正确性由环境作者或接入库定义。 | ARE 与 OpenEnv 不同；Gaia2 结果主要说明评测行为，而非已发布 RL 训练配方。 |
| [AgentGym-RL](https://arxiv.org/abs/2509.08755) | 2025-09-10 | [代码](https://github.com/WooooDyy/AgentGym-RL) · [详情](docs/catalog_details_zh.md#agentgym-rl--paper-agentgym-rl) | 解耦训练与环境服务，通过逐步扩大交互时长进行多轮 RL。 | RL 实验: 任务奖励与正确性由环境作者或接入库定义。 | 需要逐个配置底层环境及其服务，并非无依赖的单体模拟器。 |
| [AgentGym](https://arxiv.org/abs/2406.04151) | 2024-06-06 | [代码](https://github.com/WooooDyy/AgentGym) · [详情](docs/catalog_details_zh.md#agentgym--paper-agentgym) | 标准化多类环境服务与轨迹，支持通用代理探索及迭代学习。 | SFT／轨迹训练: 任务奖励与正确性由环境作者或接入库定义。 | 原始 AgentEvol 研究与后续 AgentGym-RL 发布使用不同学习流程。 |

**仓库**

| 项目 | 链接 | Stars | 标签 | 摘要 |
| --- | --- | --- | --- | --- |
| Verifiers | [GitHub](https://github.com/PrimeIntellect-ai/verifiers) · [详情](docs/catalog_details_zh.md#verifiers--project-verifiers) | ★ 4,679 | framework, rollout | 用可组合任务集、harness、rubric 和运行时构建训练及评测环境。 |
| OpenEnv | [GitHub](https://github.com/huggingface/OpenEnv) · [详情](docs/catalog_details_zh.md#openenv--project-openenv) | ★ 2,674 | framework, rollout | 通过 Gym 风格 API 和远程服务统一隔离环境的部署与交互。 |
| NeMo Gym | [GitHub](https://github.com/NVIDIA-NeMo/Gym) · [详情](docs/catalog_details_zh.md#nemo-gym--project-nemo-gym) | ★ 1,225 | framework, rollout | 为代理后训练提供环境服务、验证器、沙箱适配和可扩展 rollout 采集。 |
| AgentGym-RL | [GitHub](https://github.com/WooooDyy/AgentGym-RL) · [详情](docs/catalog_details_zh.md#agentgym-rl--project-agentgym-rl) | ★ 874 | mixed, rl | 解耦训练与环境服务，通过逐步扩大交互时长进行多轮 RL。 |
| AgentGym | [GitHub](https://github.com/WooooDyy/AgentGym) · [详情](docs/catalog_details_zh.md#agentgym--project-agentgym) | ★ 850 | mixed, sft | 标准化多类环境服务与轨迹，支持通用代理探索及迭代学习。 |
| Meta ARE | [GitHub](https://github.com/facebookresearch/meta-agents-research-environments) · [详情](docs/catalog_details_zh.md#meta-are--project-are) | ★ 561 | mixed, evaluation | 将应用、事件与场景分离，模拟动态世界并在异步变化下评测代理。 |
| GEM | [GitHub](https://github.com/axon-rl/gem) · [详情](docs/catalog_details_zh.md#gem--project-gem) | ★ 510 | mixed, rl | 提供统一代理环境 API、异步向量化执行和多环境接入 RL 训练器的示例。 |
| AgentEnv (Scale) | [GitHub](https://github.com/scaleapi/agentenv-framework) · [详情](docs/catalog_details_zh.md#agentenv-scale--project-scale-agentenv) | ★ 165 | framework, rollout | 提供版本化环境镜像、可组合任务执行、插件与代理评分的 SDK 和 CLI。 |

**博客**

| 文章 | 发布方 | 日期 | 摘要 | 证据 |
| --- | --- | --- | --- | --- |
| [Introducing AgentEnv: An Open-Source Framework for Building RL Environments](https://labs.scale.com/blog/introducing-agentenv) | Scale Labs | 2026-10-05 | 介绍可复用环境块、数据工件、世界规则和任务 DAG，以及跨代理和沙箱的执行方式。 | [详情](docs/catalog_details_zh.md#introducing-agentenv-an-open-source-framework-for-building-rl-environments--blog-scale-agentenv) |
| [Welcome RL Environments to the hub](https://huggingface.co/blog/rl-environments) | Hugging Face | 2026-09-28 | 通过数据集标签和框架兼容元数据，在 Hub 发现与版本化 RL 任务集。 | [详情](docs/catalog_details_zh.md#welcome-rl-environments-to-the-hub--blog-hf-env-hub) |
| [Multi-Agent Systems in PRIME-RL](https://www.primeintellect.ai/blog/multi-agent-systems) | Prime Intellect | 2026-08-07 | 为自博弈、用户模拟与评判增加可编程代理交互、学习角色选择及归因。 | [详情](docs/catalog_details_zh.md#multi-agent-systems-in-prime-rl--blog-multi-agent-rl) |
| [Training a coding agent using the OpenCode harness in remote HF sandboxes with TRL and OpenEnv](https://huggingface.co/blog/sergiopaniego/trl-openenv-harness-training) | Sergio Paniego / author technical blog | 2026-08-05 | 展示每个 rollout 独立沙箱、代理捕获精确 token 轨迹，以及基于工作区评分的 AsyncGRPO。 | [详情](docs/catalog_details_zh.md#training-a-coding-agent-using-the-opencode-harness-in-remote-hf-sandboxes-with-trl-and-openenv--blog-trl-openenv) |
| [Scaling Agentic RL: 365,000+ Environments for SWE, Terminal, and Search](https://www.primeintellect.ai/blog/scaling-agentic-rl) | Prime Intellect | 2026-07-22 | 统一任务集生命周期与沙箱，保留上游评分逻辑，并在 rollout 期间隔离评分材料。 | [详情](docs/catalog_details_zh.md#scaling-agentic-rl-365000-environments-for-swe-terminal-and-search--blog-prime-scale) |
| [verifiers v1: Decomposing Tasksets and Harnesses for Agentic RL & Evaluations](https://www.primeintellect.ai/blog/verifiers-v1) | Prime Intellect | 2026-07-12 | 分离任务集、harness 和运行时，同时保留分支轨迹及训练 token。 | [详情](docs/catalog_details_zh.md#verifiers-v1-decomposing-tasksets-and-harnesses-for-agentic-rl--evaluations--blog-verifiers-v1) |
| [The Open Source Community is backing OpenEnv for Agentic RL](https://huggingface.co/blog/openenv-agentic-rl) | OpenEnv contributors / Hugging Face | 2026-06-08 | 明确 OpenEnv 是连接环境库、代理 harness 与训练器的互操作层。 | [详情](docs/catalog_details_zh.md#the-open-source-community-is-backing-openenv-for-agentic-rl--blog-openenv-community) |
| [Scaling OpenEnv: From Free Usage to Thousands of Concurrent Environments](https://huggingface.co/blog/burtenshaw/openenv-scaling) | Ben Burtenshaw / author technical blog | 2026-01-20 | 比较从 Spaces、Docker 到集群的环境会话并发部署方案。 | [详情](docs/catalog_details_zh.md#scaling-openenv-from-free-usage-to-thousands-of-concurrent-environments--blog-openenv-scaling) |
| [How to Train Scientific Agents with Reinforcement Learning](https://developer.nvidia.com/blog/how-to-train-scientific-agents-with-reinforcement-learning/) | NVIDIA / Edison Scientific | 2025-12-15 | 以 Aviary 为例介绍模型、资源和代理服务，构建并验证科学任务 rollout。 | [详情](docs/catalog_details_zh.md#how-to-train-scientific-agents-with-reinforcement-learning--blog-nemo-science) |
| [The Building Blocks of Agentic AI: From Kernels to Clusters](https://ai.meta.com/blog/introducing-pytorch-native-agentic-stack/) | Meta | 2025-10-24 | OpenEnv 小节介绍共享环境 Hub、工具／观测接口，以及训练前由人或模型直接交互验证环境。 | [详情](docs/catalog_details_zh.md#the-building-blocks-of-agentic-ai-from-kernels-to-clusters--blog-meta-openenv) |
| [Building the Open Agent Ecosystem Together: Introducing OpenEnv](https://huggingface.co/blog/openenv) | Meta-PyTorch / Hugging Face | 2025-10-23 | 介绍代理交互的环境契约、容器打包及共享中心。 | [详情](docs/catalog_details_zh.md#building-the-open-agent-ecosystem-together-introducing-openenv--blog-openenv-launch) |
| [Environments Hub: A Community Hub To Scale RL To Open AGI](https://www.primeintellect.ai/blog/environments) | Prime Intellect | 2025-08-27 | 介绍将任务、反馈与训练接入打包为可发布复用的 verifiers 环境。 | [详情](docs/catalog_details_zh.md#environments-hub-a-community-hub-to-scale-rl-to-open-agi--blog-environments-hub) |

### 沙箱与交互执行

**论文**

| 论文 | 日期 | 资源 | 环境／任务贡献 | 质量保障 | 代码情况 |
| --- | --- | --- | --- | --- | --- |
| [DeepSeek Elastic Compute (DSec)](https://arxiv.org/abs/2609.22978) | 2026-09-19 | [详情](docs/catalog_details_zh.md#deepseek-elastic-compute-dsec--paper-dsec) | 统一函数调用、容器、microVM 与完整 VM；支持 Agent 构建可复用环境，以及长交互任务的挂起和恢复。 | 环境基础设施: 环境构建、隔离与生命周期管理的系统证据；不是独立任务 benchmark。 | 生产基础设施论文；未确认官方公开的 DSec 完整实现，3FS 等关联项目不等于 DSec 平台。 |

**仓库**

| 项目 | 链接 | Stars | 标签 | 摘要 |
| --- | --- | --- | --- | --- |
| Harbor | [GitHub](https://github.com/harbor-framework/harbor) · [详情](docs/catalog_details_zh.md#harbor--project-harbor) | ★ 5,891 | framework, rollout | 跨代理与沙箱提供方运行容器化任务，支持并行评测和 RL rollout 生成。 |
| MiMo-V2.6 RL OSS Environments (XiaomiMiMo/verl) | [GitHub](https://github.com/XiaomiMiMo/verl) · [RL OSS 数据](https://huggingface.co/datasets/XiaomiMiMo/MiMo-V2.6-RL-oss) · [Docker 镜像](https://hub.docker.com/r/xiaomimimo/mimo-v2.6-rl-oss) · [技术报告（配套）](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL/blob/main/MiMo_V2_6_technical_report.pdf) · [社区 Explorer（非官方）](https://huggingface.co/spaces/FineEnvs/MiMo-RL-Envs-Explorer) · [详情](docs/catalog_details_zh.md#mimo-v26-rl-oss-environments-xiaomimimoverl--project-xiaomi-mimo-verl) | ★ 666 | agentic-rl, multi-domain, mimo-oss | 在 verl 分支发布五类 RL 环境配方，关联任务数据、Docker 镜像和验证器。 |
| MiMo Agent (mimoagent) | [GitHub](https://github.com/XiaomiMiMo/mimoagent) · [详情](docs/catalog_details_zh.md#mimo-agent-mimoagent--project-xiaomi-mimoagent) | ★ 39 | agentic-rl, multi-domain, mimo-oss | 分离代理、模型协议、执行后端和数据评分器，记录训练轨迹并对环境终态评分。 |

**博客**

| 文章 | 发布方 | 日期 | 摘要 | 证据 |
| --- | --- | --- | --- | --- |
| [Prime Sandboxes: MicroVMs for Agentic RL Training at Scale](https://www.primeintellect.ai/blog/sandboxes) | Prime Intellect | 2026-09-23 | 介绍基于虚拟机的 rollout 隔离、镜像复用及大规模训练环境并发。 | [详情](docs/catalog_details_zh.md#prime-sandboxes-microvms-for-agentic-rl-training-at-scale--blog-prime-sandboxes) |
| [Custom reward functions for multi-turn reinforcement learning with Amazon Nova Forge](https://aws.amazon.com/blogs/machine-learning/custom-reward-functions-for-multi-turn-reinforcement-learning-with-amazon-nova-forge/) | Amazon / AWS | 2026-08-14 | BYOO 容器管理多轮状态、用户模拟、代码执行和 verifier，再将完整 episode 与聚合奖励送回训练。 | [详情](docs/catalog_details_zh.md#custom-reward-functions-for-multi-turn-reinforcement-learning-with-amazon-nova-forge--blog-aws-nova-rewards) |
| [Deploying Multi-Turn RL Infrastructure for Amazon Nova on Amazon SageMaker HyperPod](https://aws.amazon.com/blogs/machine-learning/deploying-multi-turn-rl-infrastructure-for-amazon-nova-on-amazon-sagemaker-hyperpod/) | Amazon / AWS | 2026-07-06 | 以 Wordle 为例分离 HyperPod 训练、ECS 奖励环境和有状态消息路由，并管理每轮训练的临时资源。 | [详情](docs/catalog_details_zh.md#deploying-multi-turn-rl-infrastructure-for-amazon-nova-on-amazon-sagemaker-hyperpod--blog-aws-nova-infra) |
| [Introducing SWE-1.5: Our Fast Agent Model](https://cognition.com/blog/swe-1-5) | Cognition | 2025-10-29 | 披露在 Cascade harness 下执行真实任务 RL，并用 otterlink VM 支持代码执行、浏览和高并发，贴近 Devin 生产环境。 | [详情](docs/catalog_details_zh.md#introducing-swe-15-our-fast-agent-model--blog-cognition-swe15) |

## 领域环境与评测基准

### 软件、终端与可执行技能

**论文**

| 论文 | 日期 | 资源 | 环境／任务贡献 | 质量保障 | 代码情况 |
| --- | --- | --- | --- | --- | --- |
| [SkillScriptBench](https://arxiv.org/abs/2610.04008) | 2026-10-02 | [详情](docs/catalog_details_zh.md#skillscriptbench--paper-skillscriptbench) | 构造可执行技能包测试，包含脚本故障注入及受控的包编辑场景。 | 评测环境: 通过受控故障注入及可执行包编辑测试，区分脚本修复和文档修改。 | 属于可执行技能修复基准，而非通用世界生成器；未找到官方代码。 |
| [Terminal-Bench](https://arxiv.org/abs/2601.11868) | 2026-01-17 | [代码](https://github.com/harbor-framework/terminal-bench) · [详情](docs/catalog_details_zh.md#terminal-bench--paper-terminal-bench) | 将真实终端任务与隔离执行环境、参考解和结果测试打包。 | 评测环境: 任务专属执行测试或验证器评分；具体划分以各项来源为准。 | 本论文描述 Terminal-Bench 2.0；评测任务必须与训练数据隔离。 |

**仓库**

| 项目 | 链接 | Stars | 标签 | 摘要 |
| --- | --- | --- | --- | --- |
| Terminal-Bench | [GitHub](https://github.com/harbor-framework/terminal-bench) · [详情](docs/catalog_details_zh.md#terminal-bench--project-terminal-bench) | ★ 852 | executable, evaluation | 将真实终端任务与隔离执行环境、参考解和结果测试打包。 |

**博客**

| 文章 | 发布方 | 日期 | 摘要 | 证据 |
| --- | --- | --- | --- | --- |
| [Introducing SWE-bench Verified](https://openai.com/index/introducing-swe-bench-verified/) | OpenAI | 2024-08-13 | 通过人工核查题意、测试有效性与可解性，筛选 SWE-bench 任务；配合 Docker 执行环境提高评测可靠性。 | [详情](docs/catalog_details_zh.md#introducing-swe-bench-verified--blog-openai-swe-verified) |

### 浏览器、桌面与移动端

**论文**

| 论文 | 日期 | 资源 | 环境／任务贡献 | 质量保障 | 代码情况 |
| --- | --- | --- | --- | --- | --- |
| [BrowserGym](https://arxiv.org/abs/2412.05467) | 2024-12-06 | [代码](https://github.com/ServiceNow/BrowserGym) · [详情](docs/catalog_details_zh.md#browsergym--paper-browsergym) | 统一浏览器观察、动作和基准接口，配合 AgentLab 管理实验。 | 评测环境: 交互后的状态、产物或 rubric 评估，具体类型依任务而异。 | 统一接口不意味着其中每个基准都可作为训练集。 |
| [AndroidWorld](https://arxiv.org/abs/2405.14573) | 2024-05-23 | [代码](https://github.com/google-research/android_world) · [详情](docs/catalog_details_zh.md#androidworld--paper-androidworld) | 在 Android 模拟器中提供可参数化任务、初始化和基于状态的成功检查。 | 评测环境: 交互后的状态、产物或 rubric 评估，具体类型依任务而异。 | 应用版本与模拟器配置影响复现；基准成功率不是训练效果证据。 |
| [OSWorld](https://arxiv.org/abs/2404.07972) | 2024-04-11 | [代码](https://github.com/xlang-ai/OSWorld) · [详情](docs/catalog_details_zh.md#osworld--paper-osworld) | 提供真实桌面任务初始化与跨应用的执行式评估器。 | 评测环境: 交互后的状态、产物或 rubric 评估，具体类型依任务而异。 | GUI 执行昂贵且依赖平台；评测划分不应直接转为 RL 练习数据。 |
| [WebArena](https://arxiv.org/abs/2307.13854) | 2023-07-25 | [代码](https://github.com/web-arena-x/webarena) · [详情](docs/catalog_details_zh.md#webarena--paper-webarena) | 托管可复现网站并检查任务结果，评测真实多步网页操作。 | 评测环境: 交互后的状态、产物或 rubric 评估，具体类型依任务而异。 | 必须维护网站重置及部署镜像，并控制公开测试任务的污染。 |

**仓库**

| 项目 | 链接 | Stars | 标签 | 摘要 |
| --- | --- | --- | --- | --- |
| OSWorld | [GitHub](https://github.com/xlang-ai/OSWorld) · [详情](docs/catalog_details_zh.md#osworld--project-osworld) | ★ 3,179 | desktop, evaluation | 提供真实桌面任务初始化与跨应用的执行式评估器。 |
| WebArena | [GitHub](https://github.com/web-arena-x/webarena) · [详情](docs/catalog_details_zh.md#webarena--project-webarena) | ★ 1,619 | browser, evaluation | 托管可复现网站并检查任务结果，评测真实多步网页操作。 |
| BrowserGym | [GitHub](https://github.com/ServiceNow/BrowserGym) · [详情](docs/catalog_details_zh.md#browsergym--project-browsergym) | ★ 1,390 | browser, evaluation | 统一浏览器观察、动作和基准接口，配合 AgentLab 管理实验。 |
| AndroidWorld | [GitHub](https://github.com/google-research/android_world) · [详情](docs/catalog_details_zh.md#androidworld--project-androidworld) | ★ 945 | mobile, evaluation | 在 Android 模拟器中提供可参数化任务、初始化和基于状态的成功检查。 |
| benchmark | [GitHub](https://github.com/browser-use/benchmark) · [详情](docs/catalog_details_zh.md#benchmark--project-browser-use-bench) | ★ 149 | gui-bench | 介绍 BU Bench 的真实网页任务筛选、加密测试分发和模型成功判定。 |

**博客**

| 文章 | 发布方 | 日期 | 摘要 | 证据 |
| --- | --- | --- | --- | --- |
| [Browser Use benchmark construction](https://browser-use.com/posts/ai-browser-agent-benchmark) | Browser Use | 2026-01-31 | 介绍 BU Bench 的真实网页任务筛选、加密测试分发和模型成功判定。 | [详情](docs/catalog_details_zh.md#browser-use-benchmark-construction--blog-browser-use-bench) |

### 工具与企业工作流

**论文**

| 论文 | 日期 | 资源 | 环境／任务贡献 | 质量保障 | 代码情况 |
| --- | --- | --- | --- | --- | --- |
| [MM-ToolSandBox](https://arxiv.org/abs/2607.11818) | 2026-07-13 | [代码](https://github.com/apple-aiml-research/ml-mmtoolsandbox) · [详情](docs/catalog_details_zh.md#mm-toolsandbox--paper-mm-toolsandbox) | 将有状态工具评测扩展到视觉输入、场景生成和多轮状态变化。 | 评测环境: 任务状态、轨迹里程碑或 rubric 评估。 | 这是视觉工具调用基准，不代表已完成 RL 训练；图像信息提取错误需单独分析。 |
| [C-World (formerly ToolGym)](https://arxiv.org/abs/2601.06328) | 2026-01-09 | [代码](https://github.com/Ziqiao-git/C-World) · [详情](docs/catalog_details_zh.md#c-world-formerly-toolgym--paper-c-world) | 生成计算机工具使用环境，包含任务生成、可扰动转移以及真实执行或模拟工具响应。 | SFT／轨迹训练: 任务状态、轨迹里程碑或 rubric 评估。 | 当前论文已改名 C-World，项目页与 README 仍保留 ToolGym 名称；真实 API 与模拟模式需区分，评分使用模型评审。 |
| [τ²-bench](https://arxiv.org/abs/2506.07982) | 2025-06-09 | [代码](https://github.com/sierra-research/tau2-bench) · [详情](docs/catalog_details_zh.md#τ²-bench--paper-tau2) | 建模助手与模拟用户共同修改的状态，提供组合任务与结果评估。 | 评测环境: 共享世界任务结果及规则遵循检查。 | 用户模拟器行为影响结果；基准任务应作为留出评测，而非直接训练数据。 |
| [TheAgentCompany](https://arxiv.org/abs/2412.14161) | 2024-12-18 | [代码](https://github.com/TheAgentCompany/TheAgentCompany) · [详情](docs/catalog_details_zh.md#theagentcompany--paper-theagentcompany) | 构建由网站、文件和模拟同事组成的自包含工作场所，评测长程职业任务。 | 评测环境: 任务状态、轨迹里程碑或 rubric 评估。 | 工作场所基准本身不保证新任务的训练评测隔离或可靠 RL 奖励。 |
| [ToolSandbox](https://arxiv.org/abs/2408.04682) | 2024-08-08 | [代码](https://github.com/apple-aiml-research/ToolSandbox) · [详情](docs/catalog_details_zh.md#toolsandbox--paper-toolsandbox) | 结合有状态工具执行、用户模拟与整段对话轨迹上的里程碑检查。 | 评测环境: 轨迹中间里程碑与最终状态。 | 有状态评测基础设施可复用，但论文主要证据是评测，而非策略训练。 |
| [AppWorld](https://arxiv.org/abs/2407.18901) | 2024-07-26 | [代码](https://github.com/StonyBrookNLP/appworld) · [详情](docs/catalog_details_zh.md#appworld--paper-appworld) | 通过可执行 API 模拟互联个人应用，检查最终状态及非预期副作用。 | 评测环境: 基于状态的单元测试，包含副作用检查。 | 训练、开发和测试任务及软件、数据许可各有边界，需遵循官方划分政策。 |
| [WorkArena](https://arxiv.org/abs/2403.07718) | 2024-03-12 | [代码](https://github.com/ServiceNow/WorkArena) · [详情](docs/catalog_details_zh.md#workarena--paper-workarena) | 将 ServiceNow 工作流转为浏览器任务，以程序化方式验证企业操作。 | 评测环境: 任务状态、轨迹里程碑或 rubric 评估。 | 需要合适的 ServiceNow 实例和凭据，并非完全离线自包含模拟器。 |
| [WebShop](https://arxiv.org/abs/2207.01206) | 2022-07-04 | [代码](https://github.com/princeton-nlp/WebShop) · [详情](docs/catalog_details_zh.md#webshop--paper-webshop) | 构建带自然语言目标和商品属性奖励的购物环境，用于交互学习。 | RL 实验: 任务状态、轨迹里程碑或 rubric 评估。 | 商品目录与网站行为经过简化；购物成功率衡量的能力范围较窄。 |

**仓库**

| 项目 | 链接 | Stars | 标签 | 摘要 |
| --- | --- | --- | --- | --- |
| τ²-bench | [GitHub](https://github.com/sierra-research/tau2-bench) · [详情](docs/catalog_details_zh.md#τ²-bench--project-tau2) | ★ 2,181 | executable, evaluation | 建模助手与模拟用户共同修改的状态，提供组合任务与结果评估。 |
| TheAgentCompany | [GitHub](https://github.com/TheAgentCompany/TheAgentCompany) · [详情](docs/catalog_details_zh.md#theagentcompany--project-theagentcompany) | ★ 792 | mixed, evaluation | 构建由网站、文件和模拟同事组成的自包含工作场所，评测长程职业任务。 |
| WebShop | [GitHub](https://github.com/princeton-nlp/WebShop) · [详情](docs/catalog_details_zh.md#webshop--project-webshop) | ★ 602 | browser, rl | 构建带自然语言目标和商品属性奖励的购物环境，用于交互学习。 |
| AppWorld | [GitHub](https://github.com/StonyBrookNLP/appworld) · [详情](docs/catalog_details_zh.md#appworld--project-appworld) | ★ 529 | executable, evaluation | 通过可执行 API 模拟互联个人应用，检查最终状态及非预期副作用。 |
| ToolSandbox | [GitHub](https://github.com/apple-aiml-research/ToolSandbox) · [详情](docs/catalog_details_zh.md#toolsandbox--project-toolsandbox) | ★ 287 | executable, evaluation | 结合有状态工具执行、用户模拟与整段对话轨迹上的里程碑检查。 |
| WorkArena | [GitHub](https://github.com/ServiceNow/WorkArena) · [详情](docs/catalog_details_zh.md#workarena--project-workarena) | ★ 274 | browser, evaluation | 将 ServiceNow 工作流转为浏览器任务，以程序化方式验证企业操作。 |
| MM-ToolSandBox | [GitHub](https://github.com/apple-aiml-research/ml-mmtoolsandbox) · [详情](docs/catalog_details_zh.md#mm-toolsandbox--project-mm-toolsandbox) | ★ 29 | executable, evaluation | 将有状态工具评测扩展到视觉输入、场景生成和多轮状态变化。 |
| C-World (formerly ToolGym) | [GitHub](https://github.com/Ziqiao-git/C-World) · [详情](docs/catalog_details_zh.md#c-world-formerly-toolgym--project-c-world) | ★ 10 | mixed, sft | 生成计算机工具使用环境，包含任务生成、可扰动转移以及真实执行或模拟工具响应。 |

**博客**

| 文章 | 发布方 | 日期 | 摘要 | 证据 |
| --- | --- | --- | --- | --- |
| [OpenEnv in Practice: Evaluating Tool-Using Agents in Real-World Environments](https://huggingface.co/blog/openenv-turing) | Turing / Hugging Face | 2026-02-12 | 用日历任务揭示工具环境中的状态、权限、时间推理和故障恢复要求。 | [详情](docs/catalog_details_zh.md#openenv-in-practice-evaluating-tool-using-agents-in-real-world-environments--blog-calendar-gym) |
| [Scaling Enterprise Agent Performance with Reinforcement Learning via Verifiable Feedback Loops](https://labs.scale.com/blog/scaling-enterprise-agent-performance-with-reinforcement-learning-via-verifiable-feedback-loops) | Scale Labs | 2025-11-17 | 讨论领域 SQL 与企业推理训练中的环境设计和可验证反馈。 | [详情](docs/catalog_details_zh.md#scaling-enterprise-agent-performance-with-reinforcement-learning-via-verifiable-feedback-loops--blog-scale-enterprise) |

### 游戏与交互推理

**论文**

| 论文 | 日期 | 资源 | 环境／任务贡献 | 质量保障 | 代码情况 |
| --- | --- | --- | --- | --- | --- |
| [TextArena](https://arxiv.org/abs/2504.11442) | 2025-04-15 | [代码](https://github.com/TextArena/TextArena) · [详情](docs/catalog_details_zh.md#textarena--paper-textarena) | 将文字游戏、规则、多玩家交互和奖励接口打包，用于代理训练与评测。 | 可训练接口: 任务参考答案或游戏规则决定的结果。 | 胜率依赖对手与规则，不能直接衡量工作场景能力。 |

**仓库**

| 项目 | 链接 | Stars | 标签 | 摘要 |
| --- | --- | --- | --- | --- |
| TextArena | [GitHub](https://github.com/TextArena/TextArena) · [详情](docs/catalog_details_zh.md#textarena--project-textarena) | ★ 430 | game, rl-ready | 将文字游戏、规则、多玩家交互和奖励接口打包，用于代理训练与评测。 |

**博客**

| 文章 | 发布方 | 日期 | 摘要 | 证据 |
| --- | --- | --- | --- | --- |
| [SIMA 2: An agent that plays, reasons, and learns with you in virtual 3D worlds](https://deepmind.google/blog/sima-2-an-agent-that-plays-reasons-and-learns-with-you-in-virtual-3d-worlds/) | Google DeepMind | 2025-11-13 | 利用多样虚拟世界开展具身交互，并考察向 Genie 生成世界的泛化。 | [详情](docs/catalog_details_zh.md#sima-2-an-agent-that-plays-reasons-and-learns-with-you-in-virtual-3d-worlds--blog-deepmind-sima2) |

### 科学与具身环境

**论文**

| 论文 | 日期 | 资源 | 环境／任务贡献 | 质量保障 | 代码情况 |
| --- | --- | --- | --- | --- | --- |
| [Aviary](https://arxiv.org/abs/2412.21154) | 2024-12-30 | [代码](https://github.com/Future-House/aviary) · [详情](docs/catalog_details_zh.md#aviary--paper-aviary) | 定义带科学工具及奖励的语言代理环境，覆盖文献、分子克隆和蛋白质任务。 | RL 实验: 领域目标和科学任务检查。 | 领域工具与外部服务增加依赖；模拟科学任务成功不等于实验室验证。 |
| [ScienceWorld](https://arxiv.org/abs/2203.07540) | 2022-03-14 | [代码](https://github.com/allenai/ScienceWorld) · [详情](docs/catalog_details_zh.md#scienceworld--paper-scienceworld) | 提供可组合实验及环境目标检查的交互式文字科学世界。 | 评测环境: 领域目标和科学任务检查。 | 简化模拟器适合规划研究，但不复现物理实验室的完整动态。 |
| [ALFWorld](https://arxiv.org/abs/2010.03768) | 2020-10-08 | [代码](https://github.com/alfworld/alfworld) · [详情](docs/catalog_details_zh.md#alfworld--paper-alfworld) | 对齐符号化文字交互与具身家务任务；BUTLER 通过 DAgger 模仿学习训练并迁移已学策略。 | 模仿学习: 领域目标和科学任务检查。 | 文字版与具身版的感知及执行成本不同；此项作为基础脉络收录。 |

**仓库**

| 项目 | 链接 | Stars | 标签 | 摘要 |
| --- | --- | --- | --- | --- |
| ALFWorld | [GitHub](https://github.com/alfworld/alfworld) · [详情](docs/catalog_details_zh.md#alfworld--project-alfworld) | ★ 881 | game, imitation | 对齐符号化文字交互与具身家务任务；BUTLER 通过 DAgger 模仿学习训练并迁移已学策略。 |
| ScienceWorld | [GitHub](https://github.com/allenai/ScienceWorld) · [详情](docs/catalog_details_zh.md#scienceworld--project-scienceworld) | ★ 395 | game, evaluation | 提供可组合实验及环境目标检查的交互式文字科学世界。 |
| Aviary | [GitHub](https://github.com/Future-House/aviary) · [详情](docs/catalog_details_zh.md#aviary--project-aviary) | ★ 284 | executable, rl | 定义带科学工具及奖励的语言代理环境，覆盖文献、分子克隆和蛋白质任务。 |

**博客**

| 文章 | 发布方 | 日期 | 摘要 | 证据 |
| --- | --- | --- | --- | --- |
| [PaperBench: Evaluating AI’s Ability to Replicate AI Research](https://openai.com/index/paperbench/) | OpenAI | 2025-04-02 | 将论文复现分解成层级 rubric，与原作者共同定义评分任务，并单独评估自动评判器。 | [详情](docs/catalog_details_zh.md#paperbench-evaluating-ais-ability-to-replicate-ai-research--blog-openai-paperbench) |

## 自适应与质量控制

### 课程与环境共演化

**论文**

| 论文 | 日期 | 资源 | 环境／任务贡献 | 质量保障 | 代码情况 |
| --- | --- | --- | --- | --- | --- |
| [VERA](https://arxiv.org/abs/2610.05923) | 2026-10-05 | [详情](docs/catalog_details_zh.md#vera--paper-vera) | 从轨迹构建可恢复沙箱，经检查筛选后交替更新模型权重与 harness 技能。 | RL 与 harness 学习: rubric 奖励、可执行检查和开发集准入门槛。 | 近期预印本；已读摘要和正文未提供可确认的官方仓库。 |
| [EnvHarness](https://arxiv.org/abs/2608.19880) | 2026-08-20 | [代码](https://github.com/google-research/envharness) · [详情](docs/catalog_details_zh.md#envharness--paper-envharness) | 用可编程的初始化、交互和组合层包装固定环境，在保留原验证器的前提下调整练习。 | RL 与 harness 学习: 原环境验证器及留出任务评测。 | 迁移结果限于所测基准；保留验证器不等于每个新包装层都保持任务语义。 |
| [SPADE](https://arxiv.org/abs/2608.19197) | 2026-08-19 | [代码](https://github.com/spade-rl/spade) · [详情](docs/catalog_details_zh.md#spade--paper-spade) | 同一策略同时扮演环境设计者与求解者，用提示辅助的 regret 信号选择可执行 reset/step 世界。 | RL 实验: 可执行环境奖励及设计者使用的提示辅助 regret 信号。 | 仍依赖语料、记忆和可解性控制；实验不能说明无界改进。 |
| [Envs-FORGE](https://arxiv.org/abs/2608.14312) | 2026-08-14 | [部分／关联代码](https://github.com/DataArcTech/DataArc-SynData-Toolkit) · [详情](docs/catalog_details_zh.md#envs-forge--paper-envs-forge) | 用验证通过率决定每个种子的合成操作，同步改写任务、数据、测试和 Docker 环境。 | RL 实验: 任务成功情况反馈到难度调整；验证细节以具体方法为准。 | 论文链接的是综合工具包；根 README 中未确认完整的论文专属复现入口。 |
| [CalibForge](https://arxiv.org/abs/2608.06352) | 2026-08-06 | [部分／关联代码](https://github.com/AweAI-Team/CalibForge) · [详情](docs/catalog_details_zh.md#calibforge--paper-calibforge) | 利用经验证的求解器分歧，或强模型通过／弱模型失败的对比，修订终端任务的可学习难度。 | SFT／轨迹训练: 根据经过验证的求解结果，选择求解器分歧或强通过／弱失败区间。 | 难度校准相对于选定求解器，不是绝对难度；公开数据及 agent 配方不等于完整合成引擎。 |
| [Beyond Simply Environment Scaling](https://arxiv.org/abs/2608.03571) | 2026-08-04 | [代码](https://github.com/GaryStack/Beyond-MMEnv-Scaling) · [详情](docs/catalog_details_zh.md#beyond-simply-environment-scaling--paper-beyond-mm-scaling) | 通过能力导向选择、交互难度与状态规模的分层课程，研究训练环境分布。 | RL 实验: 任务成功情况反馈到难度调整；验证细节以具体方法为准。 | 环境数量不是唯一变量；效果取决于所测多样性与难度设置。 |
| [EvoEnv](https://arxiv.org/abs/2605.14392) | 2026-05-14 | [详情](docs/catalog_details_zh.md#evoenv--paper-evoenv) | 合成可复用的 Python 生成器与验证器，利用求解与验证的难度差维持推理训练信号。 | RL 实验: 生成的可执行 oracle 及分阶段准入检查。 | 进行中的技术报告；可验证推理生成器不自动等价于真实的多工具工作环境。 |
| [RLVE](https://arxiv.org/abs/2511.07317) | 2025-11-10 | [代码](https://github.com/Zhiyuan-Zeng/RLVE) · [详情](docs/catalog_details_zh.md#rlve--paper-rlve) | 在人工设计的可验证推理环境集合中，按当前策略能力自适应调整程序化任务难度。 | RL 实验: 算法式答案验证及自适应求解率校准。 | 环境工程仍是人工完成；程序化推理结果不宜外推至 GUI 或企业工作流。 |
| [Environment Tuning](https://arxiv.org/abs/2510.10197) | 2025-10-11 | [代码](https://github.com/inclusionAI/AWorld-RL) · [详情](docs/catalog_details_zh.md#environment-tuning--paper-env-tuning) | 结合任务课程、环境纠错反馈和进度奖励，稳定少数据下的工具使用学习。 | RL 实验: 任务成功情况反馈到难度调整；验证细节以具体方法为准。 | 增强反馈属于训练条件；部署评测不能假定仍有同样的额外帮助。 |

**仓库**

| 项目 | 链接 | Stars | 标签 | 摘要 |
| --- | --- | --- | --- | --- |
| EnvHarness | [GitHub](https://github.com/google-research/envharness) · [详情](docs/catalog_details_zh.md#envharness--project-envharness) | ★ 621 | executable, rl+harness | 用可编程的初始化、交互和组合层包装固定环境，在保留原验证器的前提下调整练习。 |
| RLVE | [GitHub](https://github.com/Zhiyuan-Zeng/RLVE) · [详情](docs/catalog_details_zh.md#rlve--project-rlve) | ★ 235 | procedural, rl | 在人工设计的可验证推理环境集合中，按当前策略能力自适应调整程序化任务难度。 |
| Environment Tuning | [GitHub](https://github.com/inclusionAI/AWorld-RL) · [详情](docs/catalog_details_zh.md#environment-tuning--project-env-tuning) | ★ 127 | executable, rl | 结合任务课程、环境纠错反馈和进度奖励，稳定少数据下的工具使用学习。 |
| SPADE | [GitHub](https://github.com/spade-rl/spade) · [详情](docs/catalog_details_zh.md#spade--project-spade) | ★ 114 | executable, rl | 同一策略同时扮演环境设计者与求解者，用提示辅助的 regret 信号选择可执行 reset/step 世界。 |
| Beyond Simply Environment Scaling | [GitHub](https://github.com/GaryStack/Beyond-MMEnv-Scaling) · [详情](docs/catalog_details_zh.md#beyond-simply-environment-scaling--project-beyond-mm-scaling) | ★ 15 | mixed, rl | 通过能力导向选择、交互难度与状态规模的分层课程，研究训练环境分布。 |
| CalibForge | [GitHub](https://github.com/AweAI-Team/CalibForge) · [详情](docs/catalog_details_zh.md#calibforge--project-calibforge) | ★ 10 | curriculum | 利用经验证的求解器分歧，或强模型通过／弱模型失败的对比，修订终端任务的可学习难度。 |

### 验证器、契约与失败审计

**论文**

| 论文 | 日期 | 资源 | 环境／任务贡献 | 质量保障 | 代码情况 |
| --- | --- | --- | --- | --- | --- |
| [Grounded Skill-Following](https://arxiv.org/abs/2610.05161) | 2026-10-04 | [详情](docs/catalog_details_zh.md#grounded-skill-following--paper-skill-contracts) | 用允许动作、状态转移与终止条件定义运行时技能契约，提供可核验的进度反馈。 | RL 实验: 检查允许动作、契约状态转移与终止，按可核验进度分配反馈。 | 契约约束已有任务；论文所链仓库本轮无法访问，未计入可用实现。 |
| [Terminal Task Hardness Audit](https://arxiv.org/abs/2609.26826) | 2026-09-20 | [详情](docs/catalog_details_zh.md#terminal-task-hardness-audit--paper-fake-hardness) | 用执行证据区分真正未解任务、错误参考解、基础设施故障和验证器绕过。 | 质量／失败研究: 研究评分信号质量，而非定义通用奖励。 | 经过裁定的语料研究仍不能说明任务的内在难度或验证器完备性。 |
| [Hack-Verifiable Environments](https://arxiv.org/abs/2605.20744) | 2026-05-20 | [代码](https://github.com/MajoRoth/hack-verifiable-environments) · [详情](docs/catalog_details_zh.md#hack-verifiable-environments--paper-hack-verifiable) | 在 TextArena 中植入可检测的奖励投机机会，以确定性方式测量代理对评分漏洞的利用。 | 评测环境: 对预置奖励漏洞利用行为的确定性检测。 | 人为设计的漏洞支持测量，但不能穷尽真实奖励投机类型。 |

**仓库**

| 项目 | 链接 | Stars | 标签 | 摘要 |
| --- | --- | --- | --- | --- |
| Hack-Verifiable Environments | [GitHub](https://github.com/MajoRoth/hack-verifiable-environments) · [详情](docs/catalog_details_zh.md#hack-verifiable-environments--project-hack-verifiable) | ★ 10 | game, evaluation | 在 TextArena 中植入可检测的奖励投机机会，以确定性方式测量代理对评分漏洞的利用。 |

**博客**

| 文章 | 发布方 | 日期 | 摘要 | 证据 |
| --- | --- | --- | --- | --- |
| [How to Evaluate AI Agents From Tool Calls to Task Completion](https://developer.nvidia.com/blog/how-to-evaluate-ai-agents-from-tool-calls-to-task-completion/) | NVIDIA | 2026-09-21 | 区分步骤级过程评分与终态任务完成，并把可靠性分析放回有状态评测设计。 | [详情](docs/catalog_details_zh.md#how-to-evaluate-ai-agents-from-tool-calls-to-task-completion--blog-nvidia-agent-evaluation) |
| [Rubric Dropout: A Simple Way to Mitigate Reward Hacking in Rubric-as-Reward RL](https://labs.scale.com/blog/rubric-dropout) | Scale Labs | 2026-09-10 | 在奖励计算时随机移除 rubric 条目，降低对固定评分代理的过拟合。 | [详情](docs/catalog_details_zh.md#rubric-dropout-a-simple-way-to-mitigate-reward-hacking-in-rubric-as-reward-rl--blog-rubric-dropout) |
| [Who Grades the Graders? Rethinking Verifier Design for Computer Use Agents](https://labs.scale.com/blog/verifier-design-for-cua) | Scale Labs | 2026-09-02 | 比较脆弱程序检查与模型评判，讨论对专业产物使用分解、混合验证的方法。 | [详情](docs/catalog_details_zh.md#who-grades-the-graders-rethinking-verifier-design-for-computer-use-agents--blog-scale-grader) |
| [Systematic Reward Hacking and Prime Sprints](https://www.primeintellect.ai/blog/reward-hacking) | Prime Intellect | 2026-05-20 | 在构造的 backdoor-IFEval 环境中研究 RL 过程中显式与隐藏奖励的竞争。 | [详情](docs/catalog_details_zh.md#systematic-reward-hacking-and-prime-sprints--blog-reward-hacking) |
| [Measuring and improving coding audit realism with deployment resources](https://alignment.anthropic.com/2026/coding-audit-realism/) | Anthropic | 2026-03-23 | 把真实部署提示、工具定义和代码库资源引入编码审计模拟，测量并改善生成场景的真实性。 | [详情](docs/catalog_details_zh.md#measuring-and-improving-coding-audit-realism-with-deployment-resources--blog-anthropic-petri-realism) |
| [Agentic Rubrics: Teaching AI to Verify Code the Way Developers Do](https://labs.scale.com/blog/agentic-rubrics) | Scale Labs | 2026-03-11 | 根据仓库生成有上下文依据的检查清单，在不运行测试时评分候选补丁。 | [详情](docs/catalog_details_zh.md#agentic-rubrics-teaching-ai-to-verify-code-the-way-developers-do--blog-agentic-rubrics) |
| [Why SWE-bench Verified no longer measures frontier coding capabilities](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/) | OpenAI | 2026-02-23 | 审计测试过窄、题意不足与基准污染，说明可执行测试并不自动构成可靠的任务验收器。 | [详情](docs/catalog_details_zh.md#why-swe-bench-verified-no-longer-measures-frontier-coding-capabilities--blog-openai-swe-audit) |
| [Quantifying infrastructure noise in agentic coding evals](https://www.anthropic.com/engineering/infrastructure-noise) | Anthropic | 2026-02-05 | 通过资源配额对照实验说明沙箱限制会改变可靠性及编码评测的测量对象。 | [详情](docs/catalog_details_zh.md#quantifying-infrastructure-noise-in-agentic-coding-evals--blog-anthropic-infra-noise) |
| [Petri 2.0: New Scenarios, New Model Comparisons, and Improved Eval-Awareness Mitigations](https://alignment.anthropic.com/2026/petri-v2/) | Anthropic | 2026-01-22 | 补充场景与真实性过滤，减少不可信工具输出和场景细节泄露“正在接受测试”的信号。 | [详情](docs/catalog_details_zh.md#petri-20-new-scenarios-new-model-comparisons-and-improved-eval-awareness-mitigations--blog-anthropic-petri-v2) |
| [Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) | Anthropic | 2026-01-09 | 区分任务、试验、评分器与结果，讨论干净隔离环境及状态验收。 | [详情](docs/catalog_details_zh.md#demystifying-evals-for-ai-agents--blog-anthropic-evals) |
| [From shortcuts to sabotage: natural emergent misalignment from reward hacking](https://www.anthropic.com/research/emergent-misalignment-reward-hacking) | Anthropic | 2025-11-21 | 在含可投机缺陷的编码 RL 环境中研究奖励攻击，以及其向其他任务行为的泛化。 | [详情](docs/catalog_details_zh.md#from-shortcuts-to-sabotage-natural-emergent-misalignment-from-reward-hacking--blog-anthropic-reward-hacking) |
| [Petri: An open-source auditing tool to accelerate AI safety research](https://www.anthropic.com/research/petri-open-source-auditing) | Anthropic | 2025-10-06 | 从种子场景出发，审计 agent 构造多轮用户、工具与模拟环境交互，再由 judge 分析轨迹。 | [详情](docs/catalog_details_zh.md#petri-an-open-source-auditing-tool-to-accelerate-ai-safety-research--blog-anthropic-petri) |
| [Training a Misaligned Reward Seeker](https://alignment.anthropic.com/2026/reward-seeker/) | Anthropic | 未确认 | 在故意设置的对抗性训练研究中，使用有漏洞的环境研究奖励投机与检测。 | [详情](docs/catalog_details_zh.md#training-a-misaligned-reward-seeker--blog-anthropic-reward-seeker) |

## 综述与研究地图

### 环境扩展与演化综述

**论文**

| 论文 | 日期 | 资源 | 环境／任务贡献 | 质量保障 | 代码情况 |
| --- | --- | --- | --- | --- | --- |
| [Agentic Environment Engineering Survey](https://arxiv.org/abs/2606.12191) | 2026-06-10 | [详情](docs/catalog_details_zh.md#agentic-environment-engineering-survey--paper-aee-survey) | 跨领域组织环境建模、合成、评估及代理环境演化研究。 | 综述: 概念梳理；不在此定义新的任务奖励。 | 综述用于发现线索；实现和实验结论仍需回到原始来源核验。 |
| [Environment Scaling Survey](https://arxiv.org/abs/2511.09586) | 2025-11-12 | [详情](docs/catalog_details_zh.md#environment-scaling-survey--paper-scaling-survey) | 以任务生成、执行、反馈组织交互经验采集，并梳理环境扩展策略。 | 综述: 概念梳理；不在此定义新的任务奖励。 | 当前标题与早期发布不同；分类体系不是对引用系统的独立验证。 |

## 维护方式

编辑 `data/projects.yaml` 后重新生成与核验。自动元数据更新不会刷新人工复核日期；测试和链接检查不代表复现研究结果。

```bash
.venv/bin/python scripts/render_readme.py
.venv/bin/python scripts/verify_catalog.py
.venv/bin/python -m unittest discover -s tests
.venv/bin/python scripts/verify_catalog.py --links
```

- [YAML](data/projects.yaml) · [JSON](data/catalog.json) · [BibTeX](references.bib)
- [Verification / 核验报告](reports/verification/2026-10-08.md)
- [Sources / 来源核验](docs/sources_and_verification.md) · [Contributing](CONTRIBUTING.md)
