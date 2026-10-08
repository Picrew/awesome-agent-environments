# 环境选型对比 / Environment selection matrix

截至 2026-10-08。下面按使用问题比较代表性工作，不做综合排名。“实验／贡献证据”来自引用工作；本轮没有安装第三方环境或复现训练。完整资源见 [中文目录](../README_zh.md)。

造环境与做数据的输入／产物对比，另见[技能与需求合成专题](skills_to_environments.md)。这里侧重基础设施及原有代表环境，完整分类以主目录为准。

## 环境基础设施：先选职责，再选框架

补充案例：[小米 MiMo 的 verl、mimoagent 与 RL OSS 数据／镜像关系](xiaomi_mimo_rl_oss.md)。

| 系统与来源 | 主要职责／交互形态 | 反馈与生命周期 | 适合的起点 | 需要补齐或确认 |
| --- | --- | --- | --- | --- |
| [MiMo RL OSS](https://github.com/XiaomiMiMo/verl) / [mimoagent](https://github.com/XiaomiMiMo/mimoagent) | 多领域训练配方与环境运行层 | 按任务使用测试、规则、rubric 或视觉评分 | 对照工业界公开的环境与训练器连接方式 | 逐领域依赖；配方、数据和镜像属于配套材料，不能重复计数 |
| [Scale AgentEnv](https://labs.scale.com/blog/introducing-agentenv) · [代码](https://github.com/scaleapi/agentenv-framework) | Environment、Artifact、Rules；多种工具访问方式与多步任务 | 环境状态、任务规则与运行后端分离 | 企业工作流、状态化工具任务 | 部分任务没有评分器；支持容器后端不等于每个环境都能低成本重置 |
| [OpenEnv](https://huggingface.co/blog/openenv-agentic-rl) · [代码](https://github.com/huggingface/OpenEnv) | 容器化环境与类型化客户端／服务端交互契约 | 约定环境交互边界；奖励语义由具体环境负责 | 将异构环境接到训练器 | 协议一致不保证奖励一致；吞吐由环境后端决定 |
| [Verifiers](https://www.primeintellect.ai/blog/verifiers-v1) · [代码](https://github.com/PrimeIntellect-ai/verifiers) | Python 环境、rollout 与 rubric 组织；支持复杂 agent/env 交互 | 由环境执行交互并计算反馈 | 工具、多轮对话及程序验证任务 | v1 是新 API 命名，不应按文章标题推断 PyPI 主版本；外部沙箱需另配 |
| [NeMo Gym](https://github.com/NVIDIA-NeMo/Gym) | 服务化环境与模型交互，面向 agentic RL | 环境服务、rollout 和训练系统集成 | 需要独立扩展环境服务的训练流水线 | 训练器、资源服务器和环境各有部署要求；示例集不等于统一领域模拟器 |
| [Harbor](https://github.com/harbor-framework/harbor) | 任务环境、agent harness 与验证流程的执行框架 | 容器／沙箱执行任务及 grader | 终端和 SWE 任务打包、运行与轨迹采集 | 本身不替代策略优化器；任务镜像、测试依赖与数据划分仍需管理 |
| [GEM](https://arxiv.org/abs/2510.01051) · [代码](https://github.com/axon-rl/gem) | 面向 agentic LLM 的多类交互环境接口 | 可与 RL 训练流程结合的环境集合 | 对多环境训练做统一实验 | 各领域奖励、代价和难度仍不同，统一 API 不能消除这些差异 |
| [AgentGym-RL](https://arxiv.org/abs/2509.08755) · [代码](https://github.com/WooooDyy/AgentGym-RL) | 基于多环境的 agent RL 训练研究与框架 | 训练、rollout 与环境集成 | 复查多任务 RL 训练方案 | 与早期 AgentGym、Scale AgentEnv 分开；不要混用版本依赖 |

## 环境生产与共演化：比较生成对象

| 工作 | 生成／调整对象 | 执行与反馈 | 训练证据 | 发布与适用边界 |
| --- | --- | --- | --- | --- |
| [AWM](https://arxiv.org/abs/2602.10090) | 数据库、工具及任务组成的可执行世界 | SQL 状态后端与程序化验证 | RL | [官方代码](https://github.com/Snowflake-Labs/agent-world-model)；名字含 World Model，但不是纯神经状态预测器 |
| [EnvScaler](https://arxiv.org/abs/2601.05808) | 环境骨架与场景扩展 | 可执行工具交互、验证及训练集成 | SFT + RL | [官方代码](https://github.com/RUC-NLPIR/EnvScaler)；生成规模须与有效、可解且不重复的任务规模分开 |
| [Agent-World](https://arxiv.org/abs/2604.18292) | 多领域工具环境与轨迹 | 可执行环境与任务反馈 | SFT + RL | [仓库](https://github.com/RUC-NLPIR/Agent-World)发布精选子集；接入 RL 仍需适配，不能当成完整训练流水线 |
| [ScaleEnv](https://arxiv.org/abs/2602.06820) | 多样可验证环境 | 执行环境与验证奖励 | RL | 官方代码未确认；与 Scale AI 的 AgentEnv 无对应关系证据 |
| [AutoGym](https://arxiv.org/abs/2609.22592) | 先构建蓝图，再生成环境 | 可执行生成物与质量筛选 | 环境生成 | 官方代码未确认；不据生成结果推断完整在线训练效果 |
| [Skill2Env](https://arxiv.org/abs/2609.33772) | 从技能描述构造环境及示范 | 可执行任务与示范筛选 | SFT | [作者研究主页](https://github.com/AllSpark-Research/AgentEnv)已有示例任务和模型链接；完整合成与训练流水线未确认 |
| [RLVE](https://arxiv.org/abs/2511.07317) | 参数化任务难度 | 程序化生成与验证 | RL | [官方代码](https://github.com/Zhiyuan-Zeng/RLVE)；人工设计生成器与自动合成新世界是不同扩展路线 |
| [SPADE](https://arxiv.org/abs/2608.19197) | 同一策略参与环境设计与求解 | 可执行世界与 hint-regret 驱动 | RL | [官方代码](https://github.com/spade-rl/spade)；需区分生成器收益与求解器真实泛化 |
| [EnvHarness](https://arxiv.org/abs/2608.19880) | 在环境周围学习 setup／规则等包装 | 关联原环境验证器 | RL + harness | [官方代码](https://github.com/google-research/envharness)；包装变化并不等于基础环境本体被重建 |
| [VERA](https://arxiv.org/abs/2610.05923) | 从轨迹形成可恢复环境，并交替优化策略与技能 | 可执行检查、rubric 与开发集准入 | RL + harness | 官方实现未确认；环境可恢复性、筛选成本和跨任务泛化值得独立核查 |

## 模拟与领域环境：比较真实后端依赖

| 工作 | 后端／任务 | 用于训练的价值 | 关键限制 |
| --- | --- | --- | --- |
| [GenEnv](https://arxiv.org/abs/2512.19682) / [DreamGym](https://arxiv.org/abs/2511.03773) | 生成式或学习式环境模拟 | 降低交互成本，生成与学习者适配的经验 | 模拟误差会影响策略；真实环境验证必须独立，DreamGym 官方代码本轮未确认 |
| [WebWorld](https://arxiv.org/abs/2602.14721) | 学习式 Web 交互世界 | 生成用于 agent 学习的交互经验 | 关注模拟到真实网页的迁移；不要与同名网页生成工作混用 |
| [SynthTools](https://arxiv.org/abs/2511.09572) | LLM 模拟工具响应 | 可扩展地生成工具使用任务与交互 | 不等同于真实数据库／API 执行；审计机制不能自动保证状态忠实 |
| [SWE-smith](https://arxiv.org/abs/2504.21798) / [SWE-rebench V2](https://arxiv.org/abs/2602.23866) | 代码仓库、任务和可复现测试环境 | 生产 SWE 训练实例 | 安装、测试有效性、测试泄漏及仓库划分往往比接口更关键 |
| [daVinci-Env / OpenSWE](https://arxiv.org/abs/2603.13023) | 大规模可执行软件任务及训练产物 | 环境规模与轨迹训练研究 | 区分环境数量、代码仓库数量与轨迹数量；论文主体训练证据为 SFT |
| [Gym-Anything](https://arxiv.org/abs/2604.06126) | 桌面软件、虚拟机任务与验证 | 将真实软件操作转成训练轨迹 | VM 运行与重置成本；自动 verifier 的可靠性需另审 |
| [BrowserGym](https://arxiv.org/abs/2412.05467) / [OSWorld](https://arxiv.org/abs/2404.07972) / [AndroidWorld](https://arxiv.org/abs/2405.14573) | 浏览器、桌面或 Android 状态 | 可作为交互底座和泛化评测 | 主要是评测证据；不能直接把已有测试实例当训练池 |
| [AppWorld](https://arxiv.org/abs/2407.18901) / [ToolSandbox](https://arxiv.org/abs/2408.04682) / [τ²-bench](https://arxiv.org/abs/2506.07982) | 多应用状态、工具调用及用户交互 | 状态验证、长程工具操作研究 | 模拟用户与真实用户有差距；任务划分、访问方式和依赖各异 |
| [Aviary](https://arxiv.org/abs/2412.21154) / [ScienceWorld](https://arxiv.org/abs/2203.07540) | 工具化科学任务／交互科学世界 | 领域反馈与科学 agent 学习 | 领域验证不一定便宜；ScienceWorld 主要作为评测环境收录 |

## 落地时应记录的最小实验表

每个候选环境记录：任务来源与划分、`reset/step` 或会话契约、状态保存与恢复、成功条件、奖励是否可被 agent 读取或修改、每次交互与重置成本、并发上限、外部账户依赖、训练器适配、许可证与发布版本。缺少实测的列填写“未测”，不要用 README 的支持声明替代实测。

对训练环境生成研究，额外记录：生成成本、编译／启动成功率、oracle 可解率、无效任务过滤率、重复率、难度随策略变化的情况，以及在隔离测试环境上的迁移收益。相关失败类型见 [调研综述](research_landscape_zh.md)。
