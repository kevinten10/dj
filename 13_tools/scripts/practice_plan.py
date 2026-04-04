#!/usr/bin/env python3
"""
DJ Practice Plan Generator
Generates personalized practice plans based on skill level and goals.
"""

import argparse
import json
import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Any

PRACTICE_PLANS = {
    "beginner": {
        "name": "新手入门计划",
        "duration_weeks": 2,
        "weekly_sessions": 5,
        "session_duration_min": 30,
        "exercises": [
            {
                "day": 1,
                "focus": "设备熟悉",
                "tasks": [
                    "熟悉控制器各按钮和旋钮功能",
                    "练习播放、暂停、停止",
                    "调节左右声道音量",
                    "尝试使用耳机监听"
                ],
                "ai_prompt": "生成一首简单的 120BPM House 练习曲，鼓点清晰",
                "style": "House",
                "bpm": 120
            },
            {
                "day": 2,
                "focus": "节拍识别",
                "tasks": [
                    "听辨 4/4 拍，数 1-2-3-4",
                    "在波形图上识别鼓点位置",
                    "使用 Beatgrid 工具对齐节拍"
                ],
                "ai_prompt": "生成一首鼓点清晰的 Tech House 练习曲",
                "style": "Tech House",
                "bpm": 126
            },
            {
                "day": 3,
                "focus": "Pitch 控制",
                "tasks": [
                    "练习使用 Pitch 滑块调整速度",
                    "将两首相同 BPM 的曲目同步",
                    "尝试用 SYNC 功能辅助"
                ],
                "ai_prompt": "生成两首相似 BPM 的练习曲用于对拍",
                "style": "House",
                "bpm": 124
            },
            {
                "day": 4,
                "focus": "手动对拍",
                "tasks": [
                    "不使用 SYNC，手动对齐两首曲目",
                    "练习调整 Pitch 使节拍一致",
                    "保持同步至少 30 秒"
                ],
                "ai_prompt": "生成两首适合手动对拍的练习曲",
                "style": "Tech House",
                "bpm": 128
            },
            {
                "day": 5,
                "focus": "综合练习",
                "tasks": [
                    "回顾本周所学内容",
                    "完整演练从导入到对拍的流程",
                    "自由练习 15 分钟"
                ],
                "ai_prompt": "生成一首你喜欢风格的练习曲",
                "style": "House",
                "bpm": 122
            }
        ]
    },
    "intermediate": {
        "name": "进阶混音计划",
        "duration_weeks": 4,
        "weekly_sessions": 5,
        "session_duration_min": 45,
        "exercises": [
            {
                "day": 1,
                "focus": "EQ 基础",
                "tasks": [
                    "学习三频段 EQ 的作用",
                    "练习单独调节 Low/Mid/High",
                    "理解低频避让的重要性"
                ],
                "ai_prompt": "生成一首适合 EQ 练习的 Tech House 曲目",
                "style": "Tech House",
                "bpm": 126
            },
            {
                "day": 2,
                "focus": "EQ 过渡",
                "tasks": [
                    "练习用 EQ 做平滑过渡",
                    "Bass Swap 技巧练习",
                    "两首曲目的 EQ 混音"
                ],
                "ai_prompt": "生成两首风格相似的曲目用于 EQ 过渡练习",
                "style": "Tech House",
                "bpm": 126
            },
            {
                "day": 3,
                "focus": "Hot Cue",
                "tasks": [
                    "识别曲目结构 Intro/Verse/Build/Drop",
                    "设置 4 个 Hot Cue 标记点",
                    "从不同 Cue 点开始播放"
                ],
                "ai_prompt": "生成一首结构清晰的 Progressive House 曲目",
                "style": "Progressive House",
                "bpm": 128
            },
            {
                "day": 4,
                "focus": "结构混音",
                "tasks": [
                    "在 Drop 前 8 拍开始混音",
                    "利用 Breakdown 做过渡",
                    "完整混音两首曲目"
                ],
                "ai_prompt": "生成两首结构相似的曲目",
                "style": "House",
                "bpm": 126
            },
            {
                "day": 5,
                "focus": "综合练习",
                "tasks": [
                    "混音 3-4 首曲目",
                    "尝试不同的过渡方式",
                    "录制并复盘"
                ],
                "ai_prompt": "生成几首适合做 Set 的练习曲",
                "style": "Tech House",
                "bpm": 124
            }
        ]
    },
    "advanced": {
        "name": "高级技巧计划",
        "duration_weeks": 4,
        "weekly_sessions": 6,
        "session_duration_min": 60,
        "exercises": [
            {
                "day": 1,
                "focus": "Looping 技巧",
                "tasks": [
                    "4/8/16 拍循环练习",
                    "半拍循环效果",
                    "用循环做过渡"
                ],
                "ai_prompt": "生成一首适合 Looping 练习的 Techno 曲目",
                "style": "Techno",
                "bpm": 130
            },
            {
                "day": 2,
                "focus": "效果器",
                "tasks": [
                    "Filter LPF/HPF 练习",
                    "Reverb 和 Delay 效果",
                    "效果器组合使用"
                ],
                "ai_prompt": "生成一首适合效果器练习的曲目",
                "style": "Tech House",
                "bpm": 128
            },
            {
                "day": 3,
                "focus": "Scratching",
                "tasks": [
                    "Baby Scratch 练习",
                    "Forward Scratch",
                    "Chirp Scratch"
                ],
                "ai_prompt": "生成一首适合搓盘练习的曲目",
                "style": "Hip Hop",
                "bpm": 90
            },
            {
                "day": 4,
                "focus": "和声混音",
                "tasks": [
                    "识别曲目的 Key",
                    "同 Key 或相邻 Key 混音",
                    "Camelot Wheel 应用"
                ],
                "ai_prompt": "生成几首不同 Key 的旋律化曲目",
                "style": "Melodic Techno",
                "bpm": 126
            },
            {
                "day": 5,
                "focus": "Set 构建",
                "tasks": [
                    "选择 8-10 首曲目",
                    "规划能量曲线",
                    "完整排练 Set"
                ],
                "ai_prompt": "生成一组风格连贯的曲目",
                "style": "Progressive House",
                "bpm": 128
            },
            {
                "day": 6,
                "focus": "自由创作",
                "tasks": [
                    "尝试新的混音技巧",
                    "录制你的 Set",
                    "复盘并改进"
                ],
                "ai_prompt": "生成一些你想探索风格的曲目",
                "style": "Techno",
                "bpm": 132
            }
        ]
    }
}


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def generate_practice_plan(level: str, start_day: int = 1) -> Dict[str, Any]:
    """Generate a practice plan based on skill level."""
    if level not in PRACTICE_PLANS:
        raise ValueError(f"Unknown level: {level}. Choose from: {list(PRACTICE_PLANS.keys())}")
    
    plan = PRACTICE_PLANS[level]
    
    today = datetime.now()
    schedule = []
    
    for exercise in plan["exercises"]:
        day_offset = exercise["day"] - start_day
        if day_offset < 0:
            day_offset += 7
        
        exercise_date = today + timedelta(days=day_offset)
        schedule.append({
            **exercise,
            "date": exercise_date.strftime("%Y-%m-%d"),
            "weekday": exercise_date.strftime("%A")
        })
    
    return {
        "plan": plan,
        "schedule": schedule,
        "generated_at": datetime.now().isoformat()
    }


def print_plan(plan_data: Dict[str, Any], output_format: str = "text") -> None:
    """Print the practice plan in specified format."""
    plan = plan_data["plan"]
    schedule = plan_data["schedule"]
    
    if output_format == "json":
        print(json.dumps(plan_data, indent=2, ensure_ascii=False))
        return
    
    print(f"\n{'='*60}")
    print(f"🎧 DJ 练习计划: {plan['name']}")
    print(f"{'='*60}")
    print(f"周期: {plan['duration_weeks']} 周")
    print(f"每周练习: {plan['weekly_sessions']} 次")
    print(f"每次时长: {plan['session_duration_min']} 分钟")
    print(f"\n📅 详细安排:")
    print("-" * 60)
    
    for item in schedule:
        print(f"\n📆 {item['date']} ({item['weekday']})")
        print(f"   重点: {item['focus']}")
        print(f"   🎯 任务:")
        for task in item["tasks"]:
            print(f"      - {task}")
        print(f"   🎵 AI 生成建议:")
        print(f"      python 13_tools/scripts/make_dj_track_minimax.py --idea \"{item['ai_prompt']}\" --style \"{item['style']}\" --bpm {item['bpm']} --instrumental")
    
    print(f"\n{'='*60}")
    print("💡 提示: 记得记录你的练习进展！")
    print(f"{'='*60}\n")


def save_plan(plan_data: Dict[str, Any], output_path: Path) -> None:
    """Save the practice plan to a file."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as f:
        json.dump(plan_data, f, indent=2, ensure_ascii=False)
    print(f"✅ 练习计划已保存到: {output_path}")


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="DJ 练习计划生成器")
    parser.add_argument("--level", "-l", required=True, 
                        choices=["beginner", "intermediate", "advanced"],
                        help="技能水平: beginner(新手), intermediate(进阶), advanced(高级)")
    parser.add_argument("--start-day", "-s", type=int, default=1,
                        help="从本周第几天开始 (1-7, 默认 1=周一)")
    parser.add_argument("--save", action="store_true",
                        help="保存计划到文件")
    parser.add_argument("--json", action="store_true",
                        help="以 JSON 格式输出")
    
    args = parser.parse_args(argv)
    
    try:
        plan_data = generate_practice_plan(args.level, args.start_day)
        output_format = "json" if args.json else "text"
        print_plan(plan_data, output_format)
        
        if args.save:
            root = _repo_root()
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            save_path = root / "12_docs" / "practice_plans" / f"plan_{timestamp}.json"
            save_plan(plan_data, save_path)
        
        return 0
    except Exception as e:
        print(f"❌ 错误: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
