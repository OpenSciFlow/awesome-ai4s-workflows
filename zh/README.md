# AI for Science 工作流生态清单：中文摘要

OpenSciFlow 不是要替代已有工具，而是希望补上一个轻量开放层：让 AI for Science 工具更容易被发现、执行、引用、验证和复现。

## 为什么需要这个清单

AI for Science 的模型、工具和 agent 项目越来越多，但真实科研使用时经常卡在：

- 环境配置；
- 依赖管理；
- GPU / HPC 部署；
- workflow 编排；
- 日志和结果归集；
- citation 和 license；
- 可复现记录。

这个仓库整理相关项目，目的是：

1. 看清已有生态；
2. 避免重复造轮子；
3. 找到潜在互操作对象；
4. 邀请项目作者校正描述；
5. 为 `opensciflow.yaml` 和 workflow template 设计提供依据。

## 当前分类

- AI for Science agents；
- scientific workflow engines；
- 计算生物与分子模拟 workflow；
- HPC 和本地执行工具；
- 包管理与容器；
- model hubs / model zoos；
- reproducibility / provenance；
- 化学与材料工具。

## 第一阶段重点

OpenSciFlow 第一阶段不做大而全平台，先聚焦：

- 蛋白质 MD 稳定性分析；
- `opensciflow.yaml` plugin manifest；
- workflow template；
- local agent；
- run logs；
- artifacts；
- report；
- reproducibility metadata。

## 重要声明

这里列出的项目都是 related projects。除非项目维护者明确同意，OpenSciFlow 不会声称与任何项目已经合作。

如果某个项目描述不准确，欢迎开 issue 修正。

