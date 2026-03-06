#!/usr/bin/env python3
"""
美股财报分析示例脚本

依赖安装:
pip install edgartools pandas numpy yfinance matplotlib seaborn openpyxl

使用方法:
python example-analysis.py AAPL
"""

import sys
from typing import Dict, Any, Optional
import pandas as pd
import numpy as np

# 注意: 这是示例代码，实际使用需要安装相应的库


def get_stock_data(ticker: str) -> Dict[str, Any]:
    """
    从 SEC Edgar 获取股票财务数据
    
    Args:
        ticker: 股票代码，如 'AAPL'
    
    Returns:
        包含财务数据的字典
    """
    try:
        # 使用 edgartools 获取数据
        # from edgartools import Company
        # company = Company(ticker)
        # filing = company.get_filings(form="10-K").latest()
        # financials = filing.financials
        
        # 这里使用模拟数据作为示例
        return {
            'ticker': ticker,
            'company_name': f'{ticker} Inc.',
            'period': 'Q4 2025',
            'income_statement': {
                'revenue': 119_600_000_000,
                'cost_of_revenue': 52_800_000_000,
                'gross_profit': 66_800_000_000,
                'operating_expenses': 32_900_000_000,
                'operating_income': 33_900_000_000,
                'interest_expense': 800_000_000,
                'net_income': 33_900_000_000,
                'shares_outstanding': 15_550_000_000,
            },
            'balance_sheet': {
                'current_assets': 135_400_000_000,
                'inventory': 6_500_000_000,
                'cash': 61_000_000_000,
                'total_assets': 352_800_000_000,
                'current_liabilities': 125_500_000_000,
                'total_liabilities': 290_000_000_000,
                'shareholders_equity': 62_800_000_000,
            },
            'cash_flow': {
                'operating_cash_flow': 110_500_000_000,
                'capex': 10_900_000_000,
                'free_cash_flow': 99_600_000_000,
            },
            'market_data': {
                'stock_price': 185.50,
                'market_cap': 2_884_525_000_000,
            }
        }
    except Exception as e:
        print(f"获取数据失败: {e}")
        return None


def calculate_profitability_ratios(data: Dict[str, Any]) -> Dict[str, float]:
    """计算盈利能力指标"""
    income = data['income_statement']
    balance = data['balance_sheet']
    
    ratios = {
        'roe': income['net_income'] / balance['shareholders_equity'] * 100,
        'roa': income['net_income'] / balance['total_assets'] * 100,
        'gross_margin': (income['revenue'] - income['cost_of_revenue']) / income['revenue'] * 100,
        'operating_margin': income['operating_income'] / income['revenue'] * 100,
        'net_margin': income['net_income'] / income['revenue'] * 100,
    }
    
    return ratios


def calculate_liquidity_ratios(data: Dict[str, Any]) -> Dict[str, float]:
    """计算流动性指标"""
    balance = data['balance_sheet']
    
    ratios = {
        'current_ratio': balance['current_assets'] / balance['current_liabilities'],
        'quick_ratio': (balance['current_assets'] - balance['inventory']) / balance['current_liabilities'],
        'cash_ratio': balance['cash'] / balance['current_liabilities'],
    }
    
    return ratios


def calculate_leverage_ratios(data: Dict[str, Any]) -> Dict[str, float]:
    """计算杠杆指标"""
    income = data['income_statement']
    balance = data['balance_sheet']
    
    ratios = {
        'debt_to_assets': balance['total_liabilities'] / balance['total_assets'] * 100,
        'debt_to_equity': balance['total_liabilities'] / balance['shareholders_equity'],
        'interest_coverage': income['operating_income'] / income['interest_expense'] if income['interest_expense'] > 0 else float('inf'),
    }
    
    return ratios


def calculate_valuation_ratios(data: Dict[str, Any]) -> Dict[str, float]:
    """计算估值指标"""
    income = data['income_statement']
    balance = data['balance_sheet']
    market = data['market_data']
    
    eps = income['net_income'] / income['shares_outstanding']
    book_value_per_share = balance['shareholders_equity'] / income['shares_outstanding']
    
    ratios = {
        'eps': eps,
        'pe': market['stock_price'] / eps,
        'pb': market['stock_price'] / book_value_per_share,
        'ps': market['market_cap'] / income['revenue'],
    }
    
    return ratios


def calculate_cash_flow_ratios(data: Dict[str, Any]) -> Dict[str, float]:
    """计算现金流指标"""
    income = data['income_statement']
    cash_flow = data['cash_flow']
    
    ratios = {
        'ocf_margin': cash_flow['operating_cash_flow'] / income['revenue'] * 100,
        'fcf': cash_flow['free_cash_flow'],
        'fcf_margin': cash_flow['free_cash_flow'] / income['revenue'] * 100,
    }
    
    return ratios


def interpret_ratio(ratio_name: str, value: float) -> str:
    """解读财务比率"""
    interpretations = {
        'roe': [(15, '优秀 ⭐⭐⭐⭐⭐'), (10, '良好 ⭐⭐⭐⭐'), (5, '一般 ⭐⭐⭐'), (0, '较差 ⭐⭐')],
        'roa': [(10, '优秀 ⭐⭐⭐⭐⭐'), (5, '良好 ⭐⭐⭐⭐'), (2, '一般 ⭐⭐⭐'), (0, '较差 ⭐⭐')],
        'gross_margin': [(60, '优秀 ⭐⭐⭐⭐⭐'), (40, '良好 ⭐⭐⭐⭐'), (20, '一般 ⭐⭐⭐'), (0, '较差 ⭐⭐')],
        'operating_margin': [(20, '优秀 ⭐⭐⭐⭐⭐'), (10, '良好 ⭐⭐⭐⭐'), (5, '一般 ⭐⭐⭐'), (0, '较差 ⭐⭐')],
        'net_margin': [(15, '优秀 ⭐⭐⭐⭐⭐'), (8, '良好 ⭐⭐⭐⭐'), (3, '一般 ⭐⭐⭐'), (0, '较差 ⭐⭐')],
        'current_ratio': [(2.0, '优秀 ⭐⭐⭐⭐⭐'), (1.5, '良好 ⭐⭐⭐⭐'), (1.0, '一般 ⭐⭐⭐'), (0, '风险 ⚠️')],
        'quick_ratio': [(1.5, '优秀 ⭐⭐⭐⭐⭐'), (1.0, '良好 ⭐⭐⭐⭐'), (0.8, '一般 ⭐⭐⭐'), (0, '风险 ⚠️')],
        'pe': [(15, '低估 💰'), (25, '合理 ✓'), (40, '高估 ⚠️'), (float('inf'), '极高估 ⚠️⚠️')],
        'pb': [(1.0, '低估 💰'), (3.0, '合理 ✓'), (5.0, '高估 ⚠️'), (float('inf'), '极高估 ⚠️⚠️')],
    }
    
    if ratio_name not in interpretations:
        return '无基准'
    
    thresholds = interpretations[ratio_name]
    for threshold, interpretation in thresholds:
        if value >= threshold:
            return interpretation
    
    return thresholds[-1][1]


def generate_report(ticker: str):
    """生成完整的财报分析报告"""
    print(f"\n{'='*80}")
    print(f"美股财报分析报告 - {ticker}")
    print(f"{'='*80}\n")
    
    # 获取数据
    data = get_stock_data(ticker)
    if not data:
        print("无法获取数据")
        return
    
    print(f"公司: {data['company_name']}")
    print(f"报告期: {data['period']}")
    print(f"股价: ${data['market_data']['stock_price']:.2f}")
    print(f"市值: ${data['market_data']['market_cap']/1e9:.1f}B\n")
    
    # 计算所有比率
    profitability = calculate_profitability_ratios(data)
    liquidity = calculate_liquidity_ratios(data)
    leverage = calculate_leverage_ratios(data)
    valuation = calculate_valuation_ratios(data)
    cash_flow = calculate_cash_flow_ratios(data)
    
    # 盈利能力
    print("=" * 80)
    print("📊 盈利能力指标")
    print("=" * 80)
    print(f"ROE (净资产收益率):    {profitability['roe']:>8.2f}%  {interpret_ratio('roe', profitability['roe'])}")
    print(f"ROA (总资产收益率):    {profitability['roa']:>8.2f}%  {interpret_ratio('roa', profitability['roa'])}")
    print(f"毛利率:               {profitability['gross_margin']:>8.2f}%  {interpret_ratio('gross_margin', profitability['gross_margin'])}")
    print(f"营业利润率:           {profitability['operating_margin']:>8.2f}%  {interpret_ratio('operating_margin', profitability['operating_margin'])}")
    print(f"净利率:               {profitability['net_margin']:>8.2f}%  {interpret_ratio('net_margin', profitability['net_margin'])}")
    
    # 流动性
    print("\n" + "=" * 80)
    print("💧 流动性指标")
    print("=" * 80)
    print(f"流动比率:             {liquidity['current_ratio']:>8.2f}   {interpret_ratio('current_ratio', liquidity['current_ratio'])}")
    print(f"速动比率:             {liquidity['quick_ratio']:>8.2f}   {interpret_ratio('quick_ratio', liquidity['quick_ratio'])}")
    print(f"现金比率:             {liquidity['cash_ratio']:>8.2f}")
    
    # 杠杆
    print("\n" + "=" * 80)
    print("⚖️  杠杆指标")
    print("=" * 80)
    print(f"资产负债率:           {leverage['debt_to_assets']:>8.2f}%")
    print(f"债务权益比:           {leverage['debt_to_equity']:>8.2f}")
    print(f"利息保障倍数:         {leverage['interest_coverage']:>8.2f}")
    
    # 估值
    print("\n" + "=" * 80)
    print("💰 估值指标")
    print("=" * 80)
    print(f"EPS (每股收益):       ${valuation['eps']:>7.2f}")
    print(f"P/E (市盈率):         {valuation['pe']:>8.2f}   {interpret_ratio('pe', valuation['pe'])}")
    print(f"P/B (市净率):         {valuation['pb']:>8.2f}   {interpret_ratio('pb', valuation['pb'])}")
    print(f"P/S (市销率):         {valuation['ps']:>8.2f}")
    
    # 现金流
    print("\n" + "=" * 80)
    print("💵 现金流指标")
    print("=" * 80)
    print(f"经营现金流利润率:     {cash_flow['ocf_margin']:>8.2f}%")
    print(f"自由现金流:           ${cash_flow['fcf']/1e9:>7.1f}B")
    print(f"自由现金流利润率:     {cash_flow['fcf_margin']:>8.2f}%")
    
    # 综合评级
    print("\n" + "=" * 80)
    print("⭐ 综合评级")
    print("=" * 80)
    
    score = 0
    if profitability['roe'] > 15: score += 1
    if profitability['net_margin'] > 15: score += 1
    if liquidity['current_ratio'] > 1.5: score += 1
    if leverage['debt_to_equity'] < 1.0: score += 1
    if valuation['pe'] < 25: score += 1
    
    ratings = {
        5: "强烈买入 ⭐⭐⭐⭐⭐",
        4: "买入 ⭐⭐⭐⭐",
        3: "持有 ⭐⭐⭐",
        2: "观望 ⭐⭐",
        1: "谨慎 ⭐",
        0: "回避 ⚠️"
    }
    
    print(f"评分: {score}/5")
    print(f"建议: {ratings[score]}")
    
    print("\n" + "=" * 80)
    print("⚠️  免责声明")
    print("=" * 80)
    print("本报告仅供参考，不构成投资建议。投资有风险，决策需谨慎。")
    print("=" * 80 + "\n")


def main():
    """主函数"""
    if len(sys.argv) < 2:
        print("使用方法: python example-analysis.py <股票代码>")
        print("示例: python example-analysis.py AAPL")
        sys.exit(1)
    
    ticker = sys.argv[1].upper()
    generate_report(ticker)


if __name__ == "__main__":
    main()
