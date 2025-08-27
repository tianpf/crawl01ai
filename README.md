# 豆包品牌信息MCP服务器

一个基于Model Context Protocol (MCP)的服务器，用于通过豆包平台获取品牌信息并生成多维度行业评分。

## 功能特性

- 🔍 **品牌信息检索**: 通过豆包平台搜索和获取全面的品牌信息
- 📊 **行业评分**: 基于多个维度生成综合的品牌行业评分
- 🎯 **竞争分析**: 提供详细的竞争地位和市场表现分析
- 📈 **趋势分析**: 分析市场趋势和品牌发展潜力
- 🌱 **可持续性评估**: 评估品牌的ESG表现和可持续发展能力
- 🤖 **MCP兼容**: 完全兼容Model Context Protocol标准

## 安装

### 环境要求

- Python 3.8+
- 异步HTTP客户端支持

### 安装依赖

```bash
pip install -r requirements.txt
```

### 开发安装

```bash
pip install -e .
```

## 快速开始

### 1. 配置环境

复制环境配置模板：

```bash
cp .env.example .env
```

编辑 `.env` 文件，配置豆包API密钥和其他参数：

```env
DOUBAO_API_KEY=your_doubao_api_key_here
DOUBAO_BASE_URL=https://api.doubao.example.com/v1
DEBUG=false
```

### 2. 启动MCP服务器

```bash
python doubao_mcp_server.py
```

### 3. 测试功能

运行测试脚本验证功能：

```bash
python test_mcp_server.py
```

## MCP工具说明

### get_brand_info

获取指定品牌的详细信息。

**参数：**
- `brand_name` (必需): 品牌名称
- `industry` (可选): 行业类别

**示例：**
```json
{
  "tool": "get_brand_info",
  "arguments": {
    "brand_name": "华为",
    "industry": "科技"
  }
}
```

### generate_industry_score

基于品牌数据生成多维度行业评分。

**参数：**
- `brand_data` (必需): 品牌数据对象
- `scoring_criteria` (可选): 评分维度列表

**默认评分维度：**
- `market_position`: 市场地位
- `brand_awareness`: 品牌知名度
- `innovation`: 创新能力
- `financial_performance`: 财务表现
- `sustainability`: 可持续性

**示例：**
```json
{
  "tool": "generate_industry_score",
  "arguments": {
    "brand_data": {...},
    "scoring_criteria": ["market_position", "innovation", "sustainability"]
  }
}
```

### search_brand_doubao

在豆包平台搜索品牌相关信息。

**参数：**
- `query` (必需): 搜索查询词
- `limit` (可选): 返回结果数量限制，默认10

**示例：**
```json
{
  "tool": "search_brand_doubao",
  "arguments": {
    "query": "新能源汽车品牌",
    "limit": 5
  }
}
```

## 评分体系

### 评分维度

1. **市场地位 (Market Position)** - 权重25%
   - 市场份额
   - 竞争优势
   - 行业排名

2. **品牌知名度 (Brand Awareness)** - 权重20%
   - 品牌价值
   - 消费者认知
   - 媒体关注度

3. **创新能力 (Innovation)** - 权重20%
   - 研发投入
   - 专利数量
   - 创新指数

4. **财务表现 (Financial Performance)** - 权重20%
   - 营收增长
   - 盈利能力
   - 财务健康度

5. **可持续性 (Sustainability)** - 权重15%
   - ESG评级
   - 环境责任
   - 社会影响

### 评分等级

- **A+** (9.0-10.0): 行业领导者
- **A** (8.0-8.9): 行业优秀者
- **B+** (7.0-7.9): 行业良好者
- **B** (6.0-6.9): 行业平均水平
- **C+** (5.0-5.9): 低于平均
- **C** (4.0-4.9): 需要改进
- **D** (<4.0): 表现不佳

## 项目结构

```
crawl01ai/
├── README.md                 # 项目说明文档
├── LICENSE                   # 开源协议
├── requirements.txt          # Python依赖
├── setup.py                 # 安装配置
├── .env.example             # 环境配置模板
├── .gitignore              # Git忽略文件
├── doubao_mcp_server.py    # MCP服务器主文件
├── doubao_client.py        # 豆包平台客户端
├── brand_analyzer.py       # 品牌分析工具
└── test_mcp_server.py      # 测试脚本
```

## 开发说明

### 添加新的评分维度

1. 在 `IndustryScorer` 类中添加新的评分逻辑
2. 更新默认权重配置
3. 在评分算法中实现新维度的计算方法

### 扩展豆包平台集成

1. 在 `DoubaoClient` 类中添加新的API方法
2. 实现相应的数据处理逻辑
3. 更新数据标准化方法

### 自定义分析算法

1. 继承 `BrandAnalyzer` 类
2. 重写相关分析方法
3. 注册到MCP服务器中

## API参考

### DoubaoClient

豆包平台客户端，提供与豆包API的交互功能。

#### 主要方法

- `search_brand(brand_name, filters)`: 搜索品牌信息
- `get_brand_details(brand_id)`: 获取品牌详情
- `get_industry_analysis(industry, region)`: 获取行业分析
- `get_brand_sentiment(brand_name, time_range)`: 获取品牌情感分析

### BrandAnalyzer

品牌分析器，提供深度品牌分析功能。

#### 主要方法

- `analyze_brand_data(brand_data)`: 深度分析品牌数据
- `_analyze_competitive_position(brand_data)`: 分析竞争地位
- `_assess_growth_potential(brand_data)`: 评估增长潜力

### IndustryScorer

行业评分器，提供多维度评分计算。

#### 主要方法

- `calculate_weighted_score(scores, weights)`: 计算加权评分
- `benchmark_against_industry(scores, industry)`: 行业基准对比

## 许可证

本项目采用 Apache License 2.0 开源协议。详见 [LICENSE](LICENSE) 文件。

## 贡献

欢迎提交Issue和Pull Request来改进项目。

## 支持

如有问题或建议，请通过以下方式联系：

- 提交Issue: [GitHub Issues](https://github.com/tianpf/crawl01ai/issues)
- 项目主页: [GitHub Repository](https://github.com/tianpf/crawl01ai)