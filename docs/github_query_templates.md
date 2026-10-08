# 可复用检索模板

以下是用于后续补充的检索模板，不是声称逐条执行过的审计日志。搜索用于发现，收录证据应回到论文、作者页面、官方仓库或原始技术文章。

## 主题发现

```text
"agent training" "environments" "verifiable"
"environment synthesis" "reinforcement learning" LLM
"environment scaling" agents
"agent" "environment co-evolution"
"learned simulator" "agent training"
"agentic RL" "verifier" "reward hacking"
"training environments" "software engineering"
"computer use" "task generation" environment
```

## GitHub 搜索

```text
"OpenEnv" in:readme
"environment synthesis" in:readme
"verifiable environments" in:readme
"agentic reinforcement learning" in:readme
"reset" "reward" "LLM" in:readme
"<完整论文标题>" in:readme
"<arXiv ID>" in:readme
```

活跃项目发现可追加 `pushed:>=YYYY-MM-DD archived:false`，但不要用该条件过滤历史论文实现。不要设置高 star 门槛，否则容易漏掉刚发布的研究。

## 官方代码消歧

```text
"<论文全名>" GitHub
"<arXiv ID>" code
"<方法简称>" "<第一作者或机构>"
site:github.com "<arXiv ID>"
site:arxiv.org "<方法简称>" environment
```

先读论文中的 code/project 链接，再检查作者页和 README 的引用信息。同名项目、第三方复现、只有占位 README 的仓库都需要明确标注。

## 一手技术博客

```text
site:labs.scale.com/blog environment verifier
site:huggingface.co/blog OpenEnv training
site:primeintellect.ai/blog environments verifiers
site:developer.nvidia.com/blog "Gym" agent
site:snowflake.com "agent world model"
site:together.ai/blog environment agent
site:cursor.com/blog training environment
```

机构域名不是充分证据；文章需有实质技术内容。Hugging Face 社区作者文章按贡献者技术文章标注，不能自动写成 Hugging Face 官方结论。检索时同时关注正文更新日期、弃用接口和仓库迁移。

## 本轮扩展后的检索维度

```text
"skills" "task synthesis" terminal
"skill graph" "environment"
"requirement-driven" "task synthesis"
"reverse task synthesis" GUI
"tutorial replay" "agent trajectories"
"terminal recordings" "environment"
"synthetic projects" "verifiable" agents
"environment generation" "evaluation"
"trajectory data" "Docker"
"solver calibration" tasks
site:openthoughts.ai/blog agent
site:browser-use.com/posts benchmark
site:developer.nvidia.com/blog trajectories
```

查询后区分生成指令、构建运行初态、生成验证器和采集轨迹；无训练实验也可能属于核心范围。不会仅凭名称中的 Forge、World、Gym 或 Skill 判定相关性。
