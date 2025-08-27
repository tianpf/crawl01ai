#!/usr/bin/env python3
"""
测试脚本 - 验证豆包MCP服务器功能
Test Script - Verify Doubao MCP Server Functionality
"""

import asyncio
import json
import sys
import os

# 添加当前目录到Python路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from doubao_client import DoubaoClient, DoubaoDataProcessor
from brand_analyzer import BrandAnalyzer, IndustryScorer

async def test_doubao_client():
    """测试豆包客户端功能"""
    print("=== 测试豆包客户端功能 ===")
    
    client = DoubaoClient()
    
    try:
        # 测试品牌搜索
        print("\n1. 测试品牌搜索...")
        search_result = await client.search_brand("华为", {"industry": "科技", "limit": 3})
        print(f"搜索结果: {json.dumps(search_result, ensure_ascii=False, indent=2)}")
        
        # 测试获取品牌详情
        print("\n2. 测试获取品牌详情...")
        if search_result["status"] == "success" and search_result["data"]["results"]:
            brand_id = search_result["data"]["results"][0]["id"]
            details_result = await client.get_brand_details(brand_id)
            print(f"品牌详情: {json.dumps(details_result, ensure_ascii=False, indent=2)}")
        
        # 测试行业分析
        print("\n3. 测试行业分析...")
        industry_result = await client.get_industry_analysis("科技", "china")
        print(f"行业分析: {json.dumps(industry_result, ensure_ascii=False, indent=2)}")
        
        # 测试情感分析
        print("\n4. 测试情感分析...")
        sentiment_result = await client.get_brand_sentiment("华为", "30d")
        print(f"情感分析: {json.dumps(sentiment_result, ensure_ascii=False, indent=2)}")
        
    except Exception as e:
        print(f"测试过程中出现错误: {str(e)}")
    
    finally:
        await client.close()

async def test_brand_analyzer():
    """测试品牌分析器功能"""
    print("\n=== 测试品牌分析器功能 ===")
    
    analyzer = BrandAnalyzer()
    
    # 模拟品牌数据
    brand_data = {
        "brand_name": "华为",
        "industry": "科技",
        "financial_highlights": {
            "market_share": "15%",
            "revenue_growth": "12%",
            "profit_margin": "8%"
        },
        "innovation_index": 8.5,
        "sustainability_rating": "A-",
        "market_presence": {
            "domestic": "强势",
            "international": "中等"
        },
        "brand_value": "60亿美元"
    }
    
    try:
        # 测试品牌数据分析
        print("\n1. 测试深度分析...")
        analysis_result = await analyzer.analyze_brand_data(brand_data)
        print(f"分析结果: {json.dumps(analysis_result, ensure_ascii=False, indent=2)}")
        
    except Exception as e:
        print(f"分析测试中出现错误: {str(e)}")

def test_industry_scorer():
    """测试行业评分器功能"""
    print("\n=== 测试行业评分器功能 ===")
    
    scorer = IndustryScorer()
    
    # 模拟评分数据
    scores = {
        "market_position": 8.2,
        "brand_awareness": 7.8,
        "innovation": 8.5,
        "financial_performance": 7.2,
        "sustainability": 8.0
    }
    
    try:
        # 测试加权评分
        print("\n1. 测试加权评分...")
        weighted_score = scorer.calculate_weighted_score(scores)
        print(f"加权评分: {weighted_score}")
        
        # 测试行业基准对比
        print("\n2. 测试行业基准对比...")
        benchmark_result = scorer.benchmark_against_industry(scores, "科技")
        print(f"基准对比: {json.dumps(benchmark_result, ensure_ascii=False, indent=2)}")
        
    except Exception as e:
        print(f"评分测试中出现错误: {str(e)}")

def test_data_processor():
    """测试数据处理器功能"""
    print("\n=== 测试数据处理器功能 ===")
    
    # 模拟原始数据
    raw_data = {
        "basic_info": {
            "name": "华为",
            "industry": "科技",
            "founded": "1987-01-01",
            "headquarters": "中国深圳"
        },
        "financial_metrics": {
            "revenue_growth_yoy": "12%",
            "profit_margin": "8%",
            "market_share": "15%",
            "brand_value": "60亿美元",
            "revenue_breakdown": {
                "domestic": "70%",
                "international": "30%"
            }
        },
        "innovation_metrics": {
            "innovation_index": 8.5
        },
        "sustainability": {
            "esg_rating": "A-"
        }
    }
    
    try:
        # 测试数据标准化
        print("\n1. 测试数据标准化...")
        normalized_data = DoubaoDataProcessor.normalize_brand_data(raw_data)
        print(f"标准化数据: {json.dumps(normalized_data, ensure_ascii=False, indent=2)}")
        
        # 测试关键洞察提取
        print("\n2. 测试关键洞察提取...")
        insights = DoubaoDataProcessor.extract_key_insights(normalized_data)
        print(f"关键洞察: {insights}")
        
    except Exception as e:
        print(f"数据处理测试中出现错误: {str(e)}")

async def main():
    """主测试函数"""
    print("豆包MCP服务器功能测试")
    print("=" * 50)
    
    # 运行各项测试
    await test_doubao_client()
    await test_brand_analyzer()
    test_industry_scorer()
    test_data_processor()
    
    print("\n" + "=" * 50)
    print("测试完成!")

if __name__ == "__main__":
    asyncio.run(main())