# 技术报告中的环境章节

[← 主目录](../README_zh.md)

位置对应下列固定版本。页码为 PDF 阅读器从 1 开始的页序，已对照 PDF 文本；另检查了 Kimi K3、DSec 与 MiMo 的页面版式。本页是已核验的章节索引，不声称穷尽所有报告。

## Kimi K3

[Kimi K3: Open Frontier Intelligence](https://arxiv.org/abs/2607.24653) · **arXiv v2 · 2026-08-07**

报告不等于完整训练环境发布；AgentENV 是报告单独关联的沙箱实现。

| 章节 | 原文章节标题 | PDF | 环境相关内容 |
| --- | --- | --- | --- |
| [§4.2.1](https://arxiv.org/html/2607.24653v2#S4.SS2.SSS1) | Unified White-Box RL Environment | [pp. 14–15](https://arxiv.org/pdf/2607.24653v2#page=14) | 工具、上下文与 harness 模块可配置；训练中变化配置。 |
| [§4.2.2](https://arxiv.org/html/2607.24653v2#S4.SS2.SSS2) | Knowledge-Graph-Guided Task Synthesis | [pp. 15](https://arxiv.org/pdf/2607.24653v2#page=15) | 构建并采样分层概念 DAG，检索材料后合成任务。 |
| [§4.2.3](https://arxiv.org/html/2607.24653v2#S4.SS2.SSS3) | Verifiable Problems in Agentic Environments | [pp. 15–16](https://arxiv.org/pdf/2607.24653v2#page=15) | 搜索、专业工作流及交互沙箱中的视觉推理。 |
| [§4.2.4](https://arxiv.org/html/2607.24653v2#S4.SS2.SSS4) | Kernel Optimization Tasks | [pp. 16](https://arxiv.org/pdf/2607.24653v2#page=16) | 参考实现校验正确性，并给予性能奖励、检测奖励投机。 |
| [§4.2.5](https://arxiv.org/html/2607.24653v2#S4.SS2.SSS5) | Personal Assistant Tasks | [pp. 16](https://arxiv.org/pdf/2607.24653v2#page=16) | 模拟应用组成跨天持久事件环境；Agent 构建初始工作区。 |
| [§4.2.6](https://arxiv.org/html/2607.24653v2#S4.SS2.SSS6) | Autonomous Execution Tasks | [pp. 16](https://arxiv.org/pdf/2607.24653v2#page=16) | 初始状态、目标、工具与预算；公开反馈配合隐藏的终态验证。 |
| [§4.2.7](https://arxiv.org/html/2607.24653v2#S4.SS2.SSS7) | Web Development Tasks | [pp. 16](https://arxiv.org/pdf/2607.24653v2#page=16) | 跨 harness 的容器任务，以确定性检查和模型评审评价产物。 |
| [§5.3.2](https://arxiv.org/html/2607.24653v2#S5.SS3.SSS2) | Sandbox Infrastructure | [pp. 22](https://arxiv.org/pdf/2607.24653v2#page=22) | AgentENV 提供 microVM 检查点、挂起恢复与 fork；报告附开源仓库链接。 |

[AgentENV 沙箱代码](https://github.com/kvcache-ai/AgentENV)

## DeepSeek V4

[DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence](https://arxiv.org/abs/2606.19348) · **arXiv v1 · 2026-04-26**

本报告描述较早的命令日志恢复方案；后续 DSec 论文介绍解耦后的 rollout 执行，不能混作同一版本。

| 章节 | 原文章节标题 | PDF | 环境相关内容 |
| --- | --- | --- | --- |
| [§5.2.3](https://arxiv.org/html/2606.19348v1#S5.SS2.SSS3) | Preemptible and Fault-Tolerant Rollout Service | [pp. 34–35](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro/resolve/89d501aed998d33fa4f4702102ec1bb2331e10f6/DeepSeek_V4.pdf#page=34) | token 级预写日志与 KV cache 恢复，保留被中断的生成进度。 |
| [§5.2.5](https://arxiv.org/html/2606.19348v1#S5.SS2.SSS5) | Sandbox Infrastructure for Agentic AI | [pp. 35–36](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro/resolve/89d501aed998d33fa4f4702102ec1bb2331e10f6/DeepSeek_V4.pdf#page=35) | 四种 DSec 后端、分层镜像，以及复用命令结果的恢复机制。 |

## GLM-4.5

[GLM-4.5: Agentic, Reasoning, and Coding (ARC) Foundation Models](https://arxiv.org/abs/2508.06471) · **arXiv v1 · 2025-08-08**

报告披露方法，不代表完整训练任务库已经发布。

| 章节 | 原文章节标题 | PDF | 环境相关内容 |
| --- | --- | --- | --- |
| [§3.3.1](https://arxiv.org/html/2508.06471v1#S3.SS3.SSS1) | Data Collection and Synthesis for Agents | [pp. 10](https://arxiv.org/pdf/2508.06471v1#page=10) | 知识图谱构造搜索题；从 issue／PR 提取软件任务与可执行测试。 |
| [§3.5](https://arxiv.org/html/2508.06471v1#S3.SS5) | RL Infrastructure | [pp. 12–14](https://arxiv.org/pdf/2508.06471v1#page=12) | 隔离任务执行、统一 HTTP 端点及共享轨迹池，支持异步 rollout 与筛选。 |

## DeepSeek Elastic Compute (DSec)

[DeepSeek Elastic Compute (DSec): A Sandbox Infrastructure for Effective Agentic Training at Scale](https://arxiv.org/abs/2609.22978) · **arXiv v1 · 2026-09-19**

生产基础设施论文；未确认官方公开的 DSec 完整实现，3FS 等关联项目不等于 DSec 平台。

| 章节 | 原文章节标题 | PDF | 环境相关内容 |
| --- | --- | --- | --- |
| [§5.1](https://arxiv.org/html/2609.22978v1#S5.SS1) | Composable Environment Layers | [pp. 14–15](https://arxiv.org/pdf/2609.22978v1#page=14) | 组合可复用只读层与写入变更，构造任务环境。 |
| [§6.1](https://arxiv.org/html/2609.22978v1#S6.SS1) | Build environments of Agents, by Agents, for Agents | [pp. 17](https://arxiv.org/pdf/2609.22978v1#page=17) | 用增量磁盘快照将 Agent 构建会话转为可复用、经过质量检查的环境。 |
| [§6.2](https://arxiv.org/html/2609.22978v1#S6.SS2) | Separate agent loop from the RL framework | [pp. 17–18](https://arxiv.org/pdf/2609.22978v1#page=17) | worker 与 Agent 沙箱独立于可抢占 GPU 作业，保留 rollout 状态。 |
| [§6.3](https://arxiv.org/html/2609.22978v1#S6.SS3) | Suspending Sandboxes for Preemptive RL Training | [pp. 18](https://arxiv.org/pdf/2609.22978v1#page=18) | 挂起容器或 microVM 释放内存，后续请求触发透明恢复。 |

## MiMo-V2.6

[MiMo-V2.6: Scaling Reinforcement Learning Towards Self-Improvement](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL/blob/73875d00b30a89ef8cc353a0b60b0e9f9561952d/MiMo_V2_6_technical_report.pdf) · **HF revision 73875d0 · checked 2026-10-08**

公开任务子集与完整训练分布分开理解。PDF 固定到仓库版本；报告首次发布日期未确认。

| 章节 | 原文章节标题 | PDF | 环境相关内容 |
| --- | --- | --- | --- |
| [§4.2.1](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL/resolve/73875d00b30a89ef8cc353a0b60b0e9f9561952d/MiMo_V2_6_technical_report.pdf#page=9) | Code Agent Tasks | [pp. 9–11](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL/resolve/73875d00b30a89ef8cc353a0b60b0e9f9561952d/MiMo_V2_6_technical_report.pdf#page=9) | 从仓库、规格与工作流合成任务；通过轨迹审计和重复测试检查监督质量。 |
| [§4.2.2](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL/resolve/73875d00b30a89ef8cc353a0b60b0e9f9561952d/MiMo_V2_6_technical_report.pdf#page=11) | General Agent Tasks | [pp. 11–12](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL/resolve/73875d00b30a89ef8cc353a0b60b0e9f9561952d/MiMo_V2_6_technical_report.pdf#page=11) | 先构建可重置的本地工作区与软件 mock，再合成任务并修订可验证 rubric。 |
| [§4.2.3](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL/resolve/73875d00b30a89ef8cc353a0b60b0e9f9561952d/MiMo_V2_6_technical_report.pdf#page=13) | Visual Agent Tasks | [pp. 13](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL/resolve/73875d00b30a89ef8cc353a0b60b0e9f9561952d/MiMo_V2_6_technical_report.pdf#page=13) | 开放式视觉产物设计与参考复刻采用不同视觉评分方式。 |
| [§4.2.4](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL/resolve/73875d00b30a89ef8cc353a0b60b0e9f9561952d/MiMo_V2_6_technical_report.pdf#page=13) | Cybersecurity Agent Tasks | [pp. 13–14](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL/resolve/73875d00b30a89ef8cc353a0b60b0e9f9561952d/MiMo_V2_6_technical_report.pdf#page=13) | 受控漏洞复现任务以确定性规则校验指定缺陷。 |
| [§4.2.5](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL/resolve/73875d00b30a89ef8cc353a0b60b0e9f9561952d/MiMo_V2_6_technical_report.pdf#page=14) | Multi-Harness Training | [pp. 14](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL/resolve/73875d00b30a89ef8cc353a0b60b0e9f9561952d/MiMo_V2_6_technical_report.pdf#page=14) | 重新组合最小提示、工具及上下文模块，变化交互机制。 |
| [§4.2.6](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL/resolve/73875d00b30a89ef8cc353a0b60b0e9f9561952d/MiMo_V2_6_technical_report.pdf#page=14) | Reward Hacking Mitigation | [pp. 14–16](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL/resolve/73875d00b30a89ef8cc353a0b60b0e9f9561952d/MiMo_V2_6_technical_report.pdf#page=14) | 清理环境残留，对准备好的任务做对抗审计，并监测训练轨迹。 |
| [§6.1](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL/resolve/73875d00b30a89ef8cc353a0b60b0e9f9561952d/MiMo_V2_6_technical_report.pdf#page=26) | Agentic RL with Fine-grained Learning Signals | [pp. 26–27](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL/resolve/73875d00b30a89ef8cc353a0b60b0e9f9561952d/MiMo_V2_6_technical_report.pdf#page=26) | Agent Loop 管理准备、交互、评分与清理；轨迹分层区分学习信号和基础设施故障。 |
| [§6.2](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL/resolve/73875d00b30a89ef8cc353a0b60b0e9f9561952d/MiMo_V2_6_technical_report.pdf#page=27) | Harness Pool and Payload Porter: Large-Batch RL with Multiple Harnesses | [pp. 27–29](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL/resolve/73875d00b30a89ef8cc353a0b60b0e9f9561952d/MiMo_V2_6_technical_report.pdf#page=27) | 持久执行池分别配置 harness 代码、Agent 行为、环境设置及轨迹传输。 |
| [§7.2](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL/resolve/73875d00b30a89ef8cc353a0b60b0e9f9561952d/MiMo_V2_6_technical_report.pdf#page=34) | RL with Open Environments | [pp. 34–36](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL/resolve/73875d00b30a89ef8cc353a0b60b0e9f9561952d/MiMo_V2_6_technical_report.pdf#page=34) | 说明公开领域、分域 GRPO 与留出 harness 评测；发布清单另见第 33 页表 5。 |
