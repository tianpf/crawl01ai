#!/usr/bin/env python3
"""
豆包MCP服务器使用示例
Usage Example for Doubao MCP Server
"""

import asyncio
import json
import sys
import os

# 添加当前目录到Python路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from doubao_client import DoubaoClient, DoubaoDataProcessor
from brand_analyzer import BrandAnalyzer, IndustryScorer

async def demo_brand_analysis(brand_name: str = "小米"):
    """演示完整的品牌分析流程"""
    print(f"🔍 开始分析品牌: {brand_name}")
    print("=" * 60)
    
    # 1. 初始化客户端
    client = DoubaoClient()
    analyzer = BrandAnalyzer()
    scorer = IndustryScorer()
    
    try:
        # 2. 搜索品牌信息
        print(f"\n📊 第1步: 搜索品牌信息...")
        search_result = await client.search_brand(brand_name, {"industry": "科技", "limit": 5})
        
        if search_result["status"] == "success":
            print(f"✅ 找到 {len(search_result['data']['results'])} 条相关结果")
            
            # 3. 获取详细信息
            brand_id = search_result["data"]["results"][0]["id"]
            print(f"\n📋 第2步: 获取品牌详细信息...")
            details_result = await client.get_brand_details(brand_id)
            
            if details_result["status"] == "success":
                raw_data = details_result["data"]
                
                # 4. 数据标准化
                print(f"\n🔄 第3步: 数据标准化处理...")
                normalized_data = DoubaoDataProcessor.normalize_brand_data(raw_data)
                print(f"✅ 品牌: {normalized_data['brand_name']}")
                print(f"✅ 行业: {normalized_data['industry']}")
                print(f"✅ 总部: {normalized_data['headquarters']}")
                
                # 5. 生成评分
                print(f"\n🎯 第4步: 生成行业评分...")
                scoring_criteria = ["market_position", "brand_awareness", "innovation", "financial_performance", "sustainability"]
                
                # 模拟评分计算
                scores = {}
                for criterion in scoring_criteria:
                    if criterion == "market_position":
                        market_share = float(normalized_data.get("financial_highlights", {}).get("market_share", "0%").replace("%", ""))
                        scores[criterion] = min(market_share * 0.8, 10)
                    elif criterion == "innovation":
                        scores[criterion] = normalized_data.get("innovation_index", 5.0)
                    elif criterion == "financial_performance":
                        revenue_growth = float(normalized_data.get("financial_highlights", {}).get("revenue_growth", "0%").replace("%", ""))
                        profit_margin = float(normalized_data.get("financial_highlights", {}).get("profit_margin", "0%").replace("%", ""))
                        scores[criterion] = min((revenue_growth + profit_margin) / 3, 10)
                    elif criterion == "sustainability":
                        rating_map = {"A+": 10, "A": 9, "A-": 8, "B+": 7, "B": 6, "B-": 5, "C+": 4, "C": 3, "C-": 2, "D": 1}
                        scores[criterion] = rating_map.get(normalized_data.get("sustainability_rating", "C"), 5)
                    else:
                        scores[criterion] = 7.0  # 默认分数
                
                # 计算加权评分
                weighted_score = scorer.calculate_weighted_score(scores)
                
                print(f"✅ 详细评分:")
                for criterion, score in scores.items():
                    dimension_name = {
                        "market_position": "市场地位",
                        "brand_awareness": "品牌知名度", 
                        "innovation": "创新能力",
                        "financial_performance": "财务表现",
                        "sustainability": "可持续性"
                    }
                    print(f"   {dimension_name.get(criterion, criterion)}: {score:.2f}/10")
                
                print(f"✅ 综合评分: {weighted_score:.2f}/10")
                
                # 6. 行业基准对比
                print(f"\n📈 第5步: 行业基准对比...")
                benchmark_result = scorer.benchmark_against_industry(scores, "科技")
                print(f"✅ 行业排名: {benchmark_result['overall_ranking']}")
                
                # 7. 深度分析
                print(f"\n🧠 第6步: 深度品牌分析...")
                analysis_result = await analyzer.analyze_brand_data(normalized_data)
                
                if analysis_result["status"] == "success":
                    analysis = analysis_result["analysis"]
                    print(f"✅ 竞争地位: {analysis['competitive_position']['position']}")
                    print(f"✅ 市场趋势: {analysis['market_trends']['overall_trend']}")
                    print(f"✅ 风险水平: {analysis['risk_assessment']['risk_level']}")
                    print(f"✅ 增长潜力: {analysis['growth_potential']['growth_potential']}")
                
                # 8. 关键洞察
                print(f"\n💡 第7步: 关键洞察提取...")
                insights = DoubaoDataProcessor.extract_key_insights(normalized_data)
                print("✅ 关键洞察:")
                for i, insight in enumerate(insights, 1):
                    print(f"   {i}. {insight}")
                
                # 9. 情感分析
                print(f"\n😊 第8步: 品牌情感分析...")
                sentiment_result = await client.get_brand_sentiment(brand_name, "30d")
                
                if sentiment_result["status"] == "success":
                    sentiment = sentiment_result["data"]["overall_sentiment"]
                    print(f"✅ 情感评分: {sentiment['score']:.1f}/10 ({sentiment['label']})")
                    print(f"✅ 置信度: {sentiment['confidence']:.1%}")
                
                # 10. 生成总结报告
                print(f"\n📄 第9步: 生成分析报告...")
                
                grade = "A+" if weighted_score >= 9 else "A" if weighted_score >= 8 else "B+" if weighted_score >= 7 else "B" if weighted_score >= 6 else "C"
                
                print(f"\n🎉 {brand_name} 品牌分析报告")
                print("=" * 60)
                print(f"📊 综合评分: {weighted_score:.2f}/10 (等级: {grade})")
                print(f"🏆 行业排名: {benchmark_result['overall_ranking']}")
                print(f"📈 竞争地位: {analysis['competitive_position']['position']}")
                print(f"💰 市场份额: {normalized_data.get('financial_highlights', {}).get('market_share', 'N/A')}")
                print(f"🚀 创新指数: {normalized_data.get('innovation_index', 'N/A')}/10")
                print(f"🌱 ESG评级: {normalized_data.get('sustainability_rating', 'N/A')}")
                print(f"😊 公众情感: {sentiment['score']:.1f}/10 ({sentiment['label']})")
                
                print(f"\n📋 主要优势:")
                for advantage in analysis['competitive_position']['competitive_advantages']:
                    print(f"   ✓ {advantage}")
                
                print(f"\n🎯 发展建议:")
                for strategy in analysis['growth_potential']['recommended_strategies'][:3]:
                    print(f"   • {strategy}")
                
        else:
            print(f"❌ 搜索失败: {search_result['message']}")
    
    except Exception as e:
        print(f"❌ 分析过程中出现错误: {str(e)}")
    
    finally:
        await client.close()

async def demo_multiple_brands_comparison():
    """演示多品牌对比分析"""
    print("\n\n🔍 多品牌对比分析演示")
    print("=" * 60)
    
    brands = ["华为", "小米", "OPPO"]
    client = DoubaoClient()
    scorer = IndustryScorer()
    
    try:
        brand_scores = {}
        
        for brand in brands:
            print(f"\n📊 分析品牌: {brand}")
            
            # 模拟获取每个品牌的评分
            search_result = await client.search_brand(brand, {"industry": "科技"})
            
            if search_result["status"] == "success":
                # 模拟评分数据
                if brand == "华为":
                    scores = {"market_position": 8.5, "brand_awareness": 9.0, "innovation": 9.2, "financial_performance": 7.8, "sustainability": 8.0}
                elif brand == "小米":
                    scores = {"market_position": 7.2, "brand_awareness": 8.0, "innovation": 8.5, "financial_performance": 8.2, "sustainability": 7.0}
                else:  # OPPO
                    scores = {"market_position": 6.8, "brand_awareness": 7.5, "innovation": 7.0, "financial_performance": 7.5, "sustainability": 6.5}
                
                weighted_score = scorer.calculate_weighted_score(scores)
                brand_scores[brand] = {
                    "scores": scores,
                    "overall": weighted_score
                }
                
                print(f"✅ {brand} 综合评分: {weighted_score:.2f}/10")
        
        # 生成对比报告
        print(f"\n📈 品牌对比排行榜")
        print("-" * 40)
        
        sorted_brands = sorted(brand_scores.items(), key=lambda x: x[1]["overall"], reverse=True)
        
        for i, (brand, data) in enumerate(sorted_brands, 1):
            print(f"{i}. {brand}: {data['overall']:.2f}/10")
        
        print(f"\n📊 详细对比分析")
        print("-" * 40)
        
        criteria_names = {
            "market_position": "市场地位",
            "brand_awareness": "品牌知名度",
            "innovation": "创新能力", 
            "financial_performance": "财务表现",
            "sustainability": "可持续性"
        }
        
        for criterion, name in criteria_names.items():
            print(f"\n{name}:")
            criterion_scores = [(brand, data["scores"][criterion]) for brand, data in brand_scores.items()]
            criterion_scores.sort(key=lambda x: x[1], reverse=True)
            
            for brand, score in criterion_scores:
                print(f"  {brand}: {score:.1f}/10")
    
    except Exception as e:
        print(f"❌ 对比分析中出现错误: {str(e)}")
    
    finally:
        await client.close()

async def main():
    """主演示函数"""
    print("🚀 豆包品牌信息MCP服务器演示")
    print("=" * 80)
    
    # 单品牌深度分析
    await demo_brand_analysis("小米")
    
    # 多品牌对比分析
    await demo_multiple_brands_comparison()
    
    print(f"\n\n✨ 演示完成! 如需了解更多功能，请查看 README.md")

if __name__ == "__main__":
    asyncio.run(main())