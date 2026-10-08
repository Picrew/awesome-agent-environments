# Agent 环境与交互数据调研：从环境构建到经验生产

调研快照：2026-10-08。本文区分原论文报告、公开实现状态和调研判断；没有复现任何训练实验。入口是用户给出的 [VERA](https://arxiv.org/abs/2610.05923) 与 [Scale AgentEnv](https://labs.scale.com/blog/introducing-agentenv)，再沿论文引用、作者项目页、官方仓库和机构技术博客扩展。资源目录和导出由 [统一数据源](../data/projects.yaml)生成。

## 当前研究重点：两条生产主线

本文保留广义环境领域的背景梳理。当前研究重点已经收敛为：**大规模构建高质量环境**，以及**从环境与内容合成有效训练数据**。接口、沙箱、基准和模拟路线按需提供支撑，不作为同等优先的独立目标。

具体目标、数量与质量口径、SFT／RL 分支和待验证实验见[研究聚焦](research_focus_zh.md)。后文原有的研究问题是候选背景，不代表当前全部要做。

## 1. 环境、任务和数据生产的边界

可以把一次交互经验拆成：任务与初始状态 → agent 观察并采取动作 → 状态转移 → 终止与反馈 → 轨迹用于数据分析、训练或评测。环境研究可能改变其中任一环，但这些改变的含义不同。

| 层次 | 主要问题 | 代表入口 |
| --- | --- | --- |
| 运行与交互契约 | 怎样接入、隔离、重置和并发执行 | AgentEnv、OpenEnv、NeMo Gym、Verifiers、Harbor |
| 状态与任务世界 | 什么可以被观察、操作和验证 | AWM、EnvScaler、AppWorld、SWE-smith |
| 经验生成 | 怎样扩大任务与交互分布 | AutoGym、Agent-World、SynthTools、WebWorld |
| 课程与共演化 | 当前策略下一步应该练什么 | RLVE、SPADE、EnvHarness、VERA |
| 反馈质量 | 得分是否代表真正完成任务 | verifier design、reward hacking、task-hardness audit |

这是本目录的分析框架，不是这些作者共同提出的分类。**统一接口、任务更多、奖励更高是三种不同结果，不能互相替代。**

## 2. AgentEnv 与 VERA 分别解决哪一部分

Scale AgentEnv 的主要价值在环境工程结构：用 Environment、Artifact、Rules 组织可复用状态和任务，并提供不同的访问与运行方式。对于企业系统，关键不是只有一个工具函数，而是操作能否作用于持续存在的状态、结果能否被检查、同一流程能否重放。其开源框架适合作为环境结构入口；但框架能够表达规则，不代表每个已附任务都带有完备评分器。[官方介绍](https://labs.scale.com/blog/introducing-agentenv)、[框架仓库](https://github.com/scaleapi/agentenv-framework)。

VERA 更接近“如何持续生产并利用可验证经验”：从轨迹构建可恢复的沙箱，经过检查筛选，再交替更新模型策略与 harness 技能。研究对象不止运行服务，还包括环境、策略和技能之间的反馈循环。它是近期预印本，本轮读到的摘要和正文未确认官方实现，因此适合做研究方向对照，不应直接列为可下载即跑的基线。[论文](https://arxiv.org/abs/2610.05923)。

据此，本调研同时覆盖环境构造、数据生产、评测底座与训练方法，并单独标注证据类型。没有训练结果的环境生成器或评测构造方法也在范围内。

## 3. 环境扩展的构造路线

**执行式合成。** AWM 以数据库和工具构造可执行世界；EnvScaler 通过环境骨架和场景扩展生产经验。这类方法的吸引力是状态变化与检查可以落到程序执行上，但生成程序能启动，还不意味着任务有解、检查器正确或任务间没有重复。[AWM](https://arxiv.org/abs/2602.10090)、[EnvScaler](https://arxiv.org/abs/2601.05808)。

**真实软件上的任务生产。** SWE-smith、SWE-rebench V2 和 Gym-Anything 保留真实代码仓库或软件操作语义，把任务与验证器生产放到环境周围。其研究难点包括依赖安装、可靠重置、软件状态漂移和自动验证质量。这条路线与纯合成世界可互补，但成本口径不能直接比较。[SWE-smith](https://arxiv.org/abs/2504.21798)、[SWE-rebench V2](https://arxiv.org/abs/2602.23866)、[Gym-Anything](https://arxiv.org/abs/2604.06126)。

**学习式模拟。** DreamGym、GenEnv、WebWorld 用生成模型参与交互经验生产；SynthTools 也模拟工具响应。它们有潜力降低昂贵交互的成本，不过环境模型的错误会改变策略学到的行为。需要在独立真实后端或隔离任务上检验迁移，而不能只看模型内得分。[DreamGym](https://arxiv.org/abs/2511.03773)、[GenEnv](https://arxiv.org/abs/2512.19682)、[WebWorld](https://arxiv.org/abs/2602.14721)、[SynthTools](https://arxiv.org/abs/2511.09572)。

**参数化生成与自适应课程。** RLVE 使用可调难度的程序化环境；SPADE 让策略参与设计和求解；EnvHarness 研究环境包装与训练的联动。这里更值得比较的是“怎样找到当前策略有学习价值的任务”，而不只是生成任务总量。[RLVE](https://arxiv.org/abs/2511.07317)、[SPADE](https://arxiv.org/abs/2608.19197)、[EnvHarness](https://arxiv.org/abs/2608.19880)。

**技能与需求驱动合成。** Skill2Env、Terminal-World、SkillSynth、SKT 把技能转为任务或交互约束；NexForge、CLI-Universe 更强调需求、运行资源和验收条件。环境和数据可作为独立产物，后续是否训练、用何种算法，不应决定这类工作的主分类。输入、产物与开放程度的逐项对比见[技能到环境专题](skills_to_environments.md)。

**从已有行为逆向生产。** AgentTrek 从教程指导回放，OS-Genesis 从探索反推任务，TerminalWorld 从真实终端录制还原环境。它们让已有行为成为任务或数据来源，与从提示词直接合成世界形成互补。[AgentTrek](https://arxiv.org/abs/2412.09605)、[OS-Genesis](https://arxiv.org/abs/2412.19723)、[TerminalWorld](https://arxiv.org/abs/2605.22535)。

## 4. 当前最容易误读的三个统计口径

**环境、任务、轨迹不是同一单位。** Prime Intellect 的扩展文章标题使用 environments，但正文数量约为 36.5 万个任务、分布在 23 个任务集中。因此不能把它与论文所说的几百个环境家族直接比较。该文还涉及测试任务集合；做训练实验时必须重新明确隔离规则。[原文](https://www.primeintellect.ai/blog/scaling-agentic-rl)。

**论文规模不是开源规模。** Agent-World 论文报告 1,978 个环境；本轮 README 明示公开精选 563 个环境。目录保留其研究贡献，同时将代码标为部分发布；公开资源和完整训练流水线也分开描述。[论文](https://arxiv.org/abs/2604.18292)、[仓库](https://github.com/RUC-NLPIR/Agent-World)。

**叙事中的闭环不等于已运行的在线闭环。** Prime Intellect 的 General Agent 文章讨论自演化方向，但所述发布使用离线生成的固定训练语料，将联合在线训练作为后续方向。Skill2Env 展示的是 SFT 证据，当前作者主页已提供示例任务和模型，但这些样例仍不等于完整合成流水线。这些工作都值得收录，但不能直接当成已开放的在线环境共演化系统。[General Agent](https://www.primeintellect.ai/blog/general-agent)、[Skill2Env](https://arxiv.org/abs/2609.33772)。

## 5. 验证器与环境一样值得研究

可执行后端只约束状态转移，不会自动保证奖励正确。终态检查可能漏掉关键约束；测试文件可能暴露答案；模型 rubric 可能奖励表面特征；环境不可解或基础设施故障又可能被误认为任务困难。

Scale 对计算机使用任务的验证器文章强调结合可观察产物与不同检查方式；Hack-Verifiable-Environments 直接研究可验证环境中的奖励攻击；任务难度审计进一步提醒，低通过率不一定意味着高质量难例。这些结果共同支持一个实验要求：报告训练成功率前，先量化任务和反馈的有效性。[Verifier design](https://labs.scale.com/blog/verifier-design-for-cua)、[Hack-Verifiable-Environments](https://arxiv.org/abs/2605.20744)、[Task-hardness audit](https://arxiv.org/abs/2609.26826)。

对新环境，建议把失败拆成至少四类：agent 没有能力、任务／oracle 有缺陷、运行基础设施失败、奖励遭到利用。它们对应不同的修复方法；把它们压成一个零奖励，会使课程难度估计失真。这是本调研提出的评估建议，不是已经完成的实测结论。

## 6. 值得进一步做的研究问题

以下是基于所收材料的研究判断，**不是已经验证的新颖性声明**。

1. **从“能生成”走向“可信地生成”。** 为环境生成增加分层验收：启动成功、状态隔离、oracle 可解、反例检查、verifier 抗攻击。比较每单位成本最终得到多少有效且不同的任务，而不是只比较原始产量。
2. **在成本约束下调度课程。** 同时观察策略通过率、任务新颖性、交互长度和重置成本；难题不能只按低成功率定义。实验要与随机采样、固定难度和同预算扩容比较。
3. **环境、harness、策略的因果拆分。** 对 VERA / EnvHarness 类思路，分别冻结或更新三者，用同一隔离测试集判断收益来自环境选择、工具包装、技能记忆还是模型权重。
4. **模拟器和真实后端的混合训练。** 在低成本模拟中探索，在真实后端中校准；报告模拟误差与最终迁移收益的关系。需要避免模型同时生成任务、响应和评分形成自洽但失真的闭环。
5. **环境接口之外的可移植性。** 比较相同任务迁移到不同运行框架后的奖励、状态重置、随机性和吞吐变化。统一 `step` 接口只是第一步，任务语义与 verifier 契约也需要保存。

## 7. 覆盖边界

本轮是截至快照日的一手来源策展，不是遵循预注册检索协议的系统综述。偏重近年的语言与工具智能体环境、数据生产和评测，兼顾少量历史环境；没有全面覆盖机器人动力学、传统多智能体控制或所有游戏。每条记录有证据链接和人工复核日期，动态仓库元数据另存。链接可访问、仓库非空和论文报告了训练收益，都不等于本地复现成功。

本轮补齐项与尚未覆盖范围见[覆盖审计](coverage_audit.md)。
