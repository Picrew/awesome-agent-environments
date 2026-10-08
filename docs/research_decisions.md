# 来源裁决与发布边界

人工复核日期：2026-10-08。这里记录容易造成错误收录的具体问题；“未确认”只描述本轮证据边界，不表示作者没有代码。

| 问题 | 本轮处理 | 依据 |
| --- | --- | --- |
| AgentEnv 的重名 | Scale AgentEnv 使用 `scaleapi/agentenv-framework`；AgentGym 的 `agentenv` 包不能与其合并 | [Scale 博客](https://labs.scale.com/blog/introducing-agentenv)、[AgentGym](https://github.com/WooooDyy/AgentGym) |
| ScaleEnv 与 Scale AI | 将 ScaleEnv 论文视为独立工作，不据名称建立公司归属 | [ScaleEnv 论文](https://arxiv.org/abs/2602.06820) |
| OpenEnv 迁移 | 主项目使用当前 `huggingface/OpenEnv`，历史 Meta 发布博客保留原时间 | [当前仓库](https://github.com/huggingface/OpenEnv)、[社区治理文章](https://huggingface.co/blog/openenv-agentic-rl) |
| Apple 仓库迁移 | ToolSandbox / MM-ToolSandBox 采用 API 返回的 `apple-aiml-research` 规范地址 | [ToolSandbox](https://github.com/apple-aiml-research/ToolSandbox)、[MM-ToolSandBox](https://github.com/apple-aiml-research/ml-mmtoolsandbox) |
| C-World / ToolGym | 论文当前标题为 C-World；作者页和 README 保留 ToolGym，旧仓库跳转到 C-World，按同一工作关联 | [论文](https://arxiv.org/abs/2601.06328)、[作者页](https://ziqiao-git.github.io/C-World/)、[仓库](https://github.com/Ziqiao-git/C-World) |
| Skill2Env 主页修正 | 当前 v2 已改指向 AllSpark AgentEnv 研究主页；记录为部分／关联代码。旧空仓库判断不再作为当前状态 | [v2](https://arxiv.org/html/2609.33772v2)、[研究主页](https://github.com/AllSpark-Research/AgentEnv) |
| Envs-FORGE 关联大仓库 | 标为部分／关联代码；不能从整个工具包的存在推断全部论文实现已公开 | [论文](https://arxiv.org/abs/2608.14312)、[工具包](https://github.com/DataArcTech/DataArc-SynData-Toolkit) |
| Agent-World 发布子集 | 公开精选 563 个环境，与论文 1,978 个环境分开；RL 接入需要适配 | [论文](https://arxiv.org/abs/2604.18292)、[README](https://github.com/RUC-NLPIR/Agent-World) |
| AWM 的 world model 含义 | 归为可执行环境合成，而非神经世界模型 | [论文](https://arxiv.org/abs/2602.10090)、[机构说明](https://www.snowflake.com/en/blog/engineering/agent-world-model-for-agentic-reinforment-learning/) |
| SynthTools 响应机制 | 归为模拟式生成；不把工具响应模拟写成确定性真实 API 执行 | [论文](https://arxiv.org/abs/2511.09572) |
| DreamGym 非官方复现 | 搜到同名第三方复现不据此填写官方代码 | [原论文](https://arxiv.org/abs/2511.03773) |
| AutoForge 同名项目 | 普通 coding agent、3D 打印等同名仓库不作为论文代码 | [原论文](https://arxiv.org/abs/2512.22857) |
| WebWorld 同名论文 | 收录 QwenLM 对应的 2602.14721，不与其他同名工作共用 work_id | [论文](https://arxiv.org/abs/2602.14721)、[代码](https://github.com/QwenLM/WebWorld) |
| SWE-rebench V2 地址 | 采用 SWE-rebench 组织下的 V2 仓库，不保留猜测的 nebius 地址 | [论文](https://arxiv.org/abs/2602.23866)、[代码](https://github.com/SWE-rebench/SWE-rebench-V2) |
| ARE 地址 | 使用 `meta-agents-research-environments`，不根据缩写猜 `facebookresearch/ARE` | [官方仓库](https://github.com/facebookresearch/meta-agents-research-environments) |
| Terminal-Bench 版本 | 论文记录对应 2.0；仓库是持续演进的项目，不能据当前 HEAD 推断论文版本 | [论文](https://arxiv.org/abs/2601.11868)、[仓库](https://github.com/harbor-framework/terminal-bench) |
| Prime 的大规模数字 | 约 36.5 万任务／23 个任务集，不写成 36.5 万独立环境家族 | [原文](https://www.primeintellect.ai/blog/scaling-agentic-rl) |
| General Agent 的自演化叙述 | 离线生成的发布与未来在线联合训练分开表述 | [原文](https://www.primeintellect.ai/blog/general-agent) |
| Verifiers v1 与包版本 | v1 API 命名不等于当时包版本为 1.0 | [原文](https://www.primeintellect.ai/blog/verifiers-v1) |
| TRL / OpenEnv 博客更新 | 原文章日期与后续更新分开；当前内容已转向 Harbor 集成，不复用过时 opencode_env 安装步骤 | [原文](https://huggingface.co/blog/sergiopaniego/trl-openenv-harness-training) |
| CoderForge 发布对象 | 收录为轨迹生产的技术博客，不称为完整环境库发布；未可靠提取日期则留空 | [原文](https://www.together.ai/blog/coderforge-preview) |
| Composer 2 | 作为生产训练系统案例；不将内部环境舰队标为开源项目 | [原文](https://cursor.com/blog/composer-2-technical-report) |
| 综述改题 | 2511.09586 使用当前标题，旧题 Scaling Environments… 仅用于检索消歧 | [当前摘要](https://arxiv.org/abs/2511.09586) |
| ALFWorld 训练范式 | 主要结果来自 DAgger 模仿学习；正文还报告了 RL 探索困难，因此不把主要训练证据笼统写成 RL | [论文正文](https://arxiv.org/html/2010.03768) |

## 首轮尚未确认官方代码的论文

以下保留首轮记录。第二轮新增论文的最新状态逐项记录于主目录；完整状态以 `data/projects.yaml` 为准。已检查论文摘要，并针对代码归属疑点补查正文、作者／项目页面和定向检索：

| 工作 | 原始来源 |
| --- | --- |
| VERA | [2610.05923](https://arxiv.org/abs/2610.05923) |
| AutoGym | [2609.22592](https://arxiv.org/abs/2609.22592) |
| EvoEnv | [2605.14392](https://arxiv.org/abs/2605.14392) |
| ScaleEnv | [2602.06820](https://arxiv.org/abs/2602.06820) |
| AutoForge | [2512.22857](https://arxiv.org/abs/2512.22857) |
| DreamGym | [2511.03773](https://arxiv.org/abs/2511.03773) |
| InfiniteWeb | [2601.04126](https://arxiv.org/abs/2601.04126) |
| Terminal Task Hardness Audit | [2609.26826](https://arxiv.org/abs/2609.26826) |

后续若找到新发布，应先补上作者关联证据，再更新状态。普通定期 HTTP 检查不能把“未确认”自动改为“官方”。EvoEnv 是进行中的技术报告；其结果和发布状态应随版本重新审查。

## 范围扩展后的补充裁决

| 问题 | 本轮处理 | 一手依据 |
| --- | --- | --- |
| EnvForge 名称歧义 | 用户确认目标是 Envs-FORGE 等环境研究，不收录 `.env` 配置管理的同名软件 | [Envs-FORGE](https://arxiv.org/abs/2608.14312) |
| 两个 Terminal World | 技能驱动的 Terminal-World 与录制还原的 TerminalWorld 分用两个 work_id；不互相挪用代码 | [技能版](https://arxiv.org/abs/2605.20876)、[录制版](https://arxiv.org/abs/2605.22535) |
| TerminalTraj / Skill Contracts 链接失效 | 论文给出的仓库页面和 GitHub API 均返回 404；保留论文，代码状态为未确认，不计入项目条数 | [TerminalTraj 论文](https://arxiv.org/abs/2602.01244)、[Skill Contracts 正文](https://arxiv.org/html/2610.05161) |
| WebForge 开放范围与评分 | 公开 README 主要是运行评测与 LLM 比对终态答案；标为部分／关联代码，不能写成纯确定性生成系统 | [作者仓库](https://github.com/yuandaxia2001/WebForge) |
| ScaleSWE 公开子集 | 论文 100k 实例与 README 说明的初始 20k 公开实例分开；数据、Docker 镜像、训练轨迹各计各的单位 | [作者仓库](https://github.com/AweAI-Team/ScaleSWE) |
| DeNovoSWE 的“from scratch” | 描述的是求解任务从文档写出整个仓库；构造数据仍依托真实包与测试，归仓库驱动构建 | [论文](https://arxiv.org/abs/2606.10728)、[数据字段](https://github.com/AweAI-Team/DeNovoSWE) |
| SWE-Playground 作者代码 | 正文 HTML 没有可提取代码链接，继续核对作者项目页后确认 neulab 实现，撤销早期未确认判断 | [作者页](https://neulab.github.io/SWE-Playground/)、[代码](https://github.com/neulab/SWE-Playground) |
| Endless Terminals 引用年份 | README 中 BibTeX 年份与 arXiv 首次提交年份不一致；本目录统一使用 arXiv 首次提交日期 2026-01-23 | [论文页](https://arxiv.org/abs/2601.16443)、[README](https://github.com/kanishkg/endless-terminals) |
| CLI-Gym / CLI-Universe | 前者反转健康环境为故障状态，后者从需求构造任务；不同机制、不同工作标识 | [CLI-Gym](https://arxiv.org/abs/2602.10999)、[CLI-Universe](https://arxiv.org/abs/2606.22883) |
| Envs-FORGE 的主分类 | 其核心是以 verifier 奖励和种子通过率选择合成动作，归“课程与环境共演化”；在构建专题交叉引用 | [论文](https://arxiv.org/abs/2608.14312) |
