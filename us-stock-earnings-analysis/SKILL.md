---
name: us-stock-earnings-analysis
description: 美股财报深度分析工具，支持 SEC Edgar 数据获取、财务比率计算、多期对比和投资洞察生成
---

# 美股财报深度分析 Skill

这个 skill 提供全面的美股上市公司财报分析能力，从 SEC Edgar 获取数据到生成投资洞察的完整工作流。

## 核心能力

### 1. 数据获取
- **SEC Edgar 集成**: 自动获取 10-K、10-Q、8-K 等财报文件
- **XBRL 解析**: 标准化财务数据，支持跨公司对比
- **实时更新**: 获取最新财报和季度报告
- **历史数据**: 支持多年历史数据分析

### 2. 财务比率计算

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

### 3. 分析功能

#### 趋势分析
- 多期财务数据对比（季度/年度）
- 关键指标增长率计算
- 同比/环比变化分析
- 可视化趋势图表

#### 行业对比
- 同行业公司对比
- 行业平均值基准
- 相对估值分析
- 竞争优势识别

#### 风险评估
- 财务健康度评分
- 破产风险指标（Altman Z-Score）
- 现金流健康度
- 债务压力测试

#### 投资洞察
- 价值投资指标
- 成长性评估
- 股息投资分析
- 风险收益比

## 使用方法

### 基础用法

```
分析 AAPL 的最新季度财报
```

```
对比 MSFT 和 GOOGL 的财务状况
```

```
计算 TSLA 的所有估值指标
```

### 高级用法

```
分析 NVDA 过去 5 年的盈利能力趋势
```

```
评估 META 的现金流健康度和债务风险
```

```
对比科技行业（AAPL, MSFT, GOOGL, META）的 ROE 和 P/E
```

```
生成 AMZN 的完整投资分析报告，包括财务比率、趋势分析和投资建议
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
   - 从 SEC Edgar 获取最新财报
   - 解析 XBRL 数据
   - 提取三大财务报表

2. **数据验证**
   - 检查数据完整性
   - 识别异常值
   - 标记缺失项

3. **比率计算**
   - 计算所有相关财务比率
   - 多期数据对比
   - 计算增长率

4. **分析解读**
   - 行业基准对比
   - 识别优势和风险
   - 趋势判断

5. **生成报告**
   - 结构化输出
   - 可视化图表
   - 投资建议

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

### 场景 1: 快速财报分析
```
用户: 分析 NVDA 最新季度财报

助手:
1. 从 SEC Edgar 获取 NVDA Q4 2025 10-Q
2. 计算关键财务比率
3. 对比上一季度和去年同期
4. 生成简要摘要和投资评级
```

### 场景 2: 深度价值投资分析
```
用户: 评估 BRK.B 是否被低估

助手:
1. 获取 5 年历史财务数据
2. 计算内在价值（DCF 模型）
3. 对比 P/B、P/E 历史区间
4. 分析安全边际
5. 给出买入/持有/卖出建议
```

### 场景 3: 行业对比
```
用户: 对比半导体行业龙头（NVDA, AMD, INTC）

助手:
1. 获取三家公司最新财报
2. 计算标准化财务比率
3. 生成对比表格和图表
4. 识别各自优势和劣势
5. 推荐最佳投资标的
```

### 场景 4: 风险评估
```
用户: 评估 TSLA 的财务风险

助手:
1. 分析债务结构和偿债能力
2. 计算 Altman Z-Score
3. 评估现金流稳定性
4. 识别潜在风险因素
5. 给出风险等级评分
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
- ⚠️ 需要准确的财务数据输入

### 分析局限
- ⚠️ 无法预测突发事件影响
- ⚠️ 不考虑管理层质量等定性因素
- ⚠️ 市场情绪难以量化
- ⚠️ 宏观经济变化影响

### 使用建议
- 💡 结合多种分析方法
- 💡 关注行业特殊性
- 💡 定期更新分析
- 💡 不要单纯依赖量化指标
- 💡 咨询专业财务顾问

## 相关资源

### 学习资料
- [SEC Edgar 官方文档](https://www.sec.gov/edgar)
- [XBRL 标准说明](https://www.xbrl.org/)
- [财务比率分析指南](https://www.investopedia.com/financial-ratios/)
- [edgartools 文档](https://github.com/dgunning/edgartools)

### 相关 Skills
- `analyzing-financial-statements` - 基础财务比率计算
- `ljg-paper` - 学术论文分析（可用于研究财报分析方法）
- `financial-data` - 交易数据和风险指标

## 更新日志

- **v1.0** (2026-03-06): 初始版本
  - SEC Edgar 数据集成
  - 完整财务比率计算
  - 趋势和行业对比分析
  - 投资洞察生成

## 作者

改编自 @Microck/analyzing-financial-statements，增强了美股特定功能和 SEC Edgar 集成。
