# 数据获取与验证指南

## 🎯 核心原则

**数据质量 > 数据数量**

所有分析的基础是准确、及时的数据。错误的数据会导致错误的结论。

---

## 📊 股价数据获取

### 1. 获取实时/最新股价

#### ✅ 推荐方法

**方法 A: 使用 Yahoo Finance API**
```python
import yfinance as yf

ticker = yf.Ticker("AAPL")
current_price = ticker.info['currentPrice']
market_cap = ticker.info['marketCap']
volume = ticker.info['volume']

print(f"当前价格: ${current_price}")
print(f"市值: ${market_cap/1e9:.1f}B")
print(f"更新时间: {ticker.info['regularMarketTime']}")
```

**方法 B: 使用 Web 搜索（当 API 不可用时）**
```
搜索关键词: "AAPL stock price real-time quote today"
```

**必须包含的信息**:
- 当前价格或最新收盘价
- 价格时间点（日期 + 时间）
- 交易量
- 52周区间（用于验证）

#### ❌ 常见错误

**错误 1: 使用极值价格**
```
❌ 错误: "当前股价: $77.05（52周低点）"
✅ 正确: "当前股价: $108.51（2026年3月6日收盘）"
       "52周区间: $77.05 - $199.30"
```

**错误 2: 不标注时间**
```
❌ 错误: "股价 $150"
✅ 正确: "股价 $150（2026年3月6日 16:00 EST 收盘）"
```

**错误 3: 混淆不同时间点的价格**
```
❌ 错误: 使用盘前价格计算 P/E
✅ 正确: 使用正常交易时段收盘价
```

**错误 4: 使用过时数据**
```
❌ 错误: "当前股价 $199（2025年10月数据）"
✅ 正确: "当前股价 $108（2026年3月6日），
       历史高点 $199（2025年10月）"
```

### 2. 验证股价数据

**验证清单**:

```
[ ] 价格在 52 周区间内
    - 如果超出，需要更新 52 周区间
    - 或者数据源有误

[ ] 价格时间点明确
    - 必须包含日期
    - 最好包含具体时间
    - 标注时区（EST/EDT）

[ ] 价格来源可靠
    - Yahoo Finance ✅
    - Google Finance ✅
    - Bloomberg ✅
    - CNBC ✅
    - 随机网站 ❌

[ ] 价格与最近新闻一致
    - 如果有重大新闻，价格应该反映
    - 财报发布后，价格应该有波动

[ ] 市值计算合理
    - 市值 = 股价 × 流通股数
    - 与财经网站显示的市值接近
    - 误差应 < 5%
```

**验证示例**:

```python
def validate_stock_price(ticker, price, date):
    """验证股价数据"""
    import yfinance as yf
    
    stock = yf.Ticker(ticker)
    info = stock.info
    
    # 检查 1: 价格在 52 周区间内
    week_52_low = info['fiftyTwoWeekLow']
    week_52_high = info['fiftyTwoWeekHigh']
    
    if not (week_52_low <= price <= week_52_high):
        print(f"⚠️ 警告: 价格 ${price} 超出 52周区间 ${week_52_low}-${week_52_high}")
        return False
    
    # 检查 2: 市值合理性
    shares_outstanding = info['sharesOutstanding']
    calculated_market_cap = price * shares_outstanding
    reported_market_cap = info['marketCap']
    
    diff_pct = abs(calculated_market_cap - reported_market_cap) / reported_market_cap * 100
    
    if diff_pct > 5:
        print(f"⚠️ 警告: 市值计算偏差 {diff_pct:.1f}%")
        return False
    
    print(f"✅ 价格验证通过: ${price} ({date})")
    return True
```

---

## 💰 市值数据获取

### 1. 获取市值

**方法 A: 直接获取**
```python
import yfinance as yf

ticker = yf.Ticker("AAPL")
market_cap = ticker.info['marketCap']
print(f"市值: ${market_cap/1e9:.1f}B")
```

**方法 B: 计算**
```
市值 = 当前股价 × 流通股数
```

### 2. 验证市值

**交叉验证**:
```
1. Yahoo Finance 显示的市值
2. Google Finance 显示的市值
3. 股价 × 流通股数 计算的市值

三者应该接近（误差 < 5%）
```

**合理性检查**:
```
- 与同行业公司对比
- 与历史市值对比
- 与公司规模（营收、利润）匹配
```

---

## 📈 财报数据获取

### 1. SEC Edgar（最权威）

**获取步骤**:

1. 访问 SEC Edgar: https://www.sec.gov/edgar/searchedgar/companysearch.html
2. 搜索公司名称或 Ticker
3. 选择报告类型：
   - 10-K: 年度报告
   - 10-Q: 季度报告
   - 8-K: 重大事件报告
4. 下载 XBRL 格式（标准化数据）

**使用 edgartools**:
```python
from edgartools import Company

# 获取公司
company = Company("AAPL")

# 获取最新 10-K
filing = company.get_filings(form="10-K").latest()

# 提取财务报表
financials = filing.financials
income_stmt = financials.income_statement
balance_sheet = financials.balance_sheet
cash_flow = financials.cash_flow_statement

# 查看数据
print(income_stmt.head())
```

### 2. 公司投资者关系网站

**优点**:
- 数据完整
- 包含演示文稿
- 有财报电话会议记录

**示例**:
- Apple: https://investor.apple.com
- Microsoft: https://www.microsoft.com/en-us/investor
- Tesla: https://ir.tesla.com

### 3. 财经数据平台

**Yahoo Finance**:
```python
import yfinance as yf

ticker = yf.Ticker("AAPL")

# 财务报表
income_stmt = ticker.financials
balance_sheet = ticker.balance_sheet
cash_flow = ticker.cashflow

# 关键指标
info = ticker.info
revenue = info['totalRevenue']
net_income = info['netIncomeToCommon']
```

**注意事项**:
- 数据可能有延迟
- 可能缺少某些细节
- 需要与 SEC 文件交叉验证

---

## 🔍 数据验证流程

### 标准验证流程

```
1. 数据获取
   ↓
2. 初步检查（完整性）
   ↓
3. 合理性验证（是否在正常范围）
   ↓
4. 交叉验证（多个来源对比）
   ↓
5. 时效性确认（数据是否最新）
   ↓
6. 标注来源和时间
```

### 验证检查表

#### 股价数据
- [ ] 价格在 52 周区间内
- [ ] 标注了具体时间点
- [ ] 来源可靠
- [ ] 与最近新闻一致
- [ ] 市值计算合理

#### 财报数据
- [ ] 来自官方来源（SEC Edgar）
- [ ] 报告期明确
- [ ] 数据完整（三大报表）
- [ ] 与上期数据连贯
- [ ] 无异常波动（或有合理解释）

#### 财务比率
- [ ] 计算公式正确
- [ ] 使用同期数据
- [ ] 在行业合理范围内
- [ ] 趋势合理
- [ ] 标注了计算方法

---

## 📝 数据标注规范

### 股价标注

**完整格式**:
```
股价: $108.51
时间: 2026年3月6日 16:00 EST 收盘
来源: Yahoo Finance
52周区间: $77.05 - $199.30
```

**简化格式**:
```
当前股价: $108.51（2026年3月6日收盘）
```

### 财报数据标注

**完整格式**:
```
营收: $119.6B
报告期: Q4 2025（2025年10月-12月）
发布日期: 2026年2月3日
来源: SEC 10-K
```

**简化格式**:
```
Q4 2025 营收: $119.6B
```

### 财务比率标注

**完整格式**:
```
ROE: 54.0%
计算: 净利润 $33.9B / 股东权益 $62.8B
数据期: Q4 2025
```

**简化格式**:
```
ROE: 54.0%（Q4 2025）
```

---

## 🚨 常见错误与修正

### 错误 1: 使用极值价格

**错误示例**:
```
当前股价: $77.05
市值: $43B
P/E: 25x
```

**问题**:
- $77.05 是 52 周低点，不是当前价格
- 导致市值、P/E 等所有估值指标错误

**正确做法**:
```
当前股价: $108.51（2026年3月6日收盘）
52周区间: $77.05 - $199.30
市值: $60.5B
P/E: 36x
```

### 错误 2: 混淆不同时期数据

**错误示例**:
```
P/E = 当前股价 / 去年 EPS
```

**问题**:
- 股价是最新的，EPS 是过时的
- 应该使用 TTM（过去12个月）EPS

**正确做法**:
```
P/E (TTM) = 当前股价 / 过去12个月 EPS
或
P/E (Forward) = 当前股价 / 预期未来12个月 EPS
```

### 错误 3: 不标注数据时间

**错误示例**:
```
营收: $119.6B
净利润: $33.9B
```

**问题**:
- 不知道是哪个季度/年度的数据
- 无法进行趋势分析

**正确做法**:
```
Q4 2025 财务数据:
- 营收: $119.6B (+8.2% YoY)
- 净利润: $33.9B (+10.5% YoY)
- 报告期: 2025年10月-12月
```

### 错误 4: 单一来源数据

**错误示例**:
```
仅从一个新闻网站获取数据
```

**问题**:
- 可能有错误或过时
- 可能缺少关键信息

**正确做法**:
```
交叉验证:
1. SEC Edgar（官方财报）
2. Yahoo Finance（市场数据）
3. 公司 IR 网站（演示文稿）
4. 财报电话会议（管理层解读）
```

---

## 🛠️ 实用工具

### Python 库

```bash
# 安装必要的库
pip install yfinance edgartools pandas numpy
```

### 数据获取脚本

```python
import yfinance as yf
from datetime import datetime

def get_stock_data(ticker):
    """获取完整的股票数据"""
    
    stock = yf.Ticker(ticker)
    info = stock.info
    
    # 当前价格
    current_price = info.get('currentPrice') or info.get('regularMarketPrice')
    
    # 验证价格
    week_52_low = info['fiftyTwoWeekLow']
    week_52_high = info['fiftyTwoWeekHigh']
    
    if not (week_52_low <= current_price <= week_52_high):
        print(f"⚠️ 警告: 价格可能有误")
    
    # 返回数据
    data = {
        'ticker': ticker,
        'current_price': current_price,
        'market_cap': info['marketCap'],
        'pe_ratio': info.get('trailingPE'),
        'week_52_range': f"${week_52_low:.2f} - ${week_52_high:.2f}",
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'source': 'Yahoo Finance'
    }
    
    return data

# 使用示例
data = get_stock_data("AAPL")
print(f"股价: ${data['current_price']:.2f}")
print(f"时间: {data['timestamp']}")
print(f"来源: {data['source']}")
```

---

## 📋 数据获取检查清单

在开始分析前，确保完成以下检查：

### 股价数据
- [ ] 获取了实时/最新收盘价
- [ ] 价格在 52 周区间内
- [ ] 标注了价格时间点
- [ ] 标注了数据来源
- [ ] 验证了市值计算

### 财报数据
- [ ] 从 SEC Edgar 获取官方数据
- [ ] 确认了报告期和发布日期
- [ ] 获取了完整的三大报表
- [ ] 数据与上期连贯
- [ ] 交叉验证了关键数字

### 市场数据
- [ ] 获取了交易量
- [ ] 获取了流通股数
- [ ] 获取了 52 周区间
- [ ] 获取了分析师评级（如需要）

### 文档
- [ ] 所有数据都标注了时间
- [ ] 所有数据都标注了来源
- [ ] 关键假设已说明
- [ ] 数据局限性已提示

---

## 🎯 最佳实践总结

### DO ✅

1. **使用实时数据**
   - 获取最新的股价和市值
   - 使用当天或最近交易日的收盘价

2. **明确标注**
   - 所有数据标注时间点
   - 所有数据标注来源
   - 计算方法清晰说明

3. **交叉验证**
   - 从多个来源获取数据
   - 验证数据的一致性
   - 检查合理性

4. **保持更新**
   - 定期更新数据
   - 关注最新财报
   - 跟踪重大新闻

### DON'T ❌

1. **不要使用极值**
   - ❌ 不要用 52 周高点作为当前价格
   - ❌ 不要用 52 周低点作为当前价格

2. **不要混淆时间**
   - ❌ 不要混用不同时期的数据
   - ❌ 不要使用过时的数据

3. **不要省略标注**
   - ❌ 不要省略数据时间点
   - ❌ 不要省略数据来源

4. **不要单一来源**
   - ❌ 不要只从一个来源获取数据
   - ❌ 不要不验证数据准确性

---

## 📞 数据来源推荐

### 免费数据源

1. **SEC Edgar** (官方财报)
   - https://www.sec.gov/edgar

2. **Yahoo Finance** (股价、财报)
   - https://finance.yahoo.com

3. **Google Finance** (股价、基本面)
   - https://www.google.com/finance

4. **CNBC** (实时报价)
   - https://www.cnbc.com/quotes/

5. **公司 IR 网站** (官方信息)
   - 各公司投资者关系页面

### 付费数据源（更专业）

1. **Bloomberg Terminal**
2. **FactSet**
3. **S&P Capital IQ**
4. **Refinitiv Eikon**

---

**记住**: 准确的数据是优秀分析的基础！
