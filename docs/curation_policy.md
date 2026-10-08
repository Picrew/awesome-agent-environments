# 收录与分层标准 / Curation policy

本目录研究 **Agent 环境构建、任务合成与交互数据生产**，同时覆盖采集数据、训练和评测。训练不是收录前提。目标是帮助研究者理解环境如何构建、复用、扩展和验证，而非汇总所有含有 `agent`、`gym` 或 `RL` 的项目。

## 范围

收录以下对象：环境接口与运行设施；可执行任务世界与生成器；用于生成交互经验的学习式模拟器；依赖学习者反馈的课程和环境共演化；SWE、GUI、工具、科学等领域环境；直接影响训练有效性的验证器与失败分析。

评测环境构造本身也是研究对象，不需要借助潜在训练用途才能收录；主要证据为评测时标为 `evaluation`。训练框架只有在其环境接口或运行机制本身构成研究对象时才纳入。传统机器人和连续控制环境不做全面覆盖；ALFWorld 等仅作为语言智能体环境谱系的代表。

不收录：泛用 Agent 编排框架、仅有模型权重的发布、普通提示词仓库、没有环境贡献的训练器、与智能体交互环境和数据生产无关的同名项目、缺少可核查来源的宣传转述。大规模轨迹发布若与环境生产过程直接相关，可作为有一手证据的论文或技术博客收录，但不得标成可复用环境代码。

## 大类、小类与工作

详见[分类设计](taxonomy_iterations.md)。一级按构建、经验生产、基础设施、领域基准、质量和综述区分，二级细化每种职责。每项工作只有一个主位置；资源类型、执行形态和实验证据保留为独立字段。

## 四种资源、一个工作标识

| 资源 | 最低要求 | 必须说明 |
| --- | --- | --- |
| 技术博客 | 原机构或项目贡献者撰写，能明确指出环境构造、交互数据生产、环境执行或验收机制 | 发布者、日期可得性、与论文的关系、是否开放实现 |
| 论文 | 可访问的原始论文页面，已读取摘要；关键机制和代码归属有必要时查正文／作者页 | 完整标题、作者、首次提交日期、贡献／实验证据、官方代码状态 |
| 模型技术报告 | 已核对环境相关正文与指定 PDF 版本 | 独立记录章节标题、网页位置、PDF 页码与开放边界 |
| GitHub 项目 | 公开、非空，且已核查 README 与工作关系 | 快照 star、push、归档状态、许可元数据、运行与发布边界 |

`work_id` 关联同一工作的论文、博客、项目；资源数不是独立成果数。不同研究使用同名方法时不能共用标识。博客补充论文说明也不算独立复现。数据集、镜像、报告等可作为 `artifacts` 附在实现条目下，不另外凑入论文或博客计数。

## 贡献／实验证据标签（`evidence_type`）

| 值 | 含义 |
| --- | --- |
| `rl` / `sft` / `rl+sft` | 所引用工作报告了相应训练实验；不表示本目录复现成功 |
| `imitation` | 模仿学习，如历史环境中的 DAgger；不把它混写为 LLM 的 RL 后训练 |
| `rl+harness` | 同时涉及策略训练与 harness／技能层更新 |
| `rl-ready` | 有可供学习器交互的接口；不据此推断完整训练结果 |
| `generation` | 主要证据是环境、任务或轨迹生成 |
| `evaluation` | 主要作为评测环境或测试套件 |
| `framework` | 运行、连接或调度基础设施 |
| `methodology` | 对环境质量、奖励或失败原因的研究 |
| `survey` / `technical-account` | 综述／技术文章；不能直接与训练实验标签比较 |

项目继承配套论文的训练标签时，含义是“关联工作的证据”，不是“当前仓库已提供该训练的全部组件”。后者由 `limitation` 和代码发布状态说明。

## 官方代码与开放程度

只有论文、作者／机构项目页、或可确认作者身份的仓库 README 建立关系后才给出代码链接。不根据论文简称猜仓库地址，不把第三方复现当作官方发布。一个可打开的仓库不等于完整复现材料。

- `author-linked`：作者关联的实现已确认；数据、权重、依赖和训练脚本是否齐全仍需单独核对。
- `partial-or-associated`：只发布部分材料，或关联大仓库但尚未定位到完整方法实现。
- `empty-repository`：作者给出了链接，但当前仓库为空；保留论文链接，不作为独立实现收录。
- `not-confirmed`：本轮没有确认官方代码；不是断言代码不存在。
- `not-applicable`：综述等不以代码发布为评价对象。

GitHub API 的 SPDX 标签只描述仓库许可元数据。`none` / `NOASSERTION` 不应解释为允许任意使用；代码、数据、网站实例和云服务可能有各自的许可和访问条件。

## 活跃度与排序

快照日为 `catalog.as_of`。公开、未归档、非空，且 `pushed_at` 距快照日不超过 60 个自然日（含边界）的项目标为近期活跃。更早实现标为历史／参考，仍保留其研究价值；归档状态单列。未来时间戳视作错误。

主目录保留大类与小类，论文、仓库、博客分别制表；同组资源在详情互链。文章按已确认日期逆序排列，无日期的文章置后；仓库在小类内按 star 快照降序排列，便于浏览。star 只作为元数据展示。没有 star 门槛，也不以最近提交代替质量判断。更新元数据不会自动推进人工复核日期。

## 摘要的最低质量

每条资源提供中英文机制摘要和边界。摘要回答“环境贡献是什么”；边界回答“读者不能据此推断什么”。数量必须区分环境家族、实例、任务、任务集和轨迹；开源子集与论文规模分开。模拟器与真实可执行后端、终态验证与模型打分、SFT 数据与在线 RL 都不能混写。

涉及评测环境时，应预先划分训练、开发和测试实例，并检查模板、网站、仓库和生成来源的交叉污染。评测代码可访问不是将其测试任务加入训练集的依据。

## Evidence standard (English)

Use primary sources, distinguish reported experiments from our own verification, and link companion artifacts with a shared work identifier. A live repository is not proof of reproducibility. Benchmark inclusion does not authorize training on held-out tests. Metadata refreshes and human evidence reviews have separate timestamps. Every entry needs both a mechanism summary and a material limitation in English and Chinese.

## Report sections and presentation

Model reports use `kind: report` and require version-pinned section links, bilingual passage summaries and one-based PDF viewer pages. A dedicated environment paper such as DSec remains `kind: paper`; its indexed sections do not add to resource counts. Core company articles are presented first by research theme, without changing their underlying contribution category. Adjacent background articles remain in the evidence inventory but are excluded from selected-catalog counts.

Repository and paper tables retain companion resources and link to generated details for evidence and release boundaries. Natural Markdown heading anchors replace raw HTML anchors so HTML-disabled readers do not show markup as text. Exact publication dates remain unset when only a month or no date can be verified.

## 公司博客的主题相关性门槛

逐篇回答两个问题：**文章具体解释了环境研究中的哪个问题？正文给出了哪些机制或产物？** 公司名、模型规模、榜单表现和“用了 RL”本身都不能成为收录理由。

当前前置文章只按两条生产主线归类：大规模高质量环境，以及从环境与内容生产有效训练数据。执行、一般评测、泛模拟和审计机制归为分类支撑。每篇用 `blog_theme`、双语 `research_question` 和 `core_contents` 显式记录；主题名不是文章的宣传标签。

通用运行时、产品能力概览、训练规模或任务域列表若缺乏足够机制，记为 `catalog_scope: background`，保留双语相关性判断与原始证据，但不出现在核心表、分类主目录或入选资源统计中。模型技术报告的环境章节独立审查，不因其发布博客降为背景而一并移除。

“环境使用”也可能相关，例如讲清容器任务如何产生经测试验证的轨迹；必须写明使用的是已有环境，不冒称新环境构建。“沙箱基础设施”也可能相关，例如解释 rollout 状态与奖励路由；纯产品隔离架构属于背景。

## 当前研究重点与完整资料库

保留原有大类／小类作为检索结构，另用 `research_focus` 指定两条研究主线及代表论文。重点索引是人工研究取舍，不自动把某类别所有资源都判为高优先级。

公司文章按 `core`（前置主线）、`supporting`（原分类支撑）、`background`（仅背景）区分。支撑资料仍在入选目录，背景资料单列，不通过删除证据来改变统计。单纯接口统一、沙箱部署、静态基准或泛世界生成不自动进入生产主线。

“能构造”与“能带来学习收益”分别陈述。SFT、在线 RL 与离线经验的接入条件必须分开；不得以生成规模、环境通过率或训练 reward 代替独立测试上的训练收益。研究设想明确标注待验证，与作者报告的证据分开。
