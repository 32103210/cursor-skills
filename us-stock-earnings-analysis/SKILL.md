---
name: us-stock-earnings-analysis
description: 美股投资分析工具，覆盖财务分析、竞争格局、催化剂识别、风险评估、股价异动分析和投资论点构建，生成专业级股权研究报告
---

# 美股投资深度分析 Skill

这个 skill 提供专业级的美股上市公司投资分析能力，整合定量财务分析和定性战略分析，从数据获取到生成完整的股权研究报告。

## 核心能力

### 1. 数据获取
- **SEC Edgar 集成**: 自动获取 10-K、10-Q、8-K 等财报文件
- **XBRL 解析**: 标准化财务数据，支持跨公司对比
- **实时股价**: 从 Yahoo Finance/Google Finance 获取实时报价
- **财报电话会议**: 分析管理层发言和 Q&A 内容
- **新闻与公告**: 获取影响股价的关键事件

⚠️ **重要数据获取原则**（详见 `references/data-acquisition-guide.md`）:
1. **股价数据**: 必须使用当前实时报价，不能使用 52 周高点/低点
2. **数据验证**: 获取数据后必须验证合理性和时效性
3. **多源验证**: 关键数据从多个来源交叉验证
4. **明确标注**: 清楚标注数据的时间点和来源

### 2. 定量分析: 财务比率计算

#### 盈利能力指标
- **ROE** (净资产收益率): 净利润 / 股东权益
- **ROA** (总资产收益率): 净利润 / 总资产
- **毛利率**: (营收 - 营业成本) / 营收
- **营业利润率**: 营业利润 / 营收
- **净利率**: 净利润 / 营收

#### 流动性指标
- **流动比率**: 流动资产 / 流动负债
- **速动比率**: (流动资产 - 存货) / 流动负债
- **现金比率**: 现金及等价物 / 流动负债

#### 杠杆指标
- **资产负债率**: 总负债 / 总资产
- **债务权益比**: 总负债 / 股东权益
- **利息保障倍数**: EBIT / 利息费用
- **偿债覆盖率**: (净利润 + 折旧) / 债务本息

#### 效率指标
- **资产周转率**: 营收 / 平均总资产
- **存货周转率**: 营业成本 / 平均存货
- **应收账款周转率**: 营收 / 平均应收账款
- **应付账款周转天数**: (平均应付账款 / 营业成本) × 365

#### 估值指标
- **P/E** (市盈率): 股价 / 每股收益
- **P/B** (市净率): 股价 / 每股净资产
- **P/S** (市销率): 市值 / 营收
- **EV/EBITDA**: 企业价值 / EBITDA
- **PEG**: P/E / 盈利增长率

#### 每股指标
- **EPS** (每股收益): 净利润 / 流通股数
- **每股净资产**: 股东权益 / 流通股数
- **每股股息**: 总股息 / 流通股数
- **股息率**: 年度股息 / 股价

### 3. 定性分析

#### 投资论点构建（详见 `references/full-report-template.md`）
- 核心投资逻辑（2-4 句话）
- Bull / Base / Bear Case 三情景分析
- 关键假设和驱动因素
- 目标价区间推导

#### 催化剂分析（详见 `references/catalyst-analysis.md`）
- 正面催化剂识别（产品发布、市场扩张、监管利好、并购）
- 负面催化剂识别（竞争加剧、监管风险、宏观逆风）
- 催化剂时间表
- 市场预期差分析（催化剂是否已被 price-in）

#### 股价异动分析（详见 `references/price-movement-analysis.md`）
- 下跌/上涨原因分类（公司/行业/宏观/技术因素）
- 临时性波动 vs 结构性变化的判断
- 市场反应是否过度的评估
- 基于异动的投资决策框架

#### 竞争分析与护城河（详见 `references/competitive-moat-analysis.md`）
- Porter 五力分析
- 护城河类型识别（网络效应、转换成本、成本优势、品牌、有效规模）
- SWOT 分析
- 竞争对手对标

#### 业务展望（详见 `references/business-outlook-guide.md`）
- 管理层指引解读
- 财报电话会议关键信息提取
- TAM/SAM/SOM 市场机会评估
- 战略执行评估

#### 风险评估（详见 `references/risk-assessment-framework.md`）
- 五维风险分类（运营/财务/市场/监管/ESG）
- 风险概率 x 影响矩阵量化
- Top 3 关键风险深度分析
- 情景分析和敏感性分析

### 4. 趋势与对比分析

#### 趋势分析
- 多期财务数据对比（季度/年度）
- 关键指标增长率计算
- 同比/环比变化分析

#### 行业对比
- 同行业公司对比
- 行业平均值基准
- 相对估值分析（P/E, P/S, EV/EBITDA 对标）

## 使用方法

### 基础用法（财务分析）

```
分析 AAPL 的最新季度财报
```

```
对比 MSFT 和 GOOGL 的财务状况
```

### 定性分析

```
分析 SE 最近两个季度股价下跌 60% 的原因
```

```
评估 NVDA 的护城河和竞争优势
```

```
分析 TSLA 面临的关键风险因素
```

```
解读 META 管理层最新的业务指引和战略方向
```

### 完整投资分析（推荐）

```
生成 SE 的完整投资分析报告，包括:
1. 投资论点（Bull/Base/Bear Case）
2. 财务分析和趋势
3. 股价下跌原因分析
4. 竞争格局和护城河
5. 催化剂分析
6. 风险评估
7. 估值和目标价
8. 业务展望
```

```
AMZN 深度研究报告：投资论点、竞争优势、催化剂、风险和目标价
```

### 数据输入格式

支持多种输入方式：

1. **股票代码** (推荐)
   ```
   分析 AAPL
   ```

2. **SEC Edgar CIK**
   ```
   获取 CIK 0000320193 的 10-K 报告
   ```

3. **上传财报文件**
   - Excel 格式财务报表
   - CSV 格式财务数据
   - PDF 格式财报（需要解析）

4. **JSON 格式**
   ```json
   {
     "ticker": "AAPL",
     "period": "Q4 2025",
     "income_statement": {...},
     "balance_sheet": {...},
     "cash_flow": {...}
   }
   ```

## 输出格式

### 1. 简要摘要
```
公司: Apple Inc. (AAPL)
报告期: Q4 2025
营收: $119.6B (+8.2% YoY)
净利润: $33.9B (+10.5% YoY)
EPS: $2.18
P/E: 28.5
ROE: 147.3%
评级: 强烈买入 ⭐⭐⭐⭐⭐
```

### 2. 详细报告
- Excel 格式财务比率表
- 趋势分析图表
- 行业对比表
- 投资建议文档
- 风险提示清单

### 3. 可视化
- 收入和利润趋势图
- 财务比率雷达图
- 现金流瀑布图
- 同行业对比柱状图

## 工作流程

### 标准分析流程

1. **数据获取**
   - 获取实时股价和市值（必须验证时效性，详见 `references/data-acquisition-guide.md`）
   - 从 SEC Edgar 获取最新财报
   - 获取财报电话会议记录
   - 收集近期新闻和公告

2. **数据验证**
   - 验证股价是当前实时报价（不能用极值）
   - 交叉验证财报数据
   - 标记缺失和异常项

3. **定量分析**
   - 计算财务比率（参考 `references/ratio-formulas.md`）
   - 多期对比和趋势分析
   - 与行业基准对标（参考 `references/industry-benchmarks.md`）

4. **定性分析**
   - 竞争格局和护城河评估（参考 `references/competitive-moat-analysis.md`）
   - 催化剂识别和评估（参考 `references/catalyst-analysis.md`）
   - 管理层指引和战略解读（参考 `references/business-outlook-guide.md`）
   - 风险评估和量化（参考 `references/risk-assessment-framework.md`）
   - 如有近期股价异动，进行原因分析（参考 `references/price-movement-analysis.md`）

5. **构建投资论点**
   - 提炼核心投资逻辑
   - 构建 Bull / Base / Bear Case
   - 推导目标价区间

6. **生成报告**（参考 `references/full-report-template.md`）
   - 按模板结构输出
   - 明确标注所有数据的时间点和来源
   - 给出明确的投资评级和目标价
   - 列出关键假设和监控指标

### 🚨 数据获取关键原则

#### 股价数据获取

**✅ 正确做法**:
1. 使用实时报价 API 或最新收盘价
2. 明确标注价格时间点（如 "截至 2026年3月6日收盘"）
3. 从可靠来源获取：Yahoo Finance, Google Finance, Bloomberg
4. 验证价格在合理区间内（52周区间内）

**❌ 错误做法**:
1. ❌ 使用 52 周高点作为当前价格
2. ❌ 使用 52 周低点作为当前价格
3. ❌ 使用过时的历史价格
4. ❌ 混淆盘前/盘后价格与正常交易价格
5. ❌ 不标注价格的时间点

**验证清单**:
- [ ] 价格在 52 周区间内
- [ ] 价格时间点明确（日期 + 时间）
- [ ] 价格来源可靠
- [ ] 价格与最近新闻一致
- [ ] 市值 = 股价 × 流通股数 合理

#### 市值数据获取

**计算公式**:
```
市值 = 当前股价 × 流通股数
```

**验证方法**:
1. 从财经网站直接获取市值
2. 用股价 × 流通股数验证
3. 检查是否在合理范围（与同行业对比）

#### 财报数据获取

**优先级**:
1. SEC Edgar 官方文件（最权威）
2. 公司投资者关系网站
3. 财经数据平台（Yahoo Finance, Bloomberg）
4. 新闻稿和财报电话会议

**验证方法**:
1. 交叉验证多个来源
2. 检查数据一致性
3. 确认报告期和发布日期
4. 注意会计政策变更

## 最佳实践

### 数据质量
1. ✅ 优先使用 SEC Edgar 官方数据
2. ✅ 验证数据完整性和一致性
3. ✅ 对异常值进行标注和说明
4. ✅ 使用 XBRL 标准化数据格式

### 分析深度
1. ✅ 至少对比 3-5 年历史数据
2. ✅ 包含季度和年度分析
3. ✅ 考虑行业和宏观经济背景
4. ✅ 同时关注定量和定性因素

### 风险提示
1. ⚠️ 标注不寻常的财务指标
2. ⚠️ 识别会计政策变更影响
3. ⚠️ 提示行业特殊性
4. ⚠️ 说明数据局限性

### 报告质量
1. 📊 使用清晰的可视化
2. 📝 提供具体的数据支持
3. 🎯 给出明确的投资建议
4. ⚡ 突出关键发现

## 示例场景

### 场景 1: 股价异动分析
```
用户: SE 最近两个季度股价从 $199 跌到 $77，为什么？

助手:
1. 获取异动期间的关键事件时间线
2. 分析 Q4 财报: EPS $0.63 miss 预期 $0.91
3. 分析运营费用激增 28%（竞争驱动的营销投入）
4. 分析管理层下调 2026 GMV 增速指引至 25%
5. 评估 TikTok Shop 竞争加剧的结构性影响
6. 判断市场反应是否过度
```

### 场景 2: 完整投资分析
```
用户: 生成 SE 的完整投资分析报告

助手:
1. 执行摘要: 评级 + 目标价 + 核心论点
2. 投资论点: Bull/Base/Bear Case
3. 公司分析: 三大业务板块 + 竞争格局
4. 财务分析: 3 季度趋势 + 关键比率
5. 催化剂: AI 集成、金融牌照、市场扩张
6. 估值: 相对估值 + 目标价
7. 风险: 竞争、利润率、宏观
8. 展望: 管理层指引解读
```

### 场景 3: 竞争与护城河分析
```
用户: 评估 NVDA 的护城河有多宽

助手:
1. Porter 五力分析（GPU 行业）
2. 护城河类型: CUDA 生态转换成本 + 技术领先
3. ROIC vs WACC 超额回报趋势
4. 竞争对手（AMD, Intel, 自研芯片）威胁评估
5. 护城河可持续性判断
```

### 场景 4: 催化剂与风险分析
```
用户: META 接下来有哪些看点和风险？

助手:
1. 正面催化剂: AI 广告优化、Reels 变现、Quest 销量
2. 负面催化剂: 监管压力、TikTok 竞争、元宇宙亏损
3. 催化剂时间表和影响量化
4. 风险矩阵（概率 x 影响评分）
5. 对投资论点的综合影响
```

### 场景 5: 业务展望分析
```
用户: 解读 TSLA 管理层最新的战略方向

助手:
1. 财报电话会议关键发言提取
2. 指引解读: 交付量、毛利率、资本支出
3. 战略评估: FSD、Robotaxi、储能、人形机器人
4. 指引可信度评估（历史兑现率）
5. TAM 市场机会分析
```

## 技术集成

### 推荐工具

#### Python 库
```python
# SEC Edgar 数据获取
import edgartools
from edgartools import Company, Filing

# 财务分析
import pandas as pd
import numpy as np

# 可视化
import matplotlib.pyplot as plt
import seaborn as sns

# 估值模型
from scipy.optimize import minimize
```

#### 数据源
- **SEC Edgar**: 官方财报数据
- **Yahoo Finance**: 实时股价和市值
- **Alpha Vantage**: 补充财务数据
- **FRED**: 宏观经济数据

### 示例代码

#### 获取财报数据
```python
from edgartools import Company

# 获取公司信息
company = Company("AAPL")

# 获取最新 10-K
filing = company.get_filings(form="10-K").latest()

# 提取财务报表
financials = filing.financials
income_stmt = financials.income_statement
balance_sheet = financials.balance_sheet
cash_flow = financials.cash_flow_statement
```

#### 计算财务比率
```python
def calculate_ratios(income_stmt, balance_sheet):
    ratios = {}
    
    # 盈利能力
    ratios['roe'] = income_stmt['net_income'] / balance_sheet['shareholders_equity']
    ratios['roa'] = income_stmt['net_income'] / balance_sheet['total_assets']
    ratios['gross_margin'] = (income_stmt['revenue'] - income_stmt['cost_of_revenue']) / income_stmt['revenue']
    
    # 流动性
    ratios['current_ratio'] = balance_sheet['current_assets'] / balance_sheet['current_liabilities']
    ratios['quick_ratio'] = (balance_sheet['current_assets'] - balance_sheet['inventory']) / balance_sheet['current_liabilities']
    
    # 杠杆
    ratios['debt_to_equity'] = balance_sheet['total_liabilities'] / balance_sheet['shareholders_equity']
    
    return ratios
```

## 局限性

### 数据局限
- ⚠️ 历史数据不代表未来表现
- ⚠️ 某些指标可能不适用所有行业
- ⚠️ 行业基准仅供参考
- ⚠️ 实时股价可能有延迟

### 分析局限
- ⚠️ 无法预测突发事件（黑天鹅）
- ⚠️ 市场情绪和资金流向难以精确量化
- ⚠️ 管理层发言可能存在误导
- ⚠️ 护城河评估具有主观性

### 使用建议
- 💡 定量和定性分析结合使用
- 💡 关注行业特殊性
- 💡 定期更新分析（至少每季度）
- 💡 保持独立思考，不盲从管理层叙事
- 💡 本报告不构成投资建议，决策前请咨询专业顾问

## 相关资源

### 学习资料
- [SEC Edgar 官方文档](https://www.sec.gov/edgar)
- [XBRL 标准说明](https://www.xbrl.org/)
- [财务比率分析指南](https://www.investopedia.com/financial-ratios/)
- [edgartools 文档](https://github.com/dgunning/edgartools)

### 参考文档（本 Skill 包含）

**核心分析框架**:
- `references/full-report-template.md` - **完整报告模板**（分析时必须参考此结构）
- `references/catalyst-analysis.md` - 催化剂分析框架
- `references/price-movement-analysis.md` - 股价异动分析框架
- `references/competitive-moat-analysis.md` - 竞争分析与护城河评估
- `references/business-outlook-guide.md` - 业务展望与战略分析指南
- `references/risk-assessment-framework.md` - 风险评估框架

**数据与计算参考**:
- `references/data-acquisition-guide.md` - **数据获取与验证指南**（必读！）
- `references/ratio-formulas.md` - 财务比率计算公式速查表
- `references/industry-benchmarks.md` - 各行业财务指标基准
- `references/example-analysis.py` - Python 示例分析脚本

### 相关 Skills
- `analyzing-financial-statements` - 基础财务比率计算
- `ljg-paper` - 学术论文分析（可用于研究财报分析方法）
- `financial-data` - 交易数据和风险指标

## 更新日志

- **v2.0** (2026-03-06): 从"财务计算器"升级为"完整投资分析工具"
  - ✅ 新增催化剂分析框架（正面/负面催化剂识别和量化）
  - ✅ 新增股价异动分析框架（下跌原因分类、过度反应判断）
  - ✅ 新增竞争分析与护城河评估（Porter 五力、护城河类型、SWOT）
  - ✅ 新增业务展望指南（管理层指引解读、TAM 分析、战略评估）
  - ✅ 新增风险评估框架（五维分类、概率x影响矩阵、情景分析）
  - ✅ 新增完整报告模板（8节标准股权研究报告结构）
  - ✅ 新增投资论点构建（Bull/Base/Bear Case）
  - ✅ 整合定量和定性分析的完整工作流程

- **v1.1** (2026-03-06): 数据质量改进
  - 🚨 修复股价数据获取错误
  - ✅ 新增数据获取与验证指南

- **v1.0** (2026-03-06): 初始版本
  - SEC Edgar 数据集成、财务比率计算、趋势分析

## 作者

基于 @Microck/analyzing-financial-statements 改编，参考 Wall Street Prep、Finzer 等专业股权研究报告标准，增强了定性分析和完整投资报告生成能力。
