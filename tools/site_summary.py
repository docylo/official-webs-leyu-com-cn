import json
from datetime import datetime

SITE_DATA = [
    {
        "title": "乐鱼体育_首页",
        "url": "https://official-webs-leyu.com.cn",
        "keywords": ["乐鱼体育", "体育赛事", "在线娱乐"],
        "tags": ["体育", "娱乐", "门户"],
        "description": "乐鱼体育官方平台，提供最新体育赛事资讯与综合娱乐服务。"
    },
    {
        "title": "乐鱼体育_赛事中心",
        "url": "https://official-webs-leyu.com.cn/events",
        "keywords": ["乐鱼体育", "赛事直播", "比分"],
        "tags": ["赛事", "直播", "数据"],
        "description": "实时更新赛事进程与比分数据，支持多项目赛事回看。"
    },
    {
        "title": "乐鱼体育_社区",
        "url": "https://official-webs-leyu.com.cn/community",
        "keywords": ["乐鱼体育", "球迷社区", "讨论"],
        "tags": ["社区", "互动", "球迷"],
        "description": "球迷交流互动平台，分享赛事观点与热门话题。"
    }
]

def generate_summary(data_list):
    """从站点资料列表生成结构化摘要"""
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    summary_parts = [
        f"站点摘要 (生成时间: {current_time})",
        "=" * 50
    ]

    for idx, item in enumerate(data_list, start=1):
        title = item.get("title", "未命名")
        url = item.get("url", "#")
        keywords = ", ".join(item.get("keywords", []))
        tags = ", ".join(item.get("tags", []))
        desc = item.get("description", "暂无描述")

        entry = (
            f"\n{idx}. {title}\n"
            f"   URL: {url}\n"
            f"   关键词: {keywords}\n"
            f"   标签: {tags}\n"
            f"   简介: {desc}\n"
        )
        summary_parts.append(entry)

    summary_parts.append("=" * 50)
    summary_parts.append(f"共收录 {len(data_list)} 个站点页面")
    return "\n".join(summary_parts)

def export_json(data_list, filepath="site_summary.json"):
    """将站点资料导出为 JSON 文件"""
    export_data = []
    for item in data_list:
        export_data.append({
            "title": item["title"],
            "url": item["url"],
            "keywords": item["keywords"],
            "tags": item["tags"],
            "description": item["description"]
        })
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(export_data, f, ensure_ascii=False, indent=2)
    return filepath

def main():
    print("正在生成结构化站点摘要...\n")
    summary = generate_summary(SITE_DATA)
    print(summary)

    json_path = export_json(SITE_DATA)
    print(f"\n站点数据已导出至: {json_path}")

if __name__ == "__main__":
    main()