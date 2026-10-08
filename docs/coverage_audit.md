# 覆盖审计：本轮补到了哪里

快照：2026-10-08。本目录是有边界的一手来源调研，不能称为“已经收齐所有相关工作”。原版偏重训练和 RL，容易漏掉独立的数据生产与评测环境构造；这轮已按更宽的研究对象重审。

## 用户指定线索的处理

- **Envs-FORGE 与 Skill2Env**：原数据已有，现纳入统一的生成路线对照。Skill2Env 归技能构建，Envs-FORGE 的核心是基于反馈选择合成动作，归自适应课程。`EnvForge` 搜索会混入管理 `.env` 文件的无关项目，不能凭名字收录。
- **skills → tasks / environments**：补入 Terminal-World、SkillSynth、Terminal-Task-Gen、SKT；并加入技能契约和可执行技能基准，区分生成、执行和评测三类贡献。
- **小米 verl / OSS**：保留 XiaomiMiMo/verl 与 mimoagent、数据／镜像／技术报告的关联，详见[小米专题](xiaomi_mimo_rl_oss.md)。这确认了技术材料，不等于确认某场直播的标题、场次和时间。
- **标题与分类**：改为 Awesome Agent Environments；训练不再是入选前提。6 个大类、20 个小类按贡献组织，同一工作下关联论文、博客与项目。

## 按研究链路核查缺口

| 链路 | 原来容易漏掉的材料 | 本轮补充代表 | 覆盖判断 |
| --- | --- | --- | --- |
| 技能与需求变为任务 | 只搜索 environment / RL，漏掉 skill / data engineering | SkillSynth、SKT、Terminal-Task-Gen、NexForge、CLI-Universe | 已形成一条可比较的主要路线，仍需追踪后续发布 |
| 环境构建本身 | 把纯评测构造器排除 | WebForge、ClawEnvKit、SkillScriptBench | 已纳入，不要求训练结果 |
| 真实行为变为数据 | 漏掉教程、探索、录制与逆向任务 | AgentTrek、OS-Genesis、InSTA、TerminalWorld | 与从零生成分开，减少概念混用 |
| 软件任务生产 | 仅关注修 bug 的仓库环境 | SWE-Playground、DeNovoSWE、SWE-Universe、ScaleSWE、TerminalTraj、Endless Terminals、CLI-Gym | 覆盖修复、测试和整仓构建；不是所有 SWE 基准大全 |
| 数据配方与采集 | 把轨迹筛选、teacher、运行观测当成训练器细节 | OpenThoughts-Agent、LiteCoder、NeMo Relay 技术文章 | 单独归入经验生产，记录并不等于任务成功 |
| 业务世界构造 | 只从单个任务向后补环境 | AgentMercury、RandomWorld，加上已有 AWM / EnvScaler | 区分持久世界、程序化工具和 LLM 响应模拟 |
| 质量与难度 | 把执行成功当作环境质量完成 | CalibForge、Skill Contracts，加上已有失败审计 | 区分可执行、可解、可学习和抗投机 |

检索同时使用方法名、完整标题、arXiv ID、论文引用、作者主页和仓库引用信息。综述和其他 awesome 仅用于发现候选；收录摘要与发布判断回到一手页面。见[检索模板](github_query_templates.md)与[抓取来源清单](../reports/research/source-manifest.json)。

## 开放程度核验的实际发现

- Skill2Env：当前 v2 关联 AllSpark AgentEnv 研究主页，已公开示例任务；按部分／关联代码记录，仍不声称完整合成流水线可复现。
- Envs-FORGE：链接到关联工具包，不把整个工具包等同于完整论文实现。
- TerminalTraj 与 Grounded Skill-Following：论文给出的仓库在本轮页面/API 查询中返回 404；可能是删除、改名或未公开，本轮无法区分，按未确认处理。失败抓取保留在来源清单中。
- WebForge：公开 README 主要说明评测、轨迹记录和 LLM 终态答案比较；不能写成完整生成器已开放，也不能写成纯确定性评测。
- ScaleSWE / DeNovoSWE：论文规模与发布说明所称的公开部分数据要分开。CalibForge 的数据发布也不能直接证明任务生成引擎完整开放。
- AgentMercury：公共语料样本和可执行世界库是不同发布物。
- LiteCoder / OpenThoughts-Agent：早期博客与后续论文／仓库采用不同规模和配方，按资源各自说明，避免混成同一天的发布。

## 仍然有限的范围

这份目录偏重语言、代码、工具和计算机操作智能体。传统连续控制、机器人动力学、自动驾驶模拟器、工业数字孪生、所有游戏与多智能体社会模拟没有做穷尽检索。也没有纳入每一个纯静态合成问答数据集、通用 agent harness 或只发布模型权重的项目。

无法稳定访问的材料不靠二手转述补造代码状态。当前没有计算数据库级查全率，没有预注册系统综述的检索与筛选流程，不能据资源条数推断“齐全度百分比”。

后续增量最有价值的是：追踪已收论文的正式代码／数据发布；补领域空白的一手来源；检查是否新增了一种构造或验证机制。元数据、HTTP 成功和作者报告结果均不代表本地复现。当前数量及检查结果以[自动核验报告](../reports/verification/2026-10-08.md)为准。

## 第二轮网络复查限制（历史记录）

调研内容抓取和 GitHub 元数据读取完成后，最终 207 个 URL 的复查中出现 206 次 SSL 连接超时，仅 1 项成功。超时没有取得 HTTP 状态，不能推断原页面删除。该网络限制与前面两项明确返回 HTTP 404 的论文附仓库不同，详情见[核验报告](../reports/verification/2026-10-08.md)。

## 第三轮：模型公司与报告章节

开头新增模型公司原始博客专区，补入 OpenAI、Anthropic、Google DeepMind、Qwen、Moonshot AI，并将已有 Cursor、NVIDIA、Together AI 条目前置。环境生成、训练部署、评测方法分别说明，不把产品发布等同于环境开放。

[报告章节索引](technical_report_sections_zh.md)单列 Kimi K3、DeepSeek V4、GLM-4.5 、DSec 和 MiMo-V2.6 共 25 处章节，给出版本、原文章节标题、网页锚点和 PDF 页码。DSec 同时属于沙箱基础设施论文，只统计一次；新增 CompoWorld 补充共享状态与服务组合路线。

第三轮结束时共 192 条资源、117 组工作；报告中的章节和 MiMo Explorer 等配套链接不额外累计。不声称覆盖所有模型报告；未经逐节核验的内容继续作为线索保留。

## 第四轮：北美公司博客补漏

新增 26 篇官方文章，OpenAI 精选由 2 篇增至 8 篇，Anthropic 由 3 篇增至 10 篇，并补查 Meta、xAI、Microsoft、AWS、NVIDIA、Cohere、Poolside、Reflection、Cognition、Together AI 与 Google DeepMind。第四轮结束时公司专区共 38 篇，整个目录 218 条资源、139 组工作、62 篇博客。

每篇新增文章标注相关章节或段落，区分机制披露与实际开放。逐公司统计、收录边界与原文定位见[公司博客补查](north_american_company_blogs.md)。最新网络结果见核验报告，前面的超时数字属于历史轮次。

## 第五轮：按核心主题重审

前一轮按公司补漏过宽，把产品介绍、通用运行时和环境研究放在同一级。本轮重新审查 38 篇公司文章，将 12 篇相关性间接或机制披露不足的文章转为背景资料；26 篇按六个研究问题组织，逐篇显式列出核心问题、具体内容和原文定位。

当前入选目录为 206 条资源，其中 50 篇博客；完整证据库保留 218 条记录，另存的 12 篇背景文章不计入入选数量。论文、模型报告、项目及技术报告章节未被删除。公司逐篇取舍见[主题相关性与取舍](north_american_company_blogs.md)。本轮为已核验材料的内容重审，未刷新历史网络请求结果。

## 第六轮：收敛到环境生产与训练数据生产

本轮不扩充资源数，保留 6 个大类、20 个小类和所有论文／项目／报告位置。开头六主题收敛为两条主线；从既有资源选出 18 篇代表论文，并将公司前置文章从 26 篇收敛到 7 篇，另外 19 篇回到原分类作支撑，原有 12 篇背景继续单列。

新增[研究聚焦](research_focus_zh.md)：给出数量、质量、成本与学习收益口径，区分 SFT／在线 RL／离线经验，并提出三个待验证实验设想。主目录仍有 206 条入选资源（含支撑），完整证据库 218 条；没有把我们的假设写成论文结论，也没有声称已完成训练复现。
