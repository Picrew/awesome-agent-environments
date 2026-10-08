# 小米 MiMo：verl 与 RL OSS 环境

补查日期：2026-10-08。首版漏收了这组工业界发布；根据用户线索，现将两个实现入口与配套材料补入双语目录。它符合范围的原因是提供了具体训练环境、评分器和运行配方。

## 入口与关系

| 入口 | 角色 |
| --- | --- |
| [XiaomiMiMo/verl](https://github.com/XiaomiMiMo/verl) | 小米的 verl fork；当前默认分支 `mimo-oss`，包含五类环境的训练配方 |
| [MiMo-V2.6-RL-oss](https://huggingface.co/datasets/XiaomiMiMo/MiMo-V2.6-RL-oss) | 配套训练任务数据；OSS 也出现在该数据集及镜像名称中 |
| [Docker 镜像](https://hub.docker.com/r/xiaomimimo/mimo-v2.6-rl-oss) | 配套执行环境镜像；本轮只核查发布入口，未拉取运行 |
| [mimoagent](https://github.com/XiaomiMiMo/mimoagent) | 分离 agent、模型协议、环境后端与数据／grader；负责 rollout 和终态评分 |
| [uni-agent](https://github.com/XiaomiMiMo/uni-agent) | Code 路线中的模型网关和轨迹捕获依赖 |
| [技术报告](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL/blob/main/MiMo_V2_6_technical_report.pdf) | 已核对 §4.2.1–4.2.6、§6.1–6.2 和 §7.2；详见[逐节内容](technical_report_sections_zh.md#mimo-v26) |
| [MiMo RL Envs Explorer](https://huggingface.co/spaces/FineEnvs/MiMo-RL-Envs-Explorer) | FineEnvs 维护的**非官方社区**浏览与 rollout 入口，作为 MiMo 配套链接收录 |
| [RL 直播页](https://mimo.xiaomi.com/rl/) | 官方动态展示入口；本轮静态读取没有得到历史直播内容，不据此声称核验过每场直播 |

这些入口属于同一套发布的不同部分，不能将 `verl`、`mimo-oss` 分支和数据集各算作一套独立环境。

## 五类任务与反馈

| 领域 | 任务 | 验证方式 |
| --- | --- | --- |
| Code | 软件工程 | 执行测试 |
| Cyber | 漏洞复现 | 规则检查 |
| General | 知识工作 | Rubric 评分 |
| Visual | 网页开发 | 视觉评分 |
| Music | 符号音乐创作 | 规则检查 |

分类来自 [官方数据卡](https://huggingface.co/datasets/XiaomiMiMo/MiMo-V2.6-RL-oss)。这里是五类任务／环境配方，不是五个任务实例，也不能把数据集行数当作独立环境家族数量。

## 使用边界

各领域需要分别配置启动脚本旁的环境变量和依赖。训练仓库说明：Code 经 uni-agent 运行 mimoagent；Cyber、General、Visual 从 verl AgentLoop 驱动 mimoagent；Music 不使用这两个子模块。[代码说明](https://github.com/XiaomiMiMo/verl)。

收录两个 GitHub 项目，并在训练配方条目旁展示数据、镜像和报告链接。报告已按环境相关章节单独审读，列为模型技术报告，和上述实现共用工作标识；动态直播页不冒充技术博客。本轮没有完成安装、镜像启动或 RL 复现。

## 社区 Explorer

[空间 README](https://huggingface.co/spaces/FineEnvs/MiMo-RL-Envs-Explorer/raw/main/README.md) 明确标为 unofficial，支持浏览五类任务、提交 rollout 并查看评分。它是社区配套界面，不替代官方数据、环境镜像或训练配方；本轮核查页面与说明，没有提交远程任务。
