# 这是一个基本的工作流程，帮助你开始使用 Actions

name: CI

# 控制工作流何时运行
on:
  # 在推送或拉取请求事件上触发工作流，但只针对 "main" 分支
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

  # 允许你从 Actions 标签页手动运行此工作流
  workflow_dispatch:

# 工作流程包含一个或多个作业，可以按顺序或并行运行
jobs:
  # 这个工作流包含一个名为 "build" 的作业
  build:
    # 作业将在的运行器上运行
    runs-on: ubuntu-latest

    # 步骤代表作业的一系列任务，将作为作业的一部分执行
    steps:
      # 检出你的仓库到 $GITHUB_WORKSPACE 下，这样你的作业就可以访问它
      - uses: actions/checkout@v4

      # 使用运行器 shell 运行单个命令
      - name: 运行单行脚本
        run: echo 你好，世界！

      # 使用运行器 shell 运行一组命令
      - name: 运行多行脚本
        run: |
          echo 添加其他操作以构建，
          echo 测试和部署你的项目。
